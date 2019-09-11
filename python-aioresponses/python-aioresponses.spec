#
# spec file for package python-aioresponses
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-aioresponses
Version:        0.6.0
Release:        0
Summary:        Python module for mocking out requests made by ClientSession from aiohttp
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pnuckowski/aioresponses
Source:         https://files.pythonhosted.org/packages/source/a/aioresponses/aioresponses-%{version}.tar.gz
Patch0:         disable-online-test.patch
BuildRequires:  %{python_module aiohttp >= 2.0.0}
BuildRequires:  %{python_module asynctest >= 0.12.2}
BuildRequires:  %{python_module ddt >= 1.1.0}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pytest >= 3.8.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing}
BuildRequires:  %{python_module yarl}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiohttp >= 2.0.0
BuildArch:      noarch
%python_subpackages

%description
This is a Python module for mocking out requests made by ClientSession
from the aiohttp package.

%prep
%setup -q -n aioresponses-%{version}
%patch0 -p1

%build
export LC_ALL=en_US.UTF-8
%python_build

%install
export LC_ALL=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LC_ALL=en_US.UTF-8
%python_exec setup.py test

%files %{python_files}
%doc AUTHORS AUTHORS.rst ChangeLog README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
