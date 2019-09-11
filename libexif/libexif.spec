#
# spec file for package libexif
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


Name:           libexif
Version:        0.6.21
Release:        0
Url:            http://libexif.sourceforge.net
Summary:        An EXIF Tag Parsing Library for Digital Cameras
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        https://downloads.sourceforge.net/project/libexif/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
Patch0:         libexif-build-date.patch
Patch1:         CVE-2016-6328.patch
Patch2:         CVE-2017-7544.patch
BuildRequires:  doxygen
BuildRequires:  pkg-config

%define pname libexif12

%define debug_package_requires %{pname} = %{version}-%{release}

%package -n %{pname}
Summary:        An EXIF Tag Parsing Library for Digital Cameras
Group:          System/Libraries
Provides:       libexif = %{version}
Obsoletes:      libexif < %{version}

%description
This library is used to parse EXIF information from JPEGs created by
digital cameras.

%description -n %{pname}
This library is used to parse EXIF information from JPEGs created by
digital cameras.

%package devel
Summary:        An EXIF Tag Parsing Library for Digital Cameras (Development files)
Group:          Development/Libraries/C and C++
Requires:       %{pname} = %{version}
Requires:       glibc-devel

%description devel
This library is used to parse EXIF information from JPEGs created by
digital cameras.

%prep 
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
export CFLAGS="%optflags $(getconf LFS_CFLAGS)"
%configure \
	--disable-static \
	--with-doc-dir=%{_docdir}/%{name}
make %{?_smp_mflags}

%check
make check

%install
%makeinstall
%find_lang %{name}-12
rm -f %{buildroot}/%{_libdir}/*.la

%post -n %{pname} -p /sbin/ldconfig

%postun -n %{pname} -p /sbin/ldconfig

%files -n %{pname} -f %{name}-12.lang
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%doc %{_docdir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%changelog
