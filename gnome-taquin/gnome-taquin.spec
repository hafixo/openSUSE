#
# spec file for package gnome-taquin
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


Name:           gnome-taquin
Version:        3.32.0
Release:        0
Summary:        A computer version of the 15-puzzle and other sliding puzzles
License:        GPL-3.0-or-later
Group:          Amusements/Games/Board/Puzzle
URL:            https://wiki.gnome.org/Apps/Taquin
Source0:        https://download.gnome.org/sources/gnome-taquin/3.32/%{name}-%{version}.tar.xz

BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.15.0
BuildRequires:  pkgconfig(libcanberra-gtk3) >= 0.26
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.32.0

%description
Taquin is a computer version of the 15-puzzle and other sliding puzzles.

The object of Taquin is to move tiles so that they reach their places,
either indicated with numbers, or with parts of a great image.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%find_lang gnome-taquin %{?no_lang_C} %{name}.lang
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Taquin.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Taquin.gschema.xml
%{_datadir}/%{name}/
%{_datadir}/metainfo/org.gnome.Taquin.appdata.xml
%{_datadir}/icons/hicolor/*/apps/*
%doc %{_datadir}/help/C/%{name}/
%{_mandir}/man6/%{name}.6%{?ext_man}

%files lang -f %{name}.lang

%changelog
