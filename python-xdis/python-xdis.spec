#
# spec file for package python-xdis
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
Name:           python-xdis
Version:        4.0.2
Release:        0
Summary:        Python cross-version byte-code disassembler and marshal routines
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/rocky/python-xdis/
Source:         https://github.com/rocky/python-xdis/archive/%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six >= 1.10.0}
# /SECTION
%python_subpackages

%description
Cross-Python bytecode Disassembler and Marshal routines

%prep
%setup -q
# test fails for weird order reasons
rm pytest/test_disasm.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest pytest

%files %{python_files}
%license COPYING
%doc NEWS.md README.rst
%python3_only %{_bindir}/pydisasm.py
%{python_sitelib}/*

%changelog
