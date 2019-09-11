#
# spec file for package libqt5-qtdeclarative
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define qt5_snapshot 0

%define libname libQtQuick5

Name:           libqt5-qtdeclarative
Version:        5.13.0
Release:        0
Summary:        Qt 5 Declarative Library
License:        LGPL-2.1-with-Qt-Company-Qt-exception-1.1 or LGPL-3.0-only
Group:          Development/Libraries/X11
Url:            https://www.qt.io
%define base_name libqt5
%define real_version 5.13.0
%define so_version 5.13.0
%define tar_version qtdeclarative-everywhere-src-5.13.0
Source:         https://download.qt.io/official_releases/qt/5.13/%{real_version}/submodules/%{tar_version}.tar.xz
Source1:        baselibs.conf
# PATCH-FIX-OPENSUSE sse2_nojit.patch -- enable JIT and sse2 only on sse2 case
Patch100:       sse2_nojit.patch
# PATCH-FIX-OPENSUSE Switch to use python3 at build time
Patch102:       qtdeclarative-switch-to-python3.patch
BuildRequires:  fdupes
BuildRequires:  libQt5Core-private-headers-devel >= %{version}
BuildRequires:  libQt5Gui-private-headers-devel >= %{version}
BuildRequires:  libQt5Test-private-headers-devel >= %{version}
BuildRequires:  libQt5Widgets-private-headers-devel >= %{version}
BuildRequires:  python3-base
BuildRequires:  pkgconfig(Qt5Core) >= %{version}
BuildRequires:  pkgconfig(Qt5Gui) >= %{version}
BuildRequires:  pkgconfig(Qt5Network) >= %{version}
BuildRequires:  pkgconfig(Qt5Sql) >= %{version}
BuildRequires:  pkgconfig(Qt5Widgets) >= %{version}
%if %qt5_snapshot
#to create the forwarding headers
BuildRequires:  perl
%endif
BuildRequires:  xz
# NOTE recheck this once/if this package gets further splitted
%requires_ge libQt5Core5
%requires_ge libQt5Gui5
%requires_ge libQt5Network5
%requires_ge libQt5Sql5
%requires_ge libQt5Test5
%requires_ge libQt5Widgets5

%description
Qt is a set of libraries for developing applications.

This package contains base tools, like string, xml, and network
handling.

%prep
%setup -q -n %{tar_version}
%autopatch -p1

%package -n %libname
Summary:        Qt 5 Declarative Library
Group:          Development/Libraries/X11
# Used by QtQuick.LocalStorage
Requires:       libQt5Sql5-sqlite

%description -n %libname
Qt is a set of libraries for developing applications.

This package contains base tools, like string, xml, and network
handling.

%package devel
Summary:        Qt Development Kit
Group:          Development/Libraries/X11
Requires:       %libname = %{version}
Requires:       %{name}-tools = %{version}
Provides:       libQt5Quick-devel = %{version}
Obsoletes:      libQt5Quick-devel < %{version}

%description devel
You need this package, if you want to compile programs with qtdeclarative.

%package tools
Summary:        Qt 5 Declarative Tools
Group:          Development/Tools/Debuggers

%description tools
Qt is a set of libraries for developing applications.

This package contains aditional tools for inspecting, testing, viewing, etc, QML imports and files.

%package private-headers-devel
Summary:        Non-ABI stable experimental API
Group:          Development/Libraries/C and C++
BuildArch:      noarch
Requires:       %{name}-devel = %{version}
Requires:       libQt5Core-private-headers-devel >= %{version}
Requires:       libQt5Gui-private-headers-devel >= %{version}
Requires:       libQt5Test-private-headers-devel >= %{version}
Requires:       libQt5Widgets-private-headers-devel >= %{version}
Provides:       libQt5Quick-private-headers-devel = %{version}
Obsoletes:      libQt5Quick-private-headers-devel < %{version}

%description private-headers-devel
This package provides private headers of libqt5-qtdeclarative that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package examples
Summary:        Qt5 quick/qml examples
Group:          Development/Libraries/X11
Recommends:     %{name}-devel
Recommends:     %{name}-tools

%description examples
Examples for libqt5-qtdeclarative (quick/qml) modules.

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%build
%if %qt5_snapshot
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif

mkdir -p %{_target_platform}
pushd %{_target_platform}
qmake-qt5 ..
popd

%{__make} %{?_smp_mflags} VERBOSE=1 -C %{_target_platform}

%ifarch %ix86
%if 0%{?sle_version:%sle_version} < 150000
# build libQt5Qml with no_sse2
mkdir -p %{_target_platform}-no_sse2
pushd %{_target_platform}-no_sse2
%qmake5 -config no_sse2 ..
make sub-src-clean
%{__make} %{?_smp_mflags} VERBOSE=1 -C src/qml
popd
%endif
%endif

%install
pushd %{_target_platform}
%qmake5_install
popd

%ifarch %ix86
%if 0%{?sle_version:%sle_version} < 150000
mkdir -p %{buildroot}%{_libqt5_libdir}//sse2
mv %{buildroot}%{_libqt5_libdir}/libQt5Qml.so.5* %{buildroot}%{_libqt5_libdir}/sse2/
pushd %{_target_platform}-no_sse2/src/qml
%qmake5_install
popd
%endif
%endif

find %{buildroot}/%{_libdir} -type f -name '*la' -print -exec perl -pi -e 's, -L%{_builddir}/\S+,,g' {} \;
find %{buildroot}/%{_libdir}/pkgconfig -type f -name '*pc' -print -exec perl -pi -e 's, -L%{_builddir}/\S+,,g' {} \;
# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

# put all the binaries to %%_bindir, add -qt5 suffix, and symlink them back to %%_qt5_bindir
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_libqt5_bindir}
for i in * ; do
  case "${i}" in
    qmlplugindump|qmlprofiler)
      mv $i ../../../bin/${i}-qt5
      ln -s ../../../bin/${i}-qt5 .
      ln -s ../../../bin/${i}-qt5 $i
      ;;
   *)
      mv $i ../../../bin/
      ln -s ../../../bin/$i .
      ;;
  esac
done
popd

%fdupes -s %{buildroot}%{_libqt5_includedir}
%fdupes -s %{buildroot}%{_libqt5_examplesdir}

%files -n %libname
%license LICENSE.*
%{_libqt5_libdir}/libQt5Q*.so.*
%ifarch %ix86
%if 0%{?sle_version:%sle_version} < 150000
%{_libqt5_libdir}/sse2/libQt5Q*.so.*
%endif
%endif
%dir %{_libqt5_archdatadir}/qml
%dir %{_libqt5_archdatadir}/qml/Qt
%{_libqt5_archdatadir}/qml/QtQuick
%{_libqt5_archdatadir}/qml/QtQuick.2
%{_libqt5_archdatadir}/qml/QtQml
%{_libqt5_archdatadir}/qml/builtins.qmltypes
%dir %{_libqt5_archdatadir}/qml/Qt/labs
%{_libqt5_archdatadir}/qml/Qt/labs/folderlistmodel/
%{_libqt5_archdatadir}/qml/Qt/labs/settings/
%{_libqt5_archdatadir}/qml/Qt/labs/sharedimage/
%{_libqt5_archdatadir}/qml/Qt/labs/qmlmodels/
%{_libqt5_archdatadir}/qml/Qt/labs/wavefrontmesh/
%{_libqt5_plugindir}/qmltooling

%files private-headers-devel
%license LICENSE.*
%{_libqt5_includedir}/Qt*/%{so_version}

%files tools
%license LICENSE.*
%{_bindir}/*
%{_libqt5_bindir}/*

%files devel
%license LICENSE.*
%exclude %{_libqt5_includedir}/Qt*/%{so_version}
%{_libqt5_includedir}/Qt*
%{_libqt5_libdir}/cmake/Qt5*
%{_libqt5_libdir}/libQt5*.prl
%{_libqt5_libdir}/libQt5Q*.so
%{_libqt5_libdir}/libQt5*.a
%{_libqt5_libdir}/pkgconfig/Qt5Q*.pc
%{_libqt5_archdatadir}/mkspecs/modules/*.pri
%{_libqt5_archdatadir}/mkspecs/features/qmlcache.prf
%{_libqt5_archdatadir}/mkspecs/features/qtquickcompiler.prf
%{_libqt5_archdatadir}/qml/QtTest

%files examples
%license LICENSE.*
%{_libqt5_examplesdir}/

%changelog
