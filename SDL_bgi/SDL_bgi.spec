#
# spec file for package SDL_bgi
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           SDL_bgi
%define lname	libSDL_bgi2
Version:        2.2.4
Release:        0
Summary:        BGI-compatible 2D graphics C library with SDL backend
License:        Zlib AND GPL-2.0-or-later
Group:          Development/Libraries/X11
Url:            http://libXbgi.sf.net/

Source:         http://downloads.sf.net/libxbgi/%name-%version.tar.gz
Patch1:         sdlbgi-automake.diff
BuildRequires:  automake >= 1.11
BuildRequires:  libtool >= 2
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(sdl2)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
SDL_bgi is largely compatible with BGI, the Borland Graphics
Interface that was the de-facto standard in PC graphics back in DOS
days. It is easy to use, and it also provides extensions for RGB
colours and mouse support.

%package -n %lname
Summary:        SDL Graphics Routines for Primitives and Other Support Functions
Group:          System/Libraries

%description -n %lname
SDL_bgi is a Borland Graphics Interface (BGI) emulation library for
SDL. It provides extensions for RGB colors and mouse support.

%package -n libSDL_bgi-devel
Summary:        Libraries, includes and more to develop SDL_bgi applications
Group:          Development/Libraries/X11
Requires:       %lname = %version
Provides:       SDL_bgi-devel = %version-%release

%description -n libSDL_bgi-devel
SDL_bgi is a Borland Graphics Interface (BGI) emulation library for
SDL. It provides extensions for RGB colors and mouse support.

Unlike other BGI-compatible libraries, the purpose of SDL_bgi is not
full compatibility with BGI. Rather, it is meant to be an
introduction to SDL-based graphics: SDL and BGI commands can be mixed
together.

%prep
%setup -q
%patch -P 1 -p1

%build
autoreconf -fi
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
b="%buildroot"
rm -f "$b/%_libdir"/*.la
mkdir -p "$b/%_includedir/SDL_bgi" "$b/%_libdir/pkgconfig"
ln -s "../SDL2/SDL_bgi.h" "$b/%_includedir/SDL_bgi/graphics.h"
install -pm0644 test/dos.h test/conio.h "$b/%_includedir/SDL_bgi/"
cat >"$b/%_libdir/pkgconfig/SDL_bgi.pc" <<-EOF
	Name: SDL_bgi
	Description: BGI-compatible API with SDL backend
	Version: %version
	Requires: sdl SDL_gfx
	Libs: -lSDL_bgi
EOF

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%doc LICENSE
%_libdir/libSDL_bgi.so.2*

%files -n libSDL_bgi-devel
%doc README.md doc/*
%_includedir/SDL2/
%_includedir/SDL_bgi/
%_libdir/libSDL_bgi.so
%_libdir/pkgconfig/SDL_bgi.pc

%changelog
