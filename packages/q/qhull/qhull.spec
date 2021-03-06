#
# spec file for package qhull
#
# Copyright (c) 2020 SUSE LLC
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


%define sonum   7
%define srcyear 2019
%define srcver  7.3.2
Name:           qhull
Version:        2019.1
Release:        0
Summary:        Computing convex hulls, Delaunay triangulations and Voronoi diagrams
License:        Qhull
Group:          Development/Libraries/C and C++
URL:            http://www.qhull.org
Source0:        http://www.qhull.org/download/qhull-%{srcyear}-src-%{srcver}.tgz
# PATCH-FIX-UPSTREAM -- https://github.com/qhull/qhull/pull/69
Patch0:         0001-Allow-disabling-of-static-or-shared-library-builds.patch
# PATCH-FIX-OPENSUSE
Patch1:         0002-Remove-tools-from-CMake-exported-targets.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Qhull computes the convex hull, Delaunay triangulation, Voronoi diagram,
halfspace intersection about a point, furthest-site Delaunay triangulation,
and furthest-site Voronoi diagram. The source code runs in 2D
and higher dimensions. Qhull implements the Quickhull algorithm for computing
the convex hull. It handles roundoff errors from floating point arithmetic. It
computes volumes, surface areas, and approximations to the convex hull.

Qhull does not support constrained Delaunay triangulations, triangulation of
non-convex surfaces, mesh generation of non-convex objects, or medium-sized
inputs in 9-D and higher.

%package -n libqhull%{sonum}
Summary:        Computing convex hulls, Delaunay triangulations and Voronoi diagrams
# Bad naming of old packages, conflicts on the file level (libqhull.so.7)
Group:          System/Libraries
Obsoletes:      libqhull%{sonum}-7_3_2 < %{version}-%{release}
Provides:       libqhull%{sonum}-7_3_2 = %{version}-%{release}
Obsoletes:      libqhull%{sonum}-7_2_0 < %{version}

%description -n libqhull%{sonum}
Qhull computes the convex hull, Delaunay triangulation, Voronoi diagram,
halfspace intersection about a point, furthest-site Delaunay triangulation,
and furthest-site Voronoi diagram. The source code runs in 2D
and higher dimensions. Qhull implements the Quickhull algorithm for computing
the convex hull. It handles roundoff errors from floating point arithmetic. It
computes volumes, surface areas, and approximations to the convex hull.

Qhull does not support constrained Delaunay triangulations, triangulation of
non-convex surfaces, mesh generation of non-convex objects, or medium-sized
inputs in 9-D and higher.

%package devel
Summary:        Development and documentation files for qhull
Group:          Development/Libraries/C and C++
Requires:       libqhull%{sonum} = %{version}

%description devel
Qhull computes the convex hull, Delaunay triangulation, Voronoi diagram,
halfspace intersection about a point, furthest-site Delaunay triangulation,
and furthest-site Voronoi diagram.

This package contains the header files for the Qhull libraries.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake \
        -DDOC_INSTALL_DIR="%{_docdir}/%{name}" \
        -DINCLUDE_INSTALL_DIR="%{_includedir}" \
        -DLIB_INSTALL_DIR="%{_lib}" \
        -DBIN_INSTALL_DIR="%{_bindir}" \
        -DMAN_INSTALL_DIR="%{_mandir}/man1/"
%make_jobs

%install
%cmake_install
# Fixup wrong location
%if "%{_lib}" != "lib"
mv %{buildroot}%{_prefix}/lib/cmake %{buildroot}%{_libdir}/
%endif

%post -n libqhull%{sonum} -p /sbin/ldconfig
%postun -n libqhull%{sonum} -p /sbin/ldconfig

%files
%license COPYING.txt
%doc src/Changes.txt
%{_docdir}/%{name}/
%{_bindir}/qconvex
%{_bindir}/qdelaunay
%{_bindir}/qhalf
%{_bindir}/qhull
%{_bindir}/qvoronoi
%{_bindir}/rbox
%{_mandir}/man1/*

%files -n libqhull%{sonum}
%license COPYING.txt
%{_libdir}/libqhull.so.%{sonum}
%{_libdir}/libqhull.so.%{srcver}
%{_libdir}/libqhull_p.so.%{sonum}
%{_libdir}/libqhull_p.so.%{srcver}
%{_libdir}/libqhull_r.so.%{sonum}
%{_libdir}/libqhull_r.so.%{srcver}

%files devel
%license COPYING.txt
%{_includedir}/libqhull/
%{_includedir}/libqhull_r/
%{_includedir}/libqhullcpp/
%{_libdir}/libqhull.so
%{_libdir}/libqhull_p.so
%{_libdir}/libqhull_r.so
%{_libdir}/cmake/Qhull

%changelog
