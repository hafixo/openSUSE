#
# spec file for package akonadi-contact
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


%define rname akonadi-contacts
%define sonum   5
%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           akonadi-contact
Version:        19.08.0
Release:        0
Summary:        KDE PIM Libraries for Akonadi Contacts
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  akonadi-mime-devel
BuildRequires:  akonadi-server-devel >= %{_kapp_version}
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  grantlee5-devel
BuildRequires:  kcalcore-devel
BuildRequires:  kcodecs-devel >= %{kf5_version}
BuildRequires:  kcompletion-devel >= %{kf5_version}
BuildRequires:  kcontacts-devel
BuildRequires:  kf5-filesystem
BuildRequires:  kio-devel >= %{kf5_version}
BuildRequires:  kmime-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Prison)
BuildRequires:  pkgconfig(Qt5Test) >= 5.6.0
BuildRequires:  pkgconfig(Qt5WebEngine) >= 5.6.0
BuildRequires:  pkgconfig(Qt5WebEngineWidgets) >= 5.6.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.6.0
Requires:       libKF5AkonadiContact5 = %{version}
Requires:       libKF5ContactEditor5 = %{version}
Recommends:     %{name}-lang
Provides:       akonadi-contacts = %{version}
Obsoletes:      akonadi-contacts < %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64

%description
This package provides a library used for handling personal contacts,
as part of the KDE Personal Information Management (PIM) software.

%package -n libKF5AkonadiContact5
Summary:        Library for personal contact handling
Group:          System/Libraries
Requires:       akonadi-contact >= %{version}
Obsoletes:      akonadi-socialutils
Obsoletes:      akonadi-socialutils-devel

%description -n libKF5AkonadiContact5
This package provides a library used for handling personal contacts,
as part of the KDE Personal Information Management (PIM) software.

%package -n libKF5ContactEditor5
Summary:        Library for personal contact handling
Group:          System/Libraries
Requires:       akonadi-contact >= %{version}

%description -n libKF5ContactEditor5
This package provides a library used for handling personal contacts,
as part of the KDE Personal Information Management (PIM) software.

%package -n akonadi-plugin-contacts
Summary:        Plugins for personal contact handling
Group:          System/Libraries
Requires:       akonadi-contact >= %{version}

%description -n akonadi-plugin-contacts
This package provides plugins required by PIM applications to read and write contact data.

%package devel
Summary:        KDE PIM Libraries: Build Environment
Group:          Development/Libraries/KDE
Requires:       akonadi-contact = %{version}
Requires:       akonadi-server-devel
Requires:       kcontacts-devel
Requires:       libKF5AkonadiContact5 = %{version}
Requires:       libKF5ContactEditor5 = %{version}
Obsoletes:      akonadi-contacts-devel < %{version}
Provides:       akonadi-contacts-devel = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop KDE PIM applications.

%lang_package

%prep
%setup -q -n %{rname}-%{version}

%build
%cmake_kf5 -d build -- -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
%make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -n libKF5AkonadiContact5 -p /sbin/ldconfig
%postun -n libKF5AkonadiContact5 -p /sbin/ldconfig
%post -n libKF5ContactEditor5 -p /sbin/ldconfig
%postun -n libKF5ContactEditor5 -p /sbin/ldconfig

%files
%license COPYING*
%dir %{_kf5_plugindir}
%dir %{_kf5_plugindir}/akonadi/contacts/
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_datadir}/akonadi/contact/
%{_kf5_plugindir}/akonadi/contacts/plugins/
%{_kf5_plugindir}/kcm_akonadicontact_actions.so
%{_kf5_servicesdir}/akonadicontact_actions.desktop

%files -n libKF5AkonadiContact5
%license COPYING*
%{_kf5_libdir}/libKF5AkonadiContact.so.*

%files -n libKF5ContactEditor5
%license COPYING*
%{_kf5_libdir}/libKF5ContactEditor.so.*

%files -n akonadi-plugin-contacts
%{_kf5_plugindir}/akonadi_serializer_addressee.so
%{_kf5_plugindir}/akonadi_serializer_contactgroup.so
%dir %{_kf5_sharedir}/akonadi
%dir %{_kf5_sharedir}/akonadi/plugins
%dir %{_kf5_sharedir}/akonadi/plugins/serializer
%{_kf5_sharedir}/akonadi/plugins/serializer/akonadi_serializer_addressee.desktop
%{_kf5_sharedir}/akonadi/plugins/serializer/akonadi_serializer_contactgroup.desktop

%files devel
%license COPYING*
%dir %{_kf5_includedir}/Akonadi
%dir %{_kf5_includedir}/ContactEditor
%dir %{_kf5_includedir}/akonadi
%dir %{_kf5_includedir}/contacteditor
%{_kf5_includedir}/Akonadi/Contact/
%{_kf5_includedir}/ContactEditor
%{_kf5_includedir}/akonadi/contact/
%{_kf5_includedir}/contacteditor
%{_kf5_cmakedir}/KF5AkonadiContact/
%{_kf5_cmakedir}/KF5ContactEditor/
%{_kf5_libdir}/libKF5AkonadiContact.so
%{_kf5_libdir}/libKF5ContactEditor.so
%{_kf5_mkspecsdir}/qt_AkonadiContact.pri
%{_kf5_mkspecsdir}/qt_ContactEditor.pri

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
