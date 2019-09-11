#
# spec file for package dnsmasq
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           dnsmasq
Summary:        DNS Forwarder and DHCP Server
License:        GPL-2.0-only OR GPL-3.0-only
Group:          Productivity/Networking/DNS/Servers
Version:        2.80
Release:        0
Provides:       dns_daemon
PreReq:         /usr/sbin/useradd /bin/mkdir
Url:            http://www.thekelleys.org.uk/dnsmasq/
Source0:        http://www.thekelleys.org.uk/%{name}/%{name}-%{version}.tar.xz
Source1:        http://www.thekelleys.org.uk/%{name}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Source3:        dnsmasq.reg
Source4:        dnsmasq.service
Source5:        rc.dnsmasq-suse
Source8:        %{name}-rpmlintrc
Patch0:         dnsmasq-groups.patch
Patch1:         0001-fix-build-after-y2038-changes-in-glibc.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  dbus-1-devel
BuildRequires:  dos2unix
BuildRequires:  libidn2-devel
BuildRequires:  libnettle-devel
BuildRequires:  lua-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libnetfilter_conntrack)
Requires(pre):  group(nogroup)
%if 0%{?suse_version} >= 1210
BuildRequires:  pkgconfig(systemd)
%endif
Requires(pre):  group(nogroup)

%description
Dnsmasq provides network infrastructure for small networks: DNS,
DHCP, router advertisement and network boot.

The DNS subsystem supprots forwarding of all query types, and caching
of common record types, DNSSEC included. The DHCP subsystem supports
DHCPv4, DHCPv6, BOOTP and PXE. RA can be used stand-alone or in
conjunction with DHCPv6.

%package utils
Summary:        Utilities for manipulating DHCP server leases
Group:          Productivity/Networking/DNS/Servers

%description utils
Utilities that use the standard DHCP protocol to query/remove a DHCP
server's leases.

%prep
%setup -q
%patch0
%patch1 -p1

# Remove the executable bit from python example files to
# avoid unwanted automatic dependencies
find contrib -name *.py -exec chmod a-x '{}' +

# Some docs have the DOS line ends
dos2unix contrib/systemd/dbus_activation

# SED-FIX-UPSTREAM -- Fix paths
sed -i -e 's|\(PREFIX *= *\)/usr/local|\1/usr|;
	   s|$(LDFLAGS)|$(CFLAGS) $(LDFLAGS)|' \
	Makefile

# use lua5.3 instead of lua5.3
sed -i -e 's|lua5.2|lua5.3|' Makefile

# SED-FIX-UPSTREAM -- Fix man page
sed -i -e 's|The defaults to "dip",|The default is "nogroup",|' \
	man/dnsmasq.8

# SED-FIX-UPSTREAM -- Fix cachesize, group and user
sed -i -e 's|CACHESIZ 150|CACHESIZ 2000|;
	   s|CHUSER "nobody"|CHUSER "dnsmasq"|;
	   s|CHGRP "dip"|CHGRP "nogroup"|' \
	src/config.h

# Fix trust-anchor.conf location
sed -i -e '/trust-anchors.conf/c\#conf-file=/etc/dnsmasq.d/trust-anchors.conf' \
	dnsmasq.conf.example

%build
mv po/no.po po/nb.po
export CFLAGS="%optflags -std=gnu99 -fPIC -DPIC -fpie"
export LDFLAGS="-Wl,-z,relro,-z,now -pie"
# the dnsmasq make system hashes the configuration flags, so we have to supply the
# same flags for make and make install, else everything gets recompiled
%define _copts   "-DHAVE_DBUS -DHAVE_CONNTRACK -DHAVE_LIBIDN2 -DHAVE_DNSSEC -DHAVE_LUASCRIPT"
make %{?_smp_mflags} AWK=gawk all-i18n CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS" COPTS=%{_copts}
make -C contrib/lease-tools %{?_smp_mflags}

%pre
if ! /usr/bin/getent group tftp >/dev/null; then
    %{_sbindir}/groupadd -r tftp
fi
if ! /usr/bin/getent passwd tftp >/dev/null; then
    %{_sbindir}/useradd -c "TFTP account" -d /srv/tftpboot -G tftp -g tftp \
    -r -s /bin/false tftp
fi
if ! /usr/bin/getent passwd dnsmasq >/dev/null; then
    /usr/sbin/useradd -r -d /var/lib/empty -s /bin/false -c "dnsmasq" -g nogroup -G tftp dnsmasq
fi

%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
# reload dbus after install or upgrade to apply new policies
if [ -z "${TRANSACTIONAL_UPDATE}" -a -x /usr/bin/systemctl ]; then
        /usr/bin/systemctl reload dbus.service 2>/dev/null || :
fi

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service
# reload dbus after uninstall, our policies are gone again
if [ $1 -eq 0 -a -z "${TRANSACTIONAL_UPDATE}" \
     -a -x /usr/bin/systemctl ]; then
        /usr/bin/systemctl reload dbus.service 2>/dev/null || :
fi

%install
make install-i18n DESTDIR=%{buildroot} PREFIX=/usr AWK=gawk COPTS=%{_copts}
install -d -m 755 %{buildroot}/%{_sysconfdir}/slp.reg.d
install -m 644 dnsmasq.conf.example %{buildroot}/%{_sysconfdir}/dnsmasq.conf
install -m 644 %SOURCE3 %{buildroot}/%{_sysconfdir}/slp.reg.d/
install -d 755 %{buildroot}/etc/dbus-1/system.d/
install -m 644 dbus/dnsmasq.conf %{buildroot}/etc/dbus-1/system.d/dnsmasq.conf
install -D -m 0644 %SOURCE4 %{buildroot}%{_unitdir}/dnsmasq.service
install -d -m 0755 %{buildroot}/srv/tftpboot
ln -sf %{_sbindir}/service %{buildroot}/usr/sbin/rcdnsmasq
install -d -m 755 %{buildroot}/%{_sysconfdir}/dnsmasq.d
install -m 644 trust-anchors.conf %{buildroot}/%{_sysconfdir}/dnsmasq.d/trust-anchors.conf

# utils subpackage
mkdir -p %{buildroot}/%{_bindir} %{buildroot}/%{_mandir}/man1
install -m 755 contrib/lease-tools/dhcp_release %{buildroot}/%{_bindir}/dhcp_release
install -m 644 contrib/lease-tools/dhcp_release.1 %{buildroot}/%{_mandir}/man1/dhcp_release.1
install -m 755 contrib/lease-tools/dhcp_lease_time %{buildroot}/%{_bindir}/dhcp_lease_time
install -m 644 contrib/lease-tools/dhcp_lease_time.1 %{buildroot}/%{_mandir}/man1/dhcp_lease_time.1
rm contrib/lease-tools/{dhcp_release,dhcp_lease_time}
rm -rf contrib/Suse
rm -rf contrib/Solaris10
rm -rf contrib/dnsmasq_MacOSX-pre10.4
rm -rf contrib/slackware-dnsmasq
rm -rf contrib/MacOSX-launchd

%find_lang %{name} --with-man

%files -f %{name}.lang
%defattr(-,root,root,-)
%license COPYING COPYING-v3
%doc CHANGELOG FAQ doc.html setup.html dnsmasq.conf.example contrib dbus
%config(noreplace) %{_sysconfdir}/dnsmasq.conf
%{_sbindir}/dnsmasq
%{_sbindir}/rcdnsmasq
%dir %{_sysconfdir}/slp.reg.d/
%config %attr(0644,root,root) /%{_sysconfdir}/slp.reg.d/dnsmasq.reg
%{_mandir}/man8/dnsmasq.8.gz
%config(noreplace) /etc/dbus-1/system.d/dnsmasq.conf
%{_unitdir}/dnsmasq.service
%dir %{_sysconfdir}/dnsmasq.d
%config(noreplace) %{_sysconfdir}/dnsmasq.d/trust-anchors.conf

%dir %attr(0755,tftp,tftp) /srv/tftpboot

%files utils
%defattr(-,root,root,-)
%{_bindir}/dhcp_*
%{_mandir}/man1/dhcp_*

%changelog
