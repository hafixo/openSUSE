#
# spec file for package rockdodger
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           rockdodger
Version:        1.0.2
Release:        0
Summary:        Addictive rock-dodging greeblie-killing platform game
License:        GPL-2.0+
Group:          Amusements/Games/Arcade/LogicGame
Url:            https://bitbucket.org/rpkrawczyk/rockdodger
Source0:        https://bitbucket.org/rpkrawczyk/%{name}/downloads/%{name}-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM bmwiedemann https://bitbucket.org/rpkrawczyk/rockdodger/pull-requests/1/allow-to-override-compiledate/diff
Patch0:         reproducible.patch
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(sdl)

%description
Addictive rock-dodging greeblie-killing platform game.

Dodge the rocks for as long as possible until you die. Kill greeblies to
make the universe safe for non-greeblie life once again.

%prep
%setup -q
%patch0 -p1

# Correct path and highscore
sed -i -e 's|usr/local|usr|;
           s|localstatedir =|#localstatedir =|
           s|$(localstatedir)/games|$(datarootdir)/$(PACKAGENAME)|' \
       Makefile data/Makefile
sed -i '/touch $(gamesdir)/,/chmod g+rw/s/^/#/' Makefile

%build
make %{?_smp_mflags} CC="cc %{optflags}"

%install
%make_install

# install icon
install -Dm 0644 spacerocks.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

# install Desktop file
install -Dm 0644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root)
%doc COPYING
%attr(0755,root,root) %{_bindir}/%{name}
%{_mandir}/man6/%{name}.6%{ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/%{name}

%changelog
