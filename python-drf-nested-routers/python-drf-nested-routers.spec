#
# spec file for package python-drf-nested-routers
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
Name:           python-drf-nested-routers
Version:        0.91.0
Release:        0
Summary:        Nested resources for the Django Rest Framework
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/alanjds/drf-nested-routers
Source:         https://github.com/alanjds/drf-nested-routers/archive/v%{version}.tar.gz
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module djangorestframework >= 3.6.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
Requires:       python-djangorestframework >= 3.6.0
BuildArch:      noarch
%python_subpackages

%description
Nested resources for the Django Rest Framework.

%prep
%setup -q -n drf-nested-routers-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
