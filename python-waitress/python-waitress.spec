#
# spec file for package python-waitress
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
Name:           python-waitress
Version:        1.3.0
Release:        0
Summary:        Waitress WSGI server
License:        ZPL-2.1
Group:          Development/Languages/Python
URL:            https://github.com/Pylons/waitress
Source:         https://files.pythonhosted.org/packages/source/w/waitress/waitress-%{version}.tar.gz
# intersphinx inventories, as fetched with fetch-intersphinx-inventories.sh
# https://docs.python.org/3/objects.inv -> python3.inv
Source1:        python3.inv
Source2:        fetch-intersphinx-inventories.sh
Patch:          local-intersphinx-inventories.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION documentation requirements
BuildRequires:  python3-Sphinx
BuildRequires:  python3-docutils
BuildRequires:  python3-pylons-sphinx-themes
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
Waitress is a pure-Python WSGI server. It has no dependencies except
ones which live in the Python standard library. It supports HTTP/1.0
and HTTP/1.1.

For more information, see the "docs" directory of the Waitress package or
http://docs.pylonsproject.org/projects/waitress/en/latest/ .

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
Requires:       %{name} = %{version}

%description doc
This package contains documentation files for %{name}.

%prep
%setup -q -n waitress-%{version}
%patch -p1
cp %{S:1} docs/

%build
%python_build
export SPHINXOPTS=-vvv
python3 setup.py build_sphinx && rm build/sphinx/html/.buildinfo

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Tests require a network connection
rm waitress/tests/test_adjustments.py
%python_exec setup.py test

%files %{python_files}
%license LICENSE.txt
%doc COPYRIGHT.txt README.rst
%python3_only %{_bindir}/waitress-serve
%{python_sitelib}/*

%files %{python_files doc}
%license LICENSE.txt
%doc build/sphinx/html

%changelog
