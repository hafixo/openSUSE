#
# spec file for package puddletag
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           puddletag
Version:        1.2.0
Release:        0
Summary:        An audio tag editor
License:        GPL-3.0
Group:          Productivity/Multimedia/Sound/Utilities
Url:            http://docs.puddletag.net
Source0:        https://github.com/keithgg/puddletag/releases/download/v%{version}/puddletag-%{version}.tar.gz
Patch0:         fix-puddletag-wrong-shebang.patch
BuildRequires:  python-setuptools
BuildRequires:  update-desktop-files
Requires:       python-configobj
Requires:       python-mutagen
Requires:       python-pyparsing
Requires:       python-qt4
BuildArch:      noarch
Requires(post): update-desktop-files
Requires(postun): update-desktop-files

%description
puddletag is an audio tag editor (primarily created) for GNU/Linux similar
to the Windows program, Mp3tag. Unlike most taggers for GNU/Linux, it uses
a spreadsheet-like layout so that all the tags you want to edit by hand are
visible and easily editable. The usual tag editor features are supported
like extracting tag information from filenames, renaming files based on
their tags by using patterns and basic tag editing. Then there’re
Functions, which can do things like replace text, trim it, do case
conversions, etc. Actions can automate repetitive tasks. Doing web lookups
using Amazon (including cover art), Discogs (does cover art too!), FreeDB
and MusicBrainz is also supported. There’s quite a bit more, but I’ve
reached my comma quota. Supported formats: ID3v1, ID3v2 (mp3), MP4 (mp4,
m4a, etc.), VorbisComments (ogg, flac), Musepack (mpc), Monkey’s Audio
(.ape) and WavPack (wv).

%prep
%setup -q
%patch0 -p1

%build

%install
python setup.py install --root=%{buildroot} --prefix=%{_prefix}
%suse_update_desktop_file %{name} Mixer

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc HACKING README TODO copyright changelog
%{_bindir}/puddletag
%{python_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
