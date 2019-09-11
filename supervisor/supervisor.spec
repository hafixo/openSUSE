#
# spec file for package supervisor
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


Name:           supervisor
Version:        3.3.5
Release:        0
Summary:        A system for controlling process state under UNIX
License:        SUSE-Repoze
Group:          Development/Languages/Python
URL:            http://supervisord.org/
Source:         https://files.pythonhosted.org/packages/source/s/supervisor/supervisor-%{version}.tar.gz
Source2:        supervisord.conf
Source3:        supervisord.service
Source4:        supervisord-tmpfiles.conf
BuildRequires:  fdupes
BuildRequires:  python-meld3
BuildRequires:  python-mock >= 0.5.0
BuildRequires:  python-rpm-macros
BuildRequires:  python-setuptools
Requires:       python-meld3 >= 0.6.5
Suggests:       python-cElementTree >= 1.0.2
BuildArch:      noarch
%{?systemd_requires}

%description
Supervisor is a client/server system that allows its users to
control a number of processes on UNIX-like operating systems.

%prep
%setup -q
sed -i 's|#!<<PYTHON>>|#!%{_bindir}/python2|g' supervisor/tests/fixtures/unkillable_spew.py supervisor/tests/fixtures/spew.py
find . -name '*.py' -exec sed -i "s|#!%{_bindir}/env python|#!%{_bindir}/python2|g" {} \;

%build
%python2_build

%install
%python2_install
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_sysconfdir}/supervisord.d
install -D -m 0644 %{SOURCE4} %{buildroot}/%{_tmpfilesdir}/supervisord.conf
install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/supervisord.service
install -d -m 0750 %{buildroot}%{_localstatedir}/log/supervisord/
install -m 0660 %{SOURCE2} %{buildroot}%{_sysconfdir}/
install -d %{buildroot}%{_sbindir}/
ln -s service %{buildroot}%{_sbindir}/rcsupervisord
%fdupes %{buildroot}%{python_sitelib}/

%pre
%service_add_pre supervisord.service

%post
%service_add_post supervisord.service
%tmpfiles_create %{_tmpfilesdir}/supervisord.conf

%preun
%service_del_preun supervisord.service

%postun
%service_del_postun supervisord.service

%check
python2 setup.py test

%files
%license LICENSES.txt COPYRIGHT.txt
%doc README.rst CHANGES.txt
%{_bindir}/echo_supervisord_conf
%{_bindir}/pidproxy
%{_bindir}/supervisorctl
%{_bindir}/supervisord
%{python_sitelib}/*
%{_tmpfilesdir}/supervisord.conf
%dir %ghost /run/supervisord
%dir %attr(-,root,root) %ghost %{_rundir}/%{name}
%{_unitdir}/supervisord.service
%{_sbindir}/rcsupervisord
%config(noreplace) %{_sysconfdir}/supervisord.conf
%dir %{_sysconfdir}/supervisord.d
%dir %attr(750,root,root)%{_localstatedir}/log/supervisord

%changelog
