#
# spec file for package killbots
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
%bcond_without lang
Name:           killbots
Version:        19.08.0
Release:        0
Summary:        Robots-like game by KDE
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kguiaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kitemviews-devel
BuildRequires:  knotifyconfig-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkdegames-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5QuickWidgets)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
Killbots is a turn-based game of evading "killer" robots on a board.
Robots home in on the player, but can crash into other robots or
debris, rendering them inert. The player has to strategically move
and can optionally use teleportation to a random location.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q -n killbots-%{version}

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif

%files
%license COPYING*
%dir %{_kf5_configkcfgdir}
%doc %lang(en) %{_kf5_htmldir}/en/killbots/
%{_kf5_applicationsdir}/org.kde.killbots.desktop
%{_kf5_bindir}/killbots
%{_kf5_configkcfgdir}/killbots.kcfg
%{_kf5_iconsdir}/hicolor/*/apps/killbots.*
%{_kf5_sharedir}/killbots/
%{_kf5_appstreamdir}/org.kde.killbots.appdata.xml

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
