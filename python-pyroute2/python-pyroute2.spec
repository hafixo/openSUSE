#
# spec file for package python-pyroute2
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
Name:           python-pyroute2
Version:        0.5.6
Release:        0
Summary:        Python Netlink library
License:        GPL-2.0-or-later OR Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/svinota/pyroute2
Source:         https://files.pythonhosted.org/packages/source/p/pyroute2/pyroute2-%{version}.tar.gz
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Pyroute2 is a pure Python netlink library. It requires only Python stdlib, no
3rd party libraries. The library was started as an RTNL protocol
implementation, so the name is pyroute2, but now it supports many netlink
protocols. Some supported netlink families and protocols:

  * rtnl, network settings --- addresses, routes, traffic controls
  * nfnetlink --- netfilter API: ipset, nftables, ...
  * ipq --- simplest userspace packet filtering, iptables QUEUE target
  * devlink --- manage and monitor devlink-enabled hardware
  * generic --- generic netlink families
  * nl80211 --- wireless functions API (basic support)
  * taskstats --- extended process statistics
  * acpi_events --- ACPI events monitoring
  * thermal_events --- thermal events monitoring
  * VFS_DQUOT --- disk quota events monitoring

%prep
%setup -q -n pyroute2-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests require root access
#%%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} nosetests-%{$python_bin_suffix} -v

%files %{python_files}
%license README.license.md
%doc README.md CHANGELOG.md README.report.md
%license LICENSE.Apache.v2 LICENSE.GPL.v2
%{python_sitelib}/*
%python3_only %{_bindir}/ss2
%python3_only %{_bindir}/pyroute2-cli

%changelog
