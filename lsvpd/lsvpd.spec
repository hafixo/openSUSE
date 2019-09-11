#
# spec file for package lsvpd
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           lsvpd
Version:        1.7.9
Release:        0
Summary:        VPD Hardware Inventory Utilities for Linux
License:        GPL-2.0+
Group:          System/Monitoring
Url:            http://sourceforge.net/projects/linux-diag/
Source0:        http://sourceforge.net/projects/linux-diag/files/lsvpd-new/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  librtas-devel
BuildRequires:  libvpd2-devel
BuildRequires:  sg3_utils-devel
BuildRequires:  zlib-devel
Requires:       /bin/sed
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  ppc ppc64 ppc64le

%description
The lsvpd package contains both the lsvpd, lscfg and lsmcode commands.
These commands, along with a boot-time scanning script called
update-device-tree, constitute a simple hardware inventory system. The
lsvpd command provides Vital Product Data (VPD) about hardware
components to higher-level serviceability tools. The lscfg command
provides a more human-readable format of the VPD, as well as some
system-specific information.  lsmcode lists microcode and firmware
levels.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -UPCI_IDS -DPCI_IDS='\"%{_datadir}/pci.ids\"' -UUSB_IDS -DUSB_IDS='\"%{_datadir}/usb.ids\"'"
export CXXFLAGS="%{optflags} -UPCI_IDS -DPCI_IDS='\"%{_datadir}/pci.ids\"' -UUSB_IDS -DUSB_IDS='\"%{_datadir}/usb.ids\"'"
%configure
make %{?_smp_mflags}
chmod 644 README* COPYING NEWS

%install
%make_install
mkdir %{buildroot}/sbin
for i in lscfg lsmcode lsvio lsvpd update-lsvpd-db
do
 if test -f %{buildroot}%{_sbindir}/$i
 then
   ln -sfvbn ..%{_sbindir}/$i %{buildroot}/sbin/$i
 fi
done
if [ -e %{_sysconfdir}/udev/rules.d/99-lsvpd.rules ] ; then
	rm %{_sysconfdir}/udev/rules.d/99-lsvpd.rules
fi
if [ -e %{_sysconfdir}/udev/rules.d/99-lsvpd.disabled ] ; then
	rm %{_sysconfdir}/udev/rules.d/99-lsvpd.disabled
fi

%post
if [ -d %{_localstatedir}/lib/lsvpd ] ; then
  rm -rf %{_localstatedir}/lib/lsvpd
fi
%{_sbindir}/vpdupdate
exit 0

%files
%defattr(-,root,root)
%doc README COPYING NEWS
%dir %{_sysconfdir}/lsvpd
%attr (644,root,root) %config %{_sysconfdir}/lsvpd/*
/sbin/*
%attr (755,root,root) %{_sbindir}/*
%{_mandir}/*/*

%changelog
