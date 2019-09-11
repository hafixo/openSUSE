#
# spec file for package kdelibs4support
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


%define lname   libKF5KDELibs4Support5
%define _tar_path 5.61
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kdelibs4support
Version:        5.61.0
Release:        0
Summary:        Code and utilities to ease the transition to KDE Frameworks 5
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/portingAids/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/portingAids/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
BuildRequires:  NetworkManager-devel
BuildRequires:  cmake >= 3.0
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kbookmarks-devel >= %{_kf5_bugfix_version}
BuildRequires:  kcompletion-devel >= %{_kf5_bugfix_version}
BuildRequires:  kconfig-devel >= %{_kf5_bugfix_version}
BuildRequires:  kconfigwidgets-devel >= %{_kf5_bugfix_version}
BuildRequires:  kcrash-devel >= %{_kf5_bugfix_version}
BuildRequires:  kdbusaddons-devel >= %{_kf5_bugfix_version}
BuildRequires:  kded-devel >= %{_kf5_bugfix_version}
BuildRequires:  kdesignerplugin-devel >= %{_kf5_bugfix_version}
BuildRequires:  kdoctools-devel >= %{_kf5_bugfix_version}
BuildRequires:  kemoticons-devel >= %{_kf5_bugfix_version}
BuildRequires:  kf5-filesystem
BuildRequires:  kglobalaccel-devel >= %{_kf5_bugfix_version}
BuildRequires:  kguiaddons-devel >= %{_kf5_bugfix_version}
BuildRequires:  ki18n-devel >= %{_kf5_bugfix_version}
BuildRequires:  kiconthemes-devel >= %{_kf5_bugfix_version}
BuildRequires:  kio-devel >= %{_kf5_bugfix_version}
BuildRequires:  kitemviews-devel >= %{_kf5_bugfix_version}
BuildRequires:  knotifications-devel >= %{_kf5_bugfix_version}
BuildRequires:  kparts-devel >= %{_kf5_bugfix_version}
BuildRequires:  kservice-devel >= %{_kf5_bugfix_version}
BuildRequires:  ktextwidgets-devel >= %{_kf5_bugfix_version}
BuildRequires:  kunitconversion-devel >= %{_kf5_bugfix_version}
BuildRequires:  kwidgetsaddons-devel >= %{_kf5_bugfix_version}
BuildRequires:  kwindowsystem-devel >= %{_kf5_bugfix_version}
BuildRequires:  kxmlgui-devel >= %{_kf5_bugfix_version}
BuildRequires:  perl-URI
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Concurrent) >= 5.6.0
BuildRequires:  cmake(Qt5Core) >= 5.6.0
BuildRequires:  cmake(Qt5DBus) >= 5.6.0
BuildRequires:  cmake(Qt5Designer) >= 5.6.0
BuildRequires:  cmake(Qt5Network) >= 5.6.0
BuildRequires:  cmake(Qt5PrintSupport) >= 5.6.0
BuildRequires:  cmake(Qt5Svg) >= 5.6.0
BuildRequires:  cmake(Qt5Test) >= 5.6.0
BuildRequires:  cmake(Qt5Widgets) >= 5.6.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.6.0
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
Recommends:     %{name}-lang = %{version}
Provides:       kde4support = %{version}
Obsoletes:      kde4support < %{version}

%description
This package includes CMake macros and C++
classes whose functionality has been replaced by code in CMake, Qt and
other frameworks.

Code should aim to port away from this framework eventually.  The API
documentation of the classes in this framework and the notes at
<https://community.kde.org/Frameworks/Porting_Notes> should help with
this.

Note that some of the classes in this framework, especially
KStandardDirs, may not work correctly unless any libraries and other
software using the KDE4 Support framework are installed to the same
location as KDELibs4Support, although it may be sufficient to set the
KDEDIRS environment variable correctly.

%package -n kssl
Summary:        Code and utilities to ease the transition to KDE Frameworks 5
License:        GPL-2.0-or-later
Group:          System/GUI/KDE

%description -n kssl
This package includes CMake macros and C++
classes whose functionality has been replaced by code in CMake, Qt and
other frameworks.

Code should aim to port away from this framework eventually.  The API
documentation of the classes in this framework and the notes at
<https://community.kde.org/Frameworks/Porting_Notes> should help with
this.

Note that some of the classes in this framework, especially
KStandardDirs, may not work correctly unless any libraries and other
software using the KDE4 Support framework are installed to the same
location as KDELibs4Support, although it may be sufficient to set the
KDEDIRS environment variable correctly.

%package -n %{lname}
Summary:        Code and utilities to ease the transition to KDE Frameworks 5
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
Requires:       kded >= %{_kf5_bugfix_version}

%description -n %{lname}
This package includes CMake macros and C++
classes whose functionality has been replaced by code in CMake, Qt and
other frameworks.

Code should aim to port away from this framework eventually.  The API
documentation of the classes in this framework and the notes at
<https://community.kde.org/Frameworks/Porting_Notes> should help with
this.

Note that some of the classes in this framework, especially
KStandardDirs, may not work correctly unless any libraries and other
software using the KDE4 Support framework are installed to the same
location as KDELibs4Support, although it may be sufficient to set the
KDEDIRS environment variable correctly.

%package devel
Summary:        Code and utilities to ease the transition to KDE Frameworks 5
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       %{name} = %{version}
Requires:       extra-cmake-modules
Requires:       karchive-devel >= %{_kf5_bugfix_version}
Requires:       kauth-devel >= %{_kf5_bugfix_version}
Requires:       kconfigwidgets-devel >= %{_kf5_bugfix_version}
Requires:       kcoreaddons-devel >= %{_kf5_bugfix_version}
Requires:       kcrash-devel >= %{_kf5_bugfix_version}
Requires:       kdbusaddons-devel >= %{_kf5_bugfix_version}
Requires:       kdesignerplugin-devel >= %{_kf5_bugfix_version}
Requires:       kdoctools-devel >= %{_kf5_bugfix_version}
Requires:       kemoticons-devel >= %{_kf5_bugfix_version}
Requires:       kguiaddons-devel >= %{_kf5_bugfix_version}
Requires:       kiconthemes-devel >= %{_kf5_bugfix_version}
Requires:       kinit-devel >= %{_kf5_bugfix_version}
Requires:       kitemmodels-devel >= %{_kf5_bugfix_version}
Requires:       knotifications-devel >= %{_kf5_bugfix_version}
Requires:       kparts-devel >= %{_kf5_bugfix_version}
Requires:       ktextwidgets-devel >= %{_kf5_bugfix_version}
Requires:       kunitconversion-devel >= %{_kf5_bugfix_version}
Requires:       kwindowsystem-devel >= %{_kf5_bugfix_version}
Requires:       cmake(Qt5Core) >= 5.6.0
Requires:       cmake(Qt5DBus) >= 5.6.0
Requires:       cmake(Qt5PrintSupport) >= 5.6.0
Requires:       cmake(Qt5Xml) >= 5.6.0
Provides:       kde4support-devel = %{version}
Obsoletes:      kde4support-devel < %{version}

%description devel
This package includes CMake macros and C++
classes whose functionality has been replaced by code in CMake, Qt and
other frameworks.

Code should aim to port away from this framework eventually.  The API
documentation of the classes in this framework and the notes at
<https://community.kde.org/Frameworks/Porting_Notes> should help with
this.

Note that some of the classes in this framework, especially
KStandardDirs, may not work correctly unless any libraries and other
software using the KDE4 Support framework are installed to the same
location as KDELibs4Support, although it may be sufficient to set the
KDEDIRS environment variable correctly. Development files.

%lang_package

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%if %{with lang}
%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%if %{with lang}
%files lang -f %{name}.lang
%endif

%files
%license COPYING*
%doc README*
%{_kf5_bindir}/kdebugdialog5
%{_kf5_bindir}/kf5-config
%{_kf5_configdir}/colors/
%{_kf5_configdir}/kdebug.areas
%{_kf5_configdir}/kdebugrc
%{_kf5_libexecdir}/filesharelist
%{_kf5_libexecdir}/fileshareset
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
# within kssl package
%exclude %{_kf5_plugindir}/kcm_ssl.so
%exclude %{_kf5_servicesdir}/kcm_ssl.desktop
%{_kf5_servicetypesdir}/
%{_kf5_datadir}/kdoctools/
%{_kf5_datadir}/widgets/
%{_kf5_sharedir}/locale/kf5_all_languages
%{_kf5_datadir}/locale/
%doc %lang(en) %{_kf5_mandir}/*/kf5-config.*
%dir %{_kf5_htmldir}/en
%dir %{_kf5_htmldir}
%doc %lang(en) %{_kf5_htmldir}/en/*/

%files -n kssl
%license COPYING*
%doc README*
%{_kf5_configdir}/ksslcalist
%{_kf5_plugindir}/kcm_ssl.so
%{_kf5_servicesdir}/kcm_ssl.desktop
%{_kf5_datadir}/kssl/

%files -n %{lname}
%license COPYING*
%doc README*
%{_kf5_libdir}/libKF5KDELibs4Support.so.*

%files devel
%{_kf5_libdir}/libKF5KDELibs4Support.so
%{_kf5_libdir}/cmake/KF5KDELibs4Support/
%{_kf5_libdir}/cmake/KF5KDE4Support/
%{_kf5_libdir}/cmake/KDELibs4/
%{_kf5_includedir}/kdelibs4support_version.h
%{_kf5_includedir}/KDELibs4Support/
%dir %{_kf5_includedir}/KDELibs4Support/
%{_kf5_sharedir}/dbus-1/interfaces/kf5_org.freedesktop.PowerManagement.Inhibit.xml
%{_kf5_sharedir}/dbus-1/interfaces/kf5_org.freedesktop.PowerManagement.xml
%{_kf5_sharedir}/dbus-1/interfaces/kf5_org.kde.Solid.Networking.Client.xml
%{_kf5_sharedir}/dbus-1/interfaces/kf5_org.kde.Solid.PowerManagement.PolicyAgent.xml

%changelog
