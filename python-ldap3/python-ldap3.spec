#
# spec file for package python-ldap3
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
Name:           python-ldap3
Version:        2.6
Release:        0
Summary:        A strictly RFC 4511 conforming LDAP V3 pure Python client
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/cannatag/ldap3
Source:         https://github.com/cannatag/ldap3/archive/v%{version}.tar.gz
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pyasn1 >= 0.1.8}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-testsuite
Requires:       python-pyasn1 >= 0.1.8
BuildArch:      noarch
%python_subpackages

%description
ldap3 is a strictly RFC 4511 conforming LDAP V3 pure Python **client**.
The same codebase works with Python, Python 3, PyPy and PyPy3.

This project was formerly named **python3-ldap**.
The name has been changed to avoid confusion with the python-ldap library.

%prep
%setup -q -n ldap3-%{version}
sed -i 's/\r$//' COPYING.LESSER.txt COPYING.txt README.rst LICENSE.txt

%build
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%check
%python_exec %{_bindir}/nosetests -s test || :

%files %{python_files}
%license COPYING.LESSER.txt COPYING.txt LICENSE.txt
%doc README.rst
%{python_sitelib}/ldap3
%{python_sitelib}/ldap3-%{version}-py*.egg-info

%changelog
