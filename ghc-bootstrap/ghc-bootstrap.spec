#
# spec file for package ghc-bootstrap
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%ifarch %{ix86}
%define longarch i386
%endif
%ifarch ppc
%define longarch powerpc
%endif
%ifarch ppc64
%define longarch powerpc64
%endif
%ifarch ppc64le
%define longarch powerpc64le
%endif
%ifarch s390
%define longarch s390
%endif
%ifarch s390x
%define longarch s390x
%endif
%ifarch aarch64
%define longarch aarch64
%endif
%ifarch %{arm}
%define longarch arm
%endif
%ifarch x86_64
%define longarch x86_64
%endif
%ifarch s390 s390x
%define sysname ibm
%endif
%ifarch x86_64 %{ix86}
%define sysname deb8
%endif
%ifarch ppc64 ppc64le aarch64 %{arm}
%define sysname unknown
%endif

Name:           ghc-bootstrap
Version:        8.4.3
Release:        0
Url:            https://build.opensuse.org/package/view_file/devel:languages:haskell:bootstrap
Summary:        Binary distributions of The Glorious Glasgow Haskell Compiler
License:        BSD-3-Clause
Group:          Development/Languages/Other
Source1:        README.openSUSE
Source2:        LICENSE
Source10:       ghc-8.4.3-i386-deb8-linux.tar.xz
Source12:       ghc-8.4.3-powerpc64-unknown-linux.tar.xz
Source13:       ghc-8.4.3-powerpc64le-unknown-linux.tar.xz
Source14:       ghc-8.4.3-x86_64-deb8-linux.tar.xz
Source16:       ghc-8.4.3-s390x-ibm-linux.tar.xz
Source17:       ghc-8.4.3-aarch64-unknown-linux.tar.xz
Source18:       ghc-8.4.3-arm-unknown-linux.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fdupes
BuildRequires:  gmp-devel
BuildRequires:  libncurses5
%ifnarch %{arm} s390x
BuildRequires:  libnuma-devel
%endif
%ifarch aarch64 %{arm}
BuildRequires:  binutils-gold
Requires:       binutils-gold
%endif
%ifarch s390x
BuildRequires:  libffi-devel
%endif
Requires:       gmp-devel
Requires:       libncurses5
# This package is not meant to be used outside OBS
Requires:       this-is-only-for-build-envs

ExclusiveArch:  %{ix86} ppc64 ppc64le x86_64 s390x aarch64 %{arm}
Provides:       ghc-bootstrap-devel

AutoReq:        off

%description
This package contains a binary distribution of "The Glorious Glasgow
Haskell Compilation System". See README.openSUSE on how the tarballs
were produced.

Do not install this package! Install 'ghc' instead. 


%prep
cp %SOURCE1 .
cp %SOURCE2 .
cp %SOURCE10 .
cp %SOURCE12 .
cp %SOURCE13 .
cp %SOURCE14 .
cp %SOURCE16 .
cp %SOURCE17 .
cp %SOURCE18 .

%build
tar Jxf ghc-%{version}-%{longarch}-%{sysname}-linux.tar.xz
cd ghc-%{version}
./configure --prefix=/opt

%install
cd ghc-%{version}
%makeinstall
%fdupes -s %{buildroot}

%post
/opt/bin/ghc-pkg recache

%files
%defattr(-,root,root,-)
%doc README.openSUSE
%doc LICENSE
/opt

%changelog
