#
# spec file for package plasma5-desktop
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


%define kf5_version 5.58.0

%bcond_without lang
Name:           plasma5-desktop
Version:        5.16.4
Release:        0
# Full Plasma 5 version (e.g. 5.9.3)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.9.3 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        The KDE Plasma Workspace Components
License:        GPL-2.0-only
Group:          System/GUI/KDE
Url:            http://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/plasma-desktop-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/%{version}/plasma-desktop-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch1:         0001-Use-themed-user-face-icon-in-kickoff.patch
# PATCHES 100-200 and above are from upstream 5.16 branch
# PATCHES 201-300 and above are from upstream master/5.17 branch
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  extra-cmake-modules >= 1.8.0
BuildRequires:  fdupes
BuildRequires:  glib2-devel
BuildRequires:  kf5-filesystem
BuildRequires:  libtag-devel
BuildRequires:  phonon4qt5-devel >= 4.6.60
BuildRequires:  update-desktop-files
BuildRequires:  xz
%if 0%{?suse_version} < 1330
# It does not build with the default compiler (GCC 4.8) on Leap 42.x
BuildRequires:  gcc7-c++
%endif
%if 0%{?suse_version} > 1320 || 0%{?sle_version} >= 120200
BuildRequires:  cmake(AppStreamQt) >= 0.10.4
%endif
BuildRequires:  cmake(KDED) >= %{kf5_version}
BuildRequires:  cmake(KF5Activities) >= %{kf5_version}
BuildRequires:  cmake(KF5ActivitiesStats) >= %{kf5_version}
BuildRequires:  cmake(KF5Attica) >= %{kf5_version}
BuildRequires:  cmake(KF5Auth) >= %{kf5_version}
BuildRequires:  cmake(KF5Baloo) >= %{kf5_version}
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Declarative) >= %{kf5_version}
BuildRequires:  cmake(KF5DocTools) >= %{kf5_version}
BuildRequires:  cmake(KF5Emoticons)
BuildRequires:  cmake(KF5GlobalAccel) >= %{kf5_version}
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5KCMUtils) >= %{kf5_version}
BuildRequires:  cmake(KF5KDELibs4Support) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff) >= %{kf5_version}
BuildRequires:  cmake(KF5Notifications) >= %{kf5_version}
BuildRequires:  cmake(KF5NotifyConfig) >= %{kf5_version}
BuildRequires:  cmake(KF5People) >= %{kf5_version}
BuildRequires:  cmake(KF5Plasma) >= %{kf5_version}
BuildRequires:  cmake(KF5PlasmaQuick) >= %{kf5_version}
BuildRequires:  cmake(KF5Runner) >= %{kf5_version}
BuildRequires:  cmake(KF5Wallet) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(KRunnerAppDBusInterface) >= %{_plasma5_version}
BuildRequires:  cmake(KSMServerDBusInterface) >= %{_plasma5_version}
BuildRequires:  cmake(KWinDBusInterface) >= %{_plasma5_version}
BuildRequires:  cmake(LibKWorkspace) >= %{_plasma5_bugfix}
BuildRequires:  cmake(LibTaskManager) >= %{_plasma5_version}
BuildRequires:  cmake(Qt5Concurrent) >= 5.4.0
BuildRequires:  cmake(Qt5DBus) >= 5.4.0
BuildRequires:  cmake(Qt5Qml) >= 5.4.0
BuildRequires:  cmake(Qt5Quick) >= 5.4.0
BuildRequires:  cmake(Qt5QuickWidgets) >= 5.4.0
BuildRequires:  cmake(Qt5Sql) >= 5.4.0
BuildRequires:  cmake(Qt5Svg) >= 5.4.0
BuildRequires:  cmake(Qt5Test) >= 5.4.0
BuildRequires:  cmake(Qt5Widgets) >= 5.4.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.4.0
BuildRequires:  cmake(ScreenSaverDBusInterface) >= %{_plasma5_version}
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xorg-evdev)
BuildRequires:  pkgconfig(xorg-libinput)
BuildRequires:  pkgconfig(xorg-server)
BuildRequires:  pkgconfig(xorg-synaptics)
%ifarch %arm aarch64
BuildRequires:  pkgconfig(glesv2)
%else
BuildRequires:  pkgconfig(gl)
%endif
#BuildRequires:  pkgconfig(xrender)
BuildRequires:  breeze5-icons
BuildRequires:  xkeyboard-config
# Includes some plugins for kpackage needed during build
BuildRequires:  plasma5-workspace >= %{_plasma5_bugfix}
Requires:       %{name}-branding = %{version}
Requires:       libqt5-qtgraphicaleffects
Requires:       plasma5-workspace >= %{_plasma5_bugfix}
# hardcode versions of plasma-framework-componets and plasma-framework-private packages, as upstream doesn't keep backwards compability there
%requires_ge plasma-framework-components
%requires_ge plasma-framework-private
Requires:       kde-user-manager
# Various KCMs use it
Requires:       kirigami2
%if 0%{?suse_version} > 1314 && "%{suse_version}" != "1320"
Requires:       kinfocenter5
Requires:       kmenuedit5
Requires:       ksysguard5
%endif
# needed for the ActivityManager
Requires:       kactivities5-imports
Conflicts:      kactivities5 < 5.20.0
Recommends:     plasma5-addons
Recommends:     %{name}-lang
%if 0%{?suse_version} > 1314 && "%{suse_version}" != "1320"
Provides:       kdebase4-workspace = 5.3.0
Obsoletes:      kdebase4-workspace < 5.3.0
Provides:       kcm-touchpad = %{version}
Obsoletes:      kcm-touchpad < %{version}
Provides:       kdebase4-workspace-plasma-calendar = %{version}
Obsoletes:      kdebase4-workspace-plasma-calendar < %{version}
Provides:       kdebase4-workspace-plasma-engine-akonadi = %{version}
Obsoletes:      kdebase4-workspace-plasma-engine-akonadi < %{version}
%else
Conflicts:      kdebase4-workspace
Conflicts:      kcm-touchpad
%endif
Conflicts:      kio-extras5 <= 5.3.2
Provides:       kcm-touchpad5 = %{version}
Obsoletes:      kcm-touchpad5 < %{version}
# libinput configuration is lacking in comparision
Recommends:     xf86-input-synaptics
Provides:       %{name}-branding = %{version}
Provides:       %{name}-branding-upstream = %{version}
Obsoletes:      %{name}-branding-upstream < %{version}
Provides:       plasma5-addons-kimpanel = %{version}
Obsoletes:      plasma5-addons-kimpanel < %{version}
Provides:       %{name}-kimpanel = %{version}
Obsoletes:      %{name}-kimpanel < %{version}
Obsoletes:      synaptiks

%description
This package contains the basic packages for a Plasma workspace.

%lang_package

%prep
%autosetup -p1 -n plasma-desktop-%{version}

# Workaround for boo#1038368
sed -i"" "s/Name=Desktop/Name=Desktop Containment/g" containments/desktop/package/metadata.desktop

%build
  %if 0%{?suse_version} < 1330
    # It does not build with the default compiler (GCC 4.8) on Leap 42.x
    export CC=gcc-7
    export CXX=g++-7
  %endif
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %make_jobs

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %kf5_find_lang
  %kf5_find_htmldocs
%endif

  # Copy the icon for kcolorschemeeditor.desktop
  mkdir -p %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/apps
  mkdir -p %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/preferences
  if [ -f %{_kf5_iconsdir}/breeze/apps/32/preferences-desktop-color.svg ]; then
      cp %{_kf5_iconsdir}/breeze/apps/32/preferences-desktop-color.svg %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/apps/
  else
      cp %{_kf5_iconsdir}/breeze/preferences/32/preferences-desktop-color.svg %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/preferences/
  fi

  # remove empty/invalid appstream xml files. kpackagetool5 generates invalid files sometimes...
  # remove this once kpackagetool5 is fixed
  find %{buildroot}%{_kf5_appstreamdir} -type f -size 0 -print -delete

  # no devel files needed here
  rm -rfv %{buildroot}%{_kf5_sharedir}/dbus-1/interfaces/
  %fdupes %{buildroot}/%{_prefix}

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING*
%{_kf5_dbuspolicydir}/org.kde.fontinst.conf
%{_kf5_dbuspolicydir}/org.kde.kcontrol.kcmclock.conf
%{_kf5_knsrcfilesdir}/colorschemes.knsrc
%{_kf5_knsrcfilesdir}/emoticons.knsrc
%{_kf5_knsrcfilesdir}/icons.knsrc
%{_kf5_knsrcfilesdir}/kfontinst.knsrc
%{_kf5_knsrcfilesdir}/plasma-themes.knsrc
%{_kf5_knsrcfilesdir}/lookandfeel.knsrc
%{_kf5_knsrcfilesdir}/xcursor.knsrc
%{_kf5_knsrcfilesdir}/ksplash.knsrc
%{_kf5_bindir}/kaccess
%{_kf5_bindir}/kapplymousetheme
%{_kf5_bindir}/kfontinst
%{_kf5_bindir}/kfontview
%{_kf5_bindir}/knetattach
%{_kf5_bindir}/krdb
%{_kf5_bindir}/kcm-touchpad-list-devices
%{_kf5_bindir}/solid-action-desktop-gen
%{_kf5_bindir}/lookandfeeltool
%{_kf5_bindir}/kcolorschemeeditor
%{_kf5_libdir}/kconf_update_bin/krdb_clearlibrarypath
%{_kf5_libdir}/libexec/
%{_kf5_libdir}/libkdeinit5_kaccess.so
%exclude %{_kf5_libdir}/libkfontinst.so
%{_kf5_libdir}/libkfontinst.so.*
%exclude %{_kf5_libdir}/libkfontinstui.so
%{_kf5_libdir}/libkfontinstui.so.*
%{_kf5_plugindir}/
%{_kf5_qmldir}/
%{_kf5_applicationsdir}/org.kde.kfontview.desktop
%{_kf5_applicationsdir}/org.kde.knetattach.desktop
%{_kf5_applicationsdir}/org.kde.kcolorschemeeditor.desktop
%{_kf5_sharedir}/dbus-1/services/org.kde.fontinst.service
%{_kf5_sharedir}/dbus-1/system-services/org.kde.fontinst.service
%{_kf5_sharedir}/dbus-1/system-services/org.kde.kcontrol.kcmclock.service
%{_kf5_sharedir}/polkit-1/actions/org.kde.fontinst.policy
%{_kf5_sharedir}/polkit-1/actions/org.kde.kcontrol.kcmclock.policy
%dir %{_kf5_htmldir}/en
%dir %{_kf5_htmldir}
%doc %{_kf5_htmldir}/en/*/
%dir %{_kf5_iconsdir}/hicolor/*/
%dir %{_kf5_iconsdir}/hicolor/*/*/
%{_kf5_iconsdir}/hicolor/*/*/*.*
%{_kf5_configkcfgdir}/
%{_kf5_sharedir}/kcm_componentchooser/
%{_kf5_sharedir}/kcm_phonon/
%{_kf5_sharedir}/kcmkeys/
%{_kf5_sharedir}/kcmsolidactions/
%{_kf5_sharedir}/kconf_update/
%{_kf5_sharedir}/kcontrol/
%{_kf5_sharedir}/kdisplay/
%{_kf5_sharedir}/kfontinst/
%{_kf5_sharedir}/kxmlgui5/
%{_kf5_sharedir}/kpackage/
%{_kf5_sharedir}/kcmmouse/
%{_kf5_sharedir}/color-schemes/
%{_kf5_sharedir}/kcmkeyboard/
%{_kf5_notifydir}/
%{_kf5_sharedir}/konqsidebartng/
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}/
%{_kf5_datadir}/
%{_kf5_sharedir}/solid/
%{_kf5_plasmadir}/
%{_kf5_appstreamdir}/
%{_kf5_libdir}/libexec/kimpanel-ibus-panel
%{_kf5_qmldir}/org/kde/plasma/private/kimpanel/
%{_kf5_servicesdir}/*kimpanel*
%{_kf5_plasmadir}/services/kimpanel.operations
%{_kf5_plasmadir}/plasmoids/org.kde.plasma.kimpanel/
%{_kf5_plugindir}/plasma/dataengine/plasma_engine_kimpanel.so
%{_kf5_debugdir}/*.categories

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
