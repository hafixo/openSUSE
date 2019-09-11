#
# spec file for package python-whitenoise
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
Name:           python-whitenoise
Version:        4.1.3
Release:        0
Summary:        Static file serving for WSGI applications
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/evansd/whitenoise
Source:         https://files.pythonhosted.org/packages/source/w/whitenoise/whitenoise-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-Brotli
BuildArch:      noarch

%python_subpackages

%description
Static file serving for WSGI applications.

%prep
%setup -q -n whitenoise-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
