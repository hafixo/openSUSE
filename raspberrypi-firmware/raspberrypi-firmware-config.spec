#
# spec file for package raspberrypi-firmware-config
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


Name:           raspberrypi-firmware-config
Version:        2019.07.09
Release:        0
Summary:        Configuration for the Raspberry Pi firmware loader
License:        MIT
Group:          System/Boot
Url:            https://github.com/raspberrypi/firmware/
Source:         config.txt
BuildRequires:  raspberrypi-firmware
Requires:       raspberrypi-firmware = %{version}
Conflicts:      kernel < 4.12.14
Conflicts:      otherproviders(raspberrypi-firmware-config)
Provides:       raspberrypi-firmware-branding-openSUSE = %{version}
Obsoletes:      raspberrypi-firmware-branding-openSUSE < %{version}
Provides:       raspberrypi-firmware-config = %{version}
BuildArch:      noarch
Provides:       raspberrypi-firmware-config-rpi = %{version}
Obsoletes:      raspberrypi-firmware-config-rpi < %{version}
Provides:       raspberrypi-firmware-config-rpi0w = %{version}
Obsoletes:      raspberrypi-firmware-config-rpi0w < %{version}
Provides:       raspberrypi-firmware-config-rpi2 = %{version}
Obsoletes:      raspberrypi-firmware-config-rpi2 < %{version}
Provides:       raspberrypi-firmware-config-rpi3 = %{version}
Obsoletes:      raspberrypi-firmware-config-rpi3 < %{version}

%description
This package configures the Raspberry Pi boot process.

Note: config.txt can be used to set some params (gpu_mem, etc.)

%prep

%build

%install
install -D -p -m 0644 %{SOURCE0} %{buildroot}/boot/vc/config.txt

%post
if mountpoint -q /boot/efi && [ ! -L /boot/efi ]; then
  [ -f /boot/efi/config.txt ] && cp /boot/efi/config.txt /boot/efi/config.txt.rpmsave
  cp /boot/vc/config.txt /boot/efi/config.txt
fi

%files
%defattr(-,root,root)
%config /boot/vc/config.txt

%changelog
