#
# spec file for package powerstat
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


Name:           powerstat
Version:        0.02.18
Release:        0
Summary:        Laptop power measuring tool
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            http://kernel.ubuntu.com/~cking/powerstat/
Source:         http://kernel.ubuntu.com/~cking/tarballs/%{name}/%{name}-%{version}.tar.gz

%description
Powerstat measures the power consumption of a mobile PC that has a battery
power source. The output is like vmstat but also shows power consumption
statistics. At the end of a run, powerstat will calculate the average,
standard deviation and min/max of the gathered data.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%{_bindir}/powerstat
%{_mandir}/man8/powerstat.8%{?ext_man}

%changelog
