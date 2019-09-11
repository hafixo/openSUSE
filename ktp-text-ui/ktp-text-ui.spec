#
# spec file for package ktp-text-ui
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %global _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           ktp-text-ui
Version:        19.08.0
Release:        0
Summary:        Telepathy chat handler for KDE
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://community.kde.org/Real-Time_Communication_and_Collaboration
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  breeze5-icons
BuildRequires:  extra-cmake-modules >= 1.3.0
BuildRequires:  fdupes
BuildRequires:  karchive-devel
BuildRequires:  kcmutils-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kemoticons-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kitemviews-devel
BuildRequires:  knotifications-devel
BuildRequires:  knotifyconfig-devel
BuildRequires:  kpeople5-devel
BuildRequires:  kservice-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  ktp-common-internals-devel
BuildRequires:  ktp-icons
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  pkgconfig
BuildRequires:  sonnet-devel
BuildRequires:  telepathy-logger-qt5-devel
BuildRequires:  telepathy-qt5-devel
BuildRequires:  pkgconfig(Qt5TextToSpeech)
BuildRequires:  pkgconfig(Qt5WebEngine) >= 5.7.0
# Explicitely require logger, otherwise the ui would crash
Requires:       telepathy-logger
Obsoletes:      %{name}-devel
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
Recommends:     %{name}-lang

%description
Includes KDE's implementation of the Telepathy chat handler,
a chat plasmoid, and a chat log viewer application.

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
  %endif
  %fdupes %{buildroot}
  mkdir -p %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/apps/
  cp %{_kf5_iconsdir}/breeze/apps/48/kde-im-log-viewer.svg %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/apps/

%files
%license COPYING*
%{_kf5_applicationsdir}/*.desktop
%{_kf5_bindir}/ktp-log-viewer
%{_kf5_iconsdir}/hicolor/scalable/apps/kde-im-log-viewer.svg
%{_kf5_kxmlguidir}/ktp-text-ui/
%{_kf5_libdir}/libexec/ktp-adiumxtra-protocol-handler
%{_kf5_libdir}/libexec/ktp-text-ui
%{_kf5_libdir}/libktpchat.so*
%{_kf5_libdir}/libktpimagesharer.so*
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}/
%{_kf5_sharedir}/dbus-1/services/org.freedesktop.Telepathy.Client.KTp.TextUi.service
%{_kf5_sharedir}/ktelepathy/
%{_kf5_sharedir}/ktp-log-viewer/
%{_kf5_sharedir}/telepathy/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
