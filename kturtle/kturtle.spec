#
# spec file for package kturtle
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
Name:           kturtle
Version:        19.08.0
Release:        0
Summary:        Logo Programming Environment
License:        GPL-2.0-or-later
Group:          Amusements/Teaching/Mathematics
URL:            https://edu.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kcrash-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  knewstuff-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
KTurtle is an educational Logo programming environment.

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
  %suse_update_desktop_file org.kde.%{name}       Education Math

%files
%license COPYING*
%doc AUTHORS README.md
%config %{_kf5_configdir}/kturtle.knsrc
%dir %{_kf5_appstreamdir}
%doc %lang(en) %{_kf5_htmldir}/en/kturtle/
%{_kf5_applicationsdir}/org.kde.kturtle.desktop
%{_kf5_appstreamdir}/org.kde.kturtle.appdata.xml
%{_kf5_bindir}/kturtle
%{_kf5_iconsdir}/hicolor/*/apps/kturtle.*
%{_kf5_kxmlguidir}/kturtle/
%if %{with lang}
%{_kf5_sharedir}/katepart/
%{_kf5_sharedir}/kturtle/
%endif

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
