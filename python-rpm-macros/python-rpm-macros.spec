#
# spec file for package python-rpm-macros
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


Name:           python-rpm-macros
Version:        20190610.2ee3233
Release:        0
Summary:        RPM macros for building of Python modules
License:        WTFPL
Group:          Development/Tools/Other
URL:            https://github.com/opensuse/python-rpm-macros
Source:         python-rpm-macros-%{version}.tar.bz2
# Fedora compatibility
Provides:       python2-rpm-macros
Provides:       python3-rpm-macros
BuildArch:      noarch

%description
This package contains SUSE RPM macros for Python build automation.
You should BuildRequire this package unless you are sure that you
are only building for distros newer than Leap 42.2

%prep
%setup -q
%if 0%{?suse_version} < 1330
mv macros-default-pythons macros/035-default-pythons
%endif

%build
./compile-macros.sh

%install
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/
install -m 644 macros.python_all %{buildroot}%{_rpmconfigdir}/macros.d/

%files
%license LICENSE
%doc README.md
%{_rpmconfigdir}/macros.d/macros.python_all

%changelog
