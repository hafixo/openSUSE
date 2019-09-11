#
# spec file for package kded
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
Name:           kded
Version:        5.61.0
Release:        0
Summary:        Central daemon of KDE workspaces
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
# PATCH-FIX-OPENSUSE (for now mostly to get openQA's opinion)
Patch100:       0001-Decrease-the-delay-between-change-notification-and-s.patch
BuildRequires:  cmake >= 3.0
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kcoreaddons-devel >= %{_kf5_bugfix_version}
BuildRequires:  kcrash-devel >= %{_kf5_bugfix_version}
BuildRequires:  kdbusaddons-devel >= %{_kf5_bugfix_version}
BuildRequires:  kdoctools-devel >= %{_kf5_bugfix_version}
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel >= %{_kf5_bugfix_version}
BuildRequires:  kinit-devel >= %{_kf5_bugfix_version}
BuildRequires:  kservice-devel >= %{_kf5_bugfix_version}
BuildRequires:  kwindowsystem-devel >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Core) >= 5.6.0
BuildRequires:  cmake(Qt5DBus) >= 5.6.0
BuildRequires:  cmake(Qt5Network) >= 5.6.0
BuildRequires:  cmake(Qt5Test) >= 5.6.0
BuildRequires:  cmake(Qt5Widgets) >= 5.6.0
BuildRequires:  cmake(Qt5Xml) >= 5.6.0
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
KDED runs in the background and performs a number of small tasks.
Some of these tasks are built in, others are started on demand.

%package devel
Summary:        Central daemon of KDE workspaces: Build Environment
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       extra-cmake-modules

%description devel
KDED runs in the background and performs a number of small tasks.
Some of these tasks are built in, others are started on demand.
Development files.

%lang_package

%prep
%autosetup -p1

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

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
%{_kf5_libdir}/libkdeinit5_kded5.so
%{_kf5_bindir}/kded5
%{_kf5_sharedir}/dbus-1/services/org.kde.kded5.service
%dir %{_kf5_servicetypesdir}
%{_kf5_servicetypesdir}/kdedmodule.desktop
%doc %lang(en) %{_kf5_mandir}/*/kded5.*
%{_kf5_debugdir}/kded.categories
%{_kf5_applicationsdir}/org.kde.kded5.desktop

%files devel
%{_kf5_libdir}/cmake/KDED/
%{_kf5_dbusinterfacesdir}/org.kde.kded5.xml

%changelog
