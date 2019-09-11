#
# spec file for package elementary-xfce-icon-theme
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


%define name0 elementary-xfce
Name:           elementary-xfce-icon-theme
Version:        0.13.1+git37.828aa1a8
Release:        0
Summary:        Icon theme inspired by Tango and Elementary
License:        GPL-2.0-only
Group:          System/GUI/Other
URL:            https://github.com/shimmerproject/elementary-xfce
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gtk3-tools
BuildRequires:  hicolor-icon-theme
Requires:       adwaita-icon-theme
Requires:       gtk3-tools
Requires:       hicolor-icon-theme
BuildArch:      noarch

%description
This is an icon-theme maintained with Xfce in mind,
but it supports other desktops like Gnome3 as well.
It's a fork of the upstream elementary-project,
which took place because the team decided to
drop a lot of desktop-specific symlinks.

%prep
%autosetup
# cleanup unecessary doc files
rm %{name0}-darker/{CONTRIBUTORS,AUTHORS,README.md}
rm %{name0}-dark/{CONTRIBUTORS,AUTHORS,README.md}
rm %{name0}/{CONTRIBUTORS,AUTHORS,README.md}

%build
# Nothing to build

%install
mkdir -p  %{buildroot}%{_datadir}/icons
cp -a %{name0}  %{buildroot}%{_datadir}/icons
cp -a %{name0}-dark  %{buildroot}%{_datadir}/icons
cp -a %{name0}-darker  %{buildroot}%{_datadir}/icons
chmod 0644  %{buildroot}%{_datadir}/icons/%{name0}/index.theme
chmod 0644  %{buildroot}%{_datadir}/icons/%{name0}-dark/index.theme
chmod 0644  %{buildroot}%{_datadir}/icons/%{name0}-darker/index.theme

# fix duplicate files
%fdupes -s %{buildroot}/%{_datadir}/icons/

%files
%doc AUTHORS CONTRIBUTORS README.md
%license LICENSE
%{_datadir}/icons/elementary-xfce/
%{_datadir}/icons/elementary-xfce-dark/
%{_datadir}/icons/elementary-xfce-darker/

%changelog
