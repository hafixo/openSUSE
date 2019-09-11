#
# spec file for package cpuid
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           cpuid
Version:        20180519
Release:        0
Summary:        x86 CPU identification tool
License:        GPL-2.0-or-later
Group:          System/Management
Url:            http://etallen.com/cpuid.html

Source:         http://etallen.com/cpuid/%name-%version.src.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  make
ExclusiveArch:  %ix86 x86_64

%description
cpuid executes the CPUID instruction on x86-family CPUs and decodes
the results into English descriptions. It knows about Intel, AMD, and
Cyrix CPUs, and is fairly complete.

%prep
%setup -q

%build
# remove -Werror=format-security which is used on Mandriva, as it produces
# a false positive compiler error on several printf calls:
CFLAGS=$(echo "%optflags -Wall"| sed 's/-Werror=format-security//g')

make CFLAGS="$CFLAGS"

%install
mkdir -p "%buildroot/%_bindir" "%buildroot/%_mandir/man1"
install -pm0755 cpuid cpuinfo2cpuid "%buildroot/%_bindir/"
install -pm0644 cpuid.man "%buildroot/%_mandir/man1/cpuid.1"

%files
%defattr(-,root,root)
%doc ChangeLog FUTURE LICENSE
%_bindir/cpu*
%_mandir/man1/cpuid.1*

%changelog
