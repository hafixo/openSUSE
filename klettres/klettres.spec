#
# spec file for package klettres
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
Name:           klettres
Version:        19.08.0
Release:        0
Summary:        Alphabet Learning Game
License:        GPL-2.0-or-later
Group:          Amusements/Teaching/Language
URL:            https://edu.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kcompletion-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  knewstuff-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  phonon4qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
Recommends:     %{name}-lang
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
Helps to learn the alphabet and read some syllables.

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
  %suse_update_desktop_file org.kde.%{name}       Education Languages

%files
%license COPYING
%doc AUTHORS ChangeLog
%config %{_kf5_configdir}/klettres.knsrc
%dir %{_kf5_appstreamdir}
%dir %{_kf5_configkcfgdir}
%doc %lang(en) %{_kf5_htmldir}/en/klettres/
%{_kf5_applicationsdir}/org.kde.klettres.desktop
%{_kf5_appsdir}/klettres/
%{_kf5_appstreamdir}/org.kde.klettres.appdata.xml
%{_kf5_bindir}/klettres
%{_kf5_configkcfgdir}/klettres.kcfg
%{_kf5_iconsdir}/hicolor/*/apps/klettres.*
%{_kf5_kxmlguidir}/klettres/
%{_kf5_debugdir}/klettres.categories

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
