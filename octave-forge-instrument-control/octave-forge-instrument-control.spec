#
# spec file for package octave-forge-instrument-control
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


%define octpkg  instrument-control
Name:           octave-forge-%{octpkg}
Version:        0.3.1
Release:        0
Summary:        Instrument Control for Octave
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
Url:            http://octave.sourceforge.net
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM instrument-control-no-return-in-nonvoid-function.patch badshah400@gmail.com -- Fix non-void functions not returning data typically at the end of an if-elseif-else block.
Patch0:         instrument-control-no-return-in-nonvoid-function.patch
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  octave-devel
Requires:       octave-cli >= 3.2.0

%description
Low level I/O functions for serial, i2c, parallel, tcp, gpib, vxi11 and usbtmc interfaces.
This is part of the Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
%patch0 -p1
%octave_pkg_src

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_test

%post
%octave --eval "pkg rebuild"

%postun
%octave --eval "pkg rebuild"

%files
%defattr(-,root,root)
%{octpackages_dir}/%{octpkg}-%{version}
%{octlib_dir}/%{octpkg}-%{version}

%changelog
