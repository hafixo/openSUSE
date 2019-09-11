#
# spec file for package golang-github-prometheus-prometheus
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017 Silvio Moioli <moio@suse.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%global prometheus_user prometheus
%global prometheus_group %{prometheus_user}

%{go_nostrip}

Name:           golang-github-prometheus-prometheus
Version:        2.11.1
Release:        0
Summary:        The Prometheus monitoring system and time series database
License:        Apache-2.0
Group:          System/Management
Url:            https://prometheus.io/
Source:         prometheus-%{version}.tar.xz
Source1:        prometheus.service
Source2:        prometheus.yml
Source3:        prometheus.sysconfig
Source4:        prometheus.firewall.xml
Patch1:         0001-Do-not-force-the-pure-Go-name-resolver.patch
# Lifted from Debian's prometheus package
Patch2:         0002-Default-settings.patch
# Uyuni service discovery support
Patch3:         0003-Add-Uyuni-service-discovery.patch
# Add -buildmode=pie
Patch4:         0004-prometheus-buildmode-pie.patch
BuildRequires:  fdupes
# Adding glibc-devel-static seems to be required for linking if building
# with -buildmode=pie
BuildRequires:  glibc-devel-static
BuildRequires:  golang-github-prometheus-promu
BuildRequires:  golang-packaging
BuildRequires:  xz
BuildRequires:  golang(API) >= 1.12
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}
Requires(pre):  shadow
Requires(post): %fillup_prereq
%{go_provides}

%description
Prometheus's main features are:
 - a multi-dimensional data model (time series identified by metric name and key/value pairs)
 - a flexible query language to leverage this dimensionality
 - no reliance on distributed storage; single server nodes are autonomous
 - time series collection happens via a pull model over HTTP
 - pushing time series is supported via an intermediary gateway
 - targets are discovered via service discovery or static configuration
 - multiple modes of graphing and dashboarding support

%prep
%autosetup -p1 -n prometheus-%{version}

%build
%goprep github.com/prometheus/prometheus
GOPATH=%{_builddir}/go promu build

%install
install -D -m0755 %{_builddir}/prometheus-%{version}/prometheus %{buildroot}/%{_bindir}/prometheus
install -D -m0755 %{_builddir}/prometheus-%{version}/promtool %{buildroot}/%{_bindir}/promtool
install -m 0755 -d %{buildroot}%{_datarootdir}/prometheus
cp -fr console_libraries/ consoles/ %{buildroot}%{_datarootdir}/prometheus

install -m 0755 -d %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/prometheus.service

install -d -m 0755 %{buildroot}%{_sbindir}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcprometheus

install -d -m 0755 %{buildroot}%{_sysconfdir}/prometheus
install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/prometheus/prometheus.yml

install -m 0755 -d %{buildroot}%{_fillupdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_fillupdir}/sysconfig.prometheus

install -m 0755 -d %{buildroot}%{_libdir}/firewalld/services/
install -m 0644 %{SOURCE4} %{buildroot}%{_libdir}/firewalld/services/prometheus.xml

install -d -m 0755 %{buildroot}%{_sharedstatedir}/prometheus
install -d -m 0755 %{buildroot}%{_sharedstatedir}/prometheus/data
install -d -m 0755 %{buildroot}%{_sharedstatedir}/prometheus/metrics

%fdupes %{buildroot}/%{_datarootdir}

%pre
getent group %{prometheus_group} >/dev/null || %{_sbindir}/groupadd -r %{prometheus_group}
getent passwd %{prometheus_user} >/dev/null || %{_sbindir}/useradd -r -g %{prometheus_group} -d %{_localstatedir}/lib/prometheus -s /sbin/nologin %{prometheus_user}
%service_add_pre prometheus.service

%post
%fillup_only -n prometheus
%service_add_post prometheus.service

%preun
%service_del_preun prometheus.service

%postun
%service_del_postun prometheus.service

%verifyscript
%fillup_only -n prometheus

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/prometheus
%{_bindir}/promtool
%{_unitdir}/prometheus.service
%{_sbindir}/rcprometheus
%{_datarootdir}/prometheus
%{_fillupdir}/sysconfig.prometheus
%dir %attr(0700,%{prometheus_user},%{prometheus_group}) %{_sharedstatedir}/prometheus
%dir %attr(0700,%{prometheus_user},%{prometheus_group}) %{_sharedstatedir}/prometheus/data
%dir %attr(0700,%{prometheus_user},%{prometheus_group}) %{_sharedstatedir}/prometheus/metrics
%dir %{_sysconfdir}/prometheus
%config(noreplace) %{_sysconfdir}/prometheus/prometheus.yml
%dir %{_libdir}/firewalld
%dir %{_libdir}/firewalld/services
%{_libdir}/firewalld/services/prometheus.xml

%changelog
