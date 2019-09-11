#
# spec file for package syndication
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


%define lname libKF5Syndication5
%define _tar_path 5.61
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           syndication
Version:        5.61.0
Release:        0
Summary:        RSS/Atom parsing library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= 1.0.0
BuildRequires:  kcodecs-devel >= %{kf5_bugfix_version}
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Test) >= 5.8.0
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)

%description
KF5Syndication is an RSS/Atom parsing library by KDE, which
also provides an API to fetch feeds from the network.

%package -n %{lname}
Summary:        RSS/Atom parsing library
Group:          System/Libraries

%description  -n libKF5Syndication5
KF5Syndication is an RSS/Atom parsing library, which
also provides an API to fetch feeds from the network.
This package contains the base library.

%package devel
Summary:        RSS/Atom parsing library - development headers
Group:          Development/Libraries/KDE
Requires:       libKF5Syndication5 = %{version}

%description devel
KF5Syndication is an RSS/Atom parsing library, which
also provides an API to fetch feeds from the network. This
package contains development headers.

%prep
%setup -q -n syndication-%{version}

%build
  %cmake_kf5 -d build -- -DBUILD_TESTING=ON -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
  %make_jobs

%install
  %kf5_makeinstall -C build

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_kf5_libdir}/libKF5Syndication.so.*
%{_kf5_debugdir}/syndication.categories

%files devel
%license COPYING*
%{_kf5_cmakedir}/KF5Syndication/
%{_kf5_includedir}/Syndication/
%{_kf5_includedir}/syndication_version.h
%{_kf5_libdir}/libKF5Syndication.so
%{_kf5_mkspecsdir}/qt_Syndication.pri

%changelog
