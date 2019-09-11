#
# spec file for package python-jsondiff
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
Name:           python-jsondiff
Version:        1.1.2
Release:        0
Summary:        Module to diff JSON and JSON-like structures in Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/ZoomerAnalytics/jsondiff
Source:         https://files.pythonhosted.org/packages/source/j/jsondiff/jsondiff-%{version}.tar.gz
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
BuildArch:      noarch
%python_subpackages

%description
Package to show differences between JSON and JSON-like structures in Python

%prep
%setup -q -n jsondiff-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Tests do not run in py3 and upstream is not much worried about that
#%%python_expand nosetests-%{$python_bin_suffix}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*
%python3_only %{_bindir}/jsondiff

%changelog
