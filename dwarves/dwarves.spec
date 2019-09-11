#
# spec file for package dwarves
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


Name:           dwarves
Version:        1.15
Release:        0
Summary:        DWARF utilities
License:        GPL-2.0-only
Group:          Development/Tools/Debuggers
Url:            http://acmel.wordpress.com/
#Git-Clone:	git://git.kernel.org/pub/scm/devel/pahole/pahole
#Git-Web:	http://git.kernel.org/cgit/devel/pahole/pahole.git
Source:         https://git.kernel.org/pub/scm/devel/pahole/pahole.git/snapshot/pahole-%version.tar.gz
Source2:        libbpf-0.0.3+git30.tar.xz
Source9:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  libdw-devel >= 0.142
BuildRequires:  libebl-devel
BuildRequires:  libelf-devel
BuildRequires:  pkgconfig(zlib)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# Also known by its most prominent tool
Provides:       pahole = %version-%release

%description
dwarves is a set of tools that use the DWARF debugging information
inserted in ELF binaries by compilers such as GCC, used by well known
debuggers such as GDB, and more recent ones such as systemtap.

Utilities in the dwarves suite include pahole, that can be used to
find alignment holes in structs and classes in languages such as C,
C++, but not limited to these.

It also extracts other information such as CPU cacheline alignment,
helping pack those structures to achieve more cache hits.

A diff like tool, codiff can be used to compare the effects changes
in source code generate on the resulting binaries.

Another tool is pfunct, that can be used to find all sorts of
information about functions, inlines, decisions made by the compiler
about inlining, etc.

%package -n libdwarves1
Summary:        DWARF processing libraries of dwarves tools
Group:          System/Libraries
Requires:       libebl-plugins

%description -n libdwarves1
This package contains the libdwarves shared library for the dwarves
toolset, providing processing for DWARF, a debugging data format
for ELF files.

dwarves is a set of tools that use the DWARF debugging information
inserted in ELF binaries by compilers such as GCC, used by well known
debuggers such as GDB, and more recent ones such as systemtap.

%package -n libdwarves-devel
Summary:        DWARF processing library development files
Group:          Development/Libraries/C and C++
Requires:       libdwarves1 = %version-%release

%description -n libdwarves-devel
This package contains the development files for libdwarves, a library
for processing DWARF, a debugging data format for ELF files.

%prep
%setup -qn pahole-%version -a2
mv libbpf-0*/* lib/bpf/

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install

%post   -n libdwarves1 -p /sbin/ldconfig
%postun -n libdwarves1 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README NEWS
%_bindir/*
%_mandir/man*/*

%files -n libdwarves1
%defattr(-,root,root)
%_libdir/*.so.1*

%files -n libdwarves-devel
%defattr(-,root,root)
%_libdir/*.so
%_includedir/*
%_datadir/%name

%changelog
