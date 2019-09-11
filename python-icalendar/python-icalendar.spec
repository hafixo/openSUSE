#
# spec file for package python-icalendar
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011 open-slx GmbH <Sascha.Manns@open-slx.de>
# Copyright (c) 2009 - 7/2011 Sascha Manns <saigkill@opensuse.org>
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
%define	modname icalendar
Name:           python-%{modname}
Version:        4.0.3
Release:        0
Summary:        Python parser/generator of iCalendar files package
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/collective/icalendar
Source0:        https://files.pythonhosted.org/packages/source/i/icalendar/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil
Requires:       python-pytz
Provides:       %{name}-doc = %{version}
Obsoletes:      %{name}-doc < %{version}
BuildArch:      noarch
%python_subpackages

%description
The iCalendar package is a parser/generator of iCalendar files for use
with Python. It follows the RFC 2445 (iCalendar) specification.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%check
%python_exec %{_bindir}/py.test src

%files %{python_files}
%license LICENSE.rst
%doc README.rst CHANGES.rst
%python3_only %{_bindir}/icalendar
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
