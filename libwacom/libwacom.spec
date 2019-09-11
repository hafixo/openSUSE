#
# spec file for package libwacom
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


Name:           libwacom
Version:        0.32
Release:        0
Summary:        Library to identify wacom tablets
License:        MIT
Group:          System/Libraries
URL:            http://linuxwacom.sourceforge.net/
Source:         https://github.com/linuxwacom/libwacom/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
Source2:        https://github.com/linuxwacom/libwacom/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2.sig
Source3:        http://www.who-t.net/contact/hutterer_peter.asc#/%{name}.keyring
Source99:       baselibs.conf
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gudev-1.0)

%description
libwacom is a library to identify wacom tablets and their model-specific
features. It provides easy access to information such as "is this a
built-in on-screen tablet", "what is the size of this model", etc.

%package -n libwacom2
Summary:        Library to identify wacom tablets
Group:          System/Libraries
Requires:       %{name}-data >= %{version}

%description -n libwacom2
libwacom is a library to identify wacom tablets and their model-specific
features. It provides easy access to information such as "is this a
built-in on-screen tablet", "what is the size of this model", etc.

%package data
Summary:        Library to identify wacom tablets -- Data Files
Group:          System/Libraries

%description data
libwacom is a library to identify wacom tablets and their model-specific
features. It provides easy access to information such as "is this a
built-in on-screen tablet", "what is the size of this model", etc.

%package tools
Summary:        Library to identify wacom tablets -- Tools
Group:          Hardware/Other

%description tools
libwacom is a library to identify wacom tablets and their model-specific
features. It provides easy access to information such as "is this a
built-in on-screen tablet", "what is the size of this model", etc.

%package devel
Summary:        Library to identify wacom tablets -- Development Files
Group:          Development/Libraries/C and C++
Requires:       libwacom2 = %{version}

%description devel
libwacom is a library to identify wacom tablets and their model-specific
features. It provides easy access to information such as "is this a
built-in on-screen tablet", "what is the size of this model", etc.

%prep
%setup -q

%build
%configure \
        --disable-static
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_udevrulesdir}
tools/generate-udev-rules > %{buildroot}%{_udevrulesdir}/65-libwacom.rules

find %{buildroot} -type f -name "*.la" -delete -print

%post -n libwacom2 -p /sbin/ldconfig
%postun -n libwacom2 -p /sbin/ldconfig

%files -n libwacom2
%license COPYING
%doc NEWS README
%{_libdir}/libwacom.so.2*

%files data
%dir %{_datadir}/libwacom
%{_datadir}/libwacom/*.tablet
%{_datadir}/libwacom/*.stylus
%{_datadir}/libwacom/layouts/
%dir %{_libexecdir}/udev
%dir %{_udevrulesdir}
%{_udevrulesdir}/65-libwacom.rules

%files tools
%{_bindir}/libwacom-list-local-devices
%{_mandir}/man1/libwacom-list-local-devices.1%{?ext_man}

%files devel
%{_includedir}/libwacom-1.0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libwacom.pc

%changelog
