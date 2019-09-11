#
# spec file for package python-MechanicalSoup
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
Name:           python-MechanicalSoup
Version:        0.11.0
Release:        0
Summary:        A Python library for automating interaction with websites
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hickford/MechanicalSoup
Source:         https://files.pythonhosted.org/packages/source/M/MechanicalSoup/MechanicalSoup-%{version}.tar.gz
Patch0:         bs4-47.patch
BuildRequires:  %{python_module beautifulsoup4 >= 4.4}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pytest-httpbin}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.0}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.4}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-beautifulsoup4 >= 4.4
Requires:       python-lxml
Requires:       python-requests >= 2.0
Requires:       python-six >= 1.4
BuildArch:      noarch
%python_subpackages

%description
A Python library for automating interaction with websites.
MechanicalSoup automatically stores and sends cookies,
follows redirects, and can follow links and submit forms.
It doesn't do Javascript.

The Mechanize library is incompatible with Python 3 and development
is inactive. MechanicalSoup provides a similar API to it, built on
Python giants Requests (for http sessions) and BeautifulSoup (for
document navigation).

%prep
%setup -q -n MechanicalSoup-%{version}
%patch0 -p1
# do not require cov/xdist/etc
sed -i -e '/addopts/d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
