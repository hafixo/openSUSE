#
# spec file for package python-configargparse
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
Name:           python-configargparse
Version:        0.14.0
Release:        0
Summary:        A drop-in replacement for argparse
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/zorro3/ConfigArgParse
Source:         https://files.pythonhosted.org/packages/source/C/ConfigArgParse/ConfigArgParse-%{version}.tar.gz
Patch0:         skip-test.patch
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-devel
BuildRequires:  python2-unittest2
Requires:       python-PyYAML
Requires:       python-setuptools
BuildArch:      noarch
%python_subpackages

%description
ConfigArgParse allows options to also be set via config files and/or environment
variables.

Applications with more than a handful of user-settable options are best configured
through a combination of command line args, config files, hard-coded defaults, and
in some cases, environment variables.

Python’s command line parsing modules such as argparse have very limited support
for config files and environment variables, so this module extends argparse to
add these features

%prep
%setup -q -n ConfigArgParse-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%fdupes %{buildroot}

%check
%python_exec -m unittest discover

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/configargparse*
%{python_sitelib}/ConfigArgParse-%{version}-py*.egg-info
%pycache_only %{python_sitelib}/__pycache__

%changelog
