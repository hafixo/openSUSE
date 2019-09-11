#
# spec file for package kmediaplayer
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


%define lname   libKF5MediaPlayer5
%define _tar_path 5.61
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
# Only needed for the package signature condition
%bcond_without lang
Name:           kmediaplayer
Version:        5.61.0
Release:        0
Summary:        Interface for media player KParts
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/portingAids/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/portingAids/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
BuildRequires:  cmake >= 3.0
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kbookmarks-devel >= %{_kf5_bugfix_version}
BuildRequires:  kcompletion-devel >= %{_kf5_bugfix_version}
BuildRequires:  kconfigwidgets-devel >= %{_kf5_bugfix_version}
BuildRequires:  kdbusaddons-devel >= %{_kf5_bugfix_version}
BuildRequires:  kf5-filesystem
BuildRequires:  kguiaddons-devel >= %{_kf5_bugfix_version}
BuildRequires:  ki18n-devel >= %{_kf5_bugfix_version}
BuildRequires:  kiconthemes-devel >= %{_kf5_bugfix_version}
BuildRequires:  kio-devel >= %{_kf5_bugfix_version}
BuildRequires:  kitemviews-devel >= %{_kf5_bugfix_version}
BuildRequires:  knotifications-devel >= %{_kf5_bugfix_version}
BuildRequires:  kparts-devel >= %{_kf5_bugfix_version}
BuildRequires:  kservice-devel >= %{_kf5_bugfix_version}
BuildRequires:  ktextwidgets-devel >= %{_kf5_bugfix_version}
BuildRequires:  kwidgetsaddons-devel >= %{_kf5_bugfix_version}
BuildRequires:  kwindowsystem-devel >= %{_kf5_bugfix_version}
BuildRequires:  kxmlgui-devel >= %{_kf5_bugfix_version}
BuildRequires:  solid-devel >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5DBus) >= 5.6.0
BuildRequires:  cmake(Qt5Test) >= 5.6.0
BuildRequires:  cmake(Qt5Widgets) >= 5.6.0

%description
KMediaPlayer builds on the KParts framework to provide a common interface for
KParts that can play media files.

%package -n %{lname}
Summary:        Interface for media player KParts
Group:          System/GUI/KDE
Obsoletes:      libKF5MediaPlayer4

%description -n %{lname}
KMediaPlayer builds on the KParts framework to provide a common interface for
KParts that can play media files.

%package devel
Summary:        Interface for media player KParts: Build Environment
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       ki18n-devel >= %{_kf5_bugfix_version}
Requires:       kparts-devel >= %{_kf5_bugfix_version}

%description devel
KMediaPlayer builds on the KParts framework to provide a common interface for
KParts that can play media files. Development files.

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%{_kf5_libdir}/libKF5MediaPlayer.so.*
%dir %{_kf5_servicetypesdir}
%{_kf5_servicetypesdir}/kmediaplayerengine.desktop
%{_kf5_servicetypesdir}/kmediaplayer.desktop

%files devel
%{_kf5_libdir}/libKF5MediaPlayer.so
%{_kf5_libdir}/cmake/KF5MediaPlayer/
%{_kf5_includedir}/*.h
%dir %{_kf5_includedir}/*/
%{_kf5_includedir}/*/
%{_kf5_dbusinterfacesdir}/kf5_org.kde.KMediaPlayer.xml

%changelog
