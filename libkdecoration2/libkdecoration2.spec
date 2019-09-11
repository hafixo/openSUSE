#
# spec file for package libkdecoration2
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


%define lname           libkdecorations2-5
%define lname_private   libkdecorations2private6
%bcond_without lang
Name:           libkdecoration2
Version:        5.16.4
Release:        0
Summary:        KDE's window decorations library
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
Url:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/kdecoration-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/%{version}/kdecoration-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
Source3:        baselibs.conf
BuildRequires:  cmake >= 2.8.12
BuildRequires:  extra-cmake-modules >= 0.0.11
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(Qt5Core) >= 5.4.0
BuildRequires:  cmake(Qt5Gui) >= 5.4.0
BuildRequires:  cmake(Qt5Test) >= 5.4.0

%description
Plugin based library to create window decorations.

%package devel
Summary:        KDE's window decorations library (development package)
Group:          Development/Libraries/C and C++
Requires:       %{lname_private} = %{version}
Requires:       %{lname} = %{version}
Requires:       cmake(Qt5Gui) >= 5.4.0
Obsoletes:      libkdecorations-devel

%description devel
Development files belonging to kdecoration,
plugin based library to create window decorations.

%package -n %{lname}
Summary:        KDE's window decorations library
Group:          System/GUI/KDE
Obsoletes:      libkdecorations5
Recommends:     %{lname}-lang

%description -n %{lname}
Plugin based library to create window decorations.

%package -n %{lname_private}
Summary:        KDE's window decorations library
Group:          System/GUI/KDE

%description -n %{lname_private}
Plugin based library to create window decorations.

%lang_package -n %{lname}

%prep
%setup -q -n kdecoration-%{version}

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --all-name
  %endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig
%post -n %{lname_private} -p /sbin/ldconfig
%postun -n %{lname_private} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_kf5_libdir}/libkdecorations2.so.*

%files -n %{lname_private}
%license COPYING*
%{_kf5_libdir}/libkdecorations2private.so.*

%files devel
%license COPYING*
%{_kf5_libdir}/libkdecorations2.so
%{_kf5_libdir}/libkdecorations2private.so
%{_kf5_libdir}/cmake/KDecoration2/
%{_kf5_prefix}/include/KDecoration2/
%{_kf5_includedir}/

%if %{with lang}
%files -n %{lname}-lang -f %{name}.lang
%license COPYING*
%endif

%changelog
