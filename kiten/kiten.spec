#
# spec file for package kiten
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kiten
Version:        19.08.0
Release:        0
Summary:        Japanese Reference/Study Tool
# Data files are under CC-BY-SA-3.0 (edict) and CC-BY-SA-4.0 ("kanjidic"/SKIP numbers therein)
License:        GPL-2.0-or-later AND CC-BY-SA-3.0 AND CC-BY-SA-4.0
Group:          Amusements/Teaching/Language
URL:            https://edu.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  edict
BuildRequires:  extra-cmake-modules
BuildRequires:  karchive-devel
BuildRequires:  kcompletion-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kf5-filesystem
BuildRequires:  khtml-devel
BuildRequires:  ki18n-devel
BuildRequires:  knotifications-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       fonts-KanjiStrokeOrders
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
Recommends:     %{name}-lang
Requires:       edict

%description
Kiten is a tool to learn Japanese.

%package devel
Summary:        Development files for kiten
License:        GPL-2.0-or-later
Group:          Development/Libraries/KDE
Requires:       kiten = %{version}

%description devel
Kiten is a tool to learn Japanese.

This package contains files for developing applications using kiten.

%package -n fonts-KanjiStrokeOrders
Summary:        Font for learning Japanese Kanji
License:        BSD-3-Clause
Group:          System/X11/Fonts
BuildRequires:  fontpackages-devel
Provides:       kdeedu4:%{_kde4_datadir}/fonts/kanjistrokeorders/KanjiStrokeOrders.ttf
BuildArch:      noarch
%reconfigure_fonts_prereq

%description -n fonts-KanjiStrokeOrders
This font provides an easy way to view stroke order diagrams for over 6350
kanji, 183 kana symbols, the Latin characters and quite a few other symbols.
I have also used it as a dumping ground for my own character creation doodles.

My hope is that this font will assist people who are learning kanji. I
also hope it will help teachers of Japanese in the preparation of
classroom material. Beware that Japanese stroke order can differ from the
stroke order used in other languages that use Chinese characters.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q

%build
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  for i in edict kanjidic radkfile; do
   test -e "%{_datadir}/edict/$i" && ln -fsv "%{_datadir}/edict/$i" "%{buildroot}/%{_datadir}/kiten/$i"
  done

%reconfigure_fonts_scriptlets -n fonts-KanjiStrokeOrders

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%doc AUTHORS README
%dir %{_kf5_appstreamdir}
%doc %lang(en) %{_kf5_htmldir}/en/kiten/
%{_kf5_applicationsdir}/org.kde.kiten.desktop
%{_kf5_applicationsdir}/org.kde.kitenkanjibrowser.desktop
%{_kf5_applicationsdir}/org.kde.kitenradselect.desktop
%{_kf5_appstreamdir}/org.kde.kiten.appdata.xml
%{_kf5_bindir}/kiten
%{_kf5_bindir}/kitengen
%{_kf5_bindir}/kitenkanjibrowser
%{_kf5_bindir}/kitenradselect
%{_kf5_configkcfgdir}/
%{_kf5_iconsdir}/hicolor/*/*/kiten.*
%{_kf5_libdir}/libkiten.so.*
%{_kf5_sharedir}/kiten/
%{_kf5_sharedir}/kxmlgui5/

%files devel
%{_kf5_libdir}/libkiten.so
%{_kf5_prefix}/include/libkiten/

%files -n fonts-KanjiStrokeOrders
%doc data/font/copyright.txt data/font/readme_*.txt
%dir %{_kf5_sharedir}/fonts/kanjistrokeorders/
%{_kf5_sharedir}/fonts/kanjistrokeorders/KanjiStrokeOrders.ttf

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
