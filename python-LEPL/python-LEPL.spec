#
# spec file for package python-LEPL
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
Name:           python-LEPL
Version:        5.1.3
Release:        0
Summary:        Recursive descent, full backtracking parser library
License:        MPL-1.1 OR LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            http://www.acooke.org/lepl/
Source:         https://files.pythonhosted.org/packages/source/L/LEPL/LEPL-%{version}.tar.gz
Source1:        LICENSE.MPL-1.1
Source2:        LICENSE.LGPL-3.0
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
LEPL is a recursive descent parser, written in Python.

Multiple parses can be found for ambiguous grammars and it can also
handle left-recursive grammars.

%prep
%setup -q -n LEPL-%{version}
cp %{SOURCE1} %{SOURCE2} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Test suite has never been updated for newer Python versions and
# uses generators in a way that is incompatible with PEP 479.
python setup.py develop --user
python -c 'from lepl._test import all; all()'

%files %{python_files}
%license LICENSE.MPL-1.1 LICENSE.LGPL-3.0
%{python_sitelib}/*

%changelog
