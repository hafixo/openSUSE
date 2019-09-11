#
# spec file for package python-python-afl
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
%bcond_without test
Name:           python-python-afl
Version:        0.7.2
Release:        0
Summary:        American fuzzy lop fork server and instrumentation for pure-Python code
License:        MIT
Group:          Development/Languages/Python
Url:            http://jwilk.net/software/python-afl
Source:         https://files.pythonhosted.org/packages/source/p/python-afl/python-afl-%{version}.tar.gz
# PATCH-FIX-OPENSUSE 
Patch0:         https://github.com/jwilk/python-afl/compare/%{version}...sebix:%{version}-fix-setup-tests.patch#/Use-setuptools-and-use-test-command-for-setup.patch
BuildRequires:  %{python_module Cython >= 0.19}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module nose}
BuildRequires:  afl >= 2
BuildRequires:  procps
%endif
BuildRequires:  fdupes
Requires:       afl >= 2
# name with _ automatically redirected by pypi to name with -
Provides:       python-python_afl

%python_subpackages

%description
python-afl is an experimental module that enables American fuzzy lop fork server and instrumentation for pure-Python code.

The scripts to run the fuzzer are only in the package for python3.

%prep
%setup -q -n python-afl-%{version}
%patch0 -p1

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%if %{with test}
%check
rm tests/test_cmin.py tests/test_fuzz.py tests/test_showmap.py tests/test_tmin.py
%python_exec setup.py test
%endif

%files %{python_files}
%doc doc/changelog doc/README doc/trophy-case
%license doc/LICENSE
%python3_only %{_bindir}/py-afl-cmin
%python3_only %{_bindir}/py-afl-fuzz
%python3_only %{_bindir}/py-afl-showmap
%python3_only %{_bindir}/py-afl-tmin
%{python_sitearch}/*

%changelog
