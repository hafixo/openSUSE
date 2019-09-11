#
# spec file for package python-abimap
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-abimap
Version:        0.3.1
Release:        0
Summary:        A helper for library maintainers to use symbol versioning
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/ansasaki/abimap
Source:         https://files.pythonhosted.org/packages/source/a/abimap/abimap-%{version}.tar.gz
Patch0:         abimap-0.3.0-disable-pytest-console-script-tests.patch
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
BuildArch:      noarch
# SECTION test requirements
#BuildRequires:  %%{python_module pytest-console-scripts}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
This script allows to generate and update symbol version linker scripts which
adds version information to the exported symbols. The script is intended to be
integrated as part of a shared library build to check for changes in the set of
exported symbols and update the symbol version linker script accordingly.

%package doc
Summary:        Symbol versioning helper (Documentation)
Group:          Documentation/HTML

%description doc
Documentation for the symbol versioning helper %{name}

%prep
%setup -q -n abimap-%{version}

%patch0 -p1

%build
%python_build

PYTHONPATH=${PWD}/src:${PWD}/tests sphinx-build docs html
PYTHONPATH=${PWD}/src:${PWD}/tests sphinx-build -E -b man docs man

%install
%python_install

rm -rf html/.{doctrees,buildinfo}

install -d -m 0755 %{buildroot}%{_mandir}/man1
install -m 0644 man/abimap.1 %{buildroot}%{_mandir}/man1/

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
make -j1 -C tests ABIMAP_NAME_VERSION="abimap-%{version}" ABIMAP_VERSION="%{version}"
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib}:${PWD}/tests py.test-%{$python_version} -vv tests

%files %{python_files}
%doc AUTHORS.rst CHANGELOG.rst README.rst
%license LICENSE
%python3_only %{_bindir}/abimap
%python3_only %{_mandir}/man1/abimap.1*
%{python_sitelib}/*

%files %{python_files doc}
%doc html
%license LICENSE

%changelog
