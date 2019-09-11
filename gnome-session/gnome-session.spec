#
# spec file for package gnome-session
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


Name:           gnome-session
Version:        3.32.0+5
Release:        0
Summary:        Session Tools for the GNOME Desktop
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://www.gnome.org
# We are using source services, so no download url for source
Source0:        %{name}-%{version}.tar.xz
Source1:        gnome
Source2:        gnome.desktop

# PATCH-FIX-UPSTREAM gnome-session-better-handle-empty-xdg_session_type.patch bsc#1084756 bgo#794256 yfjiang@suse.com -- solution provided by msrb@suse.com using a more reasonable way to handle gpu acceleration check
Patch0:         gnome-session-better-handle-empty-xdg_session_type.patch
# PATCH-FIX-UPSTREAM gnome-session-presence-Enable-idle-detection-when-screen-locked.patch bsc#1118286 glgo#GNOME/gnome-shell#900 xwang@suse.com -- Enable dimming screen when screen is locked
Patch1:         gnome-session-presence-Enable-idle-detection-when-screen-locked.patch
# PATCH-FIX-OPENSUSE gnome-session-s390-not-require-g-s-d_wacom.patch bsc#1129412 yfjiang@suse.com -- Remove the runtime requirement of g-s-d Wacom plugin
Patch2:         gnome-session-s390-not-require-g-s-d_wacom.patch

BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.76
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gio-2.0) >= 2.46.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.46.0
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0) >= 2.46.0
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 3.18.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.18.0
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.10
BuildRequires:  pkgconfig(libsystemd) >= 209
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xtrans)
Requires:       %{name}-core = %{version}
Requires:       %{name}-default-session = %{version}
Recommends:     %{name}-lang
# gnome-session-wayland not recommended by default yet: causes various issues:
# qemu's default video mode is 'cirrus', which stays black with GNOME Wayland
# YaST cannot be started without additional tricks
# All together this blocks us from passing openQA
# Recommends:     %%{name}-wayland

%description
This package provides the basic session tools, like session management
functionality, for the GNOME Desktop.

%package default-session
Summary:        Default session support for the GNOME Session Manager
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
Requires:       gnome-settings-daemon
Requires:       gnome-shell

%description default-session
This package contains the definition of the default GNOME session.

%package wayland
Summary:        Wayland support for the GNOME Session Manager
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
Requires:       gnome-settings-daemon
Requires:       xorg-x11-server-wayland

%description wayland
This package contains the definition of the default GNOME session on Wayland.

%package core
Summary:        Minimal version of the GNOME Session Manager
Group:          System/GUI/GNOME
Requires:       dbus-1-x11
Requires:       gsettings-desktop-schemas >= 0.1.7
Requires:       hicolor-icon-theme
%glib2_gsettings_schema_requires

%description core
This package contains a minimal version of gnome-session, that can be
used for specific cases. The gnome-session package is needed for a fully
functional GNOME desktop.

%lang_package

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%ifarch s390 s390x
%patch2 -p1
%endif
translation-update-upstream po gnome-session-3.0

%build
%meson \
  -D docbook=false \
  -D systemd=true \
%if !0%{is_opensuse}
  -D systemd_journal=false \
%endif
  %{nil}
%meson_build

%install
%meson_install
# install startup script and xsession file
install -d -m755 %{buildroot}%{_bindir}
install -m755 %{SOURCE1} %{buildroot}%{_bindir}/gnome
install -d -m755 %{buildroot}%{_datadir}/xsessions
install -m644 %{SOURCE2} %{buildroot}%{_datadir}/xsessions/gnome.desktop
%find_lang %{name}-3.0 %{?no_lang_C}
%fdupes %{buildroot}/%{_prefix}
# remove wayland files on s390/s390x
%ifarch s390 s390x
rm -fr %{buildroot}%{_datadir}/wayland-sessions
%endif

# Prepare for 'default.desktop' being update-alternative handled, boo#1039756
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop %{buildroot}%{_datadir}/xsessions/default.desktop
%ifnarch s390 s390x
touch %{buildroot}%{_sysconfdir}/alternatives/default-waylandsession.desktop
ln -s %{_sysconfdir}/alternatives/default-waylandsession.desktop %{buildroot}%{_datadir}/wayland-sessions/default.desktop
%endif

%post
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop \
  default-xsession.desktop %{_datadir}/xsessions/gnome.desktop 25

%postun
[ -f %{_datadir}/xsessions/gnome.desktop ] || %{_sbindir}/update-alternatives \
  --remove default-xsession.desktop %{_datadir}/xsessions/gnome.desktop

%files
%{_bindir}/gnome
%{_datadir}/xsessions/default.desktop
%{_datadir}/xsessions/gnome.desktop
%{_datadir}/xsessions/gnome-xorg.desktop
%ghost %{_sysconfdir}/alternatives/default-xsession.desktop

%files default-session
%{_datadir}/gnome-session/sessions/gnome.session
%{_datadir}/gnome-session/sessions/gnome-dummy.session

%ifnarch s390 s390x
%post wayland
%{_sbindir}/update-alternatives --install %{_datadir}/wayland-sessions/default.desktop \
  default-waylandsession.desktop %{_datadir}/wayland-sessions/gnome.desktop 25

%postun wayland
[ -f %{_datadir}/wayland-sessions/gnome.desktop ] || %{_sbindir}/update-alternatives \
  --remove default-waylandsession.desktop %{_datadir}/wayland-sessions/gnome.desktop

%files wayland
%dir %{_datadir}/wayland-sessions
%{_datadir}/wayland-sessions/default.desktop
%{_datadir}/wayland-sessions/gnome.desktop
%ghost %{_sysconfdir}/alternatives/default-waylandsession.desktop
# Disabled as wayland is now the default session again.
#{_datadir}/wayland-sessions/gnome-wayland.desktop
%endif

%files core
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/gnome-session
%{_bindir}/gnome-session-custom-session
%{_bindir}/gnome-session-inhibit
%{_bindir}/gnome-session-quit
%{_datadir}/GConf/gsettings/gnome-session.convert
%{_datadir}/glib-2.0/schemas/org.gnome.SessionManager.gschema.xml
%dir %{_datadir}/gnome-session
%dir %{_datadir}/gnome-session/sessions
%{_mandir}/man1/gnome-session.1%{?ext_man}
%{_mandir}/man1/gnome-session-inhibit.1%{?ext_man}
%{_mandir}/man1/gnome-session-quit.1%{?ext_man}
%{_libexecdir}/gnome-session-binary
# Helper for the session definitions, to know if hardware is accelerated
%{_libexecdir}/gnome-session-check-accelerated
%{_libexecdir}/gnome-session-check-accelerated-gl-helper
%{_libexecdir}/gnome-session-check-accelerated-gles-helper
%{_libexecdir}/gnome-session-failed
%{_datadir}/gnome-session/hardware-compatibility

%files lang -f %{name}-3.0.lang

%changelog
