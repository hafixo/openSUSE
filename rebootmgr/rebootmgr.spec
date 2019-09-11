#
# spec file for package rebootmgr
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


Name:           rebootmgr
Version:        0.18
Release:        0
Summary:        Automatic controlled reboot during a maintenance window
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          System/Base
URL:            https://github.com/SUSE/rebootmgr
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cetcd-devel
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(json-c)
%{?systemd_requires}

%description
RebootManager is a dbus service to execute a controlled reboot after updates in a defined maintenance window.

If you updated a system with e.g. transactional updates or a kernel update was applied, you can tell rebootmgrd with rebootmgrctl, that the machine should be reboot at the next possible time. This can either be immeaditly, during a defined maintenance window or, to avoid that a lot of machines boot at the same time, controlled with locks and etcd.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
ln -sf service %{buildroot}%{_sbindir}/rcrebootmgr
%fdupes %{buildroot}%{_mandir}

%pre
%service_add_pre rebootmgr.service

%post
%service_add_post rebootmgr.service

%preun
%service_del_preun rebootmgr.service

%postun
%service_del_postun rebootmgr.service

%files
%license COPYING COPYING.LIB
%doc NEWS
%dir %{_sysconfdir}/dbus-1/system.d
%config %{_sysconfdir}/rebootmgr.conf
%config %{_sysconfdir}/dbus-1/system.d/org.opensuse.RebootMgr.conf
%{_prefix}/lib/systemd/system/rebootmgr.service
%{_sbindir}/rebootmgrctl
%{_sbindir}/rebootmgrd
%{_sbindir}/rcrebootmgr
%{_datadir}/dbus-1/interfaces/org.opensuse.RebootMgr.xml
%{_mandir}/man1/rebootmgrctl.1%{?ext_man}
%{_mandir}/man5/rebootmgr.conf.5%{?ext_man}
%{_mandir}/man8/rebootmgrd.8%{?ext_man}
%{_mandir}/man8/org.opensuse.RebootMgr.conf.8%{?ext_man}
%{_mandir}/man8/rebootmgr.service.8%{?ext_man}

%changelog
