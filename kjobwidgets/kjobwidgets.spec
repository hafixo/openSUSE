#
# spec file for package kjobwidgets
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


%define lname   libKF5JobWidgets5
%define _tar_path 5.61
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kjobwidgets
Version:        5.61.0
Release:        0
Summary:        Widgets for showing progress of asynchronous jobs
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
BuildRequires:  cmake >= 3.0
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kcoreaddons-devel >= %{_kf5_bugfix_version}
BuildRequires:  kf5-filesystem
BuildRequires:  kwidgetsaddons-devel >= %{_kf5_bugfix_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5DBus) >= 5.6.0
BuildRequires:  cmake(Qt5Test) >= 5.6.0
BuildRequires:  cmake(Qt5Widgets) >= 5.6.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.6.0
BuildRequires:  pkgconfig(x11)
%if %{with lang}
BuildRequires:  cmake(Qt5LinguistTools) >= 5.6.0
%endif

%description
KJobWIdgets provides widgets for showing progress of asynchronous jobs.

%package -n %{lname}
Summary:        Widgets for showing progress of asynchronous jobs
Group:          System/GUI/KDE
Recommends:     %{lname}-lang = %{version}

%description -n %{lname}
KJobWIdgets provides widgets for showing progress of asynchronous jobs.

%package devel
Summary:        Widgets for showing progress of asynchronous jobs
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       kcoreaddons-devel >= %{_kf5_bugfix_version}
Requires:       cmake(Qt5Widgets) >= 5.6.0

%description devel
KJobWIdgets provides widgets for showing progress of asynchronous jobs.
Development files.

%lang_package -n %{lname}

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%if %{with lang}
%find_lang %{name}5 --with-qt --without-mo
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%if %{with lang}
%files -n %{lname}-lang -f %{name}5.lang
%endif

%files -n %{lname}
%license COPYING*
%{_kf5_libdir}/libKF5JobWidgets.so.*
%{_kf5_debugdir}/*.categories

%files devel
%{_kf5_libdir}/libKF5JobWidgets.so
%{_kf5_libdir}/cmake/KF5JobWidgets/
%{_kf5_includedir}/*.h
%dir %{_kf5_includedir}/*/
%{_kf5_includedir}/*/
%{_kf5_mkspecsdir}/qt_KJobWidgets.pri
%{_kf5_dbusinterfacesdir}/kf5_org.kde.JobView.xml
%{_kf5_dbusinterfacesdir}/kf5_org.kde.JobViewServer.xml
%{_kf5_dbusinterfacesdir}/kf5_org.kde.JobViewV2.xml

%changelog
