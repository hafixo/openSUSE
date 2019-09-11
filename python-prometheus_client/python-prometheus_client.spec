#
# spec file for package python-prometheus_client
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
Name:           python-prometheus_client
Version:        0.7.1
Release:        0
Summary:        Python client for the Prometheus monitoring system
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/prometheus/client_python
Source:         https://github.com/prometheus/client_python/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-futures
BuildRequires:  python-rpm-macros
Suggests:       python-twisted
BuildArch:      noarch
%python_subpackages

%description
The official Python 2 and 3 client for Prometheus.

%prep
%setup -q -n client_python-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
