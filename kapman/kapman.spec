#
# spec file for package kapman
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
Name:           kapman
Version:        19.08.0
Release:        0
Summary:        Pac-Man-like game for KDE
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
BuildRequires:  kdelibs4support-devel
BuildRequires:  kguiaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kitemviews-devel
BuildRequires:  knewstuff-devel
BuildRequires:  knotifyconfig-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkdegames-devel
BuildRequires:  phonon4qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5QuickWidgets)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
Kapman is a clone of the well known game Pac-Man. You must go through the levels escaping ghosts in a maze. You lose a life when a ghost eats you, but you can eat the ghosts for a few seconds when eating an energizer. You win points when eating pills, energizers, and bonus, and you win one life for each 10,000 points. When you have eaten all the pills and energizers of a level, you go to the next level, and the player and ghost speeds increase. The game ends when you have lost all your lives.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q -n kapman-%{version}

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file -r org.kde.kapman          Game ArcadeGame

%files
%license COPYING COPYING.DOC
%{_kf5_sharedir}/sounds/kapman/
%{_kf5_applicationsdir}/org.kde.kapman.desktop
%{_kf5_appsdir}/kapman/
%{_kf5_appstreamdir}/
%{_kf5_bindir}/kapman
%doc %lang(en) %{_kf5_htmldir}/en/kapman/
%{_kf5_iconsdir}/hicolor/*/apps/kapman.*
%{_kf5_kxmlguidir}/kapman/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
