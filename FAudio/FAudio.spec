#
# spec file for package openal-soft
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


Name:           FAudio
%define realver 1903
Version:        19.03
Release:        0
Summary:        A reimplementation of the XNA Game Studio libraries
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            https://fna-xna.github.io/
Source0:        http://fna.flibitijibibo.com/archive/FNA-%realver.zip
Source1:        baselibs.conf
Patch0:		faudio-older-sdl2.patch
BuildRequires:  unzip
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  SDL2-devel

%description
FNA is a reimplementation of the Microsoft XNA Game Studio 4.0 Refresh libraries.

%package -n libFAudio0
Summary:        A reimplementation of the XNA Game Studio libraries
Group:          System/Libraries

%description -n libFAudio0
FNA is a reimplementation of the Microsoft XNA Game Studio 4.0 Refresh libraries.


%package devel
Summary:        FAudio Development Libraries
Group:          Development/Languages/C and C++
Requires:       libFAudio0 = %{version}

%description devel
FNA is a reimplementation of the Microsoft XNA Game Studio 4.0 Refresh libraries.


%prep
%setup -q -n FNA
%patch0 -p1

%build
cd lib/FAudio
%cmake \
  -DCMAKE_BUILD_TYPE=Release 
make %{?_smp_mflags}

%install
cd lib/FAudio
%cmake_install

%post -n libFAudio0 -p /sbin/ldconfig
%postun -n libFAudio0 -p /sbin/ldconfig

%files -n libFAudio0
%license lib/FAudio/LICENSE
%{_libdir}/libFAudio.so.0*

%files devel
%license lib/FAudio/LICENSE
%{_includedir}/FAudio.h
%{_includedir}/FAPOFX.h
%{_includedir}/FACT3D.h
%{_includedir}/F3DAudio.h
%{_includedir}/FACT.h
%{_includedir}/FAPO.h
%{_includedir}/FAudioFX.h
%{_includedir}/FAPOBase.h
%{_libdir}/libFAudio.so
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/FAudio
%{_libdir}/cmake/FAudio/FAudio-config.cmake
%{_libdir}/cmake/FAudio/FAudio-targets.cmake
%{_libdir}/cmake/FAudio/FAudio-targets-release.cmake

%changelog
