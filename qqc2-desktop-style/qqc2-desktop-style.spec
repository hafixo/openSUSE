#
# spec file for package qqc2-desktop-style
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


%define _tar_path 5.61
# Only needed for the package signature condition
%bcond_without lang
Name:           qqc2-desktop-style
Version:        5.61.0
Release:        0
Summary:        A Qt Quick Controls 2 Style for Desktop UIs
License:        GPL-2.0-or-later
Group:          Development/Libraries/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/qqc2-desktop-style-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/qqc2-desktop-style-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= 0.0.8
# For dir ownership
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kf5-filesystem
BuildRequires:  kiconthemes-devel
BuildRequires:  kirigami2-devel
BuildRequires:  cmake(Qt5Core) >= 5.9.1
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
Requires:       libqt5-qtquickcontrols2
# plasma5-workspace sets up the env variables so that this theme
# is picked by default. It still works fine without it (no requires),
# but looks better with it. By itself plasma5-workspace does not use
# it (yet), so only install it with libqt5-qtquickcontrols2.
Supplements:    packageand(plasma5-workspace:libqt5-qtquickcontrols2)
# For KUA users
Provides:       plasma5-qqc2-style = %{version}
Obsoletes:      plasma5-qqc2-style < %{version}

%description
A Qt Quick Controls 2 style engine that uses the desktop style
to draw controls with QStyle.

%package devel
Summary:        Development Files for Qt Quick Controls 2 Desktop Style
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       extra-cmake-modules

%description devel
This file contains cmake files to be used by projects that depend on
qqc2-desktop-style.
Usually not needed as it is only a runtime dependency.

%prep
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build

%files
%license LICENSE*
%{_kf5_qmldir}/QtQuick/Controls.2/org.kde.desktop/
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%dir %{_kf5_plugindir}/kf5/kirigami/
%{_kf5_plugindir}/kf5/kirigami/org.kde.desktop.so
%{_kf5_qmldir}/org/kde/qqc2desktopstyle/

%files devel
%{_kf5_libdir}/cmake/KF5QQC2DeskopStyle/

%changelog
