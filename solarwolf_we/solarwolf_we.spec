#
# spec file for package solarwolf_we
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           solarwolf_we
Version:        1.0
Release:        0
Summary:        Action/arcade game originally based on SolarFox, Widescreen Edition
License:        LGPL-2.1+
Group:          Amusements/Games/Action/Arcade
Url:            http://posor.eu/solarwolf/solarwolf.htm
Source0:        http://posor.eu/solarwolf/solarwolf_we.tar.bz2
Source1:        %{name}.sh
Source2:        %{name}.desktop
Source3:        solar-wolf-logo-64.png
Source4:        %{name}-rpmlintrc
%if 0%{?suse_version}
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
BuildRequires:  python
Requires:       libmikmod
Requires:       pygame
BuildArch:      noarch

%description
Do you belong to the fans of the game Solarwolf and have switched
to a widescreen monitor like I did?
Have you ever missed the widescreen support in this great game?
Well, you are at the right place then. Here it is!
I proudly present to you the ultimate widescreen edition of Solarwolf 1.5!
It supports 16:9 and 16:10 aspect ratios.
The original game in 4:3 aspect ratio is included in this special edition.
Upgrade today and enjoy plenty of new levels and all of the old enemies.
This work is based on Solarwolf 1.5 written by Pete Shinners

The point of this game is to scramble through 48 levels of patterns,
collecting all the boxes. The part that makes it tricky is avoiding the
relentless hailstorm of fire coming at you from all directions.

%prep
%setup -q -n solarwolf
find -type d | xargs chmod 755

%build

%install
# install wrapper
install -Dm 0755 %{S:1} %{buildroot}%{_bindir}/%{name}

# install directories
mkdir -p %{buildroot}%{_datadir}/%{name}/{code,data}
for d in code data ; do
    cp -r "$d"/* %{buildroot}%{_datadir}/%{name}/"$d"
done

# install files
install -Dm 0755 *.py %{buildroot}%{_datadir}/%{name}

# install icon
install -Dm 0644 %{S:3} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# install Desktop file
install -Dm 0644 %{S:2} %{buildroot}%{_datadir}/applications/%{name}.desktop

python -m compileall -d %{_datadir}/%{name} %{buildroot}%{_datadir}/%{name}
python -O -m compileall -d %{_datadir}/%{name} %{buildroot}%{_datadir}/%{name}

%if 0%{?suse_version}
%suse_update_desktop_file %{name}
%fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root,-)
%attr(0664,root,root)%doc *.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
