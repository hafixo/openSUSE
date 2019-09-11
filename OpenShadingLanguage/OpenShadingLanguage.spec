#
# spec file for package OpenShadingLanguage
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

# The library soname versions follow the package version major and minor numbers.
%define sover %(echo %{version} | cut -d . -f 1,2)
%define sufx %(echo %{sover}|tr . _)

#NOTE: This package was created for blender, blender doesn't build against
# the 1.10.x ABI. If there is the need to update to such a version please consult me
# first davejplater@gmail.com or suffix the package with a 110 or something.

Name:           OpenShadingLanguage
Version:        1.9.13
Release:        0
Summary:        A language for programmable shading
License:        BSD-3-Clause
Group:          Productivity/Graphics/Other
Url:            https://github.com/imageworks/OpenShadingLanguage
Source0:        https://github.com/imageworks/OpenShadingLanguage/archive/Release-%{version}.tar.gz#/%{name}-Release-%{version}.tar.gz
Source1:        https://creativecommons.org/licenses/by/3.0/legalcode.txt
#PATCH-FIX-UPSTREAM 0001-Generalize-lookup-of-stdosl.h-in-install-directory-a.patch
#https://github.com/imageworks/OpenShadingLanguage/issues/955
Patch0:         0001-Generalize-lookup-of-stdosl.h-in-install-directory-a.patch
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  cmake(pugixml)
%if 0%{suse_version} >= 1500
BuildRequires:  clang-devel
%else
BuildRequires:  llvm-clang-devel >= 3.8
BuildRequires:  ncurses-devel
%endif
BuildRequires:  flex
BuildRequires:  gcc-c++
%if 0%{suse_version} >= 1500
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libboost_wave-devel
%else
# The default 1.54 is to old, 1.61 has unresolvable
# symbols in boost::wave (C++ ABI issue?)
BuildRequires:  boost-devel >= 1.55.0
BuildConflicts: boost-devel >= 1.61.0
%endif
BuildRequires:  OpenImageIO-devel
BuildRequires:  OpenEXR-devel
BuildRequires:  python
Requires:       %{name}-common-headers = %{version}
Recommends:     %{name}-doc = %{version}

%description
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

This package contains the standalone oslc compiler and some
utilities.

%package doc
Summary:        Documentation for OpenShadingLanguage
License:        CC-BY-3.0
Group:          Documentation/Other
Requires:       %{name} = %{version}

%description doc
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.
This package contains documentation.

%package MaterialX-shaders-source
Summary:        MaterialX shader nodes
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       %{name}-common-headers

%description MaterialX-shaders-source
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

This package contains the code for the MaterialX shader nodes.

%package example-shaders-source
Summary:        OSL shader examples
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       %{name}-common-headers

%description example-shaders-source
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

This package contains some OSL example shaders.

%package common-headers
Summary:        OSL standard library and auxiliary headers
Group:          Development/Languages/Other
Requires:       %{name} = %{version}

%description common-headers
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

This package contains the OSL standard library headers, as well
as some additional headers useful for writing shaders.

%package -n liboslcomp%{sufx}
Summary:        OpenShadingLanguage's compiler component library
Group:          System/Libraries

%description -n liboslcomp%{sufx}
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

%package -n liboslexec%{sufx}
Summary:        OpenShadingLanguage's execution component library
Group:          System/Libraries

%description -n liboslexec%{sufx}
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

%package -n liboslnoise%{sufx}
Summary:        OpenShadingLanguage's image noise generation library
Group:          System/Libraries

%description -n liboslnoise%{sufx}
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

%package -n liboslquery%{sufx}
Summary:        Osl library
Group:          System/Libraries

%description -n liboslquery%{sufx}
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

%package -n libtestshade%{sufx}
Summary:        Osl library
Group:          System/Libraries

%description -n libtestshade%{sufx}
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

%package -n osl.imageio%{sufx}
Summary:        Shader interface to OpenImageIO functions
Group:          System/Libraries

%description -n osl.imageio%{sufx}
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       liboslcomp%{sufx} = %{version}
Requires:       liboslexec%{sufx} = %{version}
Requires:       liboslnoise%{sufx} = %{version}
Requires:       liboslquery%{sufx} = %{version}
Requires:       libtestshade%{sufx} = %{version}
Requires:       osl.imageio%{sufx} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-Release-%{version}
%patch0 -p1

%build
# We use a combined LLVM on 15.0/TW, so libLLVMMCJIT is neither available nor needed
# On 42.3., we have to collect the split libraries ourselfs,
# as the supplied FindLLVM.cmake is broken
%if 0%{suse_version} < 1500
%define llvm_libs %(llvm-config --libfiles | tr ' ' ';')
%endif
%cmake \
      %{?llvm_libs:-DLLVM_LIBRARY="%{llvm_libs}"} \
      -DLLVM_MCJIT_LIBRARY="" \
      -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name} \
      -DOSL_INSTALL_SHADERDIR:PATH=%{_datadir}/%{name}

make %{?_smp_mflags}

%install
%cmake_install
# Add Creative Commons license for documentation
cp -v %{SOURCE1} .

find %{buildroot} -name LICENSE -print -delete
find %{buildroot} -type f -name "*.la" -delete -print

%post -n liboslcomp%{sufx} -p /sbin/ldconfig
%postun -n liboslcomp%{sufx} -p /sbin/ldconfig

%post -n liboslexec%{sufx} -p /sbin/ldconfig
%postun -n liboslexec%{sufx} -p /sbin/ldconfig

%post -n liboslnoise%{sufx} -p /sbin/ldconfig
%postun -n liboslnoise%{sufx} -p /sbin/ldconfig

%post -n liboslquery%{sufx} -p /sbin/ldconfig
%postun -n liboslquery%{sufx} -p /sbin/ldconfig

%post -n libtestshade%{sufx} -p /sbin/ldconfig
%postun -n libtestshade%{sufx} -p /sbin/ldconfig

%post -n osl.imageio%{sufx} -p /sbin/ldconfig
%postun -n osl.imageio%{sufx} -p /sbin/ldconfig


%files
%{_bindir}/*

%files doc
%license legalcode.txt
%doc %{_docdir}/%{name}/

%files MaterialX-shaders-source
%_datadir/%{name}/shaders/MaterialX

%files example-shaders-source
%_datadir/%{name}/shaders/*.osl
%_datadir/%{name}/shaders/*.oso

%files common-headers
%dir %_datadir/%{name}
%dir %_datadir/%{name}/shaders
%_datadir/%{name}/shaders/*.h

%files -n liboslcomp%{sufx}
%license LICENSE
%{_libdir}/liboslcomp.so.%{sover}*

%files -n liboslexec%{sufx}
%license LICENSE
%{_libdir}/liboslexec.so.%{sover}*

%files -n liboslnoise%{sufx}
%license LICENSE
%{_libdir}/liboslnoise.so.%{sover}*

%files -n liboslquery%{sufx}
%license LICENSE
%{_libdir}/liboslquery.so.%{sover}*

%files -n libtestshade%{sufx}
%license LICENSE
%{_libdir}/libtestshade.so.%{sover}*

%files -n osl.imageio%{sufx}
%license LICENSE
%{_libdir}/osl.imageio.so.%{sover}*

%files devel
%license LICENSE
%{_includedir}/*
%{_libdir}/*.so

%changelog
