#
# spec file for package cttop
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           cttop
Version:        0.3.g26
Release:        0
Summary:        top-like program showing Netfilter connection tracking entries
License:        GPL-2.0+
Group:          Productivity/Networking/Security
Url:            http://strlen.de/cttop.html

#Snapshot:	v0.3-26-g63e53bb
#Git-Web:	http://git.breakpoint.cc/cgit/fw/cttop.git/
#Git-Clone:	git://git.breakpoint.cc/fw/cttop
#Source:         http://strlen.de/cttop/dl/%name-%version.tar.bz2
#Source2:        http://strlen.de/cttop/dl/%name-%version.tar.bz2.sig
Source:         %name-%version.tar.xz
Source4:        %name.keyring
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  xz
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(libnetfilter_conntrack)
%if 0%{?suse_version} > 1315
BuildRequires:  pkgconfig(ncurses)
%else
BuildRequires:  ncurses-devel >= 5.9
%endif

%description
cttop is a top-like program that shows netfilter connection tracking
entries. entries can be sorted by various criteria and grouped, e.g.
by source address.

%prep
%setup -qn %name

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%_sbindir/cttop
%_mandir/man8/cttop.8*
%doc COPYING

%changelog
