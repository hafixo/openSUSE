#
# spec file for package bctoolbox
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


%define sover   1
Name:           bctoolbox
Version:        0.6.0
Release:        0
Summary:        Utility library for software from Belledonne Communications
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://linphone.org/
Source:         https://linphone.org/releases/sources/%{name}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-OPENSUSE bctoolbox-fix-pkgconfig.patch
Patch0:         bctoolbox-fix-pkgconfig.patch
Patch1:         gcc9-stringop-bogus-warning.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  mbedtls-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bcunit)
BuildRequires:  pkgconfig(zlib)

%description
Utilities library used by Belledonne Communications softwares like
belle-sip, mediastreamer2 and linphone.

%package devel
Summary:        Development files for %{name}, a utility library for linphone/belle-sip/etc
Group:          Development/Languages/C and C++
Requires:       cmake
Requires:       lib%{name}%{sover} = %{version}
Requires:       lib%{name}-tester%{sover} = %{version}
Requires:       mbedtls-devel

%description devel
Utilities library used by Belledonne Communications softwares like
belle-sip, mediastreamer2 and linphone.

This package contains development files.

%package -n lib%{name}%{sover}
Summary:        Utility library for software from Belledonne Communications
Group:          System/Libraries

%description -n lib%{name}%{sover}
Utilities library used by Belledonne Communications softwares like
belle-sip, mediastreamer2 and linphone.

This package the contains shared library.

%package -n lib%{name}-tester%{sover}
Summary:        Utility library for software from Belledonne Communications
Group:          System/Libraries

%description -n lib%{name}-tester%{sover}
Utilities library used by Belledonne Communications softwares like
belle-sip, mediastreamer2 and linphone.

This package the contains shared library for testing component.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake \
  -DMBEDTLS_V2=YES             \
  -DENABLE_TESTS_COMPONENT=YES \
  -DENABLE_TESTS=YES           \
  -DENABLE_STATIC=NO
%make_jobs

%install
%cmake_install

%post -n lib%{name}%{sover} -p /sbin/ldconfig

%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%post -n lib%{name}-tester%{sover} -p /sbin/ldconfig

%postun -n lib%{name}-tester%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%license COPYING
%{_libdir}/lib%{name}.so.%{sover}*

%files -n lib%{name}-tester%{sover}
%license COPYING
%{_libdir}/lib%{name}-tester.so.%{sover}*

%files devel
%license COPYING
%doc AUTHORS README.md
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so
%{_datadir}/%{name}/
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/bctoolbox-tester.pc
%{_libdir}/lib%{name}-tester.so

%changelog
