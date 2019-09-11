#
# spec file for package grafana
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define GRAFANA_USER    %{name}
%define GRAFANA_GROUP   %{name}
%define GRAFANA_HOME    %{_datadir}/%{name}

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%bcond_with phantomjs

Name:           grafana
Version:        6.3.3
Release:        0
Summary:        Dashboards and editors for Graphite, InfluxDB, OpenTSDB
License:        Apache-2.0
Group:          System/Monitoring
Url:            http://grafana.org/
Source:         %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
# Instructions on the build process
Source2:        README
# Makefile to automate build process
Source3:        Makefile.no_phantomjs
Source4:        Makefile.phantomjs
BuildRequires:  fdupes
BuildRequires:  go >= 1.11
BuildRequires:  golang-packaging
BuildRequires:  shadow
Requires(post): %insserv_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{with phantomjs}
BuildRequires:  phantomjs
Requires:       phantomjs
%endif
%{?systemd_requires}

%description
A graph and dashboard builder for visualizing time series metrics.

Grafana provides ways to create, explore, and share
dashboards and data with teams.

%prep
%setup -q -n grafana-%{version}
%if %{with phantomjs}
cp %{S:4} %_sourcedir/Makefile
%else
cp %{S:3} %_sourcedir/Makefile
%endif

%build
%goprep github.com/grafana/grafana
# Manual build in order to inject ldflags so grafana correctly displays
# the version in the footer of each page.  Note that we're only injecting
# main.version, not main.commit or main.buildstamp as is done in the upstream
# build.go, because we don't have access to the git commit history here.
# (The %%gobuild macro can't take quoted strings; they get split up when
# expanded to $extra_flags in process_build() in /usr/lib/rpm/golang.sh.)
export IMPORTPATH="github.com/grafana/grafana"
export BUILDFLAGS="-v -p 4 -x -buildmode=pie"
export GOPATH=%{_builddir}/go:%{_builddir}/contrib
export GOBIN=%{_builddir}/go/bin
go install $BUILDFLAGS -ldflags '-X main.version=%{version}' $IMPORTPATH/pkg/cmd/...

%install
%goinstall

# we're missing %%gosrc and %%gofilelist... (although that *might* be ok...)

install -Dm644 {packaging/rpm/systemd/,%{buildroot}%{_unitdir}/}%{name}-server.service
install -dm755 %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service  %{buildroot}%{_sbindir}/rc%{name}-server
mv %{buildroot}/%{_bindir}/grafana-* %{buildroot}/%{_sbindir}

install -Dm644 packaging/rpm/sysconfig/%{name}-server \
%{buildroot}%{_fillupdir}/sysconfig.%{name}-server

install -d -m0750 %{buildroot}%{_localstatedir}/lib/%{name}
install -d -m0750 %{buildroot}%{_localstatedir}/log/%{name}
install -d -m0755 %{buildroot}/%{_localstatedir}/lib/%{name}/plugins
install -d -m0755 %{buildroot}/%{_localstatedir}/lib/%{name}/dashboards
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}/provisioning/dashboards

install -Dm640 conf/sample.ini %{buildroot}%{_sysconfdir}/%{name}/%{name}.ini
install -Dm640 {conf/,%{buildroot}%{_sysconfdir}/%{name}/}ldap.toml
install -Dm644 {conf/,%{buildroot}%{_datadir}/%{name}/conf/}defaults.ini
install -m644 {conf/,%{buildroot}%{_datadir}/%{name}/conf/}sample.ini
install -Dm644 {conf/provisioning/dashboards/,%{buildroot}%{_datadir}/%{name}/conf/provisioning/dashboards/}sample.yaml
install -Dm644 {conf/provisioning/datasources/,%{buildroot}%{_datadir}/%{name}/conf/provisioning/datasources/}sample.yaml
cp -pr public %{buildroot}%{_datadir}/%{name}/
install -d -m755 %{buildroot}%{_datadir}/%{name}/vendor
install -d -m755 %{buildroot}%{_datadir}/%{name}/tools

%if %{with phantomjs}
# phantomjs is used for rendering PNG images of graphs.  The frontend asset
# build process downloadsa prebuilt x86_64 binary, which ends up in
# vendor/phantomjs/phantomjs.  This is ugly but works for x86_64.  It naturally
# will not work for other architectures, so instead we remove the phantomjs
# binary and install a symlink to the systemwide /usr/bin/phantomjs.
cp -pr tools/phantomjs %{buildroot}%{_datadir}/%{name}/tools/
rm -f %{buildroot}%{_datadir}/%{name}/tools/phantomjs/phantomjs
ln -s %{_bindir}/phantomjs %{buildroot}%{_datadir}/%{name}/tools/phantomjs/phantomjs
%endif

# Do *not* use %%fudpes -s -- this will result in grafana failing to load
# all the plugins (something in the plugin scanner can't cope with files
# in there being symlinks).
%fdupes %{buildroot}/%{_datadir}

%check
#gotest github.com/grafana/grafana/pkg...

%pre
%service_add_pre %{name}-server.service

echo "Creating user %{GRAFANA_USER} and group %{GRAFANA_GROUP} if not present"
getent group %{GRAFANA_GROUP} > /dev/null || groupadd -r %{GRAFANA_GROUP}
getent passwd %{GRAFANA_GROUP} > /dev/null || useradd -r -g %{GRAFANA_GROUP} \
-d %{GRAFANA_HOME} -s /sbin/nologin -c "%{GRAFANA_USER} user" %{GRAFANA_GROUP}

%post
%{fillup_only -n %{name}-server}
%service_add_post %{name}-server.service

%preun
%service_del_preun %{name}-server.service

%postun
%service_del_postun %{name}-server.service

%files
%defattr(-,root,root)
%license LICENSE*
%doc CHANGELOG*
%{_sbindir}/%{name}*
%{_sbindir}/rc%{name}-server
%{_unitdir}/%{name}-server.service
%{_fillupdir}/sysconfig.%{name}-server
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}/provisioning
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}/provisioning/dashboards
%attr(0755,root,%{GRAFANA_GROUP}) %dir %{_datadir}/%{name}/conf
%attr(0640,root,%{GRAFANA_GROUP}) %config(noreplace) %{_sysconfdir}/%{name}/%{name}.ini
%attr(0640,root,%{GRAFANA_GROUP}) %config(noreplace) %{_sysconfdir}/%{name}/ldap.toml
%attr(0755,%{GRAFANA_USER},%{GRAFANA_GROUP}) %dir %{_localstatedir}/lib/%{name}
%attr(0755,%{GRAFANA_USER},%{GRAFANA_GROUP}) %dir %{_localstatedir}/lib/%{name}/plugins
%attr(0755,%{GRAFANA_USER},%{GRAFANA_GROUP}) %dir %{_localstatedir}/lib/%{name}/dashboards
%attr(0750,%{GRAFANA_USER},%{GRAFANA_GROUP}) %dir %{_localstatedir}/log/%{name}
%doc %{_datadir}/%{name}/conf/sample.ini
%doc %{_datadir}/%{name}/conf/provisioning/dashboards/sample.yaml
%doc %{_datadir}/%{name}/conf/provisioning/datasources/sample.yaml
%config %{_datadir}/%{name}/conf/defaults.ini
%{_datadir}/%{name}

%changelog
