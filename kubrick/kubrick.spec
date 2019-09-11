#
# spec file for package kubrick
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
Name:           kubrick
Version:        19.08.0
Release:        0
Summary:        Game based on Rubik's Cube
License:        GPL-2.0-or-later
Group:          Amusements/Games/Logic
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
BuildRequires:  kdoctools-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkdegames-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(glu)
Obsoletes:      kubrick5 < %{version}
Provides:       kubrick5 = %{version}
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
This package contains the KDE game Kubrick which is based on Rubik's
Cube.

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

%files
%license COPYING COPYING.DOC
%doc %lang(en) %{_kf5_htmldir}/en/kubrick/
%{_kf5_applicationsdir}/org.kde.kubrick.desktop
%{_kf5_appstreamdir}/org.kde.kubrick.appdata.xml
%{_kf5_bindir}/kubrick
%{_kf5_debugdir}/kubrick.categories
%{_kf5_iconsdir}/hicolor/*/*/kubrick*
%{_kf5_kxmlguidir}/kubrick/
%{_kf5_sharedir}/kubrick/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
