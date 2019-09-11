#
# spec file for package python-testfixtures
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
Name:           python-testfixtures
Version:        6.10.0
Release:        0
Summary:        A collection of helpers and mock objects for unit tests and doc tests
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Simplistix/testfixtures
Source:         https://files.pythonhosted.org/packages/source/t/testfixtures/testfixtures-%{version}.tar.gz
BuildRequires:  %{python_module pytest >= 3.6}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-mock
# Test case dependencies
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module sybil}
BuildRequires:  %{python_module zope.component}
Suggests:       python-Django
Suggests:       python-Twisted
Suggests:       python-sybil
Suggests:       python-zope.component
BuildArch:      noarch
%python_subpackages

%description
TestFixtures is a collection of helpers and mock objects that are
useful when writing unit tests or doc tests.

If you're wondering why "yet another mock object library", testing is
often described as an art form and as such some styles of library will
suit some people while others will suit other styles. This library
contains common test fixtures the author found himself
repeating from package to package and so decided to extract them into
their own library and give them some tests of their own!

%prep
%setup -q -n testfixtures-%{version}
chmod a-x docs/*.txt

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/testfixtures/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=testfixtures.tests.test_django.settings
%python_expand $python -m pytest testfixtures/tests

%files %{python_files}
%license LICENSE.txt
%doc README.rst docs/*.txt
%{python_sitelib}/*

%changelog
