#
# spec file for package libqt5-qtconnectivity
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
%define libname libQt5Bluetooth5
%define base_name libqt5
%define real_version 5.13.0
%define so_version 5.13.0
%define tar_version qtconnectivity-everywhere-src-5.13.0
Name:           libqt5-qtconnectivity
Version:        5.13.0
Release:        0
Summary:        Qt 5 Nfc Addon
License:        LGPL-2.1-with-Qt-Company-Qt-exception-1.1 or LGPL-3.0-only
Group:          Development/Libraries/X11
Url:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/5.13/%{real_version}/submodules/%{tar_version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  fdupes
BuildRequires:  libqt5-qtbase-devel >= %{version}
BuildRequires:  libqt5-qtbase-private-headers-devel >= %{version}
BuildRequires:  libqt5-qtdeclarative-private-headers-devel >= %{version}
BuildRequires:  xz
BuildRequires:  pkgconfig(bluez)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{qt5_snapshot}
#to create the forwarding headers
BuildRequires:  perl
%endif

%description
Qt is a set of libraries for developing applications.

%prep
%setup -q -n %{tar_version}

%package -n %{libname}
Summary:        Qt 5 Bluez Addon
Group:          Development/Libraries/X11
Recommends:     %{name}-tools
%requires_ge libQt5DBus5

%description -n %{libname}
Qt is a set of libraries for developing applications.

%package -n libQt5Nfc5
Summary:        Qt 5 Nfc Addon
Group:          Development/Libraries/X11
%requires_ge libQt5Core5

%description -n libQt5Nfc5
Qt is a set of libraries for developing applications.

%package -n %{libname}-imports
Summary:        Qt 5 Bluez Addon
Group:          Development/Libraries/X11
Supplements:    packageand(%{libname}:libQtQuick5)
# imports splited with 5.4.1
Conflicts:      %{libname} < 5.4.1
%requires_ge libQtQuick5

%description -n %{libname}-imports
Qt is a set of libraries for developing applications.

%package -n libQt5Nfc5-imports
Summary:        Qt 5 Nfc Addon
Group:          Development/Libraries/X11
Supplements:    packageand(libQt5Nfc5:libQtQuick5)
# imports splited with 5.4.1
Conflicts:      libQt5Nfc5 < 5.4.1
%requires_ge libQtQuick5

%description -n libQt5Nfc5-imports
Qt is a set of libraries for developing applications.

%package tools
Summary:        Qt 5 Nfc Addon
Group:          Development/Libraries/X11

%description tools
Qt is a set of libraries for developing applications.

%package devel
Summary:        Qt Development Kit
Group:          Development/Libraries/X11
Requires:       %{libname} = %{version}
Requires:       libQt5Nfc5 = %{version}

%description devel
You need this package, if you want to compile programs with qtsensors.

%package private-headers-devel
Summary:        Non-ABI stable experimental API
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       libqt5-qtbase-private-headers-devel
Requires:       libqt5-qtdeclarative-private-headers-devel
BuildArch:      noarch

%description private-headers-devel
This package provides private headers of libqt5-qtsensors that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package examples
Summary:        Qt5 location examples
Group:          Development/Libraries/X11
Recommends:     %{name}-devel

%description examples
Examples for libqt5-qtconnectivity module.

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%post -n libQt5Nfc5 -p /sbin/ldconfig

%postun -n libQt5Nfc5 -p /sbin/ldconfig

%build
%if %{qt5_snapshot}
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
rm -rfv src/tools/sdpscanner/qt_attribution.json
%{qmake5}
%{make_jobs}

%install
%{qmake5_install}
find %{buildroot}/%{_libdir} -type f -name '*la' -print -exec perl -pi -e 's, -L%{_builddir}/\S+,,g' {} \;
find %{buildroot}/%{_libdir}/pkgconfig -type f -name '*pc' -print -exec perl -pi -e 's, -L%{_builddir}/\S+,,g' {} \;
# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

# put all the binaries to %%_bindir, add -qt5 suffix, and symlink them back to %%_qt5_bindir
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_libqt5_bindir}
for i in * ; do
      mv $i ../../../bin/
      ln -s ../../../bin/$i .
done
popd

%files -n %{libname}
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_libdir}/libQt5Bluetooth.so.*

%files -n %{libname}-imports
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_archdatadir}/qml/QtBluetooth/

%files -n libQt5Nfc5
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_libdir}/libQt5Nfc.so.*

%files -n libQt5Nfc5-imports
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_archdatadir}/qml/QtNfc/

%files private-headers-devel
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_includedir}/QtNfc/%{so_version}
%{_libqt5_includedir}/QtBluetooth/%{so_version}

%files devel
%defattr(-,root,root,755)
%doc LICENSE.*
%exclude %{_libqt5_includedir}/QtNfc/%{so_version}
%exclude %{_libqt5_includedir}/QtBluetooth/%{so_version}
%{_libqt5_includedir}/QtNfc
%{_libqt5_includedir}/QtBluetooth
%{_libqt5_libdir}/cmake/Qt5Bluetooth/
%{_libqt5_libdir}/cmake/Qt5Nfc/
%{_libqt5_libdir}/libQt5Bluetooth.prl
%{_libqt5_libdir}/libQt5Nfc.prl
%{_libqt5_libdir}/libQt5Bluetooth.so
%{_libqt5_libdir}/libQt5Nfc.so
%{_libqt5_libdir}/pkgconfig/Qt5Bluetooth.pc
%{_libqt5_libdir}/pkgconfig/Qt5Nfc.pc
%{_libqt5_libdir}/qt5/mkspecs/modules/qt_lib_*.pri

%files tools
%defattr(-,root,root,755)
%doc LICENSE.*
%{_bindir}/sdpscanner*
%{_libqt5_bindir}/sdpscanner*

%files examples
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_examplesdir}/

%changelog
