#
# spec file for package python-humanize
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
%global modname humanize
Name:           python-humanize
Version:        0.5.1
Release:        0
Summary:        Python humanize utilities
License:        MIT
Group:          Development/Languages/Python
URL:            http://github.com/jmoiron/humanize
Source:         https://github.com/jmoiron/humanize/archive/%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module mock}
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
This modest package contains various common humanization utilities, like turning
a number into a fuzzy human readable duration ('3 minutes ago') or into a human
readable size or throughput.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand $python setup.py test

%files %{python_files}
%license LICENCE
%doc README.rst
%{python_sitelib}/*
%{python_sitelib}/humanize/locale/*

%changelog
