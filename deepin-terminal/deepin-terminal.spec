#
# spec file for package deepin-terminal
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019 Hillwood Yang <hillwood@opensuse.org>
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

Name:           deepin-terminal
Version:        3.2.6
Release:        0
Summary:        Deepin terminal
License:        GPL-3.0-or-later AND GPL-3.0-only
Group:          System/X11/Terminals
Url:            https://github.com/linuxdeepin/deepin-terminal
Source0:        https://github.com/linuxdeepin/deepin-terminal/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE deepin-terminal_unbundle_vte.patch hillwood@opensuse.org - Use vte in system default
Patch0:         deepin-terminal_unbundle_vte.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  vala
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  readline-devel
BuildRequires:  libxml2-tools
BuildRequires:  gcc-c++
BuildRequires:  intltool >= 0.35.0
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(gtk+-3.0)
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(vte-2.91)
%else
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(gnutls)
%endif
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
Recommends:     %{name}-lang
Requires:       deepin-menu
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%lang_package

%description
Deepin Terminal is an advanced terminal emulator with workspace, multiple 
windows, remote management, quake mode and other features.

%prep
%setup -q
%if 0%{?suse_version} > 1500
%patch0 -p1
%endif
sed -i 's|return @@PROJECT_PATH@@;|return "%{_datadir}/%{name}";|' project_path.c.in

%build
%cmake -DCMAKE_INSTALL_DIR=%{_prefix} \
       -DCMAKE_C_FLAGS="$RPM_OPT_FLAGS" \
       -DCMAKE_CXX_FLAGS="$RPM_OPT_FLAGS" 
%if 0%{?sle_version} > 150000 && 0%{?is_opensuse}
%cmake_build
%else
make %{?_smp_mflags}
%endif


%install
%cmake_install

%suse_update_desktop_file %{name}
%find_lang %{name}
%fdupes %{buildroot}


%files
%defattr(-,root,root,-)
%doc README.md CHANGELOG.md
%license LICENSE
%dir %{_datadir}/%{name}
%dir %{_libexecdir}/%{name}
%{_bindir}/%{name}
%{_libexecdir}/%{name}/ssh_login.sh
%{_libexecdir}/%{name}/zssh
%{_datadir}/%{name}/style.css
%{_datadir}/%{name}/theme
%{_datadir}/%{name}/image
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/deepin-terminal.svg
%{_datadir}/applications/deepin-terminal.desktop

%files lang -f %{name}.lang

%changelog
