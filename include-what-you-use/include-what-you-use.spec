#
# spec file for package include-what-you-use
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018 Aaron Puchert.
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


Name:           include-what-you-use
Version:        0.12
Release:        0
Summary:        A tool to analyze #includes in C and C++ source files
License:        NCSA
Group:          Development/Languages/C and C++
Url:            https://include-what-you-use.org/
Source0:        https://include-what-you-use.org/downloads/%{name}-%{version}.src.tar.gz
Source1:        %{name}.1
Patch1:         fix-shebang.patch
Patch2:         iwyu_include_picker.patch
Patch3:         remove-x86-specific-code.patch
BuildRequires:  clang8
BuildRequires:  clang8-devel
BuildRequires:  cmake
%if 0%{?sle_version} && 0%{?sle_version} <= 130000 && !0%{?is_opensuse}
BuildRequires:  gcc6
BuildRequires:  gcc6-c++
%endif
BuildRequires:  llvm8-devel
BuildRequires:  python
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
"Include what you use" means this: for every symbol (type, function,
variable, or macro) that you use in foo.cc (or foo.cpp), either foo.cc
or foo.h should include a .h file that exports the declaration of that
symbol. The include-what-you-use program is a tool to analyze includes
of source files to find include-what-you-use violations, and suggest
fixes for them.

The main goal of include-what-you-use is to remove superfluous includes.
It does this both by figuring out what includes are not actually needed
for this file (for both .cc and .h files), and replacing includes with
forward declarations when possible.

%package tools
Summary:        Additional tools to use %{name} effectively
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description tools
This package contains additional scripts for using %{name} as automated
refactoring tool.

%prep
%setup -q -n %{name}
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%define _lto_cflags %{nil}

# Remove obsolete files - this is now hardcoded into iwyu_include_picker.cc.
rm gcc.libc.imp gcc.symbols.imp gcc.stl.headers.imp stl.c.headers.imp
# This also obsoletes iwyu.gcc.imp.
rm iwyu.gcc.imp

# Since Clang is built using Clang, use it here too. Except for SLES, where we
# need to use GCC 6 for some reason. (Otherwise there are segfaults.)
%if 0%{?sle_version} && 0%{?sle_version} <= 130000 && !0%{?is_opensuse}
export CC=gcc-6 CXX=g++-6
%else
export CC=clang CXX=clang++
%endif
%cmake -DIWYU_LLVM_ROOT_PATH=%{_libdir} ..
%make_jobs

%install
%cmake_install

install -Dm0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1

%check
# We don't support MS style inline assembly, because we removed the dependency
# on the X86 target of LLVM.
rm tests/cxx/ms_inline_asm.cc

# Test doesn't work on ARM.
%ifarch %arm
rm tests/cxx/badinc.cc
%endif

# IWYU needs to find Clang's builtin headers. It looks for them relative to the
# binary (https://clang.llvm.org/docs/LibTooling.html#builtin-includes), but
# since it isn't installed into /usr/bin, it fails to find them. So we pass
# the directory manually to the executable, and because the test driver doesn't
# allow us to specify additional flags, we build a stub.
# Note that this isn't a problem for the installed package, because it will be
# in the same directory as the Clang binary.
export CLANG_BUILTIN_DIR=%{_libdir}/clang/%{_llvm_relver}/include
echo -e "#!/bin/bash\\nbuild/bin/include-what-you-use -isystem ${CLANG_BUILTIN_DIR} \$@" >iwyu-stub
chmod +x iwyu-stub
# We suppress stdout because it's pretty noisy. Failures are written to stderr.
./run_iwyu_tests.py -- ./iwyu-stub >/dev/null

%files
%license LICENSE.TXT
%doc docs/*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}
%{_datadir}/%{name}/

%files tools
%{_bindir}/*.py

%changelog
