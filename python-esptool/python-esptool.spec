#
# spec file for package python-esptool
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
Name:           python-esptool
Version:        2.6
Release:        0
Summary:        A serial utility to communicate & flash code to Espressif ESP8266 & ESP32 chips
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/espressif/esptool
Source:         https://github.com/espressif/esptool/archive/v%{version}.tar.gz#/esptool-%{version}.tar.gz
BuildRequires:  %{python_module ecdsa}
BuildRequires:  %{python_module pyaes}
BuildRequires:  %{python_module pyelftools}
BuildRequires:  %{python_module pyserial >= 2.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  openssl
BuildRequires:  python-rpm-macros
Requires:       python-ecdsa
Requires:       python-pyaes
Requires:       python-pyserial >= 2.5
BuildArch:      noarch

%python_subpackages

%description
A command line utility to communicate with the ROM bootloader in Espressif ESP8266 & ESP32 microcontrollers.

Allows flashing firmware, reading back firmware, querying chip parameters, etc.

%prep
%setup -q -n esptool-%{version}
rm -r ecdsa pyaes
sed -i '/flake8/d' setup.py
sed -i '/^#!/d' flasher_stub/*.py
chmod a-x flasher_stub/*.py

%build
%python_build

%install
%python_install
%python_clone %{buildroot}%{_bindir}/esptool.py
%python_clone %{buildroot}%{_bindir}/espsecure.py
%python_clone %{buildroot}%{_bindir}/espefuse.py
%python_expand sed -i '/^#!/d' %{buildroot}%{$python_sitelib}/*.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.md flasher_stub/
%{_bindir}/esptool.py-%{python_bin_suffix}
%{_bindir}/espsecure.py-%{python_bin_suffix}
%{_bindir}/espefuse.py-%{python_bin_suffix}
%python3_only %{_bindir}/esptool.py
%python3_only %{_bindir}/espsecure.py
%python3_only %{_bindir}/espefuse.py
%{python_sitelib}/*

%changelog
