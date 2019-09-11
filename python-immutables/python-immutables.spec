#
# spec file for package python-immutables
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-immutables
Version:        0.9
Release:        0
License:        Apache-2.0
Summary:        Immutable collections for Python
Url:            https://github.com/MagicStack/immutables
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/i/immutables/immutables-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes

%python_subpackages

%description
Immutable collections for Python.

%prep
%setup -q -n immutables-%{version}
sed -i 's/\.system//' setup.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%{python_expand rm %{buildroot}%{$python_sitearch}/immutables/*.[ch]
%fdupes %{buildroot}%{$python_sitearch}
}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/*

%changelog
