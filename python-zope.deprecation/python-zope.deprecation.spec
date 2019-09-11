#
# spec file for package python-zope.deprecation
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 LISA GmbH, Bingen, Germany.
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
Name:           python-zope.deprecation
Version:        4.4.0
Release:        0
Summary:        Zope Deprecation Infrastructure
License:        ZPL-2.1
Group:          Development/Languages/Python
Url:            https://pypi.python.org/pypi/zope.deprecation
Source:         https://files.pythonhosted.org/packages/source/z/zope.deprecation/zope.deprecation-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
# SECTION documentation requirements
BuildRequires:  %{python_module Sphinx}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
When we started working on Zope 3.1, we noticed that the hardest part of the
development process was to ensure backward-compatibility and correctly mark
deprecated modules, classes, functions, methods and properties. This package
provides a simple function called 'deprecated(names, reason)' to deprecate the
previously mentioned Python objects.

%package     -n %{name}-doc
Summary:        Zope 3 Deprecation Infrastructure
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Provides:       %{python_module zope.deprecation-doc = %{version}}

%description -n %{name}-doc
This package contains documentation files for %{name}.

%prep
%setup -q -n zope.deprecation-%{version}
rm -rf zope.deprecation.egg-info

%build
%python_build
%__python3 setup.py build_sphinx && rm build/sphinx/html/.buildinfo

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py -q test

%files %{python_files}
%defattr(-,root,root,-)
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%python_sitelib/*

%files -n %{name}-doc
%defattr(-,root,root,-)
%doc build/sphinx/html/

%changelog
