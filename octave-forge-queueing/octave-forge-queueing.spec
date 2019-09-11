#
# spec file for package octave-forge-queueing
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define octpkg  queueing
Name:           octave-forge-%{octpkg}
Version:        1.2.5
Release:        0
Summary:        Queueing Networks and Markov chains analysis for Octave
License:        GPL-3.0+
Group:          Productivity/Scientific/Math
Url:            http://octave.sourceforge.net
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  octave-devel
Requires:       octave-cli >= 3.8.1

%description
Functions for queueing networks and Markov chains analysis.
This package can be used to compute steady-state performance measures
for open, closed and mixed networks with single or multiple job classes.
Mean Value Analysis (MVA), convolution, and various bounding techniques are
implemented. Furthermore, several transient and steady-state performance
measures for Markov chains can be computed, such as state occupancy
probabilities, mean time to absorption, time-averaged sojourn times
and so forth. Discrete- and continuous-time Markov chains are supported.
This is part of the Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
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

%changelog
