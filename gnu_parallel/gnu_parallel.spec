#
# spec file for package gnu_parallel
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


Name:           gnu_parallel
Version:        20190422
Release:        0
Summary:        Shell tool for executing jobs in parallel
License:        GPL-3.0-or-later
Group:          Productivity/File utilities
Url:            http://www.gnu.org/software/parallel/
#DL-URL: 	http://ftp.gnu.org/gnu/parallel/
Source:         http://ftp.gnu.org/gnu/parallel/parallel-%version.tar.bz2
Source2:        http://ftp.gnu.org/gnu/parallel/parallel-%version.tar.bz2.sig
Source3:        %name.keyring
Patch0:         parallel-remove-nag-screen.patch
BuildArch:      noarch

%description
GNU Parallel is a shell tool for executing jobs in parallel using one
or more computers. A job can be a single command or a small script
that has to be run for each of the lines in the input. The typical
input is a list of files, a list of hosts, a list of users, a list of
URLs, or a list of tables. A job can also be a command that reads from
a pipe. GNU Parallel can then split the input and pipe it into
commands in parallel.

%package doc
Summary:        Documentation for GNU parallel
License:        GFDL-1.3-only AND CC-BY-SA-3.0
Group:          Documentation/HTML

%description doc
GNU Parallel is a shell tool for executing jobs in parallel using one
or more computers.
This subpackage contains the documentation for Parallel.

%prep
%setup -q -n parallel-%version
%patch0 -p1

%build
%configure --docdir="%_docdir/%name"
make %{?_smp_mflags}

%install
%make_install
cp -a CITATION NEWS README cc-by-sa.txt fdl.txt "%buildroot/%_docdir/%name/"

%files
%license COPYING
%_bindir/env_parallel*
%_bindir/niceload
%_bindir/parallel
%_bindir/parcat
%_bindir/parset
%_bindir/sem
%_bindir/sql
%_mandir/man1/*.1*
%_mandir/man7/*.7*

%files doc
%_docdir/%name/

%changelog
