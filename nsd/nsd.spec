#
# spec file for package nsd
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define home       %{_localstatedir}/lib/%{name}
%define configdir  %{_sysconfdir}/%{name}
%define configfile %{configdir}/nsdc.conf
%define zonesfile  %{configdir}/nsd.zones
%define zonesdir   %{configdir}/zones
%define pidfile    %{_rundir}/nsd/nsd.pid
Name:           nsd
Version:        4.2.1
Release:        0
#
Summary:        An authoritative-only domain name server
#
License:        BSD-3-Clause
Group:          Productivity/Networking/DNS/Servers
Url:            http://open.nlnetlabs.nl/nsd/
Source:         http://open.nlnetlabs.nl/downloads/nsd/nsd-%{version}.tar.gz
Source1:        nsd.service
Source2:        tmpfiles-nsd.conf
Source4:        nsd.keyring
Source5:        https://www.nlnetlabs.nl/downloads/nsd/nsd-%{version}.tar.gz.asc
Source10:       nsd-rpmlintrc
#
BuildRequires:  libevent-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pwdutils
BuildRequires:  tcpd-devel
Requires:       pwdutils
Requires(pre):  coreutils
Requires(post): coreutils
Requires(post): findutils
Requires(pre):  shadow
Requires(post): shadow
%{?systemd_requires}

%description
NSD is a complete implementation of an authoritative domain name server, developed
by NLnet Labs, with the purpose of creating more diversity in the DNS landscape.

%prep
%setup -q

%build
%configure                             \
    --with-configdir=%{configdir}      \
    --with-zonesdir=%{zonesdir}        \
    --with-dbfile=%{home}/nsd.db       \
    --with-xfrdfile=%{home}/xfrd.state \
    --with-pidfile=%{_rundir}/nsd/nsd.pid \
    --with-logfile=/%{_localstatedir}/log/nsd/nsd.log \
    --enable-root-server               \
    --enable-bind8-stats               \
    --enable-zone-stats                \
    --enable-mmap                      \
    --with-user=_nsd                   \
    --enable-ratelimit
make %{?_smp_mflags}
iconv -f iso8859-1 -t utf-8 doc/RELNOTES > doc/RELNOTES.utf8
iconv -f iso8859-1 -t utf-8 doc/CREDITS > doc/CREDITS.utf8
mv -f doc/RELNOTES.utf8 doc/RELNOTES
mv -f doc/CREDITS.utf8 doc/CREDITS

%install
%make_install
chmod -Rv o= %{buildroot}%{configdir}/
#
install -d -m 0700 %{buildroot}%{home}            \
                   %{buildroot}%{_rundir}/%{name}
#
install -d -m 0755 %{buildroot}/%{_localstatedir}/log/nsd/
touch %{buildroot}%{home}/{nsd.db,ixfr.db,xfrd.state} %{buildroot}/%{_localstatedir}/log/nsd/nsd.log
mkdir -m 0750 %{buildroot}%{zonesdir}

install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/nsd.service
install -D -m 0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/nsd.conf
ln -s -f %{_sbindir}/service    %{buildroot}%{_sbindir}/rc%{name}

%pre
getent group _nsd >/dev/null || groupadd -r _nsd
getent passwd _nsd >/dev/null || \
    useradd -r -g _nsd -s /bin/false -c "user for %{name}" \
    -d %{home} _nsd
%service_add_pre %{name}.service

%post
systemd-tmpfiles --create  %{_tmpfilesdir}/%{name}.conf || :
%service_add_post %{name}.service

# On upgrade, we migrate from old "nsd" user to new "_nsd" user for
# config, home and default logging directories
#
# This is only used for special case of upgrading server:dns/nsd users
# as 'nsd' user was never part of openSUSE:Factory
if [ "x"$1 = "x2" ] && [ "x"`stat -c '%%G' %{home}/nsd.db` = 'xnsd' ]; then
    echo "Changing legacy group from user/group nsd:nsd to _nsd:_nsd"
    %{_bindir}/find %{_localstatedir}/log/nsd %{home} %{_rundir}/nsd -exec %{_bindir}/chown -v _nsd:_nsd {} \+
    %{_bindir}/find %{configdir} -exec %{_bindir}/chgrp -v _nsd {} \+

    # force restart because we need to remove users here
    %{_bindir}/systemctl try-restart %{name}.service ||:
fi

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc doc/*
%{configdir}/nsd.conf.sample
%doc contrib/
%{_unitdir}/nsd.service
%dir %{_tmpfilesdir}
%{_tmpfilesdir}/nsd.conf
%{_sbindir}/rcnsd
%{_sbindir}/nsd
%{_sbindir}/nsd-control
%{_sbindir}/nsd-control-setup
%{_sbindir}/nsd-checkconf
%{_sbindir}/nsd-checkzone
%{_mandir}/man5/nsd.conf.5*
%{_mandir}/man8/nsd-checkconf.8*
%{_mandir}/man8/nsd-checkzone.8*
%{_mandir}/man8/nsd.8*
%{_mandir}/man8/nsd-control.8*
#
%config(noreplace) %attr(-,root,_nsd) %{configdir}
%ghost %config %attr(640,_nsd,_nsd) %{configdir}/nsd.conf
%dir %attr(750,root,_nsd) %{zonesdir}
#
%dir %attr(750,_nsd,_nsd) %{home}
%ghost %config %attr(640,_nsd,_nsd) %{home}/nsd.db
%ghost %config %attr(640,_nsd,_nsd) %{home}/ixfr.db
%ghost %config %attr(640,_nsd,_nsd) %{home}/xfrd.state
#
%dir %attr(750,_nsd,_nsd) /%{_localstatedir}/log/nsd
%ghost %attr(640,_nsd,_nsd) /%{_localstatedir}/log/nsd/nsd.log
%ghost %attr(750,_nsd,_nsd) %{_rundir}/%{name}

%changelog
