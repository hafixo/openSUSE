#
# spec file for package gtk4
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2010 Dominique Leuenebrger, Amsterdam, Netherlands
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


# When updating the binary version, do not forget to also update baselibs.conf
%define gtk_binary_version 4.0.0
%define _name gtk+
Name:           gtk4
Version:        3.94.0
Release:        0
Summary:        The GTK+ toolkit library (version 4)
License:        LGPL-2.1-or-later
Group:          Development/Libraries/X11
URL:            http://www.gtk.org/
Source:         http://download.gnome.org/sources/gtk+/3.94/%{_name}-%{version}.tar.xz
Source2:        settings.ini
Source3:        macros.gtk4
Source98:       gtk4-rpmlintrc
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM gtk4-fix-dependency-error.patch luc14n0@linuxmail.org glgo#GNOME/gtk#1218 fix build failure when using few threads.
Patch0:         gtk4-fix-dependency-error.patch

BuildRequires:  cups-devel >= 1.2
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools >= 0.19.7
BuildRequires:  gtk-doc
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.42.1
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  vulkan-devel
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(atk) >= 2.15.1
BuildRequires:  pkgconfig(atk-bridge-2.0)
BuildRequires:  pkgconfig(cairo) >= 1.14.0
BuildRequires:  pkgconfig(cairo-gobject) >= 1.14.0
BuildRequires:  pkgconfig(cloudproviders) >= 0.2.5
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(epoxy) >= 1.4
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.30.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.53.7
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0) >= 2.53.7
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.39.0
BuildRequires:  pkgconfig(graphene-1.0) >= 1.5.1
BuildRequires:  pkgconfig(graphene-gobject-1.0) >= 1.5.1
BuildRequires:  pkgconfig(gstreamer-player-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(pango) >= 1.37.3
BuildRequires:  pkgconfig(pangocairo) >= 1.14.0
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  pkgconfig(wayland-client) >= 1.14.91
BuildRequires:  pkgconfig(wayland-cursor) >= 1.9.91
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.9
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrandr) >= 1.2.99

%description
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

%package -n libgtk-4-0
Summary:        The GTK+ toolkit library (version 4)
# gtk4-data is currently not being built, might be an upstream oversight though
Group:          System/Libraries
Requires:       %{name}-schema >= %{version}
# Require Adwaita Icon Theme: It's GTKs icon set, that's guaranteed to be there
Requires:       adwaita-icon-theme
# While hicolor is not a Requires strictly speaking, we put it as
# such instead of as a Recommends because many applications just
# assume it's there and we need to have a low-level package to
# bring it in.
Requires:       hicolor-icon-theme
# gtk+ can work without branding/translations. Built in defaults will be used then.
Recommends:     %{name}-branding
Recommends:     gvfs
Obsoletes:      %{name}-data
# IM modules have been dropped in 3.94.0
Obsoletes:      %{name}-immodule-amharic
Obsoletes:      %{name}-immodule-broadway
Obsoletes:      %{name}-immodule-inuktitut
Obsoletes:      %{name}-immodule-multipress
Obsoletes:      %{name}-immodule-thai
Obsoletes:      %{name}-immodule-tigrigna
Obsoletes:      %{name}-immodule-vietnamese
Obsoletes:      %{name}-immodule-xim
# Provide main package to make the lang subpackage installable
Provides:       %{name} = %{version}

%description -n libgtk-4-0
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

%package -n typelib-1_0-Gtk-4_0
Summary:        Introspection bindings for the GTK+ toolkit library v4
Group:          System/Libraries

%description -n typelib-1_0-Gtk-4_0
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides the GObject Introspection bindings for GTK+.

%package tools
Summary:        Auxiliary utilities for the GTK+ toolkit library v4
Group:          System/Libraries

%description tools
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

%package schema
Summary:        Config schema for the GTK+ toolkit library v4
# The schema is shared between gtk3 and gtk4 - gtk4 wins
Group:          System/Libraries
Provides:       gtk3-schema = %{version}
Obsoletes:      gtk3-schema < %{version}
BuildArch:      noarch

%description schema
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

%package branding-upstream
Summary:        Upstream theme configuration for the GTK+ toolkit library v4
Group:          System/Libraries
Requires:       libgtk-4-0 = %{version}
Supplements:    packageand(libgtk-4-0:branding-upstream)
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{version}
BuildArch:      noarch
#BRAND: Provides /usr/share/gtk-4.0/settings.ini, to define default theme and icon
#BRAND: theme.
#BRAND: Do not forget to add proper Requires in branding package if changing
#BRAND: those.

%description branding-upstream
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides the upstream theme configuration for widgets and
icon themes.

%package devel
Summary:        Development files for the GTK+ toolkit library v4
Group:          Development/Libraries/X11
Requires:       gettext-its-%{name} >= %{version}
Requires:       libgtk-4-0 = %{version}
Requires:       typelib-1_0-Gtk-4_0 = %{version}
Requires:       vulkan-devel

%description devel
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package contains the development files for GTK+ 4.x.

%package -n gettext-its-%{name}
Summary:        International Tag Set for GTK+ 4
# The ITS is compatible between GTK3 and GTK4
Group:          Development/Libraries/X11
Provides:       gettext-its-gtk3 = %{version}
Obsoletes:      gettext-its-gtk3 < %{version}

%description -n gettext-its-%{name}
This package enhances gettext with an International Tag Set for GTK+ 4

%lang_package

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1
translation-update-upstream

%build
%meson \
  -Dbuild-tests=false \
  -Ddocumentation=true \
  -Dbroadway-backend=true \
  -Dcloudproviders=false \
  -Dcolord=yes \
  -Dprint-backends=all \
  -Dvulkan=yes \
  -Dwayland-backend=true \
  -Dx11-backend=true \
  -Dxinerama=yes \
  -Dintrospection=true \
  -Dman-pages=true
%meson_build

%install
%meson_install

%find_lang gtk40
%find_lang gtk40-properties
install -m 644 -D %{SOURCE2} %{buildroot}%{_datadir}/gtk-4.0/settings.ini
# create modules directory that should have been created during the build
if test ! -d %{buildroot}%{_libdir}/gtk-4.0/modules; then
  mkdir %{buildroot}%{_libdir}/gtk-4.0/modules
else
  echo 'Remove this no-longer-needed modulesdir hack.'
fi
# create theming-engines directory that should have been created during the build
if test ! -d %{buildroot}%{_libdir}/gtk-4.0/%{gtk_binary_version}/theming-engines; then
  mkdir %{buildroot}%{_libdir}/gtk-4.0/%{gtk_binary_version}/theming-engines
else
  echo 'Remove this no-longer-needed themingdir hack.'
fi
# Install rpm macros
mkdir -p %{buildroot}%{_sysconfdir}/rpm
cp %{SOURCE3} %{buildroot}%{_sysconfdir}/rpm
%fdupes %{buildroot}%{_datadir}
%fdupes %{buildroot}%{_libdir}

%post   -n libgtk-4-0 -p /sbin/ldconfig
%postun -n libgtk-4-0 -p /sbin/ldconfig

%files -n libgtk-4-0
%license COPYING
%doc AUTHORS NEWS
%dir %{_libdir}/gtk-4.0
%dir %{_libdir}/gtk-4.0/%{gtk_binary_version}
%dir %{_libdir}/gtk-4.0/%{gtk_binary_version}/printbackends/
%{_libdir}/gtk-4.0/%{gtk_binary_version}/printbackends/libprintbackend-cups.so
%{_libdir}/gtk-4.0/%{gtk_binary_version}/printbackends/libprintbackend-cloudprint.so
%{_libdir}/gtk-4.0/%{gtk_binary_version}/printbackends/libprintbackend-file.so
%dir %{_libdir}/gtk-4.0/%{gtk_binary_version}/media/
%{_libdir}/gtk-4.0/%{gtk_binary_version}/media/libmedia-gstreamer.so
%dir %{_libdir}/gtk-4.0/%{gtk_binary_version}/theming-engines/
%dir %{_libdir}/gtk-4.0/modules
%{_libdir}/libgtk-4.so.*

%files -n typelib-1_0-Gtk-4_0
%{_libdir}/girepository-1.0/Gdk-4.0.typelib
%{_libdir}/girepository-1.0/GdkX11-4.0.typelib
%{_libdir}/girepository-1.0/Gsk-4.0.typelib
%{_libdir}/girepository-1.0/Gtk-4.0.typelib

%files tools
%{_bindir}/gtk4-broadwayd
%{_bindir}/gtk4-icon-browser
%{_bindir}/gtk4-builder-tool
%{_bindir}/gtk4-encode-symbolic-svg
%{_bindir}/gtk4-launch
%{_bindir}/gtk4-query-settings
%{_bindir}/gtk4-update-icon-cache
%{_datadir}/applications/gtk4-icon-browser.desktop
%{_mandir}/man1/gtk4-broadwayd.1%{?ext_man}
%{_mandir}/man1/gtk4-icon-browser.1%{ext_man}
%{_mandir}/man1/gtk4-builder-tool.1%{?ext_man}
%{_mandir}/man1/gtk4-encode-symbolic-svg.1%{?ext_man}
%{_mandir}/man1/gtk4-launch.1%{?ext_man}
%{_mandir}/man1/gtk4-query-settings.1%{?ext_man}
%{_mandir}/man1/gtk4-update-icon-cache.1%{?ext_man}

%files schema
%{_datadir}/glib-2.0/schemas/org.gtk.Demo.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gtk.Settings.ColorChooser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gtk.Settings.Debug.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gtk.Settings.EmojiChooser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gtk.Settings.FileChooser.gschema.xml

%files branding-upstream
%{_datadir}/gtk-4.0/settings.ini

%files devel
%doc CONTRIBUTING.md README.commits
%doc %{_datadir}/gtk-doc/html/gdk4/
%doc %{_datadir}/gtk-doc/html/gsk4/
%doc %{_datadir}/gtk-doc/html/gtk4/
%{_bindir}/gtk4-demo
%{_bindir}/gtk4-demo-application
%{_bindir}/gtk4-widget-factory
%{_mandir}/man1/gtk4-demo.1%{?ext_man}
%{_mandir}/man1/gtk4-demo-application.1%{?ext_man}
%{_mandir}/man1/gtk4-widget-factory.1%{?ext_man}
%{_datadir}/applications/gtk4-demo.desktop
%{_datadir}/metainfo/org.gtk.Demo.appdata.xml
%{_datadir}/applications/gtk4-widget-factory.desktop
%{_datadir}/metainfo/org.gtk.WidgetFactory.appdata.xml
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/gtk-4.0
%{_datadir}/gtk-4.0/gtkbuilder.rng
%{_datadir}/icons/hicolor/*/apps/gtk4-demo.png
%{_datadir}/icons/hicolor/*/apps/gtk4-widget-factory.png
%{_datadir}/icons/hicolor/*/apps/gtk4-demo-symbolic.symbolic.png
%{_datadir}/icons/hicolor/*/apps/gtk4-widget-factory-symbolic.symbolic.png
%{_includedir}/gtk-4.0/
%{_libdir}/pkgconfig/gtk+-4.0.pc
%{_libdir}/pkgconfig/gtk+-broadway-4.0.pc
%{_libdir}/pkgconfig/gtk+-wayland-4.0.pc
%{_libdir}/pkgconfig/gtk+-unix-print-4.0.pc
%{_libdir}/pkgconfig/gtk+-x11-4.0.pc
%{_libdir}/libgtk-4.so
%{_sysconfdir}/rpm/macros.gtk4

%files -n gettext-its-%{name}
%dir %{_datadir}/gettext/
%dir %{_datadir}/gettext/its/
%{_datadir}/gettext/its/gtkbuilder.its
%{_datadir}/gettext/its/gtkbuilder.loc

%files lang -f gtk40.lang -f gtk40-properties.lang

%changelog
