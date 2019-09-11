#
# spec file for package socket_wrapper
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


############################# NOTE ##################################
#
# This is a special library. You are not able to link this library.
# Do NOT create library package or a devel package!
#
############################# NOTE ##################################

Name:           socket_wrapper
Version:        1.2.3
Release:        0
Summary:        A library passing all socket communications trough Unix sockets
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            http://cwrap.org/
Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
Source2:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz.asc
Source3:        socket_wrapper.keyring
BuildRequires:  cmake
BuildRequires:  libcmocka-devel
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Requires:       cmake
Requires:       pkg-config

%description
socket_wrapper aims to help client/server software development teams willing to
gain full functional test coverage. It makes it possible to run several instances
of the full software stack on the same machine and perform locally functional
testing of complex network configurations.

To use it set the following environment variables:

LD_PRELOAD=libsocket_wrapper.so
SOCKET_WRAPPER_DIR=/path/to/swrap_dir

%prep
%setup -q

%build
%cmake \
  -DUNIT_TESTING=ON

make %{?_smp_mflags} VERBOSE=1

%install
%cmake_install

%check
pushd build
make %{?_smp_mflags} test || cat $(find Testing -name "*.log")
popd

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS README.md ChangeLog
%license LICENSE
%{_libdir}/libsocket_wrapper.so.*
%{_mandir}/man1/socket_wrapper.1*
%{_libdir}/libsocket_wrapper.so
%dir %{_libdir}/cmake/socket_wrapper
%{_libdir}/cmake/socket_wrapper/socket_wrapper-config-version.cmake
%{_libdir}/cmake/socket_wrapper/socket_wrapper-config.cmake
%{_libdir}/pkgconfig/socket_wrapper.pc

%changelog
