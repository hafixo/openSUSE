#
# spec file for package ksysguard5
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


%bcond_without lang
Name:           ksysguard5
Version:        5.16.4
Release:        0
# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.8.95 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        KDE System Guard daemon
License:        GPL-2.0-only
Group:          System/GUI/KDE
Url:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/ksysguard-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/%{version}/ksysguard-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
Source3:        ksysguardd.service
# PATCH-FIX-OPENSUSE 0001-Use-run-for-ksysguardd-s-pid-file.patch
Patch0:         0001-Use-run-for-ksysguardd-s-pid-file.patch
BuildRequires:  extra-cmake-modules >= 5.58.0
BuildRequires:  kf5-filesystem
BuildRequires:  libsensors4-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5Init)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5SysGuard) >= %{_plasma5_version}
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5Core) >= 5.12.0
BuildRequires:  cmake(Qt5Widgets) >= 5.12.0
Requires:       libksysguard5-helper
Recommends:     %{name}-lang
%if 0%{?suse_version} > 1314 && "%{suse_version}" != "1320"
Provides:       kdebase4-workspace-ksysguardd = %{version}
Obsoletes:      kdebase4-workspace-ksysguardd < %{version}
%else
Conflicts:      kdebase4-workspace-ksysguardd
%endif
BuildRequires:  update-desktop-files
%{?systemd_requires}

%description
This package contains the ksysguard daemon and application.

This package can be installed on servers without any other KDE packages
to enable monitoring them remotely with ksysguard.

%lang_package
%prep
%setup -q -n ksysguard-%{version}
%patch0 -p1

%build
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %make_jobs

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %kf5_find_lang
  %kf5_find_htmldocs
%endif
  %suse_update_desktop_file    org.kde.ksysguard      System Monitor

  install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/ksysguardd.service

%pre
%service_add_pre ksysguardd.service

%preun
%service_del_preun ksysguardd.service

%post
/sbin/ldconfig
%service_add_post ksysguardd.service

%postun
/sbin/ldconfig
%service_del_postun ksysguardd.service
exit 0

%files
%license COPYING*
%{_kf5_bindir}/ksysguard
%{_kf5_bindir}/ksysguardd
%config %{_kf5_sysconfdir}/ksysguarddrc
%{_kf5_knsrcfilesdir}/ksysguard.knsrc
%{_kf5_libdir}/libkdeinit5_ksysguard.so
%{_kf5_applicationsdir}/org.kde.ksysguard.desktop
%{_kf5_notifydir}/
%dir %{_kf5_htmldir}/en
%dir %{_kf5_htmldir}
%{_kf5_htmldir}/en/ksysguard/
%{_kf5_iconsdir}/hicolor/*/*/
%{_kf5_sharedir}/ksysguard/
%{_kf5_sharedir}/kxmlgui5/
%{_kf5_appstreamdir}/org.kde.ksysguard.appdata.xml
%{_unitdir}/ksysguardd.service

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
