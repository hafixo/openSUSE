#
# spec file for package icingaweb2-module-director
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines

Name:           icingaweb2-module-director
Version:        1.6.2
Release:        0
Summary:        Config module for Icinga Web 2
License:        GPL-2.0-or-later
Group:          System/Monitoring
Url:            https://www.icinga.org
Source0:        https://github.com/Icinga/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source90:       README.SUSE
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
Requires:       icinga2 >= 2.4.3
Requires:       icingaweb2 >= 2.2.0
Requires:       php-curl
%{?systemd_requires}

%define basedir	%{_datadir}/icingaweb2

%description
Director is an config module for icingaweb2

%prep
%setup -q
install -m644 %{SOURCE90} .

%build

%install
mkdir -p %{buildroot}%{basedir}/modules/director
mkdir -p %{buildroot}%{basedir}/modules/director/{application,contrib,doc,library,public,schema,test}
cp -prv application contrib doc library public schema test %{buildroot}%{basedir}/modules/director
cp -pv *.md *.php *.info %{buildroot}%{basedir}/modules/director
# not needed
rm %{buildroot}%{basedir}/modules/director/contrib/docker-test.sh
# systemd
install -D -m 644 %{buildroot}%{basedir}/modules/director/contrib/systemd/director-jobs.service %{buildroot}%{_unitdir}/%{name}-jobs.service
rm -r %{buildroot}%{basedir}/modules/director/contrib/systemd
mkdir -p %{buildroot}%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}-jobs
# rpmlintrc
chmod 754 %{buildroot}%{basedir}/modules/director/contrib/linux-agent-installer/Icinga2Agent.bash
# languages
%find_lang director %{name}.lang

%pre
%service_add_pre %{name}-jobs.service

%preun
%service_del_preun %{name}-jobs.service

%post
%service_add_post %{name}-jobs.service

%postun
%service_del_postun %{name}-jobs.service

%files -f %{name}.lang
%defattr(-,root,root)
%doc README.SUSE
%dir %{basedir}
%dir %{basedir}/modules
%dir %{basedir}/modules/director
%{basedir}/modules/director/*
%{_unitdir}/%{name}-jobs.service
%{_sbindir}/rc%{name}-jobs

%changelog
