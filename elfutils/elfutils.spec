#
# spec file for package elfutils
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


Name:           elfutils
Version:        0.176
Release:        0
Summary:        Higher-level library to access ELF files
License:        GPL-3.0-or-later
Group:          Development/Tools/Building
Url:            http://fedorahosted.org/elfutils/

#Git-Clone:	git://sourceware.org/git/elfutils
Source:         https://fedorahosted.org/releases/e/l/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source4:        https://fedorahosted.org/releases/e/l/%{name}/%{version}/%{name}-%{version}.tar.bz2.sig
Source1:        README-BEFORE-ADDING-PATCHES
Source2:        baselibs.conf
Source3:        %{name}.changes
Source5:        %{name}.keyring
Patch1:         disable-tests-with-ptrace.patch
Patch2:         cfi-fix.patch
Patch3:         gcc9-tests-Don-t-printf-a-known-NULL-symname.patch
Patch4:         fix-bsc-1110929.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libbz2-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel

%description
elfutils is a collection of utilities and libraries to read, create
and modify ELF binary files, find and handle DWARF debug data,
symbols, thread state and stacktraces for processes and core files.

%package -n libasm1
Summary:        A collection of utilities and DSOs to handle compiled objects
Group:          System/Libraries

%description -n libasm1
libasm contains the "asm" and "disasm" functions to assemble and
disassamble instructions. (There is only partial support for i686 and
BPF instructions.) This is part of the elfutils package.

%package -n libasm-devel
Summary:        A collection of utilities and DSOs to handle compiled objects
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libasm1 = %{version}

%description -n libasm-devel
This package contains the headers and libraries needed to build
applications that require libasm.

%package -n libebl-plugins
Summary:        Architecture backends for libebl
Group:          System/Libraries
Provides:       libebl = %{version}-%{release}
Obsoletes:      libebl < %{version}-%{release}
Provides:       libebl1 = %{version}-%{release}
Obsoletes:      libebl1 < %{version}-%{release}

%description -n libebl-plugins
This subpackage contains the plugins to read architecture-specific
debug info. This is part of the elfutils package.

%package -n libebl-devel
Summary:        Development files for libebl and for EBL plugins
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libdw-devel = %{version}

%description -n libebl-devel
This package contains the headers and libraries needed to build
applications that require libebl, or to build additional EBL
architecutre backend plugins.

%package -n libelf1
Summary:        Library to read and write ELF files
Group:          System/Libraries
Requires:       libebl-plugins = %{version}

%description -n libelf1
This package provides a high-level library to read and write ELF files.
This is part of the elfutils package.

%package -n libelf-devel
Summary:        Development files for libelf
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libelf1 = %{version}
Conflicts:      libelf0-devel

%description -n libelf-devel
This package contains the headers and libraries needed to build
applications that require libelf.

%package -n libdw1
Summary:        Library to access DWARF debugging information
Group:          System/Libraries

%description -n libdw1
This package provides a high-level library to access the DWARF debugging
information. This is part of the elfutils package.

%package -n libdw-devel
Summary:        Development files for libdw
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libdw1 = %{version}
Requires:       libelf-devel = %{version}

%description -n libdw-devel
This package contains the headers and libraries needed to build
applications that require libdw.

%lang_package

%prep
%setup -q
%if 0%{?qemu_user_space_build}
# qemu does not support ptrace
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%define _lto_cflags %{nil}
# Change DATE/TIME macros to use last change time of elfutils.changes
# See http://lists.opensuse.org/opensuse-factory/2011-05/msg00304.html
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find . -type f -regex ".*\.c\|.*\.cpp\|.*\.h" -exec sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" {} +
# Set modversion used to verify dynamically loaded ebl backend matches to
# similarly predictable value [upstream default is hostname + date]
MODVERSION="suse-build `eval echo ${DATE} ${TIME}`"
sed --in-place "s/^MODVERSION=.*\$/MODVERSION=\"${MODVERSION}\"/" configure.ac
export CFLAGS="%optflags"
CFLAGS+=" -g" # make tests pass when user does not want debuginfo (boo#1031556)
%ifarch %sparc
# Small PIC model not sufficient
CFLAGS+=" -fPIC"
%endif
autoreconf -fi
# some patches create new test scripts, which are created 644 by default
chmod a+x tests/run*.sh
%configure --program-prefix=eu-
make %{?_smp_mflags} V=1

%install
make DESTDIR=$RPM_BUILD_ROOT install
# remove unneeded files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
ls -lR $RPM_BUILD_ROOT%{_libdir}/libelf*
%find_lang %{name}

%post -n libasm1 -p /sbin/ldconfig

%post -n libelf1 -p /sbin/ldconfig

%post -n libdw1 -p /sbin/ldconfig

%postun -n libasm1 -p /sbin/ldconfig

%postun -n libelf1 -p /sbin/ldconfig

%postun -n libdw1 -p /sbin/ldconfig

%check
make check %{?_smp_mflags} V=1

%files
%defattr(-,root,root)
%license COPYING
%doc AUTHORS ChangeLog NEWS NOTES README THANKS TODO
%{_bindir}/*

%files -n libasm1
%defattr(-,root,root)
%{_libdir}/libasm.so.*
%{_libdir}/libasm-%{version}.so

%files -n libasm-devel
%defattr(-,root,root)
%{_libdir}/libasm.so
%{_libdir}/libasm.a
%dir %{_includedir}/elfutils
%{_includedir}/elfutils/libasm.h

%files -n libebl-plugins
%defattr(-,root,root)
%{_libdir}/elfutils

%files -n libebl-devel
%defattr(-,root,root)
%{_libdir}/libebl.a
%dir %{_includedir}/elfutils
%{_includedir}/elfutils/libebl.h

%files -n libelf1
%defattr(-,root,root)
%{_libdir}/libelf.so.*
%{_libdir}/libelf-%{version}.so

%files -n libelf-devel
%defattr(-,root,root)
%{_libdir}/libelf.so
%{_libdir}/libelf.a
%{_includedir}/libelf.h
%{_includedir}/gelf.h
%{_includedir}/nlist.h
%dir %{_includedir}/elfutils
%{_includedir}/elfutils/elf-knowledge.h
%{_includedir}/elfutils/version.h
%{_libdir}/pkgconfig/libelf.pc

%files -n libdw1
%defattr(-,root,root)
%{_libdir}/libdw.so.*
%{_libdir}/libdw-%{version}.so

%files -n libdw-devel
%defattr(-,root,root)
%{_libdir}/libdw.a
%{_libdir}/libdw.so
%{_includedir}/dwarf.h
%dir %{_includedir}/elfutils
%{_includedir}/elfutils/libdw.h
%{_includedir}/elfutils/libdwelf.h
%{_includedir}/elfutils/libdwfl.h
%{_includedir}/elfutils/known-dwarf.h
%{_libdir}/pkgconfig/libdw.pc

%files lang -f %{name}.lang

%changelog
