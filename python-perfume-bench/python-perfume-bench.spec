#
# spec file for package python-perfume-bench
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
%define         skip_python2 1
Name:           python-perfume-bench
Version:        0.1.6
Release:        0
Summary:        Interactive performance benchmarking in Jupyter
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/leifwalsh/perfume
Source:         https://files.pythonhosted.org/packages/source/p/perfume-bench/perfume-bench-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-bokeh >= 0.12
Requires:       python-ipython >= 5.0
Requires:       python-ipywidgets >= 5.0
Requires:       python-matplotlib >= 2.0
Requires:       python-notebook >= 5.0
Requires:       python-numpy >= 1.11
Requires:       python-pandas >= 0.19
Requires:       python-seaborn >= 0.7
Requires:       python-statsmodels >= 0.8
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module bokeh >= 0.12}
BuildRequires:  %{python_module ipython >= 5.0}
BuildRequires:  %{python_module ipywidgets >= 5.0}
BuildRequires:  %{python_module matplotlib >= 2.0}
BuildRequires:  %{python_module notebook >= 5.0}
BuildRequires:  %{python_module numpy >= 1.11}
BuildRequires:  %{python_module pandas >= 0.19}
BuildRequires:  %{python_module seaborn >= 0.7}
BuildRequires:  %{python_module statsmodels >= 0.8}
# /SECTION
%python_subpackages

%description
Interactive performance benchmarking in Jupyter

%prep
%setup -q -n perfume-bench-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%python3_only %{_bindir}/perfume
%{python_sitelib}/*

%changelog
