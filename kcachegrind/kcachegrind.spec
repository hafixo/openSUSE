#
# spec file for package kcachegrind
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
Name:           kcachegrind
Version:        19.08.0
Release:        0
Summary:        Frontend for Cachegrind
License:        GPL-2.0-only AND BSD-4-Clause AND GFDL-1.2-only
Group:          Development/Tools/Other
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  karchive-devel
BuildRequires:  kconfig-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)
Recommends:     %{name}-lang

%description
KCachegrind is a frontend for cachegrind.

%lang_package

%prep
%setup -q

%build
%ifarch ppc64
RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
export CXXFLAGS="%{optflags} -fPIC"
export CFLAGS="%{optflags} -fPIC"
%cmake_kf5 -d build -- -DCMAKE_CXXFLAGS="%{optflags}" -DCMAKE_CFLAGS="%{optflags}"
%make_jobs

%install
  %make_install -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name --with-qt
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file    org.kde.kcachegrind    Development Profiling

%files
%license COPYING COPYING.DOC
%doc README
%{_kf5_applicationsdir}/org.kde.kcachegrind.desktop
%{_kf5_bindir}/dprof2calltree
%{_kf5_bindir}/hotshot2calltree
%{_kf5_bindir}/kcachegrind
%{_kf5_bindir}/memprof2calltree
%{_kf5_bindir}/op2calltree
%{_kf5_bindir}/pprof2calltree
%doc %lang(en) %{_kf5_htmldir}/en/kcachegrind/
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_sharedir}/kcachegrind/
%{_kf5_appstreamdir}/org.kde.kcachegrind.appdata.xml

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
