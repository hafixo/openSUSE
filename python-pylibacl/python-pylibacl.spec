#
# spec file for package python-pylibacl
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           python-pylibacl
Version:        0.5.3
Release:        0
Summary:        Python POSIX.1e ACL module
License:        LGPL-2.1+
Group:          Development/Libraries/Python
Url:            http://pylibacl.k1024.org/
Source:         https://github.com/iustin/pylibacl/releases/download/pylibacl-v%{version}/pylibacl-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  libacl-devel
BuildRequires:  python-devel
BuildRequires:  python-setuptools
# Documentation requirements:
BuildRequires:  python-Sphinx
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%endif

%description
This Python 2.4+ extension module allows you to manipulate the POSIX.1e Access
Control Lists present in some OS/file-systems combinations. It is a wrapper on
top of the systems's acl C library - see acl(5).

%package doc
Summary:        Python POSIX.1e ACL module
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}

%description doc
This Python 2.4+ extension module allows you to manipulate the POSIX.1e Access
Control Lists present in some OS/file-systems combinations. It is a wrapper on
top of the systems's acl C library - see acl(5).

%prep
%setup -q -n pylibacl-%{version}

%build
CFLAGS="%{optflags} -fno-strict-aliasing" python setup.py build
python setup.py build_sphinx

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
%fdupes -s %{buildroot}/%{_prefix}

%check
python setup.py test

%files
%defattr(-,root,root)
%doc COPYING NEWS README
%{python_sitearch}/*

%files doc
%defattr(-,root,root)
%doc build/sphinx/html

%changelog
