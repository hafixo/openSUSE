#
# spec file for package kapptemplate
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
Name:           kapptemplate
Version:        19.08.0
Release:        0
Summary:        Template for KDE Application Development
License:        GPL-2.0-only AND GFDL-1.2-only
Group:          Development/Tools/IDE
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  karchive-devel
BuildRequires:  kcompletion-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  knewstuff-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Test)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
Obsoletes:      kapptemplate5 < %{version}
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
This package contains templates to start the development of a new KDE
application/part/plugin.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q
sed -i 's|Categories=Qt;KDE;Development;|Categories=Qt;KDE;Development;IDE;X-KDE-KDevelopIDE;|g' src/application/org.kde.kapptemplate.desktop

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file    org.kde.kapptemplate

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%dir %{_kf5_appstreamdir}
%doc %lang(en) %{_kf5_htmldir}/en/*/
%{_kf5_applicationsdir}/org.kde.kapptemplate.desktop
%{_kf5_appstreamdir}/org.kde.kapptemplate.appdata.xml
%{_kf5_bindir}/kapptemplate
%{_kf5_configkcfgdir}/
%{_kf5_iconsdir}/hicolor/*/apps/kapptemplate.*
%{_kf5_sharedir}/kdevappwizard/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
