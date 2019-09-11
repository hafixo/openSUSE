#
# spec file for package libsecret
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


%define have_lang 1
Name:           libsecret
Version:        0.18.8
Release:        0
Summary:        Library for accessing the Secret Service API
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://wiki.gnome.org/Projects/Libsecret
Source0:        http://download.gnome.org/sources/libsecret/0.18/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

## SLE-only patches start at 1000
# PATCH-FIX-SLE libsecret-bsc932232-use-libgcrypt-allocators.patch bsc#932232 hpj@suse.com -- use libgcrypt allocators for FIPS mode
Patch1000:      libsecret-bsc932232-use-libgcrypt-allocators.patch

BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel >= 1.29
BuildRequires:  libgcrypt-devel >= 1.2.2
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  vala >= 0.17.2.12
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0

%description
libsecret is a library for storing and retrieving passwords and other
secrets. It communicates with the "Secret Service" using DBus.

%package -n libsecret-1-0
Summary:        Library for accessing the Secret Service API
Group:          System/Libraries
%if %{have_lang}
Recommends:     %{name}-lang
# To make the lang package happy
Provides:       %{name} = %{version}
%endif

%description -n libsecret-1-0
libsecret is a library for storing and retrieving passwords and other
secrets. It communicates with the "Secret Service" using DBus.

%package -n typelib-1_0-Secret-1
Summary:        Introspection bindings for the Secret Service API library
Group:          System/Libraries

%description -n typelib-1_0-Secret-1
libsecret is a library for storing and retrieving passwords and other
secrets. It communicates with the "Secret Service" using DBus.

This package provides the GObject Introspection bindings for libsecret.

%package tools
Summary:        Tools from the Secret Service API library
Group:          System/Libraries

%description tools
libsecret is a library for storing and retrieving passwords and other
secrets. It communicates with the "Secret Service" using DBus.

%package devel
Summary:        Development files for the Secret Service API library
Group:          Development/Libraries/GNOME
Requires:       libsecret-1-0 = %{version}
Requires:       typelib-1_0-Secret-1 = %{version}

%description devel
libsecret is a library for storing and retrieving passwords and other
secrets. It communicates with the "Secret Service" using DBus.

%if %{have_lang}
%lang_package
%endif

%prep
%setup -q
%if !0%{?is_opensuse}
%patch1000 -p1
%endif
translation-update-upstream

%build
%configure \
        --disable-static
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%if %{have_lang}
%find_lang %{name} %{?no_lang_C}
%endif
%fdupes %{buildroot}/%{_prefix}

%post -n libsecret-1-0 -p /sbin/ldconfig
%postun -n libsecret-1-0 -p /sbin/ldconfig

%files -n libsecret-1-0
%license COPYING
%doc NEWS README
%{_libdir}/libsecret-1.so.*

%files -n typelib-1_0-Secret-1
%{_libdir}/girepository-1.0/Secret-1.typelib

%files tools
%{_bindir}/secret-tool
%{_mandir}/man1/secret-tool.1%{?ext_man}

%files devel
%doc AUTHORS ChangeLog
%{_libdir}/libsecret-1.so
%{_libdir}/pkgconfig/libsecret-1.pc
%{_libdir}/pkgconfig/libsecret-unstable.pc
%{_includedir}/libsecret-1/
%{_datadir}/gir-1.0/Secret-1.gir
%doc %{_datadir}/gtk-doc/html/libsecret-1/
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libsecret-1.deps
%{_datadir}/vala/vapi/libsecret-1.vapi

%if %{have_lang}
%files lang -f %{name}.lang
%endif

%changelog
