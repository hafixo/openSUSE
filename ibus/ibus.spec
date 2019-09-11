#
# spec file for package ibus
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


%if 0%{?is_opensuse}
%define with_wayland 1
%define with_kde 1
%ifarch armv6l armv6hl ppc riscv64
%define with_emoji 0
%else
%define with_emoji 1
%endif
%else
%define with_wayland 0
%define with_kde 0
%define with_emoji 0
%endif
Name:           ibus
Version:        1.5.20
Release:        0
Summary:        The "Intelligent Input Bus" input method
License:        LGPL-2.1-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/ibus/
Source:         https://github.com/ibus/ibus/releases/download/%{version}/%{name}-%{version}.tar.gz
Source2:        README.SUSE
Source3:        xim.ibus.suse.template
Source4:        xim.d-ibus-121
Source7:        macros.ibus
Source10:       ibus-autostart
Source11:       ibus-autostart.desktop
Source99:       baselibs.conf
# PATCH-FIX-OPENSUSE ibus-python-install-dir.patch ftake@geeko.jp
Patch0:         ibus-python-install-dir.patch
# PATFH-FIX-OPENSUSE ibus-xim-fix-re-focus-after-lock.patch bnc#874869 tiwai@suse.de -- Fix lost XIM input after screenlock
Patch4:         ibus-xim-fix-re-focus-after-lock.patch
# PATCH-FIX-UPSTREAM ftake@geeko.jp
# Select an IM engine at the first login
Patch8:         im-engines-precede-xkb.patch
# PATCH-FIX-UPSTREAM ftake@geeko.jp
Patch9:         ibus-fix-check-abs-icon-path-support.patch
# PATCH-FIX-SLE hide-setup-menu.patch bnc#899259  qzhao@suse.com
# ibus-setup should not launch from main menu.
Patch10:        hide-setup-menu.patch
# PATCH-FIX-SLE setup-switch-im.patch bnc#899259  qzhao@suse.com
# switch to ibus when ibus not running.
Patch11:        setup-switch-im.patch
# PATCH-FIX-SLE ibus-disable-engines-preload-in-GNOME.patch bnc#1036729 qzhao@suse.com
# Disable ibus engines preload in GNOME for These works are handled by gnome-shell.
Patch12:        ibus-disable-engines-preload-in-GNOME.patch
BuildRequires:  dbus-1-glib-devel
BuildRequires:  dconf-devel >= 0.7.5
BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel >= 2.34.0
BuildRequires:  gobject-introspection-devel >= 0.9.6
BuildRequires:  gtk-doc >= 1.9
BuildRequires:  gtk2-devel
BuildRequires:  iso-codes-devel
BuildRequires:  libnotify-devel >= 0.7
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3-dbus-python-devel
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  unicode-ucd
BuildRequires:  update-desktop-files
# copy_deep method is supported since 0.31.1
BuildRequires:  vala >= 0.31.1
BuildRequires:  x11-tools
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  pkgconfig(xkbcommon)
Requires:       dconf
Requires:       iso-codes
Requires:       libibus-1_0-5 = %{version}
Requires:       python3-dbus-python
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
# ibus-setup will require typelib(Gdk) typelib(GdkX11), typelib(Gtk)
# which are provided by two packages in openSUSE, so we limit their
# versions to 3.0 only.
Requires:       typelib-1_0-Gtk-3_0
Recommends:     %{name}-lang
Provides:       locale(ja;ko;zh)
Obsoletes:      ibus-gnome-shell
%if %{with_kde}
BuildRequires:  libqt5-qtbase-devel
%endif
%if %{with_wayland}
BuildRequires:  pkgconfig(wayland-client) >= 1.2.0
%endif
%if %{with_emoji}
BuildRequires:  unicode-emoji
BuildRequires:  pkgconfig(cldr-emoji-annotation)
%endif
# PATCH-FEATURE-SLE FATE#319095 qzhao@suse.com
# Add conflict with fcitx to keep old IMF for people who update from SLE-12 SP0 to SP1.
%if !0%{?is_opensuse}
Conflicts:      fcitx
%endif

%description
IBus, short for Intelligent Input Bus, is an input framework. IBus
plugins then provide the particular logic how to translate keypresses
to input characters and possibly show disambiguation windows around
the text cursor.

%package -n libibus-1_0-5
Summary:        IBus libraries
Group:          System/Libraries
Obsoletes:      libibus-1_0-0

%description -n libibus-1_0-5
This package contains the libraries for IBus

%package -n typelib-1_0-IBus-1_0
Summary:        Introspection bindings for IBus
Group:          System/Libraries

%description -n typelib-1_0-IBus-1_0
This package contains the introspection bindings for the IBus library.

%package gtk
Summary:        IBus input method support for gtk2 applications
Group:          System/I18n/Chinese
Requires:       %{name} = %{version}
Supplements:    packageand(ibus:gtk2)
%{gtk2_immodule_requires}

%description gtk
This package contains ibus im module for use by gtk2.

%package gtk3
Summary:        IBus input method support for gtk3 applications
Group:          System/I18n/Chinese
BuildRequires:  gtk3-devel
Requires:       %{name} = %{version}
Supplements:    packageand(ibus:gtk3)
%{gtk3_immodule_requires}

%description gtk3
This package contains ibus im module for use by gtk3.

%package devel
Summary:        Development tools for ibus
Group:          Development/Libraries/Other
Requires:       dbus-1-devel
Requires:       glib2-devel
Requires:       gtk-doc
Requires:       ibus = %{version}
Requires:       libibus-1_0-5 = %{version}
Requires:       typelib-1_0-IBus-1_0 = %{version}

%description devel
The ibus-devel package contains the header files and developer
docs for ibus.

%lang_package

%prep
%setup -q
%patch0 -p1
%patch4 -p1
%patch8 -p1
%patch9 -p1

cp -r %{SOURCE2} .
cp -r %{SOURCE3} .
cp -r %{SOURCE4} .
sed -i 1i"SYS_LIB=%{_lib}" xim.d-ibus-121
cp -r %{SOURCE10} .
cp -r %{SOURCE11} .

%if !0%{?is_opensuse}
%patch10 -p1
%patch11 -p1
%patch12 -p1
%endif

%build
autoreconf -fi
%configure --disable-static \
           --enable-gtk3 \
           --enable-vala \
%if %{with_emoji}
           --enable-emoji-dict \
%else
           --disable-emoji-dict \
%endif
%if %{with_kde}
           --enable-appindicator \
%else
           --disable-appindicator \
%endif
           --with-python=python3 \
           --disable-python2 \
           --enable-python-library \
           --enable-introspection \
           --disable-gconf \
           --enable-dconf \
           --enable-gtk-doc \
%if %{with_wayland}
           --enable-wayland \
%endif
           --enable-surrounding-text \
           --enable-appindicator_engine_icon \
           --libexecdir=%{_libdir}/ibus

make %{?_smp_mflags}

%install
%make_install

# autostart
mkdir -p %{buildroot}%{_sysconfdir}/X11/xim.d/
install -m 644 xim.d-ibus-121 %{buildroot}%{_sysconfdir}/X11/xim.d/ibus
mkdir -p %{buildroot}%{_bindir}
install -c -m 0755 ibus-autostart %{buildroot}%{_bindir}/ibus-autostart
mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart
install -c -m 0644 ibus-autostart.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/ibus-autostart.desktop

PRIORITY=40
pushd %{buildroot}%{_sysconfdir}/X11/xim.d/
    for lang in am ar as bn el fa gu he hi hr ja ka kk kn ko lo ml my \
                pa ru sk vi zh_TW zh_CN zh_HK zh_SG \
                de fr it es nl cs pl da nn nb fi en sv
    do
        mkdir $lang
        pushd $lang
            ln -s ../ibus $PRIORITY-ibus
        popd
    done
popd

# remove static libs
find %{buildroot} -type f -name "*.la" -delete -print

mkdir -p %{buildroot}%{_datadir}/pixmaps
ln -sf %{_datadir}/icons/hicolor/48x48/apps/ibus-keyboard.png \
  %{buildroot}%{_datadir}/pixmaps/ibus-keyboard.png

# touch for %%ghost
touch %{buildroot}/%{_sysconfdir}/dconf/db/ibus

# install macros
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m 644 %{SOURCE7} %{buildroot}%{_rpmmacrodir}

%suse_update_desktop_file -r org.freedesktop.IBus.Setup Settings DesktopSettings X-SuSE-Core-System

%fdupes %{buildroot}

%find_lang ibus10 %{?no_lang_C}

%post
%glib2_gsettings_schema_post

%posttrans
dconf update

%postun
%glib2_gsettings_schema_postun
dconf update

%post gtk
%{gtk2_immodule_post}

%postun gtk
%{gtk2_immodule_postun}

%post -n libibus-1_0-5 -p /sbin/ldconfig
%postun -n libibus-1_0-5 -p /sbin/ldconfig
%post gtk3
%{gtk3_immodule_post}

%postun gtk3
%{gtk3_immodule_postun}

%files
%doc AUTHORS README README.SUSE xim.ibus.suse.template
%license COPYING
%{_rpmmacrodir}/macros.ibus
%config %{_sysconfdir}/X11/xim.d/*
%{_bindir}/ibus
%{_bindir}/ibus-autostart
%{_bindir}/ibus-daemon
%{_bindir}/ibus-setup
%{_datadir}/ibus/
%{_datadir}/applications/org.freedesktop.IBus.Setup.desktop
%{_datadir}/GConf/gsettings/ibus.convert
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.gschema.xml
%{_datadir}/icons/hicolor/*/apps/ibus*.*
%{_datadir}/pixmaps/ibus-keyboard.png
%{_libdir}/ibus
%{_datadir}/bash-completion/completions/ibus.bash
%{_datadir}/dbus-1/services/*.service
# This file is generated by dconf update
%ghost %{_sysconfdir}/dconf/db/ibus
%dir %{_sysconfdir}/dconf/db/ibus.d
# This file is not a config file. Users may not modify it.
%config %{_sysconfdir}/dconf/db/ibus.d/00-upstream-settings
%config %{_sysconfdir}/dconf/profile/ibus
%{_sysconfdir}/xdg/autostart/ibus-autostart.desktop
%{_mandir}/man1/ibus.1%{ext_man}
%{_mandir}/man1/ibus-daemon.1%{ext_man}
%{_mandir}/man1/ibus-setup.1%{ext_man}
%{_mandir}/man5/00-upstream-settings.5%{ext_man}
%{_mandir}/man5/ibus.5%{ext_man}

%if %{with_emoji}
%{_datadir}/applications/org.freedesktop.IBus.Panel.Emojier.desktop
%{_datadir}/applications/org.freedesktop.IBus.Panel.Extension.Gtk3.desktop
%{_mandir}/man7/ibus-emoji.7%{ext_man}
%endif
%{python3_sitearch}/gi/overrides/IBus.py
%{python3_sitearch}/gi/overrides/__pycache__/IBus.cpython-*.opt-1.pyc
%{python3_sitearch}/gi/overrides/__pycache__/IBus.cpython-*.pyc

%files lang -f ibus10.lang

%files -n libibus-1_0-5
%{_libdir}/libibus-1.0.so.*

%files -n typelib-1_0-IBus-1_0
%{_libdir}/girepository-1.0/IBus-1.0.typelib

%files gtk
%{_libdir}/gtk-2.0/*/immodules/im-ibus.so

%files gtk3
%{_libdir}/gtk-3.0/3.0.0/immodules/im-ibus.so

%files devel
%{_libdir}/libibus-1.0.so
%{_includedir}/ibus-1.0
%{_datadir}/gtk-doc/html/ibus
%{_libdir}/pkgconfig/ibus-1.0.pc
%{_datadir}/gir-1.0/IBus-1.0.gir
%{_datadir}/vala/vapi/ibus-1.0.deps
%{_datadir}/vala/vapi/ibus-1.0.vapi

%changelog
