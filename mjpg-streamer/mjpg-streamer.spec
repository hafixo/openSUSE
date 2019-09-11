#
# spec file for package mjpg-streamer (Version SVN Rev. 160)
#
# Copyright 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


Summary: Stream webcam video to HTTP
Name:    mjpg-streamer
Version: 1.0~pre.1529836414.f387bb4
Release: 0
License: GPL-2.0-only
Group:   Productivity/Multimedia/Video/Players
Source0: %{name}-%{version}.tar.xz
Patch1: fix-build.patch
Patch2: set_group.patch
URL:           https://github.com/jacksonliam/mjpg-streamer
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: opencv-devel
BuildRequires: SDL-devel
BuildRequires: libgphoto2-devel
BuildRequires: libjpeg-devel

%description
MJPG-streamer takes JPGs from Linux-UVC compatible webcams, from local files or other input plugins and streams them as M-JPEG via HTTP to webbrowsers, VLC and other software. It is the successor of uvc-streamer, a Linux-UVC streaming application with Pan/Tilt.

This package provides a maintained fork including support for Raspberry Pi Camera.

Enable the service by specifing the video device via

# systemctl start mjpg_streamer@0

The number reflects /dev/videoX and listening port 808X.

%prep
%setup -q -n %{name}-%version/mjpg-streamer-experimental
%patch1 -p2
%patch2 -p2

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DINCLUDE_INSTALL_DIR:PATH=/usr/include -DLIB_INSTALL_DIR:PATH=%_libdir -DSYSCONF_INSTALL_DIR:PATH=/etc -DSHARE_INSTALL_PREFIX:PATH=/usr/share -DCMAKE_INSTALL_LIBDIR:PATH=%_libdir -DCMAKE_BUILD_TYPE=RelWithDebInfo ..

%install
%cmake_install
# service file
install -m 0644 -D mjpg_streamer@.service %{buildroot}%{_unitdir}/mjpg_streamer@.service

%pre
%{_sbindir}/useradd -r -G video -d / -s /sbin/nologin mjpg_streamer 2> /dev/null || :

%post
%service_add_post mjpg_streamer@.service

%postun
%service_del_postun mjpg_streamer@.service

%files
%defattr(-,root,root,-)
%license LICENSE
%doc README.md
%{_bindir}/mjpg_streamer
/usr/lib/mjpg-streamer
/usr/share/mjpg-streamer
%{_unitdir}/mjpg_streamer@.service

