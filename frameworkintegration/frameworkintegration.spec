#
# spec file for package frameworkintegration
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


%define lname   libKF5Style5
%define _tar_path 5.61
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
# Only needed for the package signature condition
%bcond_without lang
Name:           frameworkintegration
Version:        5.61.0
Release:        0
Summary:        Plugins responsible for better integration of Qt applications in KDE Workspace
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
BuildRequires:  kconfig-devel >= %{_kf5_bugfix_version}
BuildRequires:  kconfigwidgets-devel >= %{_kf5_bugfix_version}
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel >= %{_kf5_bugfix_version}
BuildRequires:  kiconthemes-devel >= %{_kf5_bugfix_version}
BuildRequires:  kio-devel >= %{_kf5_bugfix_version}
BuildRequires:  knotifications-devel >= %{_kf5_bugfix_version}
BuildRequires:  kpackage-devel >= %{_kf5_bugfix_version}
BuildRequires:  kwidgetsaddons-devel >= %{_kf5_bugfix_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(Qt5DBus) >= 5.6.0
BuildRequires:  cmake(Qt5Widgets) >= 5.6.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.6.0
BuildRequires:  cmake(packagekitqt5)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcursor)
%if 0%{?suse_version} >= 1330 || (0%{?sle_version} >= 120200 && 0%{?is_opensuse})
BuildRequires:  cmake(AppStreamQt) >= 0.10.4
%endif

%description
Framework Integration is a set of plugins responsible for better
integration of Qt applications when running on a
KDE Plasma workspace.

Applications do not need to link to this directly.

%package -n %{lname}
Summary:        Plugins responsible for better integration of Qt applications in KDE Workspace
Group:          System/GUI/KDE
Obsoletes:      %{lname}-lang < %{version}
Obsoletes:      libKF5Style4

%description -n %{lname}
Framework Integration is a set of plugins responsible for better
integration of Qt applications when running on a
KDE Plasma workspace.

Applications do not need to link to this directly.

%package plugin
Summary:        Plugins responsible for better integration of Qt applications in KDE Workspace
Group:          System/GUI/KDE
Requires:       plasma5-integration-plugin
Conflicts:      %{lname} < 5.6.0

%description plugin
Framework Integration is a set of plugins responsible for better
integration of Qt applications when running on a
KDE Plasma workspace.

Applications do not need to link to this directly.

%package devel
Summary:        Plugins responsible for better integration of Qt applications in KDE Workspace
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       kconfigwidgets-devel >= %{_kf5_bugfix_version}
Requires:       kiconthemes-devel >= %{_kf5_bugfix_version}

%description devel
Framework Integration is a set of plugins responsible for better
integration of Qt applications when running on a
KDE Plasma workspace.

Applications do not need to link to this directly. Development files

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
%license COPYING*
%doc README*
%{_kf5_libdir}/libKF5Style.so.*

%files plugin
%license COPYING*
%doc README*
%{_kf5_datadir}/infopage/
%{_kf5_plugindir}/
%{_kf5_libexecdir}/
%{_kf5_notifydir}/

%files devel
%license COPYING*
%{_kf5_libdir}/libKF5Style.so
%{_kf5_libdir}/cmake/KF5FrameworkIntegration/
%dir %{_kf5_includedir}/KStyle/
%{_kf5_includedir}/KStyle/
%{_kf5_includedir}/*.h

%changelog
