#
# spec file for package klavaro
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


%if 0%{?suse_version} >= 1500
%define espeak    espeak-ng-compat
%else
%define espeak    espeak
%endif

Name:           klavaro
Version:        3.03
Release:        0
Summary:        Typing tutor
License:        GPL-3.0-or-later
Group:          Amusements/Teaching/Other
Url:            http://klavaro.sourceforge.net/
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE klavaro-3.00-paragraph-ru-fix.patch kkirill@opensuse.org -- replace special typographic chars
Patch0:         klavaro-3.00-paragraph-ru-fix.patch
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libcurl-devel
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
Recommends:     %{espeak}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Klavaro  is a touch typing tutor that is very
flexible and supports customizable keyboard
layouts. Users can edit and save new or unknown
keyboard layouts, as the basic course provided by
the program was designed to not depend on specific
layouts.

%lang_package
%prep
%setup -q
%patch0

%build
export CFLAGS="%{optflags}"
# Disable static linking when libgtkdatabox gtk3 appears
%configure --disable-shared
make %{?_smp_mflags}

%install
%make_install

%fdupes -s %{buildroot}

%find_lang %{name}

%if 0%{?suse_version}
%suse_update_desktop_file -r klavaro Education Teaching
%endif

%post
%if 0%{?suse_version} > 1130
%icon_theme_cache_post
%desktop_database_post
%endif

%postun
%if 0%{?suse_version} > 1130
%icon_theme_cache_postun
%desktop_database_postun
%endif

%files -f %{name}.lang
%defattr(0755, root, root, 0755)
%{_bindir}/klavaro
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_mandir}/man1/klavaro.1*
%{_datadir}/klavaro/
%dir %{_datadir}/appdata
%{_datadir}/appdata/klavaro.appdata.xml
%{_datadir}/applications/klavaro.desktop
%{_datadir}/icons/hicolor/*/apps/klavaro.png
# Remove static lib processing when libgtkdatabox gtk3 apppears
%exclude %{_libdir}/libgtkdataboks.*

%changelog
