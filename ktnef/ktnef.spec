#
# spec file for package ktnef
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


%define kf5_version 5.19.0
%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           ktnef
Version:        19.08.0
Release:        0
Summary:        KDE PIM Libraries: TNEF support
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= 5.19.0
BuildRequires:  kcalcore-devel
BuildRequires:  kcalutils-devel >= %{_kapp_version}
BuildRequires:  kcontacts-devel
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Test) >= 5.2.0
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
This package contains additional libraries for KDE PIM applications.

%package -n libKF5Tnef5
Summary:        KDE PIM Libraries: TNEF Support
Group:          System/Libraries

%description  -n libKF5Tnef5
This package contains the TNEF support library for KDE PIM applications

%package devel
Summary:        KDE PIM Libraries: Build Environment
Group:          Development/Libraries/KDE
Requires:       kcalcore-devel
Requires:       libKF5Tnef5 = %{version}

%description devel
This package contains necessary include files and libraries needed
to develop KDE PIM applications.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q -n ktnef-%{version}

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -n libKF5Tnef5 -p /sbin/ldconfig
%postun -n libKF5Tnef5 -p /sbin/ldconfig

%files -n libKF5Tnef5
%license COPYING.LIB
%{_kf5_libdir}/libKF5Tnef.so.*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%license COPYING.LIB
%{_kf5_cmakedir}/KF5Tnef/
%{_kf5_includedir}/KTNEF/
%{_kf5_includedir}/ktnef_version.h
%{_kf5_libdir}/libKF5Tnef.so
%{_kf5_mkspecsdir}/qt_KTNef.pri

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
