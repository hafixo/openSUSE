#
# spec file for package bcm20702a1-firmware
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


Name:           bcm20702a1-firmware
Version:        1201650
Release:        0
Summary:        Firmware for BCM20702A1 based devices
License:        MIT
Group:          Hardware/Wifi
Url:            https://www.asus.com/Networking/USBBT400/
BuildRequires:  kernel-firmware
Requires:       kernel-firmware
Requires(post): bluez
Requires(post): coreutils
Requires(post): unzip
Requires(post): wget
# Expand with more hardware if found
Supplements:    modalias(usb:v0A5Cp21E6d0112dcFFdsc01dp01icFFisc*ip*in*)
# Another variant: bsc#1087996
Supplements:    modalias(usb:v0A5Cp21E6d*dcFFdsc01dp01icFFisc*ip*in*)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Firmware for broadcom BCM20702A1 based devices present in various sticks and
laptops always over usb bridge.

%prep
:

%build
:

%install
:

%post
OUT="$(mktemp -d)"
cd "$OUT"
wget -q http://dlcdnet.asus.com/pub/ASUS/misc/BT/Bluetooth_V%{version}_WHQL_Win10.zip || :
if [ ! -f Bluetooth_V%{version}_WHQL_Win10.zip ]; then
    echo "Fatal error in obtaining the Windows bluetooth driver: Bluetooth_V%{version}_WHQL_Win10.zip"
else
    unzip Bluetooth_V%{version}_WHQL_Win10.zip
    cd Bluetooth
    hex2hcd BCM_DriverOnly/64/BCM20702A1_001.002.014.1443.1467.hex \
        -o BCM20702A1-0b05-17cb.hcd
    hex2hcd BCM_DriverOnly/64/BCM20702A1_001.002.014.1443.1469.hex \
        -o BCM20702A1-0b05-17cf.hcd
    hex2hcd BCM_DriverOnly/64/BCM20702A1_001.002.014.1483.1647.hex \
        -o BCM20702A1-05ac-21e1.hcd
    hex2hcd BCM_DriverOnly/64/BCM20702A1_001.002.014.1483.1669.hex \
        -o BCM20702A1-0a5c-21e6.hcd
    mkdir -p /lib/firmware/brcm/
    install -m644 BCM20702A1-0b05-17cb.hcd /lib/firmware/brcm/BCM20702A1-0b05-17cb.hcd
    install -m644 BCM20702A1-0b05-17cf.hcd /lib/firmware/brcm/BCM20702A1-0b05-17cf.hcd
    install -m644 BCM20702A1-05ac-21e1.hcd /lib/firmware/brcm/BCM20702A1-05ac-21e1.hcd
    install -m644 BCM20702A1-0a5c-21e6.hcd /lib/firmware/brcm/BCM20702A1-0a5c-21e6.hcd
fi
# Another variant: bsc#1087996
wget -q https://s3.amazonaws.com/plugable/bin/fw-0a5c_21e8.hcd || :
if [ ! -f fw-0a5c_21e8.hcd ]; then
    echo "Fatal error in obtaining the 0a5c:21e8 BT firmware"
else
    install -m644 fw-0a5c_21e8.hcd /lib/firmware/brcm/BCM20702A1-0a5c-21e8.hcd
fi
rm -rf "$OUT"
exit 0

%postun
rm -f /lib/firmware/brcm/BCM20702A1-0b05-17cb.hcd
rm -f /lib/firmware/brcm/BCM20702A1-0b05-17cf.hcd
rm -f /lib/firmware/brcm/BCM20702A1-05ac-21e1.hcd
rm -f /lib/firmware/brcm/BCM20702A1-0a5c-21e6.hcd
rm -f /lib/firmware/brcm/BCM20702A1-0a5c-21e8.hcd
exit 0

%files
%defattr(-,root,root)
%ghost /lib/firmware/brcm/BCM20702A1-0b05-17cb.hcd
%ghost /lib/firmware/brcm/BCM20702A1-0b05-17cf.hcd
%ghost /lib/firmware/brcm/BCM20702A1-05ac-21e1.hcd
%ghost /lib/firmware/brcm/BCM20702A1-0a5c-21e6.hcd
%ghost /lib/firmware/brcm/BCM20702A1-0a5c-21e8.hcd

%changelog
