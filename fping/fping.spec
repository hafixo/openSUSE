#
# spec file for package fping
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


Name:           fping
Version:        4.1
Release:        0
Summary:        A program to ping multiple hosts
License:        MIT
Group:          Productivity/Networking/Diagnostic
Url:            http://www.fping.org
Source:         http://fping.org/dist/%{name}-%{version}.tar.gz
Requires(pre):  permissions
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
FPing is a ping-like program that uses the Internet Control Message
Protocol (ICMP) echo request to determine if a target host is
responding. FPing differs from ping in that you can specify any number
of targets on the command line or specify a file containing a list of
targets to ping. Instead of sending pings to one target until it times
out or replies, FPing sends a ping packet and moves on to the next
target in a round-robin fashion.

In the default mode, if a target replies, it is noted and removed from
the list of targets to check. If a target does not respond within a
certain time limit or retry limit, it is designated as unreachable.
FPing also supports sending a specified number of pings to a target or
looping indefinitely (as in ping).

Unlike ping, FPing is meant to be used in scripts. Its output is
designed to be easy to parse.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%post
%set_permissions %{_sbindir}/fping

%verifyscript
%verify_permissions -e %{_sbindir}/fping

%files
%defattr(-,root,root)
%doc CHANGELOG.md INSTALL
%{_mandir}/man8/fping.8%{ext_man}
%verify(not mode caps) %attr(0755,root,root) %{_sbindir}/fping

%changelog
