#
# spec file for package python-PyFxA
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017-2018 The openSUSE Project.
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
Name:           python-PyFxA
Version:        0.7.3
Release:        0
Summary:        Firefox Accounts client library for Python
License:        MPL-2.0
Group:          Development/Languages/Python
URL:            https://github.com/mozilla/PyFxA
Source:         https://files.pythonhosted.org/packages/source/P/PyFxA/PyFxA-%{version}.tar.gz
BuildRequires:  %{python_module PyBrowserID}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module hawkauthlib}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pyotp}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.4.2}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyBrowserID
Requires:       python-cryptography
Requires:       python-requests >= 2.4.2
Requires:       python-six
BuildArch:      noarch
%ifpython3
Requires:       python-setuptools
%endif
%python_subpackages

%description
This is python library for interacting with the Firefox Accounts ecosystem.

%prep
%setup -q -n PyFxA-%{version}
sed -i -e '/^#!\/usr\/bin\/env python/d' fxa/__main__.py
# Remove online tests
rm -f fxa/tests/test_core.py
find ./ -type f -exec chmod -x {} +

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_monkey_patch_for_gevent gevent no longer packaged as it is deprecated
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} -v -k 'not test_monkey_patch_for_gevent' fxa/tests/

%files %{python_files}
%doc CHANGES.txt README.rst
%python3_only %{_bindir}/fxa-client
%{python_sitelib}/*

%changelog
