#
# spec file for package onedrive
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2018 LISA GmbH, Bingen, Germany.
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


%{!?_userunitdir: %{expand: %%global _userunitdir %{_unitdir}/../user}}
%define docdir %{_defaultdocdir}/%{name}

Name:           onedrive
Version:        2.4.3
Release:        0
Summary:        Client for One Drive Service for Linux
License:        GPL-3.0-only
Group:          Productivity/Networking/Other
URL:            https://github.com/abraunegg/onedrive/
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  dmd
BuildRequires:  help2man
BuildRequires:  libcurl-devel
BuildRequires:  phobos-devel-static
BuildRequires:  sqlite3-devel
Recommends:     logrotate
Suggests:       onedrive-completition-bash
Suggests:       onedrive-completition-zsh
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%package completion-bash
Summary:        OneDrive Bash completition
Group:          Productivity/Networking/Other
BuildRequires:  bash
BuildRequires:  bash-completion
Requires:       bash
Requires:       bash-completion
Requires:       onedrive = %{version}

%package completion-zsh
Summary:        OneDrive zsh completition
Group:          Productivity/Networking/Other
Requires:       zsh

%description
OneDrive is a client for Microsoft file serving service

%description completion-bash
OneDrive shell completions for Bash.

%description completion-zsh
OneDrive shell completions for zsh.

%prep
%setup -q
#sed -i /chown/d Makefile
sed -i 's/^docdir.*/docdir = @docdir@/g' Makefile.in

%build
%configure \
    --docdir=%{docdir} \
    --with-systemduserunitdir=%_userunitdir \
    --with-systemdsystemunitdir=%_unitdir \
    --enable-notifications \
    --enable-completions \
    --with-bash-completion-dir=/usr/share/bash-completion/completions/
make %{?_smp_mflags} %{name}

%install
%make_install
install -D -m 0644 config %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -d -m 0755 %{buildroot}%{_localstatedir}/log/%{name}

%pre
%service_add_pre %{name}@.service
%service_add_pre %{name}.service

%post
%service_add_post %{name}@.service
%service_add_post %{name}.service

%preun
%service_del_preun %{name}@.service
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}@.service
%service_del_postun %{name}.service

%files
%defattr(-,root,root)
%license LICENSE
%doc USAGE.md Office365.md INSTALL.md Docker.md CHANGELOG.md config README.md BusinessSharedFolders.md LICENSE
%config(noreplace) %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_bindir}/%{name}
%dir %{_userunitdir}
%{_userunitdir}/%{name}.service
%{_unitdir}/%{name}@.service
%attr(0644, root, root) %{_mandir}/man1/%{name}.1*
%{_localstatedir}/log/%{name}

%files completion-bash
%{_datadir}/bash-completion/completions/

%files completion-zsh
%dir %{_prefix}/local/share/zsh/
%dir %{_prefix}/local/share/zsh/site-functions
%{_prefix}/local/share/zsh/site-functions/_onedrive

%changelog
