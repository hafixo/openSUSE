#
# spec file for package kpackage
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
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kpackage
Version:        5.61.0
Release:        0
Summary:        Non-binary asset user-installable package managing framework
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
BuildRequires:  karchive-devel >= %{_kf5_bugfix_version}
BuildRequires:  kconfig-devel >= %{_kf5_bugfix_version}
BuildRequires:  kcoreaddons-devel >= %{_kf5_bugfix_version}
BuildRequires:  kdoctools-devel >= %{_kf5_bugfix_version}
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Core) >= 5.8.0
BuildRequires:  cmake(Qt5DBus) >= 5.8.0
BuildRequires:  cmake(Qt5Test) >= 5.8.0
Recommends:     %{name}-lang

%description
This framework lets applications to manage user installable packages of non-binary assets.

%package devel
Summary:        Non-binary asset user-installable package managing framework
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       extra-cmake-modules
Requires:       kcoreaddons-devel >= %{_kf5_bugfix_version}

%description devel
This framework lets applications to manage user installable packages of non-binary assets.
Development files.

%lang_package

%prep
%setup -q

%build
  %cmake_kf5 -d build -- -DSYSCONF_INSTALL_DIR=%{_kf5_sysconfdir}
  %make_jobs

%install
  %kf5_makeinstall -C build

%if %{with lang}
%find_lang %{name} --with-man --all-name
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%if %{with lang}
%files lang -f %{name}.lang
%endif

%files
%license COPYING*
%doc README*
%{_kf5_bindir}/kpackagetool*
%{_kf5_libdir}/libKF5Package.so.*
%dir %{_kf5_servicetypesdir}
%{_kf5_servicetypesdir}/kpackage-packagestructure.desktop
%{_kf5_servicetypesdir}/kpackage-generic.desktop
%{_kf5_servicetypesdir}/kpackage-genericqml.desktop
%doc %lang(en) %{_kf5_mandir}/*/kpackagetool*
%{_kf5_debugdir}/*.categories

%files devel
%{_kf5_libdir}/libKF5Package.so
%{_kf5_libdir}/cmake/KF5Package/
%{_kf5_includedir}/

%changelog
