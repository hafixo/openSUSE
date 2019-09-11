#
# spec file for package python-pip-shims
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
Name:           python-pip-shims
Version:        0.3.3
Release:        0
Summary:        Compatibility shims for pip versions 8 thru current
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/sarugaku/pip-shims
Source:         https://github.com/sarugaku/pip-shims/archive/%{version}.tar.gz#/pip-shims-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 36.2.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pip
Requires:       python-setuptools
Requires:       python-six
Requires:       python-wheel
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module wheel}
# /SECTION
%python_subpackages

%description
Compatibility shims for pip versions 8 thru current.

%prep
%setup -q -n pip-shims-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Skip two online tests
%pytest -k 'not (test_resolution or test_wheelbuilder)'

%files %{python_files}
%license LICENSE
%doc README.rst CHANGELOG.rst docs/*.rst
%{python_sitelib}/*

%changelog
