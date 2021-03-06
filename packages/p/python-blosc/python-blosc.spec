#
# spec file for package python-blosc
#
# Copyright (c) 2020 SUSE LLC
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
%define skip_python2 1
Name:           python-blosc
Version:        1.9.1
Release:        0
Summary:        Blosc data compressor for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Blosc/python-blosc
Source:         https://files.pythonhosted.org/packages/source/b/blosc/blosc-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module scikit-build}
BuildRequires:  %{python_module setuptools}
BuildRequires:  blosc-devel >= 1.9.0
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  ninja
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module psutil}
# /SECTION
Requires:       blosc-devel
Recommends:     python-numpy
%python_subpackages

%description
Blosc is a high performance compressor optimized for binary data in
Python.

%prep
%setup -q -n blosc-%{version}

%build
export CFLAGS="%{optflags}"
export BLOSC_DIR=%{_prefix}
%python_exec setup.py build_clib
%python_exec setup.py build_ext --inplace
%python_build

%install
export BLOSC_DIR=%{_prefix}
# This is being installed in purelib instead of platlib
# See: https://github.com/Blosc/python-blosc/issues/222
%python_exec setup.py install -O1 --skip-build --force --root %{buildroot} --install-purelib=%{$python_sitearch}
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export PYTHONDONTWRITEBYTECODE=1
%python_exec -m unittest discover -s blosc/ -v 

%files %{python_files}
%doc ANNOUNCE.rst README.rst RELEASE_NOTES.rst
%license LICENSES/*.txt
%{python_sitearch}/blosc-%{version}-py*.egg-info
%{python_sitearch}/blosc/

%changelog
