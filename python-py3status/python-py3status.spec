#
# spec file for package python-py3status
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
Name:           python-py3status
Version:        3.19
Release:        0
Summary:        Extensible i3status wrapper written in python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ultrabug/py3status
Source:         https://files.pythonhosted.org/packages/source/p/py3status/py3status-%{version}.tar.gz
BuildRequires:  %{python_module gevent >= 1.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-gevent >= 1.1
BuildArch:      noarch
%ifpython3
Provides:       py3status = %{version}
Obsoletes:      py3status < %{version}
%endif
%python_subpackages

%description
py3status is an extensible i3status wrapper written in python.

Using py3status, you can take control of your i3bar easily by:

- using one of the availables modules shipped with py3status
- writing your own modules and have their output displayed on your bar
- handling click events on your i3bar and play with them in no time
- seeing your clock tick every second whatever your i3status interval

%prep
%setup -q -n py3status-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/py3status
%python_clone -a %{buildroot}%{_bindir}/py3-cmd
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF8
%pytest tests/

%post
%python_install_alternative py3status
%python_install_alternative py3-cmd

%preun
%python_uninstall_alternative py3status
%python_uninstall_alternative py3-cmd

%files %{python_files}
%license LICENSE
%doc README.rst CHANGELOG
%python_alternative %{_bindir}/py3status
%python_alternative %{_bindir}/py3-cmd
%{python_sitelib}/*

%changelog
