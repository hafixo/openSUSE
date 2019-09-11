#
# spec file for package ktorrent
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           ktorrent
Version:        5.1.1
Release:        0
Summary:        KDE BitTorrent Client
License:        GPL-2.0-or-later
Group:          Productivity/Networking/File-Sharing
URL:            http://ktorrent.org/
Source0:        http://download.kde.org/stable/ktorrent/%{version}/%{name}-%{version}.tar.xz
Source2:        ktorrent.1
Source3:        ktupnptest.1
# PATCH-FIX-OPENSUSE initial-preference.diff cmorve69@yahoo.es -- InitialPreference to set it as the default torrent downloader
Patch0:         initial-preference.diff
%if 0%{?suse_version} < 1330
# PATCH-FIX-OPENSUSE fix-build-with-qt5.6.patch -- make it build with Qt < 5.7.0 (i.e. on Leap 42.x)
Patch1:         fix-build-with-qt5.6.patch
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  libktorrent-devel >= 2.1
BuildRequires:  phonon4qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  plasma5-workspace-devel
BuildRequires:  syndication-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DNSSD)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kross)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Plotting)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WebKit)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(taglib)
Recommends:     %{name}-lang = %{version}
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
%if 0%{?suse_version} < 1330
#!BuildIgnore:  libgcc_s1
%if 0%{?sle_version} < 120300
BuildRequires:  gcc5
BuildRequires:  gcc5-c++
%else
BuildRequires:  gcc7
BuildRequires:  gcc7-c++
%endif
%endif

%description
KTorrent is a BitTorrent application by KDE which allows you to download files
using the BitTorrent protocol. It enables you to run multiple torrents at the
same time and comes with extended features to make it a full-featured client
for BitTorrent.

%lang_package

%prep
%setup -q
%autopatch -p1

%build
%if 0%{?suse_version} < 1330
%if 0%{?sle_version} < 120300
%cmake_kf5 -d build -- -DCMAKE_C_COMPILER=gcc-5 -DCMAKE_CXX_COMPILER=g++-5
%else
%cmake_kf5 -d build -- -DCMAKE_C_COMPILER=gcc-7 -DCMAKE_CXX_COMPILER=g++-7
%endif
%else
%cmake_kf5 -d build
%endif
%make_jobs

%install
%kf5_makeinstall -C build

# Not needed, fix "devel-file-in-non-devel-package" rpmlint warning
rm -f %{buildroot}%{_libdir}/libktcore.so

# Add man pages from help2man edited.
mkdir -p %{buildroot}%{_mandir}/man1
cp -a %{SOURCE2} %{buildroot}%{_mandir}/man1
cp -a %{SOURCE3} %{buildroot}%{_mandir}/man1

# Fix any .py files with shebangs and wrong permissions.
if test -z `find %{buildroot} -name *.py -perm 0644 -print0|xargs -0r grep -l '#!'`; \
then break;
else chmod -f 0755 `find %{buildroot} -name *.py -perm 0644 -print0|xargs -0r grep -l '#!'`; \
fi

%suse_update_desktop_file -r org.kde.ktorrent Qt KDE Network P2P

%fdupes -s %{buildroot}

%find_lang %{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc ChangeLog RoadMap
%dir %{_kf5_appstreamdir}
%{_kf5_bindir}/ktmagnetdownloader
%{_kf5_bindir}/ktorrent
%{_kf5_bindir}/ktupnptest
%{_kf5_applicationsdir}/org.kde.ktorrent.desktop
%{_kf5_appstreamdir}/org.kde.ktorrent.appdata.xml
%{_kf5_htmldir}/en/ktorrent/
%{_kf5_iconsdir}/hicolor/*/*/*.png
%{_kf5_iconsdir}/hicolor/*/*/*.svgz
%{_kf5_kxmlguidir}/ktorrent/
%{_kf5_mandir}/man1/ktorrent.1%{?ext_man}
%{_kf5_mandir}/man1/ktupnptest.1%{?ext_man}
%{_kf5_notifydir}/ktorrent.notifyrc
%{_kf5_plugindir}/
%{_kf5_sharedir}/ktorrent/
%{_libdir}/libktcore.so.*

%files lang -f %{name}.lang
%{_kf5_htmldir}/*/ktorrent/
%dir %{_kf5_htmldir}/pt_BR
%exclude %{_kf5_htmldir}/en/ktorrent/

%changelog
