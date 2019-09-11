#
# spec file for package python-cfgv
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
Name:           python-cfgv
Version:        2.0.1
Release:        0
Summary:        Configuration validator producing human readable error messages
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/asottile/cfgv
Source:         https://github.com/asottile/cfgv/archive/v%{version}.tar.gz#/cfgv-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
A configuration validator for Python that produce human readable error messages.

%prep
%setup -q -n cfgv-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
