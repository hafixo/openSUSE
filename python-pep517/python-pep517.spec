#
# spec file for package python-pep517
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
Name:           python-pep517
Version:        0.5.0
Release:        0
Summary:        Wrappers to build Python packages using PEP 517 hooks
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/takluyver/pep517
Source:         https://files.pythonhosted.org/packages/source/p/pep517/pep517-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-pytoml
BuildRequires:  %{python_module pytoml}
BuildRequires:  %{python_module testpath}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module mock}
%python_subpackages

%description
Wrappers to build Python packages using PEP 517 hooks.

%prep
%setup -q -n pep517-%{version}
sed -i 's/--flake8//' pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
