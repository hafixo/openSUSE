#
# spec file for package libgravatar
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           libgravatar
Version:        19.08.0
Release:        0
Summary:        Library to download and display gravatars
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kconfig-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  pimcommon-devel >= %{_kapp_version}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Network) >= 5.6.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.6.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.6.0
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
This package contains the debug categories for the libgravatar library.

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
%endif

%package -n libKF5Gravatar5
Summary:        Libgravatar library for kdepim
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       %{name}

%description -n libKF5Gravatar5
libgravatar adds support for downloading and displaying gravatars in
applications.

%post  -n libKF5Gravatar5 -p /sbin/ldconfig
%postun -n libKF5Gravatar5 -p /sbin/ldconfig

%package devel
Summary:        Development package for libgravatar
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
Requires:       libKF5Gravatar5 = %{version}

%description devel
The development package for the libgravatar library

%files devel
%license COPYING*
%{_kf5_cmakedir}/KF5Gravatar/
%{_kf5_includedir}/Gravatar/
%{_kf5_includedir}/gravatar/
%{_kf5_includedir}/gravatar_version.h
%{_kf5_libdir}/libKF5Gravatar.so
%{_kf5_mkspecsdir}/qt_Gravatar.pri

%files
%license COPYING*
%{_kf5_debugdir}/libgravatar.categories
%{_kf5_debugdir}/libgravatar.renamecategories

%files -n libKF5Gravatar5
%license COPYING*
%{_libdir}/libKF5Gravatar.so.*

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
