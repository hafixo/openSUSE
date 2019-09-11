#
# spec file for package python-rebulk
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
Name:           python-rebulk
Version:        1.0.1
Release:        0
Summary:        Library for defining bulk search patterns to perform advanced string matching
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Toilal/rebulk
Source0:        https://pypi.io/packages/source/r/rebulk/rebulk-%{version}.tar.gz
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
ReBulk is a Python library that performs advanced searches in
strings that would be hard to implement using the re module or
String methods only.

It includes some features like Patterns, Match, Rule that
allow building a custom and complex string matcher.

%prep
%setup -q -n rebulk-%{version}
# Remove shebang from non-executable files
for i in {'chain','debug','formatters','__init__','introspector','loose','match','pattern','processors','rebulk','remodule','rules','toposort','utils','validators','__version__'}; do
sed -i -e "1d" "rebulk/$i.py"
done
for i in {'default_rules_module','__init__','rebulk_rules_module','rules_module','test_chain','test_debug','test_introspector','test_loose','test_match','test_pattern','test_processors','test_rebulk','test_rules','test_toposort','test_validators'}; do
sed -i -e "1d" "rebulk/test/$i.py"
done

%build
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
%{python_expand PYTHONPATH=%{buildroot}%{$python_sitelib}
py.test-%{$python_version} rebulk/test/
}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/rebulk
%{python_sitelib}/rebulk-%{version}-py%{python_version}.egg-info

%changelog
