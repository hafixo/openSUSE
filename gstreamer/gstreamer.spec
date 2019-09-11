#
# spec file for package gstreamer
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


%if 0%{?suse_version} > 1500
%define use_meson 1
%else
%define use_meson 0
%endif

%define gst_branch 1.0
Name:           gstreamer
Version:        1.16.0
Release:        0
Summary:        Streaming-Media Framework Runtime
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            http://gstreamer.freedesktop.org/
Source0:        https://gstreamer.freedesktop.org/src/gstreamer/%{name}-%{version}.tar.xz
Source1:        gstreamer.macros
Source2:        gstreamer.prov
Source99:       baselibs.conf
# PATCH-FEATURE-UPSTREAM gstreamer-rpm-prov.patch bgo#588784 dimstar@opensuse.org -- Add --rpm parameter to allow creation of rpm provides, patch from fedora
Patch1:         gstreamer-rpm-prov.patch
# PATCH-FIX-OPENSUSE gstreamer-pie.patch mgorse@suse.com -- create position-independent executables.
Patch2:         gstreamer-pie.patch

BuildRequires:  bison >= 2.4
BuildRequires:  check-devel
BuildRequires:  fdupes
BuildRequires:  flex >= 2.5.31
BuildRequires:  gnome-patch-translation
BuildRequires:  gobject-introspection-devel >= 1.31.1
BuildRequires:  gtk-doc >= 1.12
BuildRequires:  libcap-devel
BuildRequires:  libcap-progs
%if %{use_meson}
BuildRequires:  meson >= 0.47.0
%else
BuildRequires:  libtool
%endif
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  python3-xml
BuildRequires:  translation-update-upstream
BuildRequires:  pkgconfig(bash-completion) >= 2.0
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libdw)
%define libunwind_archs %{ix86} ia64 x86_64 %{arm} ppc ppc64 ppc64le aarch64
%ifarch %{libunwind_archs}
BuildRequires:  pkgconfig(libunwind)
%endif

# Ensure that the documentation corresponds with the installed version:
Requires:       libgstreamer-1_0-0 = %{version}
# Core modules may depend on new enough libraries:
Requires:       libgstreamer-1_0-0 >= %{version}
Requires(pre):  permissions
Recommends:     %{name}-lang = %{version}
# Generic name, never used in SuSE:
Provides:       gstreamer-doc = %{version}

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related.  Its plug-in-based architecture
means that new data types or processing capabilities can be added by
installing new plug-ins.

%package -n libgstreamer-1_0-0
Summary:        Streaming-Media Framework Runtime
Group:          System/Libraries
# We want to have core modules installed:
Requires:       %{name}

%description -n libgstreamer-1_0-0
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related.  Its plug-in-based architecture
means that new data types or processing capabilities can be added by
installing new plug-ins.

%package -n typelib-1_0-Gst-1_0
Summary:        Streaming-Media Framework Runtime -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Gst-1_0
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related.  Its plug-in-based architecture
means that new data types or processing capabilities can be added by
installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer.

%package doc
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description doc
GStreamer is a streaming media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related.  Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plug-ins.

%package utils
Summary:        Streaming-Media Framework Runtime
Group:          Productivity/Multimedia/Other
# Generic name, never used in SuSE:
Provides:       gstreamer:%{_bindir}/gst-launch-%{gst_branch} = %{version}
# Symbol for unversioned wrappers:
Provides:       gstreamer-utils_versioned = %{version}

%description utils
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related.  Its plug-in-based architecture
means that new data types or processing capabilities can be added by
installing new plug-ins.

%package devel
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
# gstreamer-utils is required for the gstreamer-provides rpm magic.
Requires:       gstreamer-utils = %{version}
Requires:       libgstreamer-1_0-0 = %{version}
Requires:       typelib-1_0-Gst-1_0 = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%lang_package

%prep
%setup -q -n gstreamer-%{version}
translation-update-upstream po gstreamer-%{gst_branch}
gnome-patch-translation-prepare po gstreamer-%{gst_branch}
# The order matters. Only run gnome-patch-translation-update after patching!
%patch1 -p1
%patch2 -p1
gnome-patch-translation-update po gstreamer-%{gst_branch}

%build
export PYTHON=%{_bindir}/python3
%if %{use_meson}
sed -i "s/^executable('gst-plugin-scanner',/executable('gst-plugin-scanner-%{_target_cpu}',/" libs/gst/helpers/meson.build
sed -i "s/gst-plugin-scanner/gst-plugin-scanner-%{_target_cpu}/" meson.build
# TODO: enable dbghelp
%{meson} \
	-Dptp-helper-permissions=capabilities \
	-Dpackage-name='openSUSE GStreamer package' \
	-Dpackage-origin='http://download.opensuse.org' \
	-Dgtk_doc=enabled \
	-Dintrospection=enabled \
	-Dbenchmarks=disabled \
	-Dexamples=disabled \
	-Dtests=disabled \
	-Ddbghelp=disabled \
%ifnarch %{libunwind_archs}
	-Dlibunwind=disabled \
%endif
	%{nil}
%{meson_build}
%else
export CFLAGS="%{optflags} -fPIE"
export LDFLAGS="-pie"
%configure \
	--with-ptp-helper-permissions=capabilities \
	--with-package-name='openSUSE GStreamer package' \
	--with-package-origin='http://download.opensuse.org' \
	--enable-gtk-doc \
	--enable-introspection \
	--disable-benchmarks \
	--disable-examples \
	--disable-static \
	--disable-tests \
	--program-transform-name='s/gst-plugin-scanner/gst-plugin-scanner-%{_target_cpu}/' \
	%{nil}
%make_build
%endif

%install
%if %{use_meson}
%{meson_install}
%else
%make_install
%endif
%find_lang %{name}-%{gst_branch}
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}%{_datadir}/gstreamer-%{gst_branch}/presets
# Install the rpm macros
install -m644 -D %{SOURCE1} %{buildroot}%{_libexecdir}/rpm/fileattrs/gstreamer.attr
install -m755 -D %{SOURCE2} %{buildroot}%{_libexecdir}/rpm/gstreamer-provides
%fdupes %{buildroot}%{_datadir}/gtk-doc

%verifyscript
%verify_permissions -e %{_libexecdir}/gstreamer-%{gst_branch}/gst-ptp-helper

%post
%set_permissions %{_libexecdir}/gstreamer-%{gst_branch}/gst-ptp-helper

%post -n libgstreamer-1_0-0 -p /sbin/ldconfig
%postun -n libgstreamer-1_0-0 -p /sbin/ldconfig

%files
%license COPYING
%dir %{_datadir}/gstreamer-%{gst_branch}
%dir %{_datadir}/gstreamer-%{gst_branch}/presets
%dir %{_libdir}/gstreamer-%{gst_branch}
%{_libdir}/gstreamer-%{gst_branch}/libgstcoreelements.so
%{_libdir}/gstreamer-%{gst_branch}/libgstcoretracers.so
%dir %{_libexecdir}/gstreamer-%{gst_branch}
%{_libexecdir}/gstreamer-%{gst_branch}/gst-completion-helper
%{_libexecdir}/gstreamer-%{gst_branch}/gst-plugin-scanner-%{_target_cpu}
%verify(not mode caps) %{_libexecdir}/gstreamer-%{gst_branch}/gst-ptp-helper
%{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/helpers/

%files -n libgstreamer-1_0-0
%{_libdir}/*.so.*

%files -n typelib-1_0-Gst-1_0
%{_libdir}/girepository-1.0/Gst-1.0.typelib
%{_libdir}/girepository-1.0/GstBase-1.0.typelib
%{_libdir}/girepository-1.0/GstCheck-1.0.typelib
%{_libdir}/girepository-1.0/GstController-1.0.typelib
%{_libdir}/girepository-1.0/GstNet-1.0.typelib

%files utils
%{_bindir}/*-%{gst_branch}
%{_mandir}/man?/*-%{gst_branch}*%{ext_man}

%files devel
%{_datadir}/aclocal/*.m4
# Own these directories to avoid build requirement on gdb
# only for directories ownership
%dir %{_datadir}/gdb
%dir %{_datadir}/gdb/auto-load
%dir %{_datadir}/gdb/auto-load%{_prefix}
%dir %{_datadir}/gdb/auto-load%{_libdir}
%{_datadir}/gdb/auto-load%{_libdir}/lib%{name}*.py
%if %{use_meson}
%{_datadir}/glib-2.0/gdb/glib_gobject_helper.py
%{_datadir}/glib-2.0/gdb/gst_gdb.py
%else
%dir %{_datadir}/gstreamer-%{gst_branch}/gdb
%{_datadir}/gstreamer-%{gst_branch}/gdb/glib_gobject_helper.py
%{_datadir}/gstreamer-%{gst_branch}/gdb/gst_gdb.py
%endif
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libexecdir}/rpm/gstreamer-provides
%{_libexecdir}/rpm/fileattrs/gstreamer.attr
%{_datadir}/gir-1.0/*.gir

%files doc
%doc AUTHORS ChangeLog NEWS README RELEASE
%{_datadir}/gtk-doc/html/*

%files lang -f %{name}-%{gst_branch}.lang

%changelog
