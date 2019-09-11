#
# spec file for package libfilezilla
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


%define major		0
%define libname		%{name}%{major}
%define develname	%{name}-devel
Name:           libfilezilla
Version:        0.17.1
Release:        0
Summary:        C++ library for filezilla
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://lib.filezilla-project.org/
Source0:        https://download.filezilla-project.org/libfilezilla/%{name}-%{version}.tar.bz2
Patch0:         %{name}-date-time.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(gnutls) >= 3.5.7
BuildRequires:  pkgconfig(nettle) >= 3.1

%description
libfilezilla is C++ library, offering some basic functionality to
build high-performing, platform-independent programs. libfilezilla is
needed for filezilla (an FTP client and server) to build.

%package -n	%{libname}
Summary:        C++ library for filezilla
Group:          System/Libraries

%description -n	%{libname}
libfilezilla is C++ library, offering some basic functionality to
build high-performing, platform-independent programs. libfilezilla is
needed for filezilla (an FTP client and server) to build. Some of the
highlights include:

* A typesafe, multi-threaded event system.
* Timers for periodic events.
* A datetime class that not only tracks timestamp but also their accuracy,
  which simplifies dealing with timestamps originating from different sources.
* Simple process handling for spawning child processes with redirected I/O.

%package -n	%{develname}
Summary:        Development package for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}-%{release}

%description -n	%{develname}
Files needed for development with %{name}.

%prep
%setup -q
%patch0

%build
autoreconf -fi
%configure --disable-static
make %{?_smp_mflags}

pushd doc
make %{?_smp_mflags} html
popd

%install
%make_install
# we don't want this
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}%{_docdir}/%{develname}
cp -r doc/doxygen-doc/* %{buildroot}%{_docdir}/%{develname}/
rm -f %{buildroot}%{_docdir}/%{develname}/latex/refman.tex
%fdupes -s %{buildroot}%{_docdir}/%{develname}
%find_lang %name

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname} -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/%{name}.so.%{major}*

%files -n %{develname}
%dir %{_docdir}/%{develname}
%{_docdir}/%{develname}/*
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
