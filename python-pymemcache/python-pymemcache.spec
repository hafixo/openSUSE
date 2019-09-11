#
# spec file for package python-pymemcache
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2014 Thomas Bechtold <thomasbechtold@jpberlin.de>
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
Name:           python-pymemcache
Version:        2.1.1
Release:        0
Summary:        A pure Python memcached client
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/Pinterest/pymemcache
Source:         https://files.pythonhosted.org/packages/source/p/pymemcache/pymemcache-%{version}.tar.gz
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
%ifpython2
BuildRequires:  python2-future
Requires:       python2-future
%endif
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch

%python_subpackages

%description
A pure-Python memcached client.

pymemcache supports the following features:

* Complete implementation of the memcached text protocol.
* Configurable timeouts for socket connect and send/recv calls.
* Access to the "noreply" flag, which can significantly increase the speed of writes.
* Flexible, simple approach to serialization and deserialization.
* The (optional) ability to treat network and memcached errors as cache misses.

%prep
%setup -q -n pymemcache-%{version}

%build
%python_build

%install
%python_install

%check
%python_exec setup.py test

%files %{python_files}
%defattr(-,root,root,-)
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*

%changelog
