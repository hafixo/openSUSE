#
# spec file for package marco
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


%define soname  libmarco-private
%define sover   1
%define _version 1.23
Name:           marco
Version:        1.23.1
Release:        0
Summary:        MATE window manager
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
# set to _version when mate-common has an equal release
BuildRequires:  mate-common >= 1.22
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  zenity
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
Requires:       zenity
Recommends:     %{name}-lang
Provides:       windowmanager
# mate-window-manager was last used in openSUSE 13.1.
Provides:       mate-window-manager = %{version}
Obsoletes:      mate-window-manager < %{version}
Obsoletes:      mate-window-manager-lang < %{version}
%glib2_gsettings_schema_requires

%description
Marco is a small window manager, using GTK+ to do everything. It is
developed mainly for the MATE Desktop.

%package -n %{soname}%{sover}
Summary:        MATE window manager shared libraries
Group:          System/GUI/Other

%description -n %{soname}%{sover}
Marco is a small window manager, using GTK+ to do everything. It is
developed mainly for the MATE Desktop.

%package themes
Summary:        MATE window manager themes
# mate-window-manager-themes was last used in openSUSE 13.1.
Group:          System/GUI/Other
Provides:       mate-window-manager-themes = %{version}
Obsoletes:      mate-window-manager-themes < %{version}
BuildArch:      noarch

%description themes
Marco is a small window manager, using GTK+ to do everything. It is
developed mainly for the MATE Desktop.

%package devel
Summary:        MATE window manager development files
Group:          Development/Libraries/Other
Requires:       %{soname}%{sover} = %{version}
# mate-window-manager-devel was last used in openSUSE 13.1.
Provides:       mate-window-manager-devel = %{version}
Obsoletes:      mate-window-manager-devel < %{version}

%description devel
Marco is a small window manager, using GTK+ to do everything. It is
developed mainly for the MATE Desktop.

%lang_package

%prep
%setup -q

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --libexecdir=%{_libexecdir}/%{name} \
  --disable-static                    \
  --disable-scrollkeeper              \
  --disable-schemas-install
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print

%suse_update_desktop_file %{name}
%suse_update_desktop_file %{buildroot}%{_datadir}/mate/wm-properties/%{name}-wm.desktop
%fdupes %{buildroot}%{_datadir}/themes/

%post -n %{soname}%{sover} -p /sbin/ldconfig

%postun -n %{soname}%{sover} -p /sbin/ldconfig

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%glib2_gsettings_schema_post

%postun
%desktop_database_postun
%glib2_gsettings_schema_postun
%endif

%files
%license COPYING
%doc NEWS README
%{_bindir}/%{name}*
%dir %{_datadir}/mate/
%{_datadir}/mate/wm-properties/
%{_datadir}/%{name}/
%{_datadir}/mate-control-center/keybindings/50-marco*.xml
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/help/C/
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man?/%{name}*.?%{?ext_man}

%files lang -f %{name}.lang

%files -n %{soname}%{sover}
%{_libdir}/*.so.%{sover}*
# Marco requires libmarco-private0 and mate-control-center requires
# it too; make libmarco-private0 own /usr/share/mate-control-center
# to avoid conflicts between packages.
%dir %{_datadir}/mate-control-center/
%dir %{_datadir}/mate-control-center/keybindings/

%files themes
%{_datadir}/themes/ClearlooksRe/
%{_datadir}/themes/Dopple-Left/
%{_datadir}/themes/Dopple/
%{_datadir}/themes/DustBlue/
%{_datadir}/themes/Spidey-Left/
%{_datadir}/themes/Spidey/
%{_datadir}/themes/Splint-Left/
%{_datadir}/themes/Splint/
%{_datadir}/themes/WinMe/
%{_datadir}/themes/eOS/

%files devel
%{_includedir}/%{name}-1/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libmarco-private.pc

%changelog
