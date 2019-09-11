#
# spec file for package python-actdiag
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
Name:           python-actdiag
Version:        0.5.4
Release:        0
Summary:        Text to activity-diagram image generator
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            http://blockdiag.com/
Source:         https://files.pythonhosted.org/packages/source/a/actdiag/actdiag-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-blockdiag >= 1.5.0
Requires:       python-setuptools
%if 0%{?suse_version} >= 1000 || 0%{?fedora_version} >= 24 ||  0%{?rhel} >= 8
Suggests:       python-docutils
Suggests:       python-nose
Suggests:       python-pep8 >= 1.3
Suggests:       python-reportlab
%endif
BuildArch:      noarch
%python_subpackages

%description
actdiag generates activity-diagram image files from spec-text files.

%prep
%setup -q -n actdiag-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.rst
%python3_only %{_bindir}/actdiag
%{python_sitelib}/*

%changelog
