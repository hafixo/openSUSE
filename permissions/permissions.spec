#
# spec file for package permissions
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


%define VERSION 20190711

Name:           permissions
Version:        %{VERSION}
Release:        0
Summary:        SUSE Linux Default Permissions
# Maintained in github by the security team.
License:        GPL-2.0-or-later
Group:          Productivity/Security
Url:            http://github.com/openSUSE/permissions
Source:         permissions-%{version}.tar.xz
Source1:        fix_version.sh
BuildRequires:  libcap-devel
Requires:       chkstat
Requires:       permissions-config
Recommends:     permissions-doc
Provides:       aaa_base:%{_sysconfdir}/permissions

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="-W -Wall %{optflags}" FSCAPS_DEFAULT_ENABLED=0

%install
%make_install fillupdir=%{_fillupdir}

%description
Permission settings of files and directories depending on the local
security settings. The local security setting ("easy", "secure", or "paranoid")
can be configured in /etc/sysconfig/security.

This package does not contain files, it just requires the necessary packages.

%files

%package doc
Summary:        SUSE Linux Default Permissions documentation
Group:          Documentation/Man
Version:        %{suse_version}_%{VERSION}
Release:        0

%description doc
Documentation for the permission files /etc/permissions*.

%files doc
%{_mandir}/man5/permissions.5%{ext_man}

%package config
Summary:        SUSE Linux Default Permissions config files
Group:          Productivity/Security
Version:        %{suse_version}_%{VERSION}
Release:        0
Requires(post): %fillup_prereq
Requires(post): chkstat
#!BuildIgnore:  group(trusted)
Requires(pre):  group(trusted)

%description config
The actual permissions configuration files, /etc/permission.*.

%files config
%config %{_sysconfdir}/permissions
%config %{_sysconfdir}/permissions.easy
%config %{_sysconfdir}/permissions.secure
%config %{_sysconfdir}/permissions.paranoid
%config(noreplace) %{_sysconfdir}/permissions.local
%{_fillupdir}/sysconfig.security

%post config
%{fillup_only -n security}
# apply all potentially changed permissions
%{_bindir}/chkstat --system

%package -n chkstat
Summary:        SUSE Linux Default Permissions tool
Group:          Productivity/Security
Version:        %{suse_version}_%{VERSION}
Release:        0

%description -n chkstat
Tool to check and set file permissions.

%files -n chkstat
%{_bindir}/chkstat
%{_mandir}/man8/chkstat.8%{ext_man}

%package -n permissions-zypp-plugin
BuildArch:      noarch
Requires:       permissions = %{VERSION}
Requires:       python3-zypp-plugin
Requires:       libzypp(plugin:commit) = 1
Summary:        A zypper commit plugin for calling chkstat
Group:          Productivity/Security

%description -n permissions-zypp-plugin
This package contains a plugin for zypper that calls `chkstat --system` after
new packages have been installed. This is helpful for maintaining custom
entries in /etc/permissions.local.

%files -n permissions-zypp-plugin
%dir /usr/lib/zypp
%dir /usr/lib/zypp/plugins
%dir /usr/lib/zypp/plugins/commit
/usr/lib/zypp/plugins/commit/permissions.py

%changelog
