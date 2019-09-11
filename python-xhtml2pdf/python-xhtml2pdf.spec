#
# spec file for package python-xhtml2pdf
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
Name:           python-xhtml2pdf
Version:        0.2.3
Release:        0
Summary:        PDF Generator Using HTML and CSS
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/xhtml2pdf/xhtml2pdf
Source:         https://files.pythonhosted.org/packages/source/x/xhtml2pdf/xhtml2pdf-%{version}.tar.gz
BuildRequires:  %{python_module Pillow >= 2.0}
BuildRequires:  %{python_module PyPDF2 >= 1.26}
BuildRequires:  %{python_module html5lib >= 1.0}
BuildRequires:  %{python_module httplib2 >= 0.7.6}
BuildRequires:  %{python_module nose >= 1.3.3}
BuildRequires:  %{python_module reportlab >= 3.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow >= 2.0
Requires:       python-PyPDF2 >= 1.26
Requires:       python-html5lib >= 1.0
Requires:       python-httplib2 >= 0.7.6
Requires:       python-reportlab >= 3.0
Requires:       python-six
Conflicts:      python-pisa
BuildArch:      noarch
%python_subpackages

%description
xhtml2pdf is a html2pdf converter using the ReportLab Toolkit, the HTML5lib and
pyPdf. It supports HTML 5 and CSS 2.1 (and some of CSS 3). It is completely
written in pure Python so it is platform independent.

The main benefit of this tool that a user with Web skills like HTML and CSS is
able to generate PDF templates very quickly without learning new technologies.

%prep
%setup -q -n xhtml2pdf-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# there are no test actually

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*
%python3_only %{_bindir}/pisa
%python3_only %{_bindir}/xhtml2pdf

%changelog
