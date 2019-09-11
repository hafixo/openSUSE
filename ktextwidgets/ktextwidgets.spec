#
# spec file for package ktextwidgets
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


%define lname   libKF5TextWidgets5
%define _tar_path 5.61
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           ktextwidgets
Version:        5.61.0
Release:        0
Summary:        KDE Text editing widgets
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
BuildRequires:  kcompletion-devel >= %{_kf5_bugfix_version}
BuildRequires:  kconfig-devel >= %{_kf5_bugfix_version}
BuildRequires:  kconfigwidgets-devel >= %{_kf5_bugfix_version}
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel >= %{_kf5_bugfix_version}
BuildRequires:  kiconthemes-devel >= %{_kf5_bugfix_version}
BuildRequires:  kservice-devel >= %{_kf5_bugfix_version}
BuildRequires:  kwidgetsaddons-devel >= %{_kf5_bugfix_version}
BuildRequires:  kwindowsystem-devel >= %{_kf5_bugfix_version}
BuildRequires:  sonnet-devel >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Core) >= 5.6.0
BuildRequires:  cmake(Qt5Test) >= 5.6.0
BuildRequires:  cmake(Qt5TextToSpeech)
# uncomment after 5.61
# BuildRequires:  cmake(Qt5UiPlugin) >= 5.6.0
BuildRequires:  cmake(Qt5Widgets) >= 5.6.0

%description
KTextWidgets provides widgets for displaying and editing text. It supports
rich text as well as plain text.

%package -n %{lname}
Summary:        KDE Text editing widgets
Group:          System/GUI/KDE
Obsoletes:      libKF5TextWidgets4
%if %{with lang}
Recommends:     %{lname}-lang = %{version}
%endif

%description -n %{lname}
KTextWidgets provides widgets for displaying and editing text. It supports
rich text as well as plain text.

%package devel
Summary:        KDE Text editing widgets: Build Environment
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       ki18n-devel >= %{_kf5_bugfix_version}
Requires:       sonnet-devel >= %{_kf5_bugfix_version}
Requires:       cmake(Qt5Widgets) >= 5.6.0

%description devel
KTextWidgets provides widgets for displaying and editing text. It supports
rich text as well as plain text. Development files.

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
%find_lang %{name}5
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%if %{with lang}
%files -n %{lname}-lang -f %{name}5.lang
%endif

%files -n %{lname}
%license COPYING*
%{_kf5_libdir}/libKF5TextWidgets.so.*
%dir %{_kf5_servicetypesdir}
%{_kf5_servicetypesdir}/kregexpeditor.desktop

%files devel
%{_kf5_libdir}/libKF5TextWidgets.so
%{_kf5_libdir}/cmake/KF5TextWidgets/
%{_kf5_includedir}/*.h
%dir %{_kf5_includedir}/*/
# %dir %{_kf5_plugindir}/designer
# %{_kf5_plugindir}/designer/ktextwidgets5widgets.so
%{_kf5_includedir}/*/
%{_kf5_mkspecsdir}/qt_KTextWidgets.pri

%changelog
