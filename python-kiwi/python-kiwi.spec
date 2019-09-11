#
# spec file for package kiwi
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via:
#
#       https://github.com/SUSE/kiwi/issues
#

# If they aren't provided by a system installed macro, define them
%{!?_defaultdocdir: %global _defaultdocdir %{_datadir}/doc}
%{!?__python3: %global __python3 /usr/bin/python3}

%if %{undefined python3_sitelib}
%global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
%endif

%if 0%{?el7}
%global python3_pkgversion 36
%else
%{!?python3_pkgversion:%global python3_pkgversion 3}
%endif

%if 0%{?debian} || 0%{?ubuntu}
%global is_deb 1
%global pygroup python
%global sysgroup admin
%global develsuffix dev
%else
%global pygroup Development/Languages/Python
%global sysgroup System/Management
%global develsuffix devel
%endif

Name:           python-kiwi
Version:        9.18.10
Provides:       kiwi-schema = 7.1
Release:        0
Url:            https://github.com/SUSE/kiwi
Summary:        KIWI - Appliance Builder Next Generation
License:        GPL-3.0-or-later
%if %{_vendor} == "debbuild"
# Needed to set Maintainer in output debs
Packager:       Marcus Schaefer <ms@suse.de>
%endif
Group:          %{pygroup}
Source:         %{name}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc
BuildRequires:  python%{python3_pkgversion}-%{develsuffix}
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  fdupes
%if 0%{?suse_version}
BuildRequires:  shadow
%endif
%if 0%{?debian} || 0%{?ubuntu}
BuildRequires:  passwd
%endif
%if 0%{?fedora} || 0%{?rhel}
BuildRequires:  chkconfig
%endif

%description
The KIWI Image System provides an operating system image builder
for Linux supported hardware platforms as well as for virtualization
and cloud systems like Xen, KVM, VMware, EC2 and more.

# python3-kiwi
%package -n python%{python3_pkgversion}-kiwi
Summary:        KIWI - Appliance Builder Next Generation
Group:          Development/Languages/Python
%if 0%{?fedora} || 0%{?rhel} >= 8 || 0%{?suse_version} || 0%{?debian} || 0%{?ubuntu}
Recommends:     jing
%endif
%if 0%{?ubuntu} || 0%{?debian}
Requires:       python%{python3_pkgversion}-yaml
%else
Requires:       python%{python3_pkgversion}-PyYAML
%endif
Requires:       python%{python3_pkgversion}-docopt
Requires:       python%{python3_pkgversion}-lxml
Requires:       python%{python3_pkgversion}-requests
Requires:       python%{python3_pkgversion}-setuptools
%if (0%{?suse_version} && 0%{?suse_version} < 1550)
Requires:       python%{python3_pkgversion}-xattr
%else
Requires:       python%{python3_pkgversion}-pyxattr
%endif
# tools used by kiwi
%if 0%{?suse_version}
%ifarch x86_64
Requires:       grub2-x86_64-efi
%endif
%ifarch %{ix86} x86_64
Recommends:     gfxboot
%endif
Requires:       qemu-tools
Requires:       squashfs
Requires:       gptfdisk
%endif
%if 0%{?fedora} || 0%{?rhel}
Requires:         chkconfig
Requires(post):   chkconfig
Requires(postun): chkconfig
Requires:       qemu-img
Requires:       squashfs-tools
Requires:       gdisk
Requires:       dnf
Provides:       kiwi-packagemanager:dnf
Provides:       kiwi-packagemanager:yum
%endif
%if 0%{?suse_version}
# If it's available, let's pull it in
Recommends:     dnf
%endif
%if 0%{?fedora} >= 26 || 0%{?suse_version}
Requires:       zypper
Provides:       kiwi-packagemanager:zypper
%endif
%if 0%{?debian} || 0%{?ubuntu}
Requires:       debootstrap
Requires:       qemu-utils
Requires:       squashfs-tools
Requires:       gdisk
%endif
Requires:       dosfstools
Requires:       e2fsprogs
Requires:       xorriso
Requires:       grub2
Requires:       kiwi-man-pages
Requires:       kiwi-tools
Requires:       lvm2
Requires:       mtools
Requires:       parted
Requires:       kpartx
Requires:       rsync
Requires:       tar >= 1.2.7
%ifarch %arm aarch64
%if 0%{?fedora} || 0%{?rhel}
Requires:       uboot-tools
%endif
%if 0%{?suse_version}
Requires:       u-boot-tools
%endif
%endif
%ifarch s390 s390x
Requires:       s390-tools
%endif

%description -n python%{python3_pkgversion}-kiwi
Python 3 library of the KIWI Image System. Provides an operating system
image builder for Linux supported hardware platforms as well as for
virtualization and cloud systems like Xen, KVM, VMware, EC2 and more.

%package -n kiwi-tools
Summary:        KIWI - Collection of Boot Helper Tools
License:        GPL-3.0-or-later
Group:          %{sysgroup}

%description -n kiwi-tools
This package contains a small set of helper tools used for the
kiwi created initial ramdisk which is used to control the very
first boot of an appliance. The tools are not meant to be used
outside of the scope of kiwi appliance building.

%if %{_vendor} != "debbuild"
%ifarch %{ix86} x86_64
%package -n kiwi-pxeboot
Summary:        KIWI - PXE boot structure
Requires:       syslinux
%if 0%{?fedora} || 0%{?rhel}
Requires(pre):  shadow-utils
%else
Requires(pre):  shadow
%endif
License:        GPL-3.0-or-later
Group:          %{sysgroup}

%description -n kiwi-pxeboot
This package contains the basic PXE directory structure which is
needed to serve kiwi built images via PXE.
%endif
%endif

%package -n dracut-kiwi-lib
Summary:        KIWI - Dracut kiwi Library
%if 0%{?fedora} || 0%{?rhel} || 0%{?suse_version} || 0%{?debian}
# Ubuntu 16.04 OBS environments refuse to set up due to
# initramfs-tools / dracut conflict and initramfs-tools is required
# to set up the build environment...
BuildRequires:  dracut
%endif
Requires:       bc
Requires:       cryptsetup
%if 0%{?fedora} || 0%{?rhel} || 0%{?ubuntu} >= 1804 || 0%{?debian} >= 9
Requires:       btrfs-progs
Requires:       gdisk
Requires:       dracut-network
%else
%if 0%{?debian} || 0%{?ubuntu}
Requires:       btrfs-tools
Requires:       gdisk
%else
Requires:       btrfsprogs
Requires:       gptfdisk
%endif
%endif
Requires:       coreutils
Requires:       e2fsprogs
Requires:       grep
Requires:       lvm2
Requires:       mdadm
Requires:       parted
Requires:       util-linux
Requires:       xfsprogs
Requires:       dialog
Requires:       pv
Requires:       curl
%if 0%{?debian} || 0%{?ubuntu}
Requires:       xz-utils
Requires:       dmsetup
%else
Requires:       xz
Requires:       device-mapper
%endif
%ifarch s390 s390x
Requires:       s390-tools
%endif
License:        GPL-3.0-or-later
Group:          %{sysgroup}

%description -n dracut-kiwi-lib
This package contains a collection of methods to provide a library
for tasks done in other kiwi dracut modules

%package -n dracut-kiwi-oem-repart
Summary:        KIWI - Dracut module for oem(repart) image type
%if 0%{?fedora} || 0%{?rhel} || 0%{?suse_version} || 0%{?debian}
# Ubuntu 16.04 OBS environments refuse to set up due to
# initramfs-tools / dracut conflict and initramfs-tools is required
# to set up the build environment...
BuildRequires:  dracut
%endif
Requires:       dracut-kiwi-lib
License:        GPL-3.0-or-later
Group:          %{sysgroup}

%description -n dracut-kiwi-oem-repart
This package contains the kiwi-repart dracut module which is
used to repartition the oem disk image to the current disk
geometry according to the setup in the kiwi image configuration

%package -n dracut-kiwi-oem-dump
Summary:        KIWI - Dracut module for oem(install) image type
%if 0%{?fedora} || 0%{?rhel} || 0%{?suse_version} || 0%{?debian}
# Ubuntu 16.04 OBS environments refuse to set up due to
# initramfs-tools / dracut conflict and initramfs-tools is required
# to set up the build environment...
BuildRequires:  dracut
%endif
Requires:       dracut-kiwi-lib
Requires:       kexec-tools
%if 0%{?suse_version} || 0%{?debian} || 0%{?ubuntu}
Requires:       multipath-tools
%endif
%if 0%{?fedora} || 0%{?rhel}
Requires:       device-mapper-multipath
%endif
Requires:       gawk
License:        GPL-3.0-or-later
Group:          %{sysgroup}

%description -n dracut-kiwi-oem-dump
This package contains the kiwi-dump dracut module which is
used to install an oem image onto a target disk. It implements
a simple installer which allows for user selected target disk
or unattended installation to target. The source of the image
to install could be either from media(CD/DVD/USB) or from
remote

%package -n dracut-kiwi-live
Summary:        KIWI - Dracut module for iso(live) image type
%if 0%{?fedora} || 0%{?rhel} || 0%{?suse_version} || 0%{?debian}
# Ubuntu 16.04 OBS environments refuse to set up due to
# initramfs-tools / dracut conflict and initramfs-tools is required
# to set up the build environment...
BuildRequires:  dracut
%endif
Requires:       dialog
Requires:       xfsprogs
Requires:       e2fsprogs
Requires:       util-linux
%if 0%{?debian} || 0%{?ubuntu}
Requires:       dmsetup
Requires:       dracut-network
%endif
%if 0%{?fedora} || 0%{?rhel}
Requires:       device-mapper
Requires:       dracut-network
%endif
%if 0%{?suse_version}
Requires:       device-mapper
%endif
Requires:       dracut
Requires:       xorriso
Requires:       parted
License:        GPL-3.0-or-later
Group:          %{sysgroup}

%description -n dracut-kiwi-live
This package contains the kiwi-live dracut module which is used
for booting iso(live) images built with KIWI

%package -n dracut-kiwi-overlay
Summary:        KIWI - Dracut module for vmx(+overlay) image type
%if 0%{?fedora} || 0%{?rhel} || 0%{?suse_version} || 0%{?debian}
# Ubuntu 16.04 OBS environments refuse to set up due to
# initramfs-tools / dracut conflict and initramfs-tools is required
# to set up the build environment...
BuildRequires:  dracut
%endif
Requires:       util-linux
Requires:       dracut
License:        GPL-3.0-or-later
Group:          %{sysgroup}

%description -n dracut-kiwi-overlay
This package contains the kiwi-overlay dracut module which is used
for booting vmx images built with KIWI and configured to use an
overlay root filesystem

%package -n kiwi-man-pages
Summary:        KIWI - manual pages
License:        GPL-3.0-or-later
Group:          %{sysgroup}

%description -n kiwi-man-pages
Provides manual pages to describe the kiwi commands

%prep
%setup -q -n kiwi-%{version}

# Drop shebang for kiwi/xml_parse.py, as we don't intend to use it
# as an independent script
sed -e "s|#!/usr/bin/env python||" -i kiwi/xml_parse.py

%if 0%{?suse_version} && 0%{?suse_version} < 1550
# For older SUSE distributions, use the other xattr Python module
sed -e "s|pyxattr|xattr|" -i setup.py
%endif

%build
# Build Python 3 version
python3 setup.py build --cflags="${RPM_OPT_FLAGS}"

%install
# Install Python 3 version
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot} %{?is_deb:--install-layout=deb}

# Install dracut modules
make buildroot=%{buildroot}/ install_dracut

# Install documentation in PDF format
make buildroot=%{buildroot}/ docdir=%{_defaultdocdir}/ install_package_docs

# Create symlinks for correct binaries
ln -sr %{buildroot}%{_bindir}/kiwi-ng %{buildroot}%{_bindir}/kiwi
ln -sr %{buildroot}%{_bindir}/kiwi-ng-3 %{buildroot}%{_bindir}/kiwi-ng
ln -sr %{buildroot}%{_bindir}/kiwicompat-3 %{buildroot}%{_bindir}/kiwicompat

%if %{_vendor} != "debbuild"
# kiwi pxeboot directory structure to be packed in kiwi-pxeboot
%ifarch %{ix86} x86_64
for i in KIWI pxelinux.cfg image upload boot; do \
    mkdir -p %{buildroot}/srv/tftpboot/$i ;\
done
%endif
%endif

%if 0%{?fedora} || 0%{?suse_version}
%fdupes %{buildroot}/srv/tftpboot
%endif

%if %{_vendor} != "debbuild"
%ifarch %{ix86} x86_64
%pre -n kiwi-pxeboot
#============================================================
# create user and group tftp if they does not exist
if ! /usr/bin/getent group tftp >/dev/null; then
    %{_sbindir}/groupadd -r tftp
fi
if ! /usr/bin/getent passwd tftp >/dev/null; then
    %{_sbindir}/useradd -c "TFTP account" -d /srv/tftpboot -G tftp -g tftp \
        -r -s /bin/false tftp
fi
%endif
%endif

%files -n python%{python3_pkgversion}-kiwi
%{_bindir}/kiwi
%{_bindir}/kiwi-ng
%{_bindir}/kiwicompat
%{_bindir}/kiwi-ng-3*
%{_bindir}/kiwicompat-3*
%{python3_sitelib}/kiwi*

%files -n kiwi-man-pages
%dir %{_defaultdocdir}/python-kiwi
%{_defaultdocdir}/python-kiwi/kiwi.pdf
%{_defaultdocdir}/python-kiwi/LICENSE
%{_defaultdocdir}/python-kiwi/README
%config %_sysconfdir/bash_completion.d/kiwi-ng.sh
%doc %{_mandir}/man8/*

%files -n kiwi-tools
%{_bindir}/dcounter
%{_bindir}/isconsole
%{_bindir}/kversion
%{_bindir}/utimer

%files -n dracut-kiwi-lib
%{_usr}/lib/dracut/modules.d/99kiwi-lib

%files -n dracut-kiwi-oem-repart
%{_usr}/lib/dracut/modules.d/90kiwi-repart

%files -n dracut-kiwi-oem-dump
%{_usr}/lib/dracut/modules.d/90kiwi-dump

%files -n dracut-kiwi-live
%{_usr}/lib/dracut/modules.d/90kiwi-live

%files -n dracut-kiwi-overlay
%{_usr}/lib/dracut/modules.d/90kiwi-overlay

%if %{_vendor} != "debbuild"
%ifarch %{ix86} x86_64
%files -n kiwi-pxeboot
%dir %attr(0755,tftp,tftp) /srv/tftpboot
%dir /srv/tftpboot/KIWI
%dir /srv/tftpboot/pxelinux.cfg
%dir /srv/tftpboot/image
%dir /srv/tftpboot/upload
%dir /srv/tftpboot/boot
%endif
%endif

%changelog
