#
# spec file for package gsequencer
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

%define libagssonumber 2
%define libgsequencersonumber 0
# The condition is run functional tests; defaulted off and needs to be
# activated with --with run_functional_tests command line switch.
%bcond_with run_functional_tests
Name:           gsequencer
Version:        2.2.36
Release:        0
Summary:        Audio processing engine
License:        GPL-3.0+ AND AGPL-3.0+ AND GFDL-1.3
Group:          Productivity/Multimedia/Sound/Midi
Url:            https://nongnu.org/gsequencer
Source0:        https://download.savannah.gnu.org/releases/gsequencer/2.2.x/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE gsequencer.0-fix-makefile-am.patch -- fix opensuse specific locations
Patch0:         gsequencer.0-fix-makefile-am.patch
BuildRequires:  fluid-soundfont-gm
BuildRequires:  hydrogen
BuildRequires:  cunit-devel
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  dssi-devel
BuildRequires:  gettext-devel >= 0.19.8
BuildRequires:  gtk-doc
BuildRequires:  ladspa-cmt
BuildRequires:  ladspa-devel
BuildRequires:  libtool
BuildRequires:  lv2-devel
BuildRequires:  lv2-swh-plugins
BuildRequires:  pkgconfig
BuildRequires:  xvfb-run
BuildRequires:  pulseaudio
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libinstpatch-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(uuid)

%description
Advanced Gtk+ Sequencer is an audio
sequencer application supporting the LADPSA, DSSI and Lv2 plugin
formats. It can output to Pulseaudio server, JACK and ALSA.

You may add multiple sinks, mix different sources by producing
sound with different sequencers. Furthermore, it features a pattern
and piano roll and there is an editor to automate ports.

%prep
%setup -q
%patch0

%build
autoreconf -fi
export CPPFLAGS='-std=gnu99 -include errno.h -DAGS_RC_FILENAME=\"'%{_datadir}'/gsequencer/styles/ags.rc\" -DAGS_ANIMATION_FILENAME=\"'%{_datadir}'/gsequencer/images/ags_supermoon-800x450.png\" -DAGS_LOGO_FILENAME=\"'%{_datadir}'/gsequencer/images/ags.png\" -DAGS_LICENSE_FILENAME=\"'%{_datadir}'/licenses/gsequencer/COPYING\" -DAGS_REDUCE_RT_EVENTS=1 -DAGS_LIBRARY_SUFFIX=\".so\" -D_FORTIFY_SOURCE=2 -Wformat -Werror=format-security -DAGS_WITH_LIBINSTPATCH=1'
%configure \
%if %{with run_functional_tests}
    --enable-run-functional-tests \ 
%endif
    --disable-oss --enable-gtk-doc --enable-gtk-doc-html

%make_build all
%make_build html

%install
%make_install
%make_install install-html
find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}%{_datadir}/doc-base/
mkdir -p %{buildroot}%{_datadir}/doc/packages
mv %{buildroot}%{_datadir}/doc/gsequencer  %{buildroot}%{_docdir}

%check
xvfb-run --server-args="-screen 0 1920x1080x24" -a make check
desktop-file-validate %{buildroot}/%{_datadir}/applications/gsequencer.desktop

%files
%license COPYING
%{_bindir}/gsequencer
%{_bindir}/midi2xml
%{_mandir}/man1/gsequencer.1*
%{_mandir}/man1/midi2xml.1*
%{_datadir}/gsequencer/
%{_datadir}/xml/gsequencer/
%{_docdir}/gsequencer/
%{_datadir}/applications/gsequencer.desktop
%{_datadir}/icons/hicolor/*/apps/gsequencer.png
%{_datadir}/metainfo/
%{_datadir}/mime/packages/

%package -n libags%{libagssonumber}
Summary:        GSequencer core libraries
Group:          System/Libraries

%description -n libags%{libagssonumber}
Advanced Gtk+ Sequencer is an audio sequencer application.
This subpackage contains part of its library set.

%package -n libgsequencer%{libgsequencersonumber}
Summary:        GSequencer core libraries
Group:          System/Libraries

%description -n libgsequencer%{libgsequencersonumber}
Advanced Gtk+ Sequencer is an audio sequencer application.
This subpackage contains part of its library set.

%package devel
Summary:        Advanced Gtk+ Sequencer library development files
Group:          Development/Libraries/C and C++
Requires:       libags%{libagssonumber} = %{version}
Requires:       libgsequencer%{libgsequencersonumber} = %{version}

%description devel
Advanced Gtk+ Sequencer library development files.

%files devel
%{_includedir}/ags/
%{_libdir}/libags.so
%{_libdir}/libags_thread.so
%{_libdir}/libags_server.so
%{_libdir}/libags_gui.so
%{_libdir}/libags_audio.so
%{_libdir}/libgsequencer.so
%{_libdir}/pkgconfig/libags.pc
%{_libdir}/pkgconfig/libags_audio.pc
%{_libdir}/pkgconfig/libags_gui.pc
%{_libdir}/pkgconfig/libgsequencer.pc

%package -n gsequencer-devel-doc
Summary:        Documentation for Advanced Gtk+ Sequencer
Group:          Documentation/HTML
BuildArch:      noarch

%description -n gsequencer-devel-doc
Advanced Gtk+ Sequencer library development documentation.

%post   -n libags%{libagssonumber} -p /sbin/ldconfig
%postun -n libags%{libagssonumber} -p /sbin/ldconfig
%post   -n libgsequencer%{libgsequencersonumber} -p /sbin/ldconfig
%postun -n libgsequencer%{libgsequencersonumber} -p /sbin/ldconfig

%files -n libags%{libagssonumber}
%defattr(-,root,root)
%{_libdir}/libags.so.%{libagssonumber}*
%{_libdir}/libags_thread.so.%{libagssonumber}*
%{_libdir}/libags_server.so.%{libagssonumber}*
%{_libdir}/libags_gui.so.%{libagssonumber}*
%{_libdir}/libags_audio.so.%{libagssonumber}*

%files -n libgsequencer%{libgsequencersonumber}
%defattr(-,root,root)
%{_libdir}/libgsequencer.so.%{libgsequencersonumber}*

%files -n gsequencer-devel-doc
%{_datadir}/gtk-doc/
%{_datadir}/doc/libags-audio-doc/

%changelog
