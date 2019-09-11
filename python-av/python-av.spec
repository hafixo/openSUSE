#
# spec file for package python-av
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-av
Version:        6.2.0
Release:        0
Summary:        Python bindings for FFmpeg's libraries
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/mikeboers/PyAV
Source:         https://files.pythonhosted.org/packages/source/a/av/av-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavutil)
Requires:       python-setuptools
BuildRequires:  %{python_module numpy}
%python_subpackages

%description
Pythonic bindings for FFmpeg's libraries.

%prep
%setup -q -n av-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Sadly needs full ffmpeg with all the codec support so we have to skip
#%%python_exec setup.py test

%files %{python_files}
%license LICENSE.txt
%doc README.md
%python3_only %{_bindir}/pyav
%{python_sitearch}/av
%{python_sitearch}/av-%{version}-py%{py_ver}.egg-info

%changelog
