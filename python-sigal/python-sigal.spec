#
# spec file for package python-sigal
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without test
Name:           python-sigal
Version:        2.0
Release:        0
Summary:        Static gallery generator
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/saimn/sigal
Source:         https://files.pythonhosted.org/packages/source/s/sigal/sigal-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-Markdown
Requires:       python-Pillow
Requires:       python-blinker
Requires:       python-click
Requires:       python-pilkit
Suggests:       python-boto
Suggests:       python-cssmin
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module Markdown}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module blinker}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pilkit}
BuildRequires:  %{python_module pytest}
BuildRequires:  ffmpeg
%endif
%python_subpackages

%description
Sigal is a static gallery generator written in Python with the following
features:

* Generates HTML pages using jinja2 templates.
* Emits relative links for a portable output.
* Supports themes, videos, EXIF tags, and ZIP downloading.
* Processes directories recursively and files in parallel.

The idea behind Sigal is to ease the use of the JavaScript libraries like
galleria_. These libraries display the images, Sigal on the other hand does
image resizing, thumbnail creation and HTML page generation.

%prep
%setup -q -n sigal-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests -k "not (test_generate_video_fit_height or test_generate_video_fit_width or test_generate_video_dont_enlarge or test_build)"

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst
%python3_only %{_bindir}/sigal
%{python_sitelib}/*

%changelog
