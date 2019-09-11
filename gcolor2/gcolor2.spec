#
# spec file for package gcolor2
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gcolor2
Version:        0.4
Release:        0
Summary:        Simple color selector
License:        GPL-2.0+
Group:          Productivity/Graphics/Other
Url:            http://gcolor2.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/gcolor2/%{name}-%{version}.tar.bz2
Source1:        gcolor2-pofiles.tar.bz2
Source2:        gcolor2.desktop
# add missing headers, function declarations and translation symbols to fix warnings
Patch0:         gcolor2-0.4-warnings.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ImageMagick
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  update-desktop-files
BuildRequires:  perl(XML::Parser)
%if 0%{?fedora} >= 15
BuildRequires:  sane-backends-libs
%endif
%define iconsdir %{_datadir}/icons/hicolor

%description 
Gcolor2 is a GTK2 color selector to provide a quick and easy way to find
colors for whatever task is at hand. Colors can be saved and deleted as well.

%prep
%setup -q -a1
%patch0 -p1

%build
echo "gcolor2.glade" >> po/POTFILES.in
autoreconf -fiv
intltoolize --force

%configure
#languages not detected
pushd po
sed -i s/"ALL_LINGUAS ="/"ALL_LINGUAS = `ls *.po | cut -d. -f1 | xargs`"/"" Makefile
popd

%{__make}

%install
%makeinstall

# Menu
%{__mkdir_p} %{buildroot}%{_datadir}/applications
install -m 644 %{S:2} %{buildroot}%{_datadir}/applications/%{name}.desktop

#icons
for size in 16 32 48; do
	SIZE="${size}x${size}"
	%{__mkdir_p} %{buildroot}%{iconsdir}/$SIZE/apps
	convert -strip -scale $SIZE pixmaps/icon.png %{buildroot}%{iconsdir}/$SIZE/apps/%{name}.png
done

%find_lang %{name}

%if %{suse_version} >= 1230
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING
%{_bindir}/gcolor2
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}
%{iconsdir}/*/apps/%{name}.png

%changelog
