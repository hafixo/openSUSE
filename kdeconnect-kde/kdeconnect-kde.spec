#
# spec file for package kdeconnect-kde
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


Name:           kdeconnect-kde
Version:        1.3.5
Release:        0
Summary:        Integration of Android with Linux desktops
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            https://community.kde.org/KDEConnect
Source:         https://download.kde.org/stable/kdeconnect/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/kdeconnect/%{version}/%{name}-%{version}.tar.xz.sig
Source100:      kdeconnect-kde.SuSEfirewall
Source101:      kdeconnect-kde-firewalld.xml
BuildRequires:  cmake >= 3.0
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(Qca-qt5)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libfakekey)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)
Requires:       sshfs
Recommends:     %{name}-lang = %{version}
Conflicts:      kdeconnect-kde4

%description
A package for integration of Android with Linux desktops.

Current feature list:
- Clipboard share: copy from or to your desktop
- Notifications sync (4.3+): Read your Android notifications
- Multimedia remote control: Use your phone as a remote control
- WiFi connection: no USB wire or Bluetooth needed
- RSA Encryption: your information is safe

Please note you will need to install KDE Connect on Android for this app to work:
https://play.google.com/store/apps/details?id=org.kde.kdeconnect_tp or
https://f-droid.org/en/packages/org.kde.kdeconnect_tp/

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build

for translation_file in kdeconnect-{cli,core,fileitemaction,kcm,kded,kio,nautilus-extension,plugins,urlhandler} plasma_applet_org.kde.kdeconnect; do
    %find_lang $translation_file %{name}.lang
done

%if %{suse_version} < 1550
# susefirewall config file
install -D -m 0644 %{SOURCE100} \
    %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/%{name}
%endif
# firewalld config file
install -D -m 0644 %{SOURCE101} \
    %{buildroot}%{_libexecdir}/firewalld/services/%{name}.xml

%suse_update_desktop_file %{buildroot}%{_kf5_applicationsdir}/org.kde.kdeconnect.nonplasma.desktop Network RemoteAccess

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc README*
%if %{suse_version} < 1550
%config(noreplace) %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/%{name}
%endif
%dir %{_datadir}/nautilus-python
%dir %{_libexecdir}/firewalld
%dir %{_libexecdir}/firewalld/services
%{_datadir}/nautilus-python/extensions/
%{_libexecdir}/firewalld/services/%{name}.xml
%{_kf5_libdir}/libkdeconnect*.so.*
%{_kf5_plugindir}/
%{_kf5_applicationsdir}/*.desktop
%dir %{_kf5_iconsdir}/hicolor/256x256
%dir %{_kf5_iconsdir}/hicolor/256x256/apps
%{_kf5_iconsdir}/hicolor/*/apps/kdeconnect.*
%{_kf5_libdir}/libexec/
%{_kf5_servicesdir}/
%{_kf5_notifydir}/
%{_kf5_servicetypesdir}/
%{_kf5_sharedir}/plasma/
%{_kf5_qmldir}/
%{_kf5_bindir}/kdeconnect-cli
%{_kf5_bindir}/kdeconnect-handler
%{_kf5_bindir}/kdeconnect-indicator
%{_kf5_sharedir}/dbus-1/services/org.kde.kdeconnect.service
%{_kf5_configdir}/autostart/org.kde.kdeconnect.daemon.desktop
%{_kf5_iconsdir}/hicolor/*/status/*
%{_kf5_htmldir}/en/kdeconnect/
%dir %{_kf5_appstreamdir}
%{_kf5_appstreamdir}/org.kde.kdeconnect.kcm.appdata.xml

%files lang -f %{name}.lang

%changelog
