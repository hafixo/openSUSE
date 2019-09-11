#
# spec file for package kamera
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
Name:           kamera
Version:        19.08.0
Release:        0
Summary:        Digital camera support for KDE applications
License:        LGPL-2.1-or-later
Group:          Productivity/Graphics/Other
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kdoctools-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libgphoto2-devel
BuildRequires:  oxygen-icon-theme-large
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)

%description
This package allows any KDE application to access and manipulate pictures on a digital camera.

%lang_package

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif

%package -n kio_kamera
Summary:        KDE I/O Slave for Cameras
License:        GPL-2.0-or-later
Group:          Hardware/Camera
Recommends:     %{name}-lang
Provides:       %{name} = %{version}

%description -n kio_kamera
This package contains a KIO slave to access digital cameras.

%post -n kio_kamera -p /sbin/ldconfig
%postun -n kio_kamera -p /sbin/ldconfig

%files -n kio_kamera
%license COPYING*
%doc README
%dir %{_kf5_htmldir}/en/kcontrol
%dir %{_kf5_sharedir}/solid/
%dir %{_kf5_sharedir}/solid/actions/
%doc %lang(en) %{_kf5_htmldir}/en/kcontrol/kamera/
%{_kf5_plugindir}/kcm_kamera.so
%{_kf5_plugindir}/kio_kamera.so
%{_kf5_servicesdir}/camera.protocol
%{_kf5_servicesdir}/kamera.desktop
%{_kf5_sharedir}/solid/actions/solid_camera.desktop

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
