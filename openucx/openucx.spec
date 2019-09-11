#
# spec file for package openucx
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


Name:           openucx
Summary:        Unifieid Communication X
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Version:        1.5.0
Release:        0
Url:            http://openucx.org/

#Git-Clone:	git://github.com/openucx/ucx
#Git-Web:	https://github.com/openucx/ucx
Source:         https://github.com/openucx/ucx/releases/download/v%version/ucx-%version.tar.gz
Source1:        baselibs.conf
Patch1:         openucx-s390x-support.patch
BuildRequires:  autoconf >= 2.63
BuildRequires:  automake >= 1.10
BuildRequires:  binutils-devel
BuildRequires:  gcc-c++
BuildRequires:  libibverbs-devel
%if 0%{?suse_version} < 1330
%ifnarch s390x
BuildRequires:  libnuma-devel
%endif
%else
BuildRequires:  libnuma-devel
%endif
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  aarch64 %power64 x86_64 s390x

%description
UCX is a communication library implementing high-performance
messaging for MPI/PGAS frameworks.

%package tools
Summary:        OpenUCX utilities
Group:          System/Console

%description tools
Miscallaneous utilities for Unified Communication X.

%package -n libucm0
Summary:        Memory (un)happing hooks for Unified Communication X
Group:          System/Libraries

%description -n libucm0
libucm is a standalone non-unloadable library which installs hooks
for virtual memory changes in the current process. Then, it calls
user-defined callbacks, which may potentially override the default
behavior, or just passively listen and update their own data. libucm
does not use libuct, to avoid making it non-unloadable as well, and
impelements a basic logging service which is safe to use from malloc
hooks.

%package -n libucm-devel
Summary:        Development files for Unified Communication X Memory Hooks
Group:          Development/Libraries/C and C++
Requires:       libucm0 = %version

%description -n libucm-devel
libucm is a standalone non-unloadable library which installs hooks
for virtual memory changes in the current process.

%package -n libucp0
Summary:        Infiniband Unified Communication Protocols
Group:          System/Libraries

%description -n libucp0
High-level API uses UCT framework to construct protocols commonly
found in applications (MPI, OpenSHMEM, PGAS, etc.)

%package -n libucp-devel
Summary:        Development files for Unified Communication Protocols (UC-P)
Group:          Development/Libraries/C and C++
Requires:       libucp0 = %version

%description -n libucp-devel
High-level API uses UCT framework to construct protocols commonly
found in applications (MPI, OpenSHMEM, PGAS, etc.)

%package -n libucs0
Summary:        Infiniband Unicified Communication Services
Group:          System/Libraries

%description -n libucs0
This framework provides basic infrastructure for component based
programming, memory management, and useful system utilities.

%package -n libucs-devel
Summary:        Development files for Unified Communication Services (UC-S)
Group:          Development/Libraries/C and C++
Requires:       libucs0 = %version

%description -n libucs-devel
This framework provides basic infrastructure for component based
programming, memory management, and useful system utilities.

%package -n libuct0
Summary:        Infiniband Unified Communication Transport
Group:          System/Libraries

%description -n libuct0
Low-level API that expose basic network operations supported by
underlying hardware.

%package -n libuct-devel
Summary:        Development files for Unified Communication Transport (UC-T)
Group:          Development/Libraries/C and C++
Requires:       libuct0 = %version

%description -n libuct-devel
Low-level API that expose basic network operations supported by
underlying hardware.

%prep
%setup -qn ucx-%version
%patch1

%build
autoreconf -fi
export UCX_CFLAGS="%optflags -Wno-error"
%ifarch x86_64
export UCX_CFLAGS="$UCX_CFLAGS -mno-avx"
%endif
%ifarch %ix86
export UCX_CFLAGS="$UCX_CFLAGS -mno-sse -mno-sse2"
%endif
%configure --disable-static --without-avx \
%if 0%{?suse_version} < 1330
%ifarch s390x
         --disable-numa \
%endif
%endif
         --docdir="%_docdir/%name"

# Override BASE_CFLAGS to disable Werror (boo#1121267)
make %{?_smp_mflags} V=1 BASE_CFLAGS="-g -Wall"

%post   -n libucp0 -p /sbin/ldconfig
%postun -n libucp0 -p /sbin/ldconfig
%post   -n libucs0 -p /sbin/ldconfig
%postun -n libucs0 -p /sbin/ldconfig
%post   -n libuct0 -p /sbin/ldconfig
%postun -n libuct0 -p /sbin/ldconfig
%post   -n libucm0 -p /sbin/ldconfig
%postun -n libucm0 -p /sbin/ldconfig

%install
%make_install
rm -fv "%buildroot/%_libdir"/*.la
# Rename example dir for consistency with the package name
mv %buildroot/%_datadir/ucx  %buildroot/%_datadir/openucx

%files tools
%defattr(-,root,root)
%_bindir/ucx_*
%_datadir/%{name}/
%_libdir/pkgconfig/ucx.pc
%doc LICENSE NEWS

%files -n libucm0
%defattr(-,root,root)
%_libdir/libucm.so.*

%files -n libucm-devel
%defattr(-,root,root)
%_includedir/ucm/
%_libdir/libucm.so

%files -n libucp0
%defattr(-,root,root)
%_libdir/libucp.so.*

%files -n libucp-devel
%defattr(-,root,root)
%_includedir/ucp/
%_libdir/libucp.so

%files -n libucs0
%defattr(-,root,root)
%_libdir/libucs.so.*

%files -n libucs-devel
%defattr(-,root,root)
%_includedir/ucs/
%_libdir/libucs.so

%files -n libuct0
%defattr(-,root,root)
%_libdir/libuct.so.*

%files -n libuct-devel
%defattr(-,root,root)
%_includedir/uct/
%_libdir/libuct.so

%changelog
