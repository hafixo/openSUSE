#
# spec file for package taisei
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


Name:           taisei
Version:        1.3
Release:        0
Summary:        Clone of the Touhou Project series of shoot ’em up games
License:        MIT
Group:          Amusements/Games/Action/Arcade
URL:            https://taisei-project.org
Source0:        https://github.com/taisei-project/taisei/releases/download/v%{version}/%{name}-v%{version}.tar.xz
Source1:        https://github.com/taisei-project/taisei/releases/download/v%{version}/%{name}-v%{version}.tar.xz.sig
Source2:        gpg.keyring
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.46.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libwebpdecoder) > 0.4
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(sdl2) >= 2.0.5
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-data
Requires(post): desktop-file-utils
Requires(post): shared-mime-info
Requires(postun): desktop-file-utils
Requires(postun): shared-mime-info
BuildRequires:  python3-Pygments
BuildRequires:  python3-docutils

%description
Taisei is an open clone of the Touhou Project series. Touhou is a one-man project
of shoot ’em up games set in an isolated world full of Japanese folklore.

%package data
Summary:        Data files for Taisei
Group:          Amusements/Games/Action/Arcade
Requires:       %{name} >= %{version}
BuildArch:      noarch

%description data
Data files for Taisei, an open clone of the Touhou Project series. Touhou is a
one-man project of shoot ’em up games set in an isolated world full of
Japanese folklore.

%prep
%setup -q -n %{name}-v%{version}

%build
_v=%{version}
%meson -Dstrip=false -Dversion_fallback=${_v//.g/-g}
%meson_build

%install
%meson_install

%if 0%{?suse_version} && !0%{?fedora_version}
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/%{name} %{buildroot}%{_docdir}/%{name}
%endif
%fdupes %{buildroot}

%files
%{_docdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-replay-viewer.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/mimetypes/taisei-replay.png
%{_datadir}/mime/packages/taisei.xml

%files data
%{_datadir}/%{name}

%changelog
