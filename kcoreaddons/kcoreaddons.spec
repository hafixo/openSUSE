#
# spec file for package kcoreaddons
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


%define lname   libKF5CoreAddons5
%define _tar_path 5.61
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kcoreaddons
Version:        5.61.0
Release:        0
Summary:        Utilities for core application functionality and accessing the OS
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
BuildRequires:  extra-cmake-modules >= %{_tar_path}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  shared-mime-info
BuildRequires:  cmake(Qt5Core) >= 5.6.0
Requires:       shared-mime-info
%if %{with lang}
BuildRequires:  cmake(Qt5LinguistTools) >= 5.6.0
%endif
Recommends:     %{name}-lang = %{version}

%description
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more.

%package -n %{lname}
Summary:        Utilities for core application functionality and accessing the OS
Group:          System/GUI/KDE
%requires_ge    libQt5Core5
Recommends:     %{name} = %{version}

%description -n %{lname}
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more.

%package devel
Summary:        Utilities for core application functionality and accessing the OS
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       %{name} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(Qt5Core) >= 5.6.0

%description devel
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more. Development files.

%lang_package

%prep
%setup -q

%build
  %cmake_kf5 -d build -- -Dlconvert_executable=%{_kf5_libdir}/qt5/bin/lconvert -DKDE4_DEFAULT_HOME=".kde4"
  %make_jobs

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%if %{with lang}
%find_lang %{name}5 --with-qt --without-mo
%endif

%post -n %{lname} -p /sbin/ldconfig
%post
%mime_database_post

%postun -n %{lname} -p /sbin/ldconfig
%postun
%mime_database_postun

%if %{with lang}
%files lang -f %{name}5.lang
%endif

%files
%license COPYING*
%doc README*
%{_kf5_appsdir}/mime/packages/kde5.xml
%{_kf5_datadir}/

%files -n %{lname}
%license COPYING*
%doc README*
%{_kf5_libdir}/libKF5CoreAddons.so.*
%{_kf5_debugdir}/kcoreaddons.categories

%files devel
%{_kf5_bindir}/desktoptojson
%{_kf5_libdir}/libKF5CoreAddons.so
%{_kf5_libdir}/cmake/KF5CoreAddons/
%{_kf5_includedir}/
%{_kf5_mkspecsdir}/qt_KCoreAddons.pri

%changelog
