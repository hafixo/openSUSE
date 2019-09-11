#
# spec file for package kmix
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without	lang
Name:           kmix
Version:        19.08.0
Release:        0
Summary:        Sound Mixer
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Mixers
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  alsa-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  glib2-devel
BuildRequires:  kcompletion-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kf5-filesystem
BuildRequires:  kglobalaccel-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  knotifications-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libpulse-devel
BuildRequires:  pkgconfig
BuildRequires:  plasma-framework-devel
BuildRequires:  solid-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
KMix is a fully featured audio mixer by KDE.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif
  %suse_update_desktop_file org.kde.kmix           AudioVideo Mixer

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%config %{_kf5_configdir}/autostart/*kmix*.desktop
%{_datadir}/plasma/services/
%{_kf5_applicationsdir}/*kmix*.desktop
%{_kf5_bindir}/kmix*
%{_kf5_dbusinterfacesdir}/org.kde.kmix.*
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_kxmlguidir}/kmix/
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_sharedir}/kmix/
%dir %{_kf5_htmldir}/en/kmix/
%{_kf5_htmldir}/en/kmix/*
%{_kf5_appstreamdir}/org.kde.kmix.appdata.xml
%{_libdir}/libkmixcore.so.*
%{_kf5_notifydir}/kmix.notifyrc

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
