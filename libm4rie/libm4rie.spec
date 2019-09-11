#
# spec file for package libm4rie
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libm4rie
# Note that libm4rie is not always updated in lockstep with libm4ri,
# and that is absolutely normal.
%define date	20150908
%define lname	libm4rie-0_0_%date
Version:        0~%date
Release:        0
Summary:        Library for fast linear arithmetic over GF(2^e)
License:        GPL-2.0+
Group:          Productivity/Scientific/Math
Url:            https://bitbucket.org/malb/m4rie

#Git-Clone:	https://bitbucket.org/malb/m4rie.git
Source:         https://bitbucket.org/malb/m4rie/downloads/m4rie-%date.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libm4ri-devel

%description
M4RIE is a library for fast arithmetic with dense matrices over the
Galois Field GF(2^e).

%package -n %lname
Summary:        Library for fast linear arithmetic over GF(2^e)
Group:          System/Libraries

%description -n %lname
M4RIE is a library for fast arithmetic with dense matrices over the
Galois Field GF(2^e).

%package devel
Summary:        Development files for GF(2^e) arithmetic with libm4rie
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
M4RIE is a library for fast arithmetic with dense matrices over the
Galois Field GF(2^e).

This subpackage contains libraries and header files for developing
applications that want to make use of libm4rie.

%prep
%setup -qn m4rie-%date

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%files -n %lname
%defattr(-,root,root)
%_libdir/libm4rie-0.0.%date.so

%files devel
%defattr(-,root,root)
%_libdir/libm4rie.so
%_includedir/m4rie/

%changelog
