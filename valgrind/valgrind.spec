#
# spec file for package valgrind
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


# during building the major version of glibc is built into the suppression file
%define glibc_main_version %(getconf GNU_LIBC_VERSION | cut -d' ' -f2 | cut -d. -f1)
%define glibc_major_version %(getconf GNU_LIBC_VERSION | cut -d' ' -f2 | cut -d. -f2)
%define building_docs 1

Name:           valgrind
Version:        3.15.0
Release:        0
Summary:        Memory Management Debugger
License:        GPL-2.0-or-later
Group:          Development/Tools/Debuggers
Url:            http://valgrind.org/
Source0:        ftp://sourceware.org/pub/valgrind/valgrind-%{version}.tar.bz2
# https://bugs.kde.org/show_bug.cgi?id=390553
# https://github.com/olafhering/valgrind/compare/olh-base-master...olh-fixes-master
Patch0:         valgrind.xen.patch
Patch1:         jit-register-unregister.diff
Patch2:         armv6-support.diff
BuildRequires:  automake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  docbook_4
%if 0%{?suse_version} < 1320
BuildRequires:  gcc8-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  libxslt
BuildRequires:  pkgconfig
BuildRequires:  procps
Requires:       glibc >= %{glibc_main_version}.%{glibc_major_version}
Requires:       glibc < %{glibc_main_version}.%{lua:print(rpm.expand("%{glibc_major_version}")+1)}
Provides:       callgrind = %{version}
Obsoletes:      callgrind < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  aarch64 %ix86 x86_64 ppc ppc64 ppc64le s390x armv7l armv7hl armv6l armv6hl
%ifarch x86_64 ppc64
%if 0%{?suse_version} < 1320
BuildRequires:  gcc8-c++-32bit
%else
BuildRequires:  gcc-c++-32bit
%endif
BuildRequires:  glibc-devel-32bit
%endif

%description
Valgrind checks all memory operations in an application, like read,
write, malloc, new, free, and delete. Valgrind can find uses of
uninitialized memory, access to already freed memory, overflows,
illegal stack operations, memory leaks, and any illegal
new/malloc/free/delete commands. Another program in the package is
"cachegrind," a profiler based on the valgrind engine.

To use valgrind you should compile your application with "-g -O0"
compiler options. Afterwards you can use it with:

valgrind --tool=memcheck --sloppy-malloc=yes --leak-check=yes
--db-attach=yes my_application, for example.

More valgrind options can be listed via "valgrind --help". There is
also complete documentation in the %{_docdir}/valgrind/
directory. A debugged application runs slower and needs much more
memory, but is usually still usable. Valgrind is still in development,
but it has been successfully used to optimize several KDE applications.

%package devel
Summary:        Memory Management Debugger
Group:          Development/Tools/Debuggers
Requires:       %{name} = %{version}

%description devel
Valgrind checks all memory operations in an application, like read,
write, malloc, new, free, and delete. Valgrind can find uses of
uninitialized memory, access to already freed memory, overflows,
illegal stack operations, memory leaks, and any illegal
new/malloc/free/delete commands. Another program in the package is
"cachegrind," a profiler based on the valgrind engine.

To use valgrind you should compile your application with "-g -O0"
compiler options. Afterwards you can use it with:

valgrind --tool=memcheck --sloppy-malloc=yes --leak-check=yes
--db-attach=yes my_application, for example.

More valgrind options can be listed via "valgrind --help". There is
also complete documentation in the %{_docdir}/valgrind/
directory. A debugged application runs slower and needs much more
memory, but is usually still usable. Valgrind is still in development,
but it has been successfully used to optimize several KDE applications.

%ifarch x86_64 ppc64 s390x
%package 32bit
Summary:        Memory Management Debugger
Group:          Development/Tools/Debuggers
Requires:       %{name} = %{version}
Provides:       valgrind:%{_libdir}/valgrind/32bit-core.xml

%description 32bit
Valgrind checks all memory operations in an application, like read,
write, malloc, new, free, and delete. Valgrind can find uses of
uninitialized memory, access to already freed memory, overflows,
illegal stack operations, memory leaks, and any illegal
new/malloc/free/delete commands. Another program in the package is
"cachegrind," a profiler based on the valgrind engine.

To use valgrind you should compile your application with "-g -O0"
compiler options. Afterwards you can use it with:

valgrind --tool=memcheck --sloppy-malloc=yes --leak-check=yes
--db-attach=yes my_application, for example.

More valgrind options can be listed via "valgrind --help". There is
also complete documentation in the %{_docdir}/valgrind/
directory. A debugged application runs slower and needs much more
memory, but is usually still usable. Valgrind is still in development,
but it has been successfully used to optimize several KDE applications.


%endif

%prep
%setup -q
%patch0 -p1
# needs porting to 3.11
##%patch1
%patch2

%build
%define _lto_cflags %{nil}
%if 0%{?suse_version} < 1320
export CC="%{_bindir}/gcc-8"
export CXX="%{_bindir}/g++-8"
%endif

export FLAGS="%{optflags}"
%ifarch %arm
# Valgrind doesn't support compiling for Thumb yet. Remove when it gets
# native thumb support.
FLAGS=${FLAGS/-mthumb/-mthumb-interwork -marm}
%endif
# not a good idea to build valgrind with fortify, as it does not link glibc
FLAGS="${FLAGS/-D_FORTIFY_SOURCE=2/}"
FLAGS="${FLAGS/-fstack-protector-strong/}"
FLAGS="${FLAGS/-fstack-protector/}"
# -m64 / -m32 is set explicitly everywhere, do not override it
FLAGS="${FLAGS/-m64/}"
export CFLAGS="$FLAGS"
export CXXFLAGS="$FLAGS"
export FFLAGS="$FLAGS"
autoreconf -fi

export GDB=%{_bindir}/gdb
%configure \
    --enable-lto=yes \
%ifarch aarch64
    --enable-only64bit \
%endif
    %{nil}

make %{?_smp_mflags}
%if %{building_docs}
pushd docs
    #make all-docs
    # building the docs needs network access at the moment :-(
    make FAQ.txt man-pages html-docs
popd
%endif

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
rm %{buildroot}/%{_libdir}/valgrind/lib*.a # drop unreproducible unused files to fix boo#1118163
mkdir -p %{buildroot}/%{_defaultdocdir}
if test -d %{buildroot}%{_datadir}/doc/valgrind; then
     mv %{buildroot}%{_datadir}/doc/valgrind %{buildroot}/%{_defaultdocdir}
fi
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a README* NEWS AUTHORS %{buildroot}/%{_defaultdocdir}/%{name}

%check
# OBS doesn't have a z13
%ifnarch s390x
# has too many spurious failures
# make %{?_smp_mflags} regtest
#patent pending self test
VALGRIND_LIB=$PWD/.in_place VALGRIND_LIB_INNER=$PWD/.in_place ./coregrind/valgrind  /usr/bin/perl -wc tests/vg_regtest
%endif

%files devel
%{_includedir}/valgrind
%{_libdir}/pkgconfig/valgrind.pc

%files
%license COPYING COPYING.DOCS
%{_bindir}/*
%doc %{_defaultdocdir}/%{name}
%doc %{_mandir}/*/*
%dir %{_libdir}/valgrind
%ifarch aarch64
%{_libdir}/valgrind/*-arm64-linux
%endif
%ifarch x86_64
%{_libdir}/valgrind/*-amd64-linux
%endif
%ifarch %ix86
%{_libdir}/valgrind/*-x86-linux
%endif
%ifarch ppc
%{_libdir}/valgrind/*-ppc32-linux
%endif
%ifarch ppc64
%{_libdir}/valgrind/*-ppc64be-linux
%endif
%ifarch ppc64le
%{_libdir}/valgrind/*-ppc64le-linux
%endif
%ifarch s390x
%{_libdir}/valgrind/*-s390x-linux
%endif
%ifarch %arm
%{_libdir}/valgrind/*-arm-linux
%endif
%dir /usr/lib/valgrind
/usr/lib/valgrind/dh_view*
%{_libdir}/valgrind/*-linux.so
%{_libdir}/valgrind/*.supp
%{_libdir}/valgrind/64bit-core.xml
%{_libdir}/valgrind/64bit-linux.xml
%{_libdir}/valgrind/64bit-sse.xml
%{_libdir}/valgrind/64bit-core-valgrind-s*.xml
%{_libdir}/valgrind/64bit-linux-valgrind-s*.xml
%{_libdir}/valgrind/64bit-sse-valgrind-s*.xml
%{_libdir}/valgrind/amd64-coresse-valgrind.xml
%{_libdir}/valgrind/amd64-linux-valgrind.xml
%{_libdir}/valgrind/power64-core-valgrind-s*.xml
%{_libdir}/valgrind/power64-core.xml
%{_libdir}/valgrind/power64-core2-valgrind-s*.xml
%{_libdir}/valgrind/power64-linux-valgrind-s*.xml
%{_libdir}/valgrind/power64-linux.xml
%{_libdir}/valgrind/64bit-avx-valgrind-s*.xml
%{_libdir}/valgrind/64bit-avx.xml
%{_libdir}/valgrind/amd64-avx-coresse-valgrind.xml
%{_libdir}/valgrind/amd64-avx-coresse.xml
%{_libdir}/valgrind/amd64-avx-linux-valgrind.xml
%{_libdir}/valgrind/amd64-avx-linux.xml
%{_libdir}/valgrind/mips64-cp0-valgrind-s*.xml
%{_libdir}/valgrind/mips64-cp0.xml
%{_libdir}/valgrind/mips64-cpu-valgrind-s*.xml
%{_libdir}/valgrind/mips64-cpu.xml
%{_libdir}/valgrind/mips64-fpu-valgrind-s*.xml
%{_libdir}/valgrind/mips64-fpu.xml
%{_libdir}/valgrind/mips64-linux-valgrind.xml
%{_libdir}/valgrind/mips64-linux.xml
%{_libdir}/valgrind/power-core-valgrind-s*.xml
%{_libdir}/valgrind/s390x-core64-valgrind-s*.xml
%{_libdir}/valgrind/s390x-core64.xml
%{_libdir}/valgrind/s390x-generic-valgrind.xml
%{_libdir}/valgrind/s390x-generic.xml
%{_libdir}/valgrind/s390x-linux64-valgrind-s*.xml
%{_libdir}/valgrind/s390x-linux64.xml
%{_libdir}/valgrind/s390x-vx-linux-valgrind.xml
%{_libdir}/valgrind/s390x-vx-linux.xml

%ifarch x86_64 ppc64 s390x
%files 32bit
%endif
%ifarch %ix86 x86_64
%{_libdir}/valgrind/*-x86-linux
%endif
%ifarch ppc ppc64
%{_libdir}/valgrind/*-ppc32-linux
%endif
%{_libdir}/valgrind/s390-acr-valgrind-s*.xml
%{_libdir}/valgrind/s390-acr.xml
%{_libdir}/valgrind/s390-fpr-valgrind-s*.xml
%{_libdir}/valgrind/s390-fpr.xml
%{_libdir}/valgrind/s390-vx-valgrind-s*.xml
%{_libdir}/valgrind/s390-vx.xml
%{_libdir}/valgrind/mips-cp0-valgrind-s*.xml
%{_libdir}/valgrind/mips-cp0.xml
%{_libdir}/valgrind/mips-cpu-valgrind-s*.xml
%{_libdir}/valgrind/mips-cpu.xml
%{_libdir}/valgrind/mips-fpu-valgrind-s*.xml
%{_libdir}/valgrind/mips-fpu.xml
%{_libdir}/valgrind/mips-linux-valgrind.xml
%{_libdir}/valgrind/mips-linux.xml
%{_libdir}/valgrind/32bit-core.xml
%{_libdir}/valgrind/32bit-linux.xml
%{_libdir}/valgrind/32bit-sse.xml
%{_libdir}/valgrind/arm-core-valgrind-s*.xml
%{_libdir}/valgrind/arm-core.xml
%{_libdir}/valgrind/arm-vfpv3-valgrind-s*.xml
%{_libdir}/valgrind/arm-vfpv3.xml
%{_libdir}/valgrind/arm-with-vfpv3-valgrind.xml
%{_libdir}/valgrind/arm-with-vfpv3.xml
%{_libdir}/valgrind/32bit-core-valgrind-s*.xml
%{_libdir}/valgrind/32bit-linux-valgrind-s*.xml
%{_libdir}/valgrind/32bit-sse-valgrind-s*.xml
%{_libdir}/valgrind/i386-coresse-valgrind.xml
%{_libdir}/valgrind/i386-linux-valgrind.xml
%{_libdir}/valgrind/power-altivec-valgrind-s*.xml
%{_libdir}/valgrind/power-altivec.xml
%{_libdir}/valgrind/power-core.xml
%{_libdir}/valgrind/power-fpu-valgrind-s*.xml
%{_libdir}/valgrind/power-fpu.xml
%{_libdir}/valgrind/power-linux-valgrind-s*.xml
%{_libdir}/valgrind/power-linux.xml
%{_libdir}/valgrind/power-vsx-valgrind-s1.xml
%{_libdir}/valgrind/power-vsx-valgrind-s2.xml
%{_libdir}/valgrind/power-vsx.xml
%{_libdir}/valgrind/powerpc-altivec32l-valgrind.xml
%{_libdir}/valgrind/powerpc-altivec32l.xml
%{_libdir}/valgrind/powerpc-altivec64l-valgrind.xml
%{_libdir}/valgrind/powerpc-altivec64l.xml

%changelog
