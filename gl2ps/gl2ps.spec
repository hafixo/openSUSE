#
# spec file for package gl2ps
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define so_ver 1
Name:           gl2ps
Version:        1.4.0
Release:        0
Summary:        OpenGL to PostScript Printing Library
License:        LGPL-2.0+ or SUSE-GL2PS-2.0
Group:          Development/Libraries/C and C++
Url:            http://www.geuz.org/gl2ps/
Source0:        http://geuz.org/gl2ps/src/%{name}-%{version}.tgz
# PATCH-FIX-UPSTREAM no-copy-dt-needed-entries.patch asterios.dramis@gmail.com -- Fix linking with --no-copy-dt-needed-entries
Patch0:         no-copy-dt-needed-entries.patch
BuildRequires:  cmake
BuildRequires:  freeglut-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?sles_version}
BuildRequires:  Mesa-devel
%else
BuildRequires:  pkgconfig(gl)
%endif
%if 0%{?suse_version} > 1230
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
%endif

%description
GL2PS is a C library providing vector output for any OpenGL
application. It uses sorting algorithms capable of handling
intersecting and stretched polygons, as well as non-manifold objects.
GL2PS provides smooth shading and text rendering, culling of
invisible primitives and mixed vector/bitmap output.

GL2PS can create PostScript (PS), Encapsulated PostScript (EPS),
Portable Document Format (PDF) and Scalable Vector Graphics (SVG)
files, as well as LaTeX files for the text fragments. It also
provides limited, experimental support for Portable LaTeX Graphics
(PGF).

The pstoedit program can also be used to transform the PostScript
files generated by GL2PS into many other vector formats such as xfig,
cgm, wmf, etc.

%package devel
Summary:        Development files for GL2PS
Group:          Development/Libraries/C and C++
Requires:       libgl2ps%{so_ver} = %{version}

%description devel
This package provides development libraries and headers needed to build
software using GL2PS.

%package -n libgl2ps%{so_ver}
Summary:        OpenGL to PostScript Printing Library
Group:          System/Libraries

%description -n libgl2ps%{so_ver}
GL2PS is a C library providing vector output for any OpenGL
application. It uses sorting algorithms capable of handling
intersecting and stretched polygons, as well as non-manifold objects.
GL2PS provides smooth shading and text rendering, culling of
invisible primitives and mixed vector/bitmap output.

%prep
%setup -q -n %{name}-%{version}-source
%patch0

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install
# Remove static libraries
rm -f %{buildroot}%{_libdir}/libgl2ps.a
# Remove doc files (they are installed in the %%files section)
rm -rf %{buildroot}%{_datadir}/doc/gl2ps/

%post -n libgl2ps%{so_ver} -p /sbin/ldconfig

%postun -n libgl2ps%{so_ver} -p /sbin/ldconfig

%files devel
%defattr(-,root,root,-)
%doc COPYING.GL2PS COPYING.LGPL README.txt gl2ps.pdf gl2psTest*.c
%{_includedir}/gl2ps.h
%{_libdir}/libgl2ps.so

%files -n libgl2ps%{so_ver}
%defattr(-,root,root,-)
%{_libdir}/libgl2ps.so.%{so_ver}*

%changelog
