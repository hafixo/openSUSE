#
# spec file for package konsole
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
Name:           konsole
Version:        19.08.0
Release:        0
Summary:        KDE Terminal
License:        GPL-2.0-or-later
Group:          System/X11/Terminals
URL:            http://www.kde.org/
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Source3:        Root_Shell.profile
Source4:        konsolesu.desktop
Source21:       utilities-terminal-su-16.png
Source22:       utilities-terminal-su-22.png
Source23:       utilities-terminal-su-32.png
Source24:       utilities-terminal-su-48.png
Source25:       utilities-terminal-su-64.png
Source26:       utilities-terminal-su-128.png
# PATCH-FIX-OPENSUSE
Patch0:         fix-build-with-gcc48.patch
BuildRequires:  fdupes
BuildRequires:  kbookmarks-devel
BuildRequires:  kcompletion-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kf5-filesystem
BuildRequires:  kglobalaccel-devel
BuildRequires:  kguiaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kinit-devel
BuildRequires:  kio-devel
BuildRequires:  knewstuff-devel
BuildRequires:  knotifications-devel
BuildRequires:  knotifyconfig-devel
BuildRequires:  kparts-devel
BuildRequires:  kpty-devel
BuildRequires:  kservice-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5DBus) >= 5.2.0
BuildRequires:  pkgconfig(Qt5PrintSupport) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Script) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2.0
Requires:       %{name}-part = %{version}
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
Konsole is a terminal emulator for the K Desktop Environment.

%package part
Summary:        KDE Terminal
Group:          System/GUI/KDE
Recommends:     %{name}-part-lang
Obsoletes:      konsole5-part < %{version}

%description part
Konsole is a terminal emulator for the K Desktop Environment.
This package provides KPart of the Konsole application.

%if %{with lang}
%package -n %{name}-part-lang
Summary:        Translations for package %{name}
Group:          System/Localization
Requires:       %{name}-part = %{version}
Supplements:    packageand(bundle-lang-other:%{name}-part)
Provides:       %{name}-lang = %{version}
Obsoletes:      %{name}-lang < %{version}
Provides:       %{name}-part-lang-all = %{version}
BuildArch:      noarch

%description -n %{name}-part-lang

Provides translations for the "%{name}" package.
%endif

%prep
%setup -q
%if 0%{?suse_version} < 1500
%patch0 -p1
%endif

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  install -D -m 0644 %{SOURCE3}  "%{buildroot}%{_kf5_sharedir}/konsole/Root Shell.profile"
  install -D -m 0644 %{SOURCE4}  %{buildroot}%{_kf5_applicationsdir}/
  install -D -m 0644 %{SOURCE21} %{buildroot}%{_kf5_iconsdir}/hicolor/16x16/apps/utilities-terminal_su.png
  install -D -m 0644 %{SOURCE22} %{buildroot}%{_kf5_iconsdir}/hicolor/22x22/apps/utilities-terminal_su.png
  install -D -m 0644 %{SOURCE23} %{buildroot}%{_kf5_iconsdir}/hicolor/32x32/apps/utilities-terminal_su.png
  install -D -m 0644 %{SOURCE24} %{buildroot}%{_kf5_iconsdir}/hicolor/48x48/apps/utilities-terminal_su.png
  install -D -m 0644 %{SOURCE25} %{buildroot}%{_kf5_iconsdir}/hicolor/64x64/apps/utilities-terminal_su.png
  install -D -m 0644 %{SOURCE26} %{buildroot}%{_kf5_iconsdir}/hicolor/128x128/apps/utilities-terminal_su.png
  %suse_update_desktop_file org.kde.konsole TerminalEmulator
  %fdupes -s %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post part -p /sbin/ldconfig
%postun part -p /sbin/ldconfig

%files
%license COPYING
%doc README
%dir %{_kf5_appstreamdir}
%dir %{_kf5_htmldir}
%dir %{_kf5_htmldir}/en
%dir %{_kf5_sharedir}/khotkeys/
%doc %lang(en) %{_kf5_htmldir}/en/konsole/
%{_kf5_knsrcfilesdir}/konsole.knsrc
%{_kf5_applicationsdir}/konsolesu.desktop
%{_kf5_applicationsdir}/org.kde.konsole.desktop
%{_kf5_appstreamdir}/org.kde.konsole.appdata.xml
%{_kf5_bindir}/konsole
%{_kf5_bindir}/konsoleprofile
%{_kf5_iconsdir}/hicolor/*/apps/utilities-terminal_su.png
%{_kf5_libdir}/libkdeinit5_konsole.so
%{_kf5_servicesdir}/ServiceMenus/
%{_kf5_sharedir}/khotkeys/konsole.khotkeys

%files part
%license COPYING
%doc README
%dir %{_kf5_plugindir}
%dir %{_kf5_servicesdir}
%dir %{_kf5_servicetypesdir}
%{_kf5_libdir}/libkonsoleprivate.so.*
%{_kf5_notifydir}/
%{_kf5_plugindir}/konsolepart.so
%{_kf5_servicesdir}/konsolepart.desktop
%{_kf5_servicetypesdir}/terminalemulator.desktop
%{_kf5_sharedir}/konsole/
%{_kf5_debugdir}/konsole.categories

%if %{with lang}
%files part-lang -f %{name}.lang
%license COPYING*
%endif

%changelog
