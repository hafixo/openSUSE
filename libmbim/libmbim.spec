#
# spec file for package libmbim
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Dominique Leuenberger, Amsterdam, The Netherlands
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


Name:           libmbim
Version:        1.18.2
Release:        0
Summary:        Mobile Broadband Interface Model (MBIM) protocol
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            http://www.freedesktop.org/wiki/Software/libmbim/
Source:         http://www.freedesktop.org/software/libmbim/%{name}-%{version}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.36
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gudev-1.0) >= 147

%description
libmbim is a glib-based library for talking to WWAN modems and devices
which speak the Mobile Interface Broadband Model (MBIM) protocol.

%package -n libmbim-glib4
Summary:        Mobile Interface Broadband Model (MBIM) protocol
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libmbim-glib4
libmbim is a glib-based library for talking to WWAN modems and devices
which speak the Mobile Interface Broadband Model (MBIM) protocol.

%package devel
Summary:        Mobile Interface Broadband Model (MBIM) protocol - Development files
License:        LGPL-2.1-or-later
Group:          Development/Languages/C and C++
Requires:       libmbim-glib4 = %{version}

%description devel
libmbim is a glib-based library for talking to WWAN modems and devices
which speak the Mobile Interface Broadband Model (MBIM) protocol.

%package -n mbimcli-bash-completion
Summary:        Bash completion for mbimcli
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Productivity/Networking/System
BuildRequires:  bash-completion
Requires:       bash-completion
Supplements:    packageand(%{name}:bash-completion)

%description -n mbimcli-bash-completion
This package contain de bash completion command for mbimcli tools.

%prep
%setup -q

%build
# Do not rely on env for choosing python
sed -i "s|env python|python3|g" build-aux/mbim-codegen/*
%configure \
  --with-udev \
  --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
make %{?_smp_mflags} check

%post -n libmbim-glib4 -p /sbin/ldconfig
%postun -n libmbim-glib4 -p /sbin/ldconfig

%files
%license COPYING
%doc NEWS
%{_bindir}/mbim-network
%{_bindir}/mbimcli
%{_libexecdir}/mbim-proxy
%{_mandir}/man1/mbim-network.1%{?ext_man}
%{_mandir}/man1/mbimcli.1%{?ext_man}

%files -n libmbim-glib4
%license COPYING.LIB

%{_libdir}/libmbim-glib.so.*

%files devel
%doc AUTHORS README
# Own these directories to not depend on gtk-doc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%doc %{_datadir}/gtk-doc/html/libmbim-glib/
%{_includedir}/libmbim-glib/
%{_libdir}/libmbim-glib.so
%{_libdir}/pkgconfig/mbim-glib.pc

%files -n mbimcli-bash-completion
%{_datadir}/bash-completion/completions/mbimcli

%changelog
