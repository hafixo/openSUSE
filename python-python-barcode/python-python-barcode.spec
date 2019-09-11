#
# spec file for package python-python-barcode
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019 Dr. Axel Braun
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
%define skip_python2 1
%define base_name python-barcode
Name:           python-%{base_name}
Version:        0.10.0
Release:        0
Summary:        Library to create Barcodes with Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/WhyNotHugo/python-barcode
Source:         https://files.pythonhosted.org/packages/source/p/%{base_name}/%{base_name}-%{version}.tar.gz
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module pathlib}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dejavu-fonts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       dejavu-fonts
Provides:       python-pyBarcode
Obsoletes:      python-pyBarcode
BuildArch:      noarch
%python_subpackages

%description
Library to create standard barcodes with Python. No external modules needed (optional PIL support included).

%prep
%setup -q -n %{base_name}-%{version}
# Fix rpmlint warning about too many +x perms when these files get installed later.
find . -type f -exec chmod a-x {} +
# doc buildscripts we don't wanna ship
rm docs/{Makefile,make.bat}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
find "%{buildroot}" -type f -name "*.ttf" | while read i; do
	ln -fs "%{_datadir}/fonts/truetype/${i##*/}" "$i"
done

%check
%python_exec test.py

%files %{python_files}
%doc docs/*
%license LICENCE
%{python_sitelib}/*
%python3_only %{_bindir}/python-barcode

%changelog
