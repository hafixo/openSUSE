#
# spec file for package less
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


Name:           less
Version:        530
Release:        0
Summary:        Text File Browser and Pager Similar to more
License:        GPL-3.0-or-later OR BSD-2-Clause
Group:          Productivity/Text/Utilities
Url:            http://www.greenwoodsoftware.com/less/
Source:         http://www.greenwoodsoftware.com/less/less-%{version}.tar.gz
Source1:        README.SUSE
Source2:        lessopen.sh
Source3:        lessclose.sh
Source4:        lesskey.src
Source5:        http://www.greenwoodsoftware.com/less/less-%{version}.sig
Source6:        http://www.greenwoodsoftware.com/less/pubkey.asc#/%{name}.keyring
Patch0:         less-429-shell.patch
Patch1:         less-429-save_line_position.patch
Patch2:         less-429-more.patch
BuildRequires:  automake
BuildRequires:  ncurses-devel
Requires:       file
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
less is a text file browser and pager similar to more. It allows
backward as well as forward movement within a file. Also, less does not
have to read the entire input file before starting. It is possible to
start an editor at any time from within less.

%prep
%setup -q
%patch0
%patch1
%patch2
#
# the ./configure script is not writable for the normal user
# rather fix permissions for all files
chmod u+w *
#
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .

%build
autoreconf -fiv
export CFLAGS="%{optflags} -fPIE"
export LDFLAGS="-pie"
%configure --with-pic
#
# regenerate help.c because less.hlp was patched
./mkhelp.pl <less.hlp >help.c
#
# build less
make %{?_smp_mflags}

%install
%make_install
#
# lesskey
install -m 755 -d %{buildroot}/%{_sysconfdir}
install -m 644 lesskey.src %{buildroot}/%{_sysconfdir}/lesskey
%{buildroot}%{_bindir}/lesskey -o %{buildroot}%{_sysconfdir}/lesskey.bin %{buildroot}%{_sysconfdir}/lesskey
#
# preprocessor
install -m 755 lessopen.sh lessclose.sh %{buildroot}/%{_bindir}
chmod -x LICENSE COPYING NEWS README.SUSE

%files
%defattr(-, root, root)
%license LICENSE COPYING
%doc NEWS README.SUSE
%{_mandir}/*/*
%config %{_sysconfdir}/*
%{_bindir}/*

%changelog
