#
# spec file for package kdesdk-thumbnailers
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
Name:           kdesdk-thumbnailers
Version:        19.08.0
Release:        0
Summary:        Translation file thumbnail generators
License:        GPL-2.0-or-later
Group:          Productivity/Other
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext-tools
BuildRequires:  kconfig-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Widgets)
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
This package allows KDE applications to show thumbnails
and previews of po files.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%dir %{_kf5_configkcfgdir}
%{_kf5_configkcfgdir}/pocreatorsettings.kcfg
%{_kf5_plugindir}/pothumbnail.so
%{_kf5_servicesdir}/pothumbnail.desktop

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
