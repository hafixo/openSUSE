#
# spec file for package pango
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


Name:           pango
Version:        1.43.0
Release:        0
Summary:        Library for Layout and Rendering of Text
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.pango.org/
Source0:        https://download.gnome.org/sources/pango/1.43/%{name}-%{version}.tar.xz
Source2:        macros.pango
Source99:       baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  help2man
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo) >= 1.12.10
BuildRequires:  pkgconfig(fontconfig) >= 2.11.91
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi) >= 0.19.7
BuildRequires:  pkgconfig(glib-2.0) >= 2.33.12
BuildRequires:  pkgconfig(gobject-2.0) >= 2.33.12
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(harfbuzz) >= 1.4.2
BuildRequires:  pkgconfig(libthai) >= 0.1.9
BuildRequires:  pkgconfig(xft) >= 2.0.0
BuildRequires:  pkgconfig(xrender)

%description
Pango is a library for layout and rendering of text, with an emphasis
on internationalization. It can be used anywhere that text layout
is needed.

Pango forms the core of text and font handling for GTK+.

%package -n libpango-1_0-0
Summary:        Library for Layout and Rendering of Text
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
Obsoletes:      pango-modules < %{version}
Provides:       pango-modules = %{version}
# bug437293
%ifarch ppc64
Obsoletes:      pango-64bit
%endif
#

%description -n libpango-1_0-0
Pango is a library for layout and rendering of text, with an emphasis
on internationalization. It can be used anywhere that text layout
is needed.

Pango forms the core of text and font handling for GTK+.

%package -n typelib-1_0-Pango-1_0
Summary:        Introspection bindings for pango, a library for text layout and rendering
Group:          System/Libraries

%description -n typelib-1_0-Pango-1_0
Pango is a library for layout and rendering of text, with an emphasis
on internationalization. It can be used anywhere that text layout
is needed.

Pango forms the core of text and font handling for GTK+.

This package provides the GObject Introspection bindings for Pango.

%package tools
Summary:        Tools for pango, a library for text layout and rendering
Group:          System/Libraries

%description tools
Pango is a library for layout and rendering of text, with an emphasis
on internationalization. It can be used anywhere that text layout
is needed.

Pango forms the core of text and font handling for GTK+.

%package devel
Summary:        Development files for pango, a library for text layout and rendering
Group:          Development/Libraries/GNOME
Requires:       libpango-1_0-0 = %{version}
Requires:       typelib-1_0-Pango-1_0 = %{version}
Provides:       pango-doc = %{version}
Obsoletes:      pango-doc < %{version}
# bug437293
%ifarch ppc64
Obsoletes:      pango-devel-64bit
%endif

%description devel
Pango is a library for layout and rendering of text, with an emphasis
on internationalization. It can be used anywhere that text layout
is needed.

Pango forms the core of text and font handling for GTK+.

This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q

%build
%meson \
	-Denable_docs=true \
	-Dgir=true \
	%{nil}
%meson_build

%install
%meson_install
# Install rpm macros
mkdir -p %{buildroot}%_rpmmacrodir
cp %{SOURCE2} %{buildroot}%_rpmmacrodir
# Remove tests, we have no need for them - FIXME if any one can figure out how to disable build of these with meson == awesome
rm -rf %{buildroot}%{_libexecdir}/installed-tests
rm -rf %{buildroot}%{_datadir}/installed-tests

%post -n libpango-1_0-0 -p /sbin/ldconfig
%postun -n libpango-1_0-0 -p /sbin/ldconfig

%files -n libpango-1_0-0
%license COPYING
%doc NEWS README.md
%{_libdir}/lib*.so.*

%files -n typelib-1_0-Pango-1_0
%{_libdir}/girepository-1.0/Pango-1.0.typelib
%{_libdir}/girepository-1.0/PangoCairo-1.0.typelib
%{_libdir}/girepository-1.0/PangoFT2-1.0.typelib
%{_libdir}/girepository-1.0/PangoXft-1.0.typelib

%files tools
%{_bindir}/pango-list
%{_bindir}/pango-view
%{_mandir}/man1/pango-view.1%{ext_man}

%files devel
%doc CODING_STYLE.md THANKS
%doc %{_datadir}/gtk-doc/html/pango/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/pango-1.0/
%{_datadir}/gir-1.0/*.gir
%_rpmmacrodir/macros.pango

%changelog
