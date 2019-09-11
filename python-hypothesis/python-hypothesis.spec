#
# spec file for package python-hypothesis
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
%define oldpython python
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%bcond_without python2
Name:           python-hypothesis%{psuffix}
Version:        4.32.2
Release:        0
Summary:        A library for property based testing
License:        MPL-2.0
Group:          Development/Languages/Python
URL:            https://github.com/HypothesisWorks/hypothesis-python
Source:         https://github.com/HypothesisWorks/hypothesis/archive/hypothesis-python-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 36}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 16.0.0
Recommends:     python-Django >= 1.11
Recommends:     python-lark-parser >= 0.6.5
Recommends:     python-numpy >= 1.9.0
Recommends:     python-pandas
Recommends:     python-pytest >= 3.0.0
Recommends:     python-python-dateutil
Recommends:     python-pytz >= 2014.1
BuildArch:      noarch
%ifpython3
Recommends:     python-dpcontracts
%endif
%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module attrs >= 16.0.0}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module hypothesis >= %{version}}
BuildRequires:  %{python_module lark-parser >= 0.6.5}
BuildRequires:  %{python_module lark-parser}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module numpy >= 1.9.0}
BuildRequires:  %{python_module pytest >= 3.0.0}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz >= 2014.1}
BuildRequires:  python3-dpcontracts
%endif
# /SECTION
%if %{with python2}
BuildRequires:  python-enum34
%endif
%ifpython2
Requires:       %{oldpython}-enum34
%endif
%python_subpackages

%description
Hypothesis is a library for testing your Python code against a much larger range
of examples than you would ever want to write by hand. It's based on the Haskell
library, Quickcheck, and is designed to integrate seamlessly into your existing
Python unit testing work flow.

Hypothesis works with most widely used versions of Python. It supports implementations
compatible with 2.6, 2.7 and 3.3+, and is known to work on CPython and PyPy (but not
PyPy3 until they support a 3.3 compatible version of the language). It does *not* currently
work on Jython or on Python 3.0 through 3.2.

%prep
%setup -q -n hypothesis-hypothesis-python-%{version}/hypothesis-python
# remove version specific tests for ease
rm -r tests/py2
rm -r tests/py3
rm -r tests/dpcontracts # py3 only
# the django fails to initialize
rm -r tests/django
# do not pull in pandas as a dep in ring1; it slows down things too much
rm -r tests/pandas

%build
%python_build

%install
%if !%{with test}
%python_install
%{python_expand \
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/hypothesis/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/hypothesis/
%fdupes %{buildroot}%{$python_sitelib}
}
%endif

%check
%if %{with test}
# test_prints_statistics_given_option_under_xdist - wrong xdist opts
%python_expand PYTHONPATH=%{$python_sitelib} py.test-%{$python_bin_suffix} -v tests -k 'not test_prints_statistics_given_option_under_xdist'
%endif

%if !%{with test}
%files %{python_files}
%license ../LICENSE.txt
%doc ../CITATION README.rst docs/changes.rst
%{python_sitelib}/hypothesis*
%endif

%changelog
