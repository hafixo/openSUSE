#
# spec file for package python-vim-vint
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
Name:           python-vim-vint
Version:        0.3.19
Release:        0
Summary:        Lint tool for Vim script Language
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/Kuniwak/vint
Source:         https://github.com/Kuniwak/vint/archive/v0.3.19.tar.gz
Patch0:         test-sys-executable.patch
Patch1:         yaml5.patch
BuildRequires:  %{python_module PyYAML >= 3.11}
BuildRequires:  %{python_module ansicolor >= 0.2.4}
BuildRequires:  %{python_module chardet >= 2.3.0}
BuildRequires:  %{python_module coverage >= 3.7.1}
BuildRequires:  %{python_module pathlib}
BuildRequires:  %{python_module pytest >= 2.6.4}
BuildRequires:  %{python_module pytest-cov >= 1.8.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-enum34 >= 1.0.4
BuildRequires:  python-rpm-macros
BuildRequires:  python-typing >= 3.6.2
BuildRequires:  python2-mock >= 1.0.1
Requires:       python-PyYAML >= 3.11
Requires:       python-ansicolor >= 0.2.4
Requires:       python-chardet >= 2.3.0
%ifpython2
Requires:       python-enum34 >= 1.0.4
Requires:       python-pathlib >= 1.0.1
Requires:       python-typing >= 3.6.2
%endif
BuildArch:      noarch

%python_subpackages

%description
A lint tool for the Vim script Language.

%prep
%setup -q -n vint-%{version}
%patch0 -p1
%patch1 -p1
sed -e 's/==/>=/g' \
    -e 's/\~=/>=/g' \
    -i setup.py \
    -i test-requirements.txt \
    -i requirements.txt
sed -i -e '/^#!\//, 1d' vint/_bundles/vimlparser.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python setup.py test

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%python3_only %{_bindir}/vint
%{python_sitelib}/*

%changelog
