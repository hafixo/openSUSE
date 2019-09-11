#
# spec file for package odp
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


Name:           odp
Version:        1.11.0.1
Release:        0
Summary:        OpenDataPlane Reference implementation
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            https://www.opendataplane.org
Source0:        https://git.linaro.org/lng/odp.git/snapshot/odp-%{version}_monarch.tar.gz
Patch0:         0001-increase_ODP_CPUMASK_SIZE.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
%if %{suse_version} >= 1330
BuildRequires:  gcc
%else
BuildRequires:  gcc6
%endif
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)
Conflicts:      otherproviders(odp-any)
Provides:       odp-any = %{version}
ExclusiveArch:  aarch64 x86_64 ppc64 ppc64le

%description
The OpenDataPlane reference implementation library, development files
and examples for the ThunderX platform.

%package libs
Summary:        OpenDataPlane Reference implementation
Group:          System/Libraries
Conflicts:      otherproviders(odp-any-libs)
Provides:       odp-any-libs = %{version}

%description libs
Reference implementation for OpenDataPlane (ODP).
The ODP project is a set of APIs for the networking data plane.

%package devel
Summary:        Development files for the OpenDataPlane reference implementation
Group:          Development/Libraries/C and C++
Requires:       %{name}-libs = %{version}-%{release}
Requires:       libopenssl-devel
Conflicts:      otherproviders(odp-any-devel)
Provides:       odp-any-devel = %{version}

%description devel
This package contains the development files for the OpenDataPlane
reference implementation.

%prep
%setup -q -n odp-1.11.0.1_monarch
# The below command is used to replace the use of git-hash with the version of the source code
sed -i "s|^AC_INIT.*|AC_INIT([OpenDataPlane], [%{version}], [lng-odp@lists.linaro.org])|" configure.ac
%patch0

%build
%if %{suse_version} >= 1330
export CFLAGS="%{optflags} -Wformat-overflow=0 -Wimplicit-fallthrough=0 -Wformat-truncation=0 -latomic"
%else
export CFLAGS="%{optflags}"
%endif
./bootstrap
%configure --disable-static

%install
%if %{suse_version} >= 1330
make V=1 DESTDIR=%{buildroot} %{?_smp_mflags} install
%else
make V=1 CC=gcc-6 DESTDIR=%{buildroot} %{?_smp_mflags} install
%endif
find %{buildroot} -type f -name 'libodp*.la' |xargs rm -f
rm -f %{buildroot}%{_bindir}/odp_*

%files libs
%defattr(-,root,root)
%doc LICENSE README CHANGELOG
%{_libdir}/libodp*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/odp*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%changelog
