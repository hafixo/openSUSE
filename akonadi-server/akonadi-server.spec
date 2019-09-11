#
# spec file for package akonadi-server
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


%define rname   akonadi
%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           akonadi-server
Version:        19.08.0
Release:        0
Summary:        PIM Storage Service
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://akonadi-project.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Source99:       akonadi-server-rpmlintrc
BuildRequires:  cmake >= 3.0.0
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  libQt5Sql-private-headers-devel
BuildRequires:  libxml2
BuildRequires:  libxslt
BuildRequires:  libxslt-devel
BuildRequires:  libxslt-tools
BuildRequires:  mariadb
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  shared-mime-info
BuildRequires:  sqlite3-devel
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DesignerPlugin)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
Requires:       libqt5-sql-mysql
Requires:       mysql
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
Suggests:       mariadb
Obsoletes:      akonadi5 < %{version}
Provides:       akonadi5 = %{version}
# Needed for users of unstable repositories
Obsoletes:      akonadi < %{version}
Obsoletes:      akonadi-runtime < %{version}
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_graph-devel
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
%if 0%{?suse_version} < 1330
# It does not build with the default compiler (GCC 4.8) on Leap 42.x
%if 0%{?sle_version} < 120300
BuildRequires:  gcc6-c++
%else
BuildRequires:  gcc7-c++
%endif
%endif
Recommends:     %{name}-lang

%description
This package contains the data files of Akonadi, the KDE PIM storage
service.

%package -n libKF5AkonadiCore5
Summary:        Core Akonadi Server library
Group:          System/Libraries
Recommends:     %{name}

%description -n libKF5AkonadiCore5
This package includes the core Akonadi library, the KDE PIM storage service.

%package -n libKF5AkonadiAgentBase5
Summary:        Akonadi Agent base library
Group:          System/Libraries
Recommends:     %{name}

%description -n libKF5AkonadiAgentBase5
This package includes the agent library for Akonadi, the KDE PIM storage service.

%package -n libKF5AkonadiWidgets5
Summary:        Akonadi Agent base library
Group:          System/Libraries
Recommends:     %{name}

%description -n libKF5AkonadiWidgets5
This package provides the basic GUI widgets for Akonadi, the KDE PIM storage service.

%package -n libKF5AkonadiPrivate5
Summary:        Akonadi Private Server library
Group:          System/Libraries
Recommends:     %{name}

%description -n libKF5AkonadiPrivate5
This package includes the Private Akonadi library for Akonadi, the KDE PIM storage service.

%package -n libKF5AkonadiXml5
Summary:        Akonadi Xml library
Group:          System/Libraries
Recommends:     %{name}

%description -n libKF5AkonadiXml5
This package includes the Akonadi Xml library for Akonadi, the KDE PIM storage service.

%package sqlite
Summary:        akonadi server's SQlite plugin
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:sqlite3)

%description sqlite
Akonadi server's SQlite plugin.

%package devel
Summary:        Akonadi Framework: Build Environment
Group:          Development/Libraries/X11
Requires:       %{name} = %{version}
Requires:       kcompletion-devel
Requires:       kdelibs4support-devel
Requires:       kitemmodels-devel
Requires:       kjobwidgets-devel
Requires:       kservice-devel
Requires:       kxmlgui-devel
Requires:       libKF5AkonadiAgentBase5 = %{version}
Requires:       libKF5AkonadiCore5 = %{version}
Requires:       libKF5AkonadiWidgets5 = %{version}
Requires:       solid-devel
Requires:       pkgconfig(Qt5Network)
Conflicts:      libakonadiprotocolinternals-devel
Obsoletes:      akonadi-devel < %{version}
Obsoletes:      libKF5AkonadiPrivate-devel < %{version}
Provides:       libKF5AkonadiPrivate-devel = %{version}
%if 0%{?suse_version} > 1325
Requires:       libboost_headers-devel
%else
Requires:       boost-devel
%endif

%description devel
This package contains development files of Akonadi, the KDE PIM storage
service.

%lang_package

%prep
%setup -q -n %{rname}-%{version}

%build
  %if 0%{?suse_version} < 1330
    # It does not build with the default compiler (GCC 4.8) on Leap 42.x
    %if 0%{?sle_version} < 120300
      export CC=gcc-6
      export CXX=g++-6
    %else
      export CC=gcc-7
      export CXX=g++-7
    %endif
  %endif
  %cmake_kf5 -d build -- -DINSTALL_QSQLITE_IN_QT_PREFIX=TRUE -DQT_PLUGINS_DIR=%{_kf5_plugindir}
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post
/sbin/ldconfig
%mime_database_post

%postun
/sbin/ldconfig
%mime_database_postun

%post -n libKF5AkonadiWidgets5 -p /sbin/ldconfig
%postun -n libKF5AkonadiWidgets5 -p /sbin/ldconfig
%post -n libKF5AkonadiCore5 -p /sbin/ldconfig
%postun -n libKF5AkonadiCore5 -p /sbin/ldconfig
%post -n libKF5AkonadiAgentBase5 -p /sbin/ldconfig
%postun -n libKF5AkonadiAgentBase5 -p /sbin/ldconfig
%post -n libKF5AkonadiPrivate5 -p /sbin/ldconfig
%postun -n libKF5AkonadiPrivate5 -p /sbin/ldconfig
%post -n libKF5AkonadiXml5 -p /sbin/ldconfig
%postun -n libKF5AkonadiXml5 -p /sbin/ldconfig

%files
%license COPYING*
%doc AUTHORS
%config %{_kf5_sysconfdir}/xdg/akonadi/mysql-global-mobile.conf
%config %{_kf5_sysconfdir}/xdg/akonadi/mysql-global.conf
%dir %{_kf5_configkcfgdir}
%dir %{_kf5_iconsdir}/hicolor/256x256
%dir %{_kf5_iconsdir}/hicolor/256x256/apps
%dir %{_kf5_sysconfdir}/xdg/akonadi
%{_datadir}/akonadi/
%{_datadir}/kf5/akonadi/
%{_datadir}/kf5/akonadi_knut_resource/
%{_kf5_bindir}/akonadi_*
%{_kf5_bindir}/akonadictl
%{_kf5_bindir}/akonadiselftest
%{_kf5_bindir}/akonadiserver
%{_kf5_bindir}/akonaditest
%{_kf5_bindir}/asapcat
%{_kf5_configkcfgdir}/resourcebase.kcfg
%{_kf5_iconsdir}/hicolor/*/apps/akonadi.png
%{_kf5_iconsdir}/hicolor/scalable/apps/akonadi.svgz
%{_kf5_plugindir}/akonadi/
%{_kf5_sharedir}/dbus-1/services/org.freedesktop.Akonadi.Control.service
%{_kf5_sharedir}/mime/packages/akonadi-mime.xml
%{_kf5_debugdir}/akonadi.*categories

%files -n libKF5AkonadiAgentBase5
%license COPYING*
%{_kf5_libdir}/libKF5AkonadiAgentBase.so.*

%files -n libKF5AkonadiCore5
%license COPYING*
%{_kf5_libdir}/libKF5AkonadiCore.so.*

%files -n libKF5AkonadiWidgets5
%license COPYING*
%{_kf5_libdir}/libKF5AkonadiWidgets.so.*

%files -n libKF5AkonadiPrivate5
%license COPYING*
%{_kf5_libdir}/libKF5AkonadiPrivate.so.*

%files -n libKF5AkonadiXml5
%license COPYING*
%{_kf5_libdir}/libKF5AkonadiXml.so.*

%files sqlite
%license COPYING*
%{_kf5_plugindir}/sqldrivers/

%files devel
%license COPYING*
%dir %{_kf5_cmakedir}
%{_kf5_bindir}/akonadi2xml
%{_kf5_dbusinterfacesdir}/org.freedesktop.Akonadi.*.xml
%{_kf5_includedir}/AkonadiAgentBase/
%{_kf5_includedir}/AkonadiCore/
%{_kf5_includedir}/AkonadiWidgets/
%{_kf5_includedir}/AkonadiXml/
%{_kf5_includedir}/akonadi/
%{_kf5_includedir}/akonadi_version.h
%{_kf5_cmakedir}/KF5Akonadi
%{_kf5_libdir}/libKF5AkonadiAgentBase.so
%{_kf5_libdir}/libKF5AkonadiCore.so
%{_kf5_libdir}/libKF5AkonadiPrivate.so
%{_kf5_libdir}/libKF5AkonadiWidgets.so
%{_kf5_libdir}/libKF5AkonadiXml.so
%{_kf5_mkspecsdir}/qt_AkonadiAgentBase.pri
%{_kf5_mkspecsdir}/qt_AkonadiCore.pri
%{_kf5_mkspecsdir}/qt_AkonadiWidgets.pri
%{_kf5_mkspecsdir}/qt_AkonadiXml.pri
%dir %{_kf5_sharedir}/kdevappwizard/
%{_kf5_sharedir}/kdevappwizard/templates/
%{_kf5_plugindir}/designer/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
