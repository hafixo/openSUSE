#
# spec file for package python-sqlitedict
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
Name:           python-sqlitedict
Version:        1.6.0
Release:        0
Summary:        Persistent dict in Python backed by sqlite3
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/piskvorky/sqlitedict
Source:         https://files.pythonhosted.org/packages/source/s/sqlitedict/sqlitedict-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module nose}
# /SECTION
BuildArch:      noarch

%python_subpackages

%description
A wrapper around Python's sqlite3 database with a Pythonic
dict-like interface and support for multi-thread access.

%prep
%setup -q -n sqlitedict-%{version}
sed -i -e '/^#!\//, 1d' sqlitedict.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%{python_expand 
rm -rf tests/db
mkdir -p tests/db
nosetests-%{$python_bin_suffix}
}

%files %{python_files}
%defattr(-,root,root,-)
%license LICENSE.apache
%doc README.rst
%{python_sitelib}/*

%changelog
