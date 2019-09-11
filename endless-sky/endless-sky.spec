#
# spec file for package endless-sky
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           endless-sky
Version:        0.9.6
Release:        0
Summary:        Space exploration, trading, and combat game
License:        GPL-3.0 and CC-BY-SA-4.0 and CC-BY-SA-3.0 and CC-BY-3.0
Group:          Amusements/Games/Action/Arcade
Url:            http://endless-sky.github.io/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
# PATCH-FIX-OPENSUSE fix-data-path.patch -- Fix installation path of data
Patch0:         fix-data-path.patch
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg8-devel
BuildRequires:  scons
BuildRequires:  xdg-utils
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Explore other star systems. Earn money by trading, carrying passengers,
or completing missions. Use your earnings to buy a better ship or to
upgrade the weapons and engines on your current one. Blow up pirates.
Take sides in a civil war. Or leave human space behind and hope to
find some friendly aliens whose culture is more civilized than your own...

%prep
%setup -q
%patch0 -p1

%build
scons

%install
scons install PREFIX=%{_prefix} DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{_prefix}/games/endless-sky %{buildroot}%{_bindir}/endless-sky

%fdupes %{buildroot}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc license.txt README.md changelog copyright
%{_bindir}/endless-sky
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/man/man6/*
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
