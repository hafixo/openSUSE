#
# spec file for package breeze-gtk
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%bcond_without lang

%define _name   breeze
Name:           breeze-gtk
Version:        5.16.4
Release:        0
Summary:        GTK+ theme matching KDE's Breeze
License:        LGPL-2.1
Group:          System/GUI/KDE
Url:            https://projects.kde.org/breeze-gtk
Source:         https://download.kde.org/stable/plasma/%{version}/breeze-gtk-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/%{version}/breeze-gtk-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-OPENSUSE update_from_BreezeGTK.patch boo#994832 -- update user's config from the old BreezyGTK theme
Patch100:       update_from_BreezeGTK.patch
BuildRequires:  breeze5-style
BuildRequires:  cmake >= 2.8.12
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  python3-cairo
BuildRequires:  sassc

%description
A GTK+ theme created to match with the new Plasma 5 Breeze theme.

%package -n metatheme-%{_name}-common
Summary:        GTK+ theme matching KDE's Breeze -- Common Files
Group:          System/GUI/KDE
# Default cursor theme
Recommends:     breeze5-cursors
Suggests:       gtk2-metatheme-%{_name}
Suggests:       gtk3-metatheme-%{_name}
Provides:       %{_name}-gtk = %{version}
Obsoletes:      %{_name}-gtk < %{version}

%description -n metatheme-%{_name}-common
A GTK+ theme created to match with the new Plasma 5 Breeze theme.

%package -n gtk2-metatheme-%{_name}
Summary:        GTK+ theme matching KDE's Breeze -- GTK+ 2 Support
Group:          System/GUI/KDE
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    packageand(breeze5-style:gtk2)
Supplements:    packageand(breeze4-style:gtk2)
BuildArch:      noarch

%description -n gtk2-metatheme-%{_name}
A GTK+ theme created to match with the new Plasma 5 Breeze theme.

%package -n gtk3-metatheme-%{_name}
Summary:        GTK+ theme matching KDE's Breeze -- GTK+ 3 Support
Group:          System/GUI/KDE
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    packageand(breeze5-style:gtk3)
Supplements:    packageand(breeze4-style:gtk3)
BuildArch:      noarch

%description -n gtk3-metatheme-%{_name}
A GTK+ theme created to match with the new Plasma 5 Breeze theme.

%prep
%autosetup -p1

%build
%cmake_kf5
make %{?_smp_mflags}

%install
%kf5_makeinstall
%fdupes %{buildroot}%{_datadir}/

%files -n metatheme-%{_name}-common
%license COPYING*
%doc README.md
%{_datadir}/themes/Breeze*/
%exclude %{_datadir}/themes/Breeze*/gtk-*/
%dir %{_kf5_sharedir}/kconf_update/
%dir %{_kf5_sharedir}/themes/Breeze*/assets/
%{_kf5_sharedir}/kconf_update/*%{_name}*
%dir %{_kf5_libdir}/kconf_update_bin/
%{_kf5_libdir}/kconf_update_bin/*%{_name}*

%files -n gtk2-metatheme-%{_name}
%{_datadir}/themes/Breeze*/gtk-2.0/

%files -n gtk3-metatheme-%{_name}
%{_datadir}/themes/Breeze*/gtk-3.*/

%changelog
