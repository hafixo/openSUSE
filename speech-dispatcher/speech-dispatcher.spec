#
# spec file for package speech-dispatcher
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


%if 0%{?suse_version} >= 1500
%define espeak    espeak-ng
%define espeakdev espeak-ng-devel
%else
%define espeak    espeak
%define espeakdev espeak-devel
%endif
Name:           speech-dispatcher
Version:        0.9.0
Release:        0
# FIXME missing backends: festival lite, ibmeci (ibm tts), dumbtts/ivona, nas
# Almost all files are under GPLv2+, however src/c/clients/spdsend/spdsend.h is
# licensed under GPLv2, which makes %%{_bindir}/spdsend GPLv2.
Summary:        Device independent layer for speech synthesis
License:        GPL-2.0-or-later
Group:          System/Daemons
URL:            https://devel.freebsoft.org/speechd
Source0:        https://download-mirror.savannah.gnu.org/releases/speechd/%{name}-%{version}.tar.gz
# Logrotate file taken from Debian
Source2:        speech-dispatcher.logrotate
Source99:       baselibs.conf
BuildRequires:  %{espeakdev}
BuildRequires:  alsa-devel
BuildRequires:  dotconf-devel
BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  libao-devel
BuildRequires:  libpulse-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtool
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros
BuildRequires:  texinfo
Requires:       python3-speechd
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         %{install_info_prereq}
Recommends:     %{espeak}
Recommends:     speech-dispatcherd-module-espeak
Suggests:       festival
Suggests:       logrotate
Provides:       speechd = %{version}
Obsoletes:      speechd < %{version}
# In 12.1, with GNOME 3, gnome-speech is completely deprecated and
# speech-dispatcher replaces it. We don't have a Provides since this is
# really just about obsoleting at technology, not providing it.
Obsoletes:      gnome-speech <= 0.4.25
%{?systemd_ordering}

%description
The goal of Speech Dispatcher project is to provide a high-level device
independent layer for speech synthesis through a simple, stable and
well documented interface.

What is a very high level GUI library to graphics, Speech Dispatcher is
to speech synthesis. The application neither needs to talk to the
devices directly nor to handle concurrent access, sound output and other
tricky aspects of the speech subsystem.

%package configure
Summary:        Configuration tool for Speech Dispatcher
Group:          System/Daemons
Requires:       %{name} = %{version}
Requires:       python3-xdg
Enhances:       %{name}

%description configure
The goal of Speech Dispatcher project is to provide a high-level device
independent layer for speech synthesis through a simple, stable and
well documented interface.

What is a very high level GUI library to graphics, Speech Dispatcher is
to speech synthesis. The application neither needs to talk to the
devices directly nor to handle concurrent access, sound output and other
tricky aspects of the speech subsystem.

This package contains spd-conf, a configuration tool for Speech
Dispatcher.

%package module-espeak
Summary:        ESpeak module for Speech Dispatcher
Group:          System/Daemons
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:%{espeak})

%description module-espeak
The goal of Speech Dispatcher project is to provide a high-level device
independent layer for speech synthesis through a simple, stable and
well documented interface.

What is a very high level GUI library to graphics, Speech Dispatcher is
to speech synthesis. The application neither needs to talk to the
devices directly nor to handle concurrent access, sound output and other
tricky aspects of the speech subsystem.

This package contains the espeak module.

%package -n libspeechd2
Summary:        Device independent layer for speech synthesis - Client library
Group:          System/Libraries
Recommends:     %{name}

%description -n libspeechd2
The goal of Speech Dispatcher project is to provide a high-level device
independent layer for speech synthesis through a simple, stable and
well documented interface.

What is a very high level GUI library to graphics, Speech Dispatcher is
to speech synthesis. The application neither needs to talk to the
devices directly nor to handle concurrent access, sound output and other
tricky aspects of the speech subsystem.

%package -n libspeechd-devel
Summary:        Device independent layer for speech synthesis - Development files
Group:          Development/Languages/C and C++
Requires:       libspeechd2 = %{version}
Provides:       %{name}-devel = %{version}
Provides:       speechd-devel = %{version}
Obsoletes:      speechd-devel < %{version}

%description -n libspeechd-devel
The goal of Speech Dispatcher project is to provide a high-level device
independent layer for speech synthesis through a simple, stable and
well documented interface.

What is a very high level GUI library to graphics, Speech Dispatcher is
to speech synthesis. The application neither needs to talk to the
devices directly nor to handle concurrent access, sound output and other
tricky aspects of the speech subsystem.

%package -n python3-speechd
Summary:        Device independent layer for speech synthesis - Python Bindings
Group:          Development/Libraries/Python
Requires:       %{name} >= %{version}

%description -n python3-speechd
The goal of Speech Dispatcher project is to provide a high-level device
independent layer for speech synthesis through a simple, stable and
well documented interface.

What is a very high level GUI library to graphics, Speech Dispatcher is
to speech synthesis. The application neither needs to talk to the
devices directly nor to handle concurrent access, sound output and other
tricky aspects of the speech subsystem.

%prep
%setup -q
# dummy module must almost never be dissabled
sed -i "s/#AddModule \"dummy\"/AddModule \"dummy\"/" -i config/speechd.conf
# you must enable at least one module (except dummy), otherwise it will load
# all available modules and may cause huge cpu usage!
sed -i "s/#AddModule \"%{espeak}\"/AddModule \"%{espeak}\"/" -i config/speechd.conf

%build
%configure --disable-static \
        --with-libao \
        --with-alsa \
        --with-pulse \
        --without-baratinoo \
        --without-flite \
        --without-kali
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcspeech-dispatcherd
# Create log dir. 0700 since the logs can contain user information.
install -d -m 0700 %{buildroot}%{_localstatedir}/log/speech-dispatcher/
# Install logrotate script
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/speech-dispatcher
# Remove config files for modules we don't support
rm %{buildroot}%{_sysconfdir}/speech-dispatcher/modules/flite.conf
rm %{buildroot}%{_sysconfdir}/speech-dispatcher/modules/ibmtts.conf
rm %{buildroot}%{_sysconfdir}/speech-dispatcher/modules/ivona.conf
# Remove config files that we don't need a second time
# but then user can not create its own configuration, because here is default, while in /etc is system-wide
# %{__rm} -r %{buildroot}%{_datadir}/speech-dispatcher/conf/
# Remove %{_infodir}/dir file
rm %{buildroot}%{_infodir}/dir
%find_lang %{name}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/spd-say.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/ssip.info.gz
%service_add_post speech-dispatcherd.service

%pre
%service_add_pre speech-dispatcherd.service

%preun
%service_del_preun speech-dispatcherd.service

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/spd-say.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/ssip.info.gz
%service_del_postun speech-dispatcherd.service

%post -n libspeechd2 -p /sbin/ldconfig

%postun -n libspeechd2 -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ANNOUNCE NEWS README.md
%license COPYING.LGPL
%dir %{_sysconfdir}/speech-dispatcher/
%dir %{_sysconfdir}/speech-dispatcher/clients
%dir %{_sysconfdir}/speech-dispatcher/modules
%config(noreplace) %{_sysconfdir}/speech-dispatcher/speechd.conf
%config(noreplace) %{_sysconfdir}/speech-dispatcher/clients/*.conf
%config(noreplace) %{_sysconfdir}/speech-dispatcher/modules/*.conf
%exclude %{_sysconfdir}/speech-dispatcher/modules/espeak.conf
%{_bindir}/*
%exclude %{_bindir}/spd-conf
%{_datadir}/sounds/speech-dispatcher/
%dir %{_libdir}/speech-dispatcher
%{_libdir}/speech-dispatcher/spd_*.so
# When adding a module, also stop removing its config file in %install
%dir %{_libdir}/speech-dispatcher-modules
%{_libdir}/speech-dispatcher-modules/sd_cicero
%{_libdir}/speech-dispatcher-modules/sd_dummy
%{_libdir}/speech-dispatcher-modules/sd_festival
%{_libdir}/speech-dispatcher-modules/sd_generic
%{_infodir}/%{name}*.info.gz
%{_infodir}/spd-say.info.gz
%{_infodir}/ssip.info.gz
# logs
%dir %attr(0700, root, root) %{_localstatedir}/log/speech-dispatcher/
%config(noreplace) %{_sysconfdir}/logrotate.d/speech-dispatcher
# systemd service file
%{_unitdir}/speech-dispatcherd.service
%{_sbindir}/rcspeech-dispatcherd

%files configure
%defattr(-,root,root,-)
%{_bindir}/spd-conf
%{python3_sitearch}/speechd_config/
%{_datadir}/speech-dispatcher/

%files module-espeak
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/speech-dispatcher/modules/espeak.conf
%{_libdir}/speech-dispatcher-modules/sd_%{espeak}

%files -n libspeechd2
%defattr(-,root,root,-)
%{_libdir}/libspeechd.so.*

%files -n libspeechd-devel
%defattr(-,root,root,-)
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n python3-speechd
%defattr(-,root,root,-)
%{python3_sitearch}/speechd/

%changelog
