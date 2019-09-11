#
# spec file for package redis
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


%define _data_dir       %{_localstatedir}/lib/%{name}
%define _log_dir        %{_localstatedir}/log/%{name}
%define _conf_dir       %{_sysconfdir}/%{name}

Name:           redis
Version:        5.0.5
Release:        0
Summary:        Persistent key-value database
License:        BSD-3-Clause
Group:          Productivity/Databases/Servers
URL:            https://redis.io
Source0:        http://download.redis.io/releases/redis-%{version}.tar.gz
Source1:        %{name}.logrotate
Source2:        %{name}.target
Source3:        %{name}@.service
Source4:        %{name}.tmpfiles.d
Source5:        README.SUSE
Source6:        %{name}.sysctl
Source7:        %{name}-sentinel@.service
Source8:        %{name}-sentinel.target
# PATCH-FIX-OPENSUSE -- openSUSE-style init script
Patch0:         %{name}-initscript.patch
# PATCH-MISSING-TAG -- See https://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch1:         %{name}-conf.patch
Patch2:         %{name}-enable-bactrace-on-x86-ia64-and_arm32_only.patch
Patch3:         %{name}-disable_integration_logging.patch
Patch4:         reproducible.patch
BuildRequires:  pkgconfig
BuildRequires:  procps
BuildRequires:  tcl
BuildRequires:  pkgconfig(systemd)
Requires:       logrotate
Requires:       sudo
Requires(pre):  shadow

%description
%{name} is an advanced key-value store. It is similar to memcached but the dataset
is not volatile, and values can be strings, exactly like in memcached,
but also lists, sets, and ordered sets. All this data types can be manipulated
with atomic operations to push/pop elements, add/remove elements, perform server
side union, intersection, difference between sets, and so forth. Redis supports
different kind of sorting abilities.

%prep
%setup -q
%patch0
%patch1
%patch2
%ifnarch %{ix86} x86_64 ia64 %{arm}
# We have no backtrace, so disable logging test
%patch3
%endif
%patch4 -p1

%build
export HOST=OBS # for reproducible builds
make %{?_smp_mflags} CFLAGS="%{optflags}" V=1

%install
install -m 0750 -d \
  %{buildroot}%{_sbindir} \
  %{buildroot}%{_log_dir} \
  %{buildroot}%{_data_dir} \
  %{buildroot}%{_conf_dir} \
  %{buildroot}%{_log_dir}/default \
  %{buildroot}%{_data_dir}/default

install -Dpm 0755 src/%{name}-benchmark  %{buildroot}%{_bindir}/%{name}-benchmark
install -Dpm 0755 src/%{name}-cli        %{buildroot}%{_bindir}/%{name}-cli
install -Dpm 0755 src/%{name}-trib.rb    %{buildroot}%{_bindir}/%{name}-trib.rb

install -Dpm 0755 src/%{name}-server     %{buildroot}%{_sbindir}/%{name}-server

ln -sfv ../sbin/redis-server             %{buildroot}%{_bindir}/%{name}-check-aof
ln -sfv ../sbin/redis-server             %{buildroot}%{_bindir}/%{name}-check-rdb
ln -sfv ../sbin/redis-server             %{buildroot}%{_sbindir}/%{name}-check-aof
ln -sfv ../sbin/redis-server             %{buildroot}%{_sbindir}/%{name}-check-rdb
ln -sfv ../sbin/redis-server             %{buildroot}%{_sbindir}/%{name}-sentinel

perl -p -i -e 's|daemonize yes|daemonize no|g' %{name}.conf
install -Dm 0640 redis.conf              %{buildroot}%{_conf_dir}/default.conf.example
install -Dm 0660 sentinel.conf           %{buildroot}%{_conf_dir}/sentinel.conf.example

# some sysctl stuff
install -Dm 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/sysctl.d/00-%{name}.conf
install -Dm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -Dm 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.target
install -Dm 0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}@.service
install -Dm 0644 %{SOURCE4} %{buildroot}%{_libexecdir}/tmpfiles.d/%{name}.conf
install -Dm 0644 %{SOURCE7} %{buildroot}%{_unitdir}/%{name}-sentinel@.service
install -Dm 0644 %{SOURCE8} %{buildroot}%{_unitdir}/%{name}-sentinel.target

ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
cp %{SOURCE5} README.SUSE

%check
%ifnarch ppc ppc64
cat <<EOF
---------------------------------------------------
The test suite often fails to start a server, with
'child process exited abnormally' -- sometimes it works.
---------------------------------------------------
EOF
make %{?_smp_mflags} test || true
%endif

%pre
getent group %{name} >/dev/null || %{_sbindir}/groupadd -r %{name} || :
getent passwd %{name} >/dev/null || \
	%{_sbindir}/useradd -g %{name} -s /bin/false -r \
	-c "User for %{name} key-value store" -d %{_data_dir} %{name} || :
%service_add_pre redis.target redis@.service redis-sentinel.target redis-sentinel@.service

%post
systemd-tmpfiles --create %{_libexecdir}/tmpfiles.d/%{name}.conf || true
%service_add_post redis.target redis@.service redis-sentinel.target redis-sentinel@.service
echo "See %{_docdir}/%{name}/README.SUSE to continue"

%preun
%service_del_preun redis.target redis@.service redis-sentinel.target redis-sentinel@.service

%postun
%service_del_postun redis.target redis@.service redis-sentinel.target redis-sentinel@.service

%files
%license COPYING
%doc 00-RELEASENOTES BUGS CONTRIBUTING README.md
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/sysctl.d/00-%{name}.conf
%{_bindir}/%{name}-*
%{_sbindir}/%{name}-*
%{_sbindir}/rc%{name}
%{_libexecdir}/tmpfiles.d/%{name}.conf
%{_unitdir}/%{name}@.service
%{_unitdir}/%{name}.target
%{_unitdir}/%{name}-sentinel@.service
%{_unitdir}/%{name}-sentinel.target
%doc README.SUSE
%config(noreplace) %attr(-,root,%{name}) %{_conf_dir}/
%dir %attr(0750,%{name},%{name}) %{_data_dir}
%dir %attr(0750,%{name},%{name}) %{_data_dir}/default
%dir %attr(0750,%{name},%{name}) %{_log_dir}

%changelog
