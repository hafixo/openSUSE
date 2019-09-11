#
# spec file for package vde2
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


Name:           vde2
Version:        2.3.2+svn587
Release:        0
Summary:        Virtual Distributed Ethernet
License:        GPL-2.0
Group:          Productivity/Networking/Other
Url:            http://vde.sourceforge.net/
Source0:        %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM: always overflows destination buffer
Patch0:         vde2-buffer-overflow.patch
# PATCH-FIX-UPSTREAM: openssl 1.1 compatibility
Patch1:         vde2-openssl_1.1_compatibility.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libpcap-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)
Recommends:     %{name}-cryptcab = %{version}
Recommends:     %{name}-slirp = %{version}
Recommends:     kvm
Recommends:     qemu

%description
VDE is a virtual network that can be spawned over a set of physical
computer over the Internet

VDE connects together:
  (1) real GNU-linux boxes (tuntap)
  (2) virtual machines: UML-User Mode Linux, qemu, bochs, MPS.

VDE can be used:
  (i) to create a general purpose tunnel (every protocol that runs
    on a Ethernet can be put into the tunnel)
  (ii) to connect a set of virtual machine to the Internet with no
    need of free access of tuntap
  (iii) to support mobility: a VDE can stay interconnected despite
    of the change of virtual cables, i.e. the change of IP addresses
    and interface in the real world

%package cryptcab
Summary:        VDE ecryption module
License:        GPL-2.0
Group:          Productivity/Networking/Other

%description cryptcab
This package contains CryptCab, which can be used
to send encrypted data over an UDP link.

%package slirp
Summary:        VDE ecryption module
License:        BSD-4-Clause AND MIT
Group:          Productivity/Networking/Other

%description slirp
slirpvde is a slirp interface for a VDE network.
Slirpvde  connects  all  the units (virtual or real machines) to the network
of the host where slirpvde runs as it were a NAT/Masquerading router.
The default route is the node 2 (10.0.2.2 in the default  network  configuration)
and DNS is re-mapped in node 3 (10.0.2.3).

Slirpvde  runs  using  standard user privileges (no need for root access):
all the connections are re-generated by slirpvde itself.

IPv4 only. IPv6 is still unsupported (will be supported when slirpvde
will be rewritten using the  LWIPv6  network stack).

%package -n libvdehist0
Summary:        VDE history library
License:        GPL-2.0
Group:          System/Libraries

%description -n libvdehist0
This package contains VDE history library
A library to manage history and command completion for vde mgmt protocol

%package -n libvdemgmt0
Summary:        VDE management library
License:        GPL-2.0
Group:          System/Libraries

%description -n libvdemgmt0
This package contains a library to interact with vde_switch
management console using pre-made unattended scripts.

%package -n libvdeplug3
Summary:        VDE plug library
License:        GPL-2.0
Group:          System/Libraries

%description -n libvdeplug3
This package contains a library that makes programs able to connect
to a local VDE switch. The simplest one is vde_plug, contained in the vde2 package.

%package -n libvdesnmp0
Summary:        VDE snmp library
License:        GPL-2.0
Group:          System/Libraries

%description -n libvdesnmp0
This package contains VDE snmp library
SNMP library for Virtual Distributed Ethernet

%package -n libvdehist-devel
Summary:        VDE hist header files
License:        GPL-2.0
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libvdehist0 = %{version}
Obsoletes:      libvdehist0-devel < %{version}-%{release}
Provides:       libvdehist0-devel = %{version}-%{release}

%description -n libvdehist-devel
This package contains VDE hist header files

%package -n libvdemgmt-devel
Summary:        VDE management files
License:        GPL-2.0
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libvdemgmt0 = %{version}
Obsoletes:      libvdemgmt0-devel < %{version}-%{release}
Provides:       libvdemgmt0-devel = %{version}-%{release}

%description -n libvdemgmt-devel
This package contains VDE management files

%package -n libvdeplug-devel
Summary:        VDE plug header files
License:        GPL-2.0
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libvdeplug3 = %{version}
Obsoletes:      libvdeplug3-devel < %{version}-%{release}
Provides:       libvdeplug3-devel = %{version}-%{release}

%description -n libvdeplug-devel
This package contains VDE plug header files

%package -n libvdesnmp-devel
Summary:        VDE SNMP header files
License:        GPL-2.0
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libvdesnmp0 = %{version}
Obsoletes:      libvdesnmp0-devel < %{version}-%{release}
Provides:       libvdesnmp0-devel = %{version}-%{release}

%description -n libvdesnmp-devel
This package contains VDE SNMP header files.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoreconf -fvi
# --enable-experimental even tho weird it has useful features and
#   vde2 on its own is no longer developed
%configure \
  --disable-silent-rules \
  --enable-kernel-switch \
  --disable-static \
  --enable-experimental \
  --disable-python
# Not thread safe makefiles
make -j1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libvdehist0 -p /sbin/ldconfig
%postun -n libvdehist0 -p /sbin/ldconfig
%post -n libvdemgmt0 -p /sbin/ldconfig
%postun -n libvdemgmt0 -p /sbin/ldconfig
%post -n libvdeplug3 -p /sbin/ldconfig
%postun -n libvdeplug3 -p /sbin/ldconfig
%post -n libvdesnmp0 -p /sbin/ldconfig
%postun -n libvdesnmp0 -p /sbin/ldconfig

%files
%doc Changelog README COPYING
%doc doc/README.VirtualBox doc/README.qemu doc/vde_autolink-HOWTO
%doc doc/README.UML doc/vdeqemu-HOWTO doc/README.vde_over_ns
%dir %{_libdir}/vde2
%dir %{_libdir}/vde2/vde_l3
%dir %{_sysconfdir}/vde2
%{_bindir}/dpipe
%{_bindir}/kvde_switch
%{_bindir}/unixcmd
%{_bindir}/unixterm
%{_bindir}/vde_autolink
%{_bindir}/vde_l3
%{_bindir}/vde_over_ns
%{_bindir}/vde_pcapplug
%{_bindir}/vde_plug
%{_bindir}/vde_plug2tap
%{_bindir}/vde_switch
%{_bindir}/vde_router
%{_bindir}/vde_vxlan
%{_bindir}/vdecmd
%{_bindir}/vdekvm
%{_bindir}/vdeq
%{_bindir}/vdeqemu
%{_bindir}/vdeterm
%{_bindir}/wirefilter
%{_sbindir}/vde_tunctl
%{_libexecdir}/vdetap
%{_libdir}/vde2/libvdetap.so
%{_libdir}/vde2/vde_l3/bfifo.so
%{_libdir}/vde2/vde_l3/pfifo.so
%{_libdir}/vde2/vde_l3/tbf.so
%dir %{_libdir}/vde2/plugins
%{_libdir}/vde2/plugins/dump.so
%{_libdir}/vde2/plugins/iplog.so
%{_libdir}/vde2/plugins/pdump.so
%config %{_sysconfdir}/vde2/vdecmd
%{_mandir}/man1/*
%{_mandir}/man8/*
%exclude %{_mandir}/man1/vde_cryptcab.*
%exclude %{_mandir}/man1/slirpvde.*

%files cryptcab
%doc Changelog README COPYING
%{_bindir}/vde_cryptcab
%{_mandir}/man1/vde_cryptcab.1%{ext_man}

%files slirp
%doc Changelog README COPYING doc/README.slirpvde
%{_bindir}/slirpvde
%{_mandir}/man1/slirpvde.1%{ext_man}

%files -n libvdehist0
%doc Changelog README COPYING
%{_libdir}/libvdehist.so.0
%{_libdir}/libvdehist.so.0.0.1

%files -n libvdemgmt0
%doc Changelog README COPYING
%dir %{_sysconfdir}/vde2/libvdemgmt
%{_libdir}/libvdemgmt.so.0
%{_libdir}/libvdemgmt.so.0.0.1
%config %{_sysconfdir}/vde2/libvdemgmt/asyncrecv.rc
%config %{_sysconfdir}/vde2/libvdemgmt/closemachine.rc
%config %{_sysconfdir}/vde2/libvdemgmt/openmachine.rc
%config %{_sysconfdir}/vde2/libvdemgmt/sendcmd.rc

%files -n libvdeplug3
%doc Changelog README COPYING COPYING.libvdeplug
%{_libdir}/libvdeplug.so.3
%{_libdir}/libvdeplug.so.3.0.1

%files -n libvdesnmp0
%doc Changelog README COPYING
%{_libdir}/libvdesnmp.so.0
%{_libdir}/libvdesnmp.so.0.0.1

%files -n libvdehist-devel
%doc Changelog README COPYING
%{_includedir}/libvdehist.h
%{_libdir}/libvdehist.so
%{_libdir}/pkgconfig/vdehist.pc

%files -n libvdemgmt-devel
%doc Changelog README COPYING
%{_includedir}/libvdemgmt.h
%{_libdir}/libvdemgmt.so
%{_libdir}/pkgconfig/vdemgmt.pc

%files -n libvdeplug-devel
%doc Changelog README COPYING
%{_includedir}/libvdeplug.h
%{_includedir}/libvdeplug_dyn.h
%{_libdir}/libvdeplug.so
%{_libdir}/pkgconfig/vdeplug.pc

%files -n libvdesnmp-devel
%doc Changelog README COPYING
%{_includedir}/libvdesnmp.h
%{_libdir}/libvdesnmp.so
%{_libdir}/pkgconfig/vdesnmp.pc

%changelog
