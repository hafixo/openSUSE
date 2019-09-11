#
# spec file for package btar
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           btar
Version:        1.1.1
Release:        0
Summary:        Featureful tar-Compatible Archiver and Compressor
License:        GPL-3.0+
Group:          Productivity/Archiving/Backup
Url:            http://freecode.com/projects/btar
Source:         http://vicerveza.homeunix.net/~viric/soft/btar/btar-%{version}.tar.gz
# pbleser: fix various things about the Makefile, such as proper place of LFLAGS,
# overridable OPTFLAGS, DESTDIR support
Patch1:         btar-makefile.patch
Patch2:         btar-librsync.patch
BuildRequires:  librsync-devel

%description
btar is a tar-compatible archiver which allows arbitrary compression and
ciphering, redundancy, differential backup, indexed extraction, multicore
compression, input and output serialisation, and tolerance to partial
archive errors.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
make %{?_smp_mflags} OPTFLAGS="%{optflags} -D_GNU_SOURCE" \

%install
%make_install PREFIX="%{_prefix}"

%files
%defattr(-,root,root)
%doc AUTHORS COPYING doc/*
%{_bindir}/btar
%{_mandir}/man1/btar.1*

%changelog
