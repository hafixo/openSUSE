#
# spec file for package kgoldrunner
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
Name:           kgoldrunner
Version:        19.08.0
Release:        0
Summary:        Action & Puzzle Solving Game
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
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
BuildRequires:  kcrash-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdoctools-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkdegames-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
Recommends:     %{name}-lang

%description
KGoldrunner is a game of action and puzzle solving

%lang_package

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

%files
%license COPYING*
%config %{_kf5_configdir}/kgoldrunner.knsrc
%doc %lang(en) %{_kf5_htmldir}/en/kgoldrunner/
%{_kf5_applicationsdir}/org.kde.kgoldrunner.desktop
%{_kf5_appsdir}/kgoldrunner
%{_kf5_appstreamdir}/org.kde.kgoldrunner.appdata.xml
%{_kf5_bindir}/kgoldrunner
%{_kf5_iconsdir}/hicolor/*/apps/kgoldrunner.*
%{_kf5_kxmlguidir}/kgoldrunner/
%{_kf5_debugdir}/kgoldrunner.categories

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
