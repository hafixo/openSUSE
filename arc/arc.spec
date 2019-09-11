#
# spec file for package arc
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


Name:           arc
Version:        5.21q
Release:        0
Summary:        Archiving tool for arc achives
License:        GPL-2.0-only
Group:          Productivity/Archiving/Compression
URL:            https://github.com/ani6al/arc
Source:         https://github.com/ani6al/arc/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         arc-5.21p-directory-traversel.patch
Patch1:         arc-5.21p-fix-arcdie.patch
Patch2:         arc-5.21p-hdrv1-read-fix.patch

%description
This package allows you to unpack *.arc file

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
make %{?_smp_mflags} OPT="%{optflags}"

%install
install -Dpm 0755 arc \
  %{buildroot}%{_bindir}/arc
install -Dpm 0755 marc \
  %{buildroot}%{_bindir}/marc
install -Dpm 0644 arc.1 \
  %{buildroot}%{_mandir}/man1/arc.1

%files
%doc Arc521.doc Arcinfo Readme
%license LICENSE
%{_bindir}/arc
%{_bindir}/marc
%{_mandir}/man1/arc.1%{ext_man}

%changelog
