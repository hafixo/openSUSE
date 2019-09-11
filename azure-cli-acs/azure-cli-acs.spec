#
# spec file for package azure-cli-acs
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


Name:           azure-cli-acs
Version:        2.3.17
Release:        0
Summary:        Microsoft Azure CLI 'acs' Command Module
License:        MIT
Group:          System/Management
Url:            https://github.com/Azure/azure-cli
Source:         https://files.pythonhosted.org/packages/source/a/azure-cli-acs/azure-cli-acs-%{version}.tar.gz
Source1:        LICENSE.txt
BuildRequires:  azure-cli-command-modules-nspkg
BuildRequires:  azure-cli-nspkg
BuildRequires:  fdupes
BuildRequires:  python3-azure-nspkg >= 3.0.0
BuildRequires:  python3-setuptools
Requires:       azure-cli-command-modules-nspkg
Requires:       azure-cli-core
Requires:       azure-cli-nspkg
Requires:       python3-PyYAML >= 4.2b1
Requires:       python3-azure-graphrbac >= 0.53.0
Requires:       python3-azure-mgmt-authorization >= 0.50.0
Requires:       python3-azure-mgmt-compute >= 4.4.0
Requires:       python3-azure-mgmt-containerservice >= 4.4.0
Requires:       python3-azure-nspkg >= 3.0.0
Requires:       python3-paramiko >= 2.0.8
Requires:       python3-scp
Requires:       python3-six
Requires:       python3-sshtunnel
Conflicts:      azure-cli < 2.0.0

BuildArch:      noarch

%description
Microsoft Azure CLI 'acs' Command Module

This package is for the 'acs' module.
i.e. 'az acs'

%prep
%setup -q -n azure-cli-acs-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-cli-acs-%{version}
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix} --install-lib=%{python3_sitelib}
%fdupes %{buildroot}%{python3_sitelib}
rm -rf %{buildroot}%{python3_sitelib}/azure/cli/command_modules/__init__.*
rm -rf %{buildroot}%{python3_sitelib}/azure/cli/command_modules/__pycache__
rm -rf %{buildroot}%{python3_sitelib}/azure/cli/__init__.*
rm -rf %{buildroot}%{python3_sitelib}/azure/cli/__pycache__
rm -rf %{buildroot}%{python3_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{python3_sitelib}/azure/__pycache__

%files
%defattr(-,root,root,-)
%doc HISTORY.rst README.rst
%license LICENSE.txt
%{python3_sitelib}/azure/cli/command_modules/acs
%{python3_sitelib}/azure_cli_acs-*.egg-info

%changelog
