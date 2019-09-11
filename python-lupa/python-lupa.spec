#
# spec file for package python-lupa
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
Name:           python-lupa
Version:        1.8
Release:        0
Summary:        Python wrapper around Lua and LuaJIT
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/scoder/lupa
Source:         https://files.pythonhosted.org/packages/source/l/lupa/lupa-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  lua-devel
BuildRequires:  lua51-luajit-devel
BuildRequires:  python-rpm-macros
Recommends:     lua51-luajit
Suggests:       lua
%python_subpackages

%description
Python wrapper around Lua and LuaJIT.

%prep
%setup -q -n lupa-%{version}

%build
export CFLAGS="-fno-strict-aliasing %{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_exec setup.py test

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.txt
%{python_sitearch}/*

%changelog
