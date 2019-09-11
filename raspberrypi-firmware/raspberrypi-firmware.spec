#
# spec file for package raspberrypi-firmware
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


Name:           raspberrypi-firmware
Version:        2019.07.09
Release:        0
Summary:        Binary bootloader and firmware files for Raspberry Pi
License:        SUSE-Firmware
Group:          System/Boot
Url:            https://github.com/raspberrypi/firmware/
Source0:        raspberrypi-firmware-%{version}.tar.bz2
Source1:        get-from-git.sh
Source99:       %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires(post): util-linux
Requires(preun):util-linux
Recommends:     raspberrypi-firmware-dt
Recommends:     raspberrypi-firmware-config

%description
Binary bootloader and firmware files for Raspberry Pi

%package extra
Summary:        Extra bootloaders for Raspberry Pi
Group:          System/Boot
Requires:       raspberrypi-firmware = %{version}-%{release}
Requires(post): util-linux
Requires(preun):util-linux

%description extra
This package provides the console, experimental and debug
firmware files for Raspberry Pi

%package extra-pi4
Summary:        Extra bootloaders for Raspberry Pi
Group:          System/Boot
Requires:       raspberrypi-firmware = %{version}-%{release}
Requires(post): util-linux
Requires(preun):util-linux

%description extra-pi4
This package provides the console, experimental and debug
firmware files for Raspberry Pi 4

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/boot/vc
cp -a boot/*.elf boot/*.bin boot/*.dat boot/LICENCE.broadcom %{buildroot}/boot/vc

%post
if mountpoint -q /boot/efi && [[ ! -L /boot/efi ]]; then
  for f in start.elf start4.elf fixup.dat fixup4.dat bootcode.bin; do
    cp /boot/vc/$f /boot/efi/
  done
fi

%preun
if mountpoint -q /boot/efi && [[ ! -L /boot/efi ]]; then
  for f in start.elf start4.elf fixup.dat fixup4.dat bootcode.bin; do
    rm -f /boot/efi/$f
  done
fi

%post extra
if mountpoint -q /boot/efi && [[ ! -L /boot/efi ]]; then
  for suffix in _cd _db _x; do
    cp /boot/vc/start${suffix}.elf /boot/efi/
    cp /boot/vc/fixup${suffix}.dat /boot/efi/
  done
fi

%preun extra
if mountpoint -q /boot/efi && [[ ! -L /boot/efi ]]; then
  for suffix in _cd _db _x; do
    rm -f /boot/efi/start${suffix}.elf
    rm -f /boot/efi/fixup${suffix}.dat
  done
fi

%post extra-pi4
if mountpoint -q /boot/efi && [[ ! -L /boot/efi ]]; then
  for suffix in 4cd 4db 4x; do
    cp /boot/vc/start${suffix}.elf /boot/efi/
    cp /boot/vc/fixup${suffix}.dat /boot/efi/
  done
fi

%preun extra-pi4
if mountpoint -q /boot/efi && [[ ! -L /boot/efi ]]; then
  for suffix in 4cd 4db 4x; do
    rm -f /boot/efi/start${suffix}.elf
    rm -f /boot/efi/fixup${suffix}.dat
  done
fi

%files
%defattr(-,root,root)
%dir /boot/vc
/boot/vc/start.elf
/boot/vc/start4.elf
/boot/vc/fixup.dat
/boot/vc/fixup4.dat
/boot/vc/bootcode.bin
%doc /boot/vc/LICENCE.broadcom

%files extra
%defattr(-,root,root)
/boot/vc/start_cd.elf
/boot/vc/start_db.elf
/boot/vc/start_x.elf
/boot/vc/fixup_cd.dat
/boot/vc/fixup_db.dat
/boot/vc/fixup_x.dat

%files extra-pi4
%defattr(-,root,root)
/boot/vc/start4cd.elf
/boot/vc/start4db.elf
/boot/vc/start4x.elf
/boot/vc/fixup4cd.dat
/boot/vc/fixup4db.dat
/boot/vc/fixup4x.dat

%changelog
