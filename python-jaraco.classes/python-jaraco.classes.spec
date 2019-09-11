#
# spec file for package python-jaraco.classes
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
Name:           python-jaraco.classes
Version:        2.0
Release:        0
Summary:        Tools to work with classes
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/jaraco/jaraco.classes
Source0:        https://files.pythonhosted.org/packages/source/j/jaraco.classes/jaraco.classes-%{version}.tar.gz
BuildRequires:  %{python_module jaraco.base >= 6.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jaraco.base >= 6.1
Requires:       python-six
BuildArch:      noarch

%python_subpackages

%description
jaraco.classes Tools for working with classes.

%prep
%setup -q -n jaraco.classes-%{version}
sed -i 's/--flake8//' pytest.ini

%build
%python_build

%install
%python_install
# We will package the namespace __init__.py separately
%{python_expand rm %{buildroot}%{$python_sitelib}/jaraco/__init__.py*
rm -rf %{buildroot}%{$python_sitelib}/jaraco/__pycache__/
%fdupes -s %{buildroot}%{$python_sitelib}
}

%check
%{python_expand py.test-%{$python_bin_suffix} \
  --ignore=_build.python3 --ignore _build.python2
}

%files %{python_files}
%license LICENSE
%doc docs/*.rst README.rst CHANGES.rst
%{python_sitelib}/jaraco.classes-%{version}-py*.egg-info
%{python_sitelib}/jaraco/classes

%changelog
