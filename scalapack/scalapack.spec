#
# spec file for package scalapack
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


%global flavor @BUILD_FLAVOR@%{nil}

%define pname scalapack
%define vers 2.0.2
%define _vers 2_0_2
%define openblas_vers 0.3.6

%if 0%{?is_opensuse} || 0%{?is_backports}
%undefine DisOMPI1
%undefine DisOMPI2
%undefine DisOMPI3
%else
%define DisOMPI1 ExclusiveArch:  do_not_build
%undefine DisOMPI2
%define DisOMPI3 ExclusiveArch:  do_not_build
%endif

%if "%flavor" == ""
ExclusiveArch:  do_not_build
%define package_name %pname
%endif

%if "%flavor" == "openmpi"
%{?DisOMPI1}
%define mpi_flavor openmpi
%define mpi_vers 1
%{bcond_with hpc}
%endif

%if "%flavor" == "openmpi2"
%{?DisOMPI2}
%define mpi_flavor openmpi
%define mpi_vers 2
%{bcond_with hpc}
%endif

%if "%flavor" == "openmpi3"
%{?DisOMPI3}
%define mpi_flavor openmpi
%define mpi_vers 3
%{bcond_with hpc}
%{bcond_without blacs_devel_headers}
%else
# Only build header back on one multibuild for non-HPC.
# Note: For HPC the headers need to be built always.
%{bcond_with blacs_devel_headers}
%endif

%if "%flavor" == "mvapich2"
%define mpi_flavor mvapich2
%{bcond_with hpc}
%endif

%if "%flavor" == "gnu-openmpi-hpc"
%{?DisOMPI1}
%define mpi_flavor openmpi
%define compiler_family gnu
%undefine c_f_ver
%define mpi_vers 1
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu-openmpi2-hpc"
%{?DisOMPI2}
%define mpi_flavor openmpi
%define compiler_family gnu
%undefine c_f_ver
%define mpi_vers 2
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu-openmpi3-hpc"
%{?DisOMPI3}
%define mpi_flavor openmpi
%define compiler_family gnu
%undefine c_f_ver
%define mpi_vers 3
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu-mpich-hpc"
%define mpi_flavor mpich
%define compiler_family gnu
%undefine c_f_ver
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu-mvapich2-hpc"
%define mpi_flavor mvapich2
%define compiler_family gnu
%undefine c_f_ver
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu7-openmpi-hpc"
%{?DisOMPI1}
%define mpi_flavor openmpi
%define compiler_family gnu
%define c_f_ver 7
%define mpi_vers 1
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu7-mvapich2-hpc"
%define mpi_flavor mvapich2
%define compiler_family gnu
%define c_f_ver 7
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu7-openmpi3-hpc"
%{?DisOMPI3}
%define mpi_flavor openmpi
%define compiler_family gnu
%define c_f_ver 7
%define mpi_vers 3
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu7-mpich-hpc"
%define mpi_flavor mpich
%define compiler_family gnu
%define c_f_ver 7
%{bcond_without hpc}
%endif

%if !0%{?is_opensuse} && !0%{?with_hpc:1}
ExclusiveArch:  do_not_build
%endif

# For compatibility package names
%if "%{mpi_flavor}" != "openmpi" || "%{mpi_vers}" != "1"
%define mpi_ext %{?mpi_vers}
%endif

%define so_ver  2
%if %{without hpc}
%if 0%{!?package_name:1}
%define package_name %{pname}-%{mpi_flavor}%{?mpi_ext}
%endif
%define libname() lib%{pname}%{so_ver}-%{mpi_flavor}%{?mpi_ext}
%define libblacsname() libblacs%{so_ver}-%{mpi_flavor}%{?mpi_ext}
%define installdir %{_libdir}/mpi/gcc/%{mpi_flavor}%{?mpi_ext}
%define p_includedir %{_includedir}
%else
%{hpc_init -c %compiler_family -m %mpi_flavor %{?c_f_ver:-v %{c_f_ver}} %{?mpi_vers:-V %{mpi_vers}} %{?ext:-e %{ext}}}

%define package_name %{hpc_package_name %{?_vers}}
%define libname() lib%{pname}%{so_ver}%{expand:%%{hpc_package_name_tail %{**}}}
%global libname_plain %{libname}
%define libblacsname() libblacs%{so_ver}%{expand:%%{hpc_package_name_tail %{**}}}
%global libblacs_plain %{libblacsname}
%define installdir %{hpc_prefix}
%define p_includedir %{hpc_includedir}
%endif

Name:           %{package_name}
Version:        %vers
Release:        0
Summary:        A subset of LAPACK routines redesigned for heterogenous computing
# This is freely distributable without any restrictions.
License:        SUSE-Public-Domain
Group:          Development/Libraries/Parallel
Url:            http://www.netlib.org/scalapack/
Source0:        http://www.netlib.org/scalapack/%{pname}-%{version}.tgz
# PATCH-FIX-OPENSUSE scalapack-2.0.2-shared-lib.patch
Patch0:         scalapack-2.0.2-shared-lib.patch
# PATCH-FIX-OPENSUSE scalapack-2.0.2-shared-blacs.patch -- build shared blacs library
Patch1:         scalapack-2.0.2-shared-blacs.patch
%if %{without hpc}
BuildRequires:  %{mpi_flavor}%{?mpi_ext}-devel
BuildRequires:  blas-devel
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
%if %{without blacs_devel_headers}
BuildRequires:  blacs-devel-headers
%endif
%else
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  %{mpi_flavor}%{?mpi_vers}-%{compiler_family}%{?c_f_ver}-hpc-macros-devel
BuildRequires:  libopenblas%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc-devel
BuildRequires:  libopenblas-%{compiler_family}-hpc >=  %{openblas_vers}
BuildRequires:  lua-lmod
BuildRequires:  pkgconfig
BuildRequires:  suse-hpc
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The ScaLAPACK (or Scalable LAPACK) library includes a subset 
of LAPACK routines redesigned for distributed memory MIMD 
parallel computers. It is currently written in a 
Single-Program-Multiple-Data style using explicit message 
passing for interprocessor communication. It assumes 
matrices are laid out in a two-dimensional block cyclic 
decomposition.

ScaLAPACK is designed for heterogeneous computing and is 
portable on any computer that supports MPI or PVM.

Like LAPACK, the ScaLAPACK routines are based on 
block-partitioned algorithms in order to minimize the frequency 
of data movement between different levels of the memory hierarchy. 
(For such machines, the memory hierarchy includes the off-processor 
memory of other processors, in addition to the hierarchy of registers, 
cache, and local memory on each processor.) The fundamental building 
blocks of the ScaLAPACK library are distributed memory versions (PBLAS) 
of the Level 1, 2 and 3 BLAS, and a set of Basic Linear Algebra 
Communication Subprograms (BLACS) for communication tasks that arise 
frequently in parallel linear algebra computations. In the ScaLAPACK 
routines, all interprocessor communication occurs within the PBLAS and the 
BLACS. One of the design goals of ScaLAPACK was to have the ScaLAPACK 
routines resemble their LAPACK equivalents as much as possible. 

%package -n     blacs-devel-headers
Summary:        Development headers for BLACS
Group:          Development/Libraries/Parallel

%description -n blacs-devel-headers
This package contains headers for BLACS.

%package -n     %{libname %_vers}
Summary:        ScaLAPACK libraries compiled against %{mpi_flavor}%{?mpi_vers}
Group:          Development/Libraries/Parallel
Obsoletes:      %{name} < %{version}
Provides:       %{name} = %{version}
%if %{with hpc}
Requires:       %{name}-module
Requires:       libopenblas%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc
%hpc_requires
%endif

%description -n %{libname %_vers}
The ScaLAPACK (or Scalable LAPACK) library includes a subset
of LAPACK routines redesigned for distributed memory MIMD
parallel computers. It is currently written in a
Single-Program-Multiple-Data style using explicit message
passing for interprocessor communication. It assumes
matrices are laid out in a two-dimensional block cyclic
decomposition.

ScaLAPACK is designed for heterogeneous computing and is
portable on any computer that supports MPI or PVM.

Like LAPACK, the ScaLAPACK routines are based on
block-partitioned algorithms in order to minimize the frequency
of data movement between different levels of the memory hierarchy.
(For such machines, the memory hierarchy includes the off-processor
memory of other processors, in addition to the hierarchy of registers,
cache, and local memory on each processor.) The fundamental building
blocks of the ScaLAPACK library are distributed memory versions (PBLAS)
of the Level 1, 2 and 3 BLAS, and a set of Basic Linear Algebra
Communication Subprograms (BLACS) for communication tasks that arise
frequently in parallel linear algebra computations. In the ScaLAPACK
routines, all interprocessor communication occurs within the PBLAS and the
BLACS. One of the design goals of ScaLAPACK was to have the ScaLAPACK
routines resemble their LAPACK equivalents as much as possible.

This package contains ScaLAPACK	libraries compiled with	%{mpi_flavor}%{?mpi_vers}.

%{?with_hpc:%{hpc_master_package -s %so_ver -n %{libname_plain} -L}}

%package -n     %{libname %_vers}-devel
Summary:        Development libraries for ScaLAPACK (%{mpi_flavor}%{?mpi_vers})
Group:          Development/Libraries/Parallel
Requires:       %{libname %_vers} = %{version}
%if %{without hpc}
Requires:       %{mpi_flavor}%{?mpi_ext}-devel
%else
%hpc_requires_devel
Requires:       libopenblas%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc-devel
%endif
Obsoletes:      %{name}-devel < %{version}
Provides:       %{name}-devel = %{version}

%description -n %{libname %_vers}-devel
This package contains development libraries for ScaLAPACK, compiled against %{mpi_flavor}%{?mpi_vers}.

%{?with_hpc:%{hpc_master_package -n %{libname_plain}-devel -s %so_ver devel}}

%package -n     %{libname %_vers}-devel-static
Summary:        Static libraries for ScaLAPACK (%{mpi_flavor}%{?mpi_vers})
Group:          Development/Libraries/Parallel
Requires:       %{libname %_vers}-devel = %{version}
Obsoletes:      %{name}-devel-static < %{version}
Provides:       %{name}-devel-static = %{version}

%description -n %{libname %_vers}-devel-static
This package contains static libraries for ScaLAPACK, compiled against %{mpi_flavor}%{?mpi_vers}.

%package        test
Summary:        Test programs for ScaLAPACK (%{mpi_flavor}%{?mpi_vers})
Group:          Development/Libraries/Parallel

%description    test
This packages contains some test programs for ScaLAPACK compiled against
%{mpi_flavor}%{?mpi_vers}.

%package -n     %{libblacsname %_vers}
Summary:        Basic Linear Algebra Communication Subprograms
Group:          Development/Libraries/Parallel
%if %{with hpc}
Requires:       %{name}-module
%hpc_requires
%endif

%description -n %{libblacsname %_vers}
The BLACS (Basic Linear Algebra Communication Subprograms) project 
provides a linear algebra oriented message passing interface for
a large range of distributed memory platforms.

The length of time required to implement efficient distributed memory
algorithms makes it impractical to rewrite programs for every new
parallel machine. The BLACS exist in order to make linear algebra
applications both easier to program and more portable.

%{?with_hpc:%{hpc_master_package -l -n %{libblacs_plain} -N blacs -s %so_ver}}

%package -n     %{libblacsname %_vers}-devel
Summary:        Development libraries for BLACS (%{mpi_flavor}%{?mpi_vers})
Group:          Development/Libraries/Parallel
Requires:       %{libblacsname %_vers} = %{version}
%if %{without hpc}
Requires:       %{mpi_flavor}%{?mpi_ext}-devel
Requires:       blacs-devel-headers
Obsoletes:      blacs-%{mpi_flavor}%{?mpi_ext}-devel < %{version}
Provides:       blacs-%{mpi_flavor}%{?mpi_ext}-devel = %{version}
%else
%hpc_requires_devel
%endif

%description -n %{libblacsname %_vers}-devel
This package contains development libraries for BLACS, compiled against %{mpi_flavor}%{?mpi_vers}.

%package -n     %{libblacsname %_vers}-devel-static
Summary:        Development libraries for BLACS (%{mpi_flavor}%{?mpi_vers})
Group:          Development/Libraries/Parallel
Requires:       %{libblacsname %_vers}-devel = %{version}

%{?with_hpc:%{hpc_master_package -n %{libblacs_plain}-devel -N blacs -s %so_ver -a devel}}

%description -n %{libblacsname %_vers}-devel-static
This package contains static libraries for BLACS, compiled against %{mpi_flavor}%{?mpi_vers}.

%if %{with hpc}
%package module
Summary:        Module files for %{name}
Group:          Development/Libraries/Parallel

%description module
This package contains module files required by SCALAPACK and BLACS, compiled against %{mpi_flavor}%{?mpi_vers}.
%endif

%prep
%setup -q -c 
%patch0 -p1
%patch1 -p1
cd %{pname}-%{version}/
cp SLmake.inc.example SLmake.inc
cd ..
%if %{without hpc}
cat > %{_sourcedir}/baselibs.conf  <<EOF
%{libname %{?_vers}}
%{libname %{?_vers}}-devel
  requires -%{mpi_flavor}%{?mpi_ext}-<targettype>
  requires "%{libname %{?_vers}}-<targettype> = <version>"
EOF
%endif

%build
%if %{with hpc}
%hpc_debug
%hpc_setup
module load openblas
%endif

RPM_OPT_FLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
cd %{pname}-%{version};
%if %{without hpc}
echo $PATH | grep -q %{mpi_flavor}%{?mpi_ext} || PATH=/usr/%_lib/mpi/gcc/%{mpi_flavor}%{?mpi_ext}/bin:$PATH
%define makeargs  CC=/usr/%_lib/mpi/gcc/%{mpi_flavor}%{?mpi_ext}/bin/mpicc FC=/usr/%_lib/mpi/gcc/%{mpi_flavor}%{?mpi_ext}/bin/mpif90 %{?_smp_flags}
%else
%define makeargs FCFLAGS+="$(pkg-config --cflags openblas)" LIBS="$(pkg-config --libs openblas)" %{?_smp_flags}
%endif
make lib CFLAGS="$RPM_OPT_FLAGS -fPIC" FCFLAGS="$RPM_OPT_FLAGS -fPIC" %makeargs
cd TESTING/EIG;
make FCFLAGS="$RPM_OPT_FLAGS" %{makeargs}
cd ../LIN;
make FCFLAGS="$RPM_OPT_FLAGS" %{makeargs}

%install

mkdir -p %{buildroot}%{installdir}/%_lib
mkdir -p %{buildroot}%{installdir}/%{_lib}/TESTING

pushd %{pname}-%{version}
for f in *.a *.so*; do
    cp -f $f %{buildroot}%{installdir}/%_lib/$f
done
cp -f TESTING/x* TESTING/*.dat %{buildroot}%{installdir}/%{_lib}/TESTING

popd
pushd %{buildroot}%{installdir}/%_lib
ln -fs libscalapack.so.%{version} libscalapack.so.%{so_ver}
ln -fs libscalapack.so.%{version} libscalapack.so
ln -fs libblacs.so.%{version} libblacs.so.%{so_ver}
ln -fs libblacs.so.%{version} libblacs.so
popd

# blacs header
%if %{with hpc} || %{with blacs_devel_headers}
mkdir -p %{buildroot}%{p_includedir}/blacs/
install -m 644 %{pname}-%{version}/BLACS/SRC/Bdef.h %{buildroot}%{p_includedir}/blacs/
%endif
%if %{with hpc}
%{?hpc_write_pkgconfig:%hpc_write_pkgconfig -l %{pname}}
%{?hpc_write_pkgconfig:%hpc_write_pkgconfig -l blacs -n blacs}
# HPC module file
%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the %{pname} library built with the %{compiler_family} toolchain and %{hpc_mpi_family}."
puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{pname} built with %{compiler_family} toolchain and %{hpc_mpi_family}."
module-whatis "Version: %{version}"
module-whatis "Category: runtime library"
module-whatis "Description: %{SUMMARY:0}"
module-whatis "URL: %{url}"

set     version                     %{version}

if [ expr [ module-info mode load ] || [module-info mode display ] ] {
    if { ![is-loaded openblas]  } {
      module load openblas
    }
}

prepend-path    PATH                %{hpc_bindir}
prepend-path    LD_LIBRARY_PATH     %{hpc_prefix}/%_lib

setenv          %{hpc_upcase %pname}_DIR        %{hpc_prefix}

if {[file isdirectory  %{hpc_includedir}]} {
prepend-path    CPATH               %{hpc_includedir}
prepend-path    C_INCLUDE_PATH      %{hpc_includedir}
prepend-path    CPLUS_INCLUDE_PATH  %{hpc_includedir}
prepend-path    INCLUDE             %{hpc_includedir}
}

if {[file isdirectory  %{hpc_libdir}]} {
prepend-path    LIBRARY_PATH        %{hpc_libdir}
%hpc_modulefile_add_pkgconfig_path

setenv          %{hpc_upcase %pname}_LIB        %{hpc_libdir}
}
EOF
%endif

# Copy docs
cd %{pname}-%{version}
cp -f README LICENSE ../

%post -n %{libname %_vers} -p /sbin/ldconfig

%postun -n %{libname %_vers} -p/sbin/ldconfig

%post -n %{libblacsname %_vers} -p /sbin/ldconfig

%postun -n %{libblacsname %_vers} -p /sbin/ldconfig

%if %{with hpc}
%postun module
%{hpc_module_delete_if_default}
%endif

%files -n %{libname %_vers}
%license LICENSE
%doc README
%{installdir}/%_lib/libscalapack.so.*
%{?with_hpc:%hpc_dirs}

%files test
%{installdir}/%_lib/TESTING

%files -n %{libname %_vers}-devel
%{installdir}/%_lib/libscalapack.so
%{?with_hpc:%hpc_pkgconfig_file}

%files -n %{libname %_vers}-devel-static
%{installdir}/%_lib/libscalapack.a

%if %{without hpc}
%if %{with blacs_devel_headers}
%files -n blacs-devel-headers
%{p_includedir}/blacs/
%endif
%endif

%files -n %{libblacsname %_vers}
%{installdir}/%_lib/libblacs.so.*

%files -n %{libblacsname %_vers}-devel
%{installdir}/%_lib/libblacs.so
%if %{with hpc}
%{hpc_pkgconfig_file -n blacs}
%dir %{p_includedir}
%{p_includedir}/blacs
%endif

%files -n %{libblacsname %_vers}-devel-static
%{installdir}/%_lib/libblacs.a

%if %{with hpc}
%files module
%hpc_modules_files
%endif

%changelog
