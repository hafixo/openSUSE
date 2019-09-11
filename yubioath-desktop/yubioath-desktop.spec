#
# spec file for package yubioath-desktop
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


%define binname yubioath
Name:           yubioath-desktop
Version:        4.3.6
Release:        0
Summary:        Graphical interface for displaying OATH codes with a Yubikey
License:        GPL-3.0-or-later
Group:          Productivity/Security
URL:            https://developers.yubico.com/yubioath-desktop/
Source0:        https://developers.yubico.com/yubioath-desktop/Releases/%{name}-%{version}.tar.gz
Source1:        https://developers.yubico.com/yubioath-desktop/Releases/%{name}-%{version}.tar.gz.sig
BuildRequires:  fdupes
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(python3)
Requires:       libqt5-qtquickcontrols
Requires:       pyotherside
Requires:       yubikey-manager

%description
The Yubico Authenticator is a graphical desktop tool for generating
Open AuTHentication (OATH) event-based HOTP and time-based TOTP
one-time password codes, with the help of a Yubikey NEO that protects
the shared secrets.

%prep
%setup -q -n %{name}
# Fix build for Leap 15 and SLE 15
sed -i 's|python |python3 |g' yubioath-desktop.pro

%build
qmake-qt5 QMAKE_CFLAGS+="%{optflags}" QMAKE_CXXFLAGS+="%{optflags}" QMAKE_STRIP="/bin/true";
make %{?_smp_mflags}

%install
make install INSTALL_ROOT="%{buildroot}";

mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m 0644 resources/icons/%{binname}.png %{buildroot}%{_datadir}/pixmaps/

mkdir -p %{buildroot}%{_datadir}/applications
install -p -m 0644 resources/%{name}.desktop %{buildroot}%{_datadir}/applications/
%suse_update_desktop_file -i %{name} System Security
%fdupes %{buildroot}

%files
%license COPYING
%doc NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{binname}.png

%changelog
