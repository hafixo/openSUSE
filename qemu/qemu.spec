#
# spec file for package qemu
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


%define build_in_tree 1
%define build_x86_firmware_from_source 0
%define build_skiboot_from_source 0
%define build_slof_from_source 0
%define kvm_available 0
%define legacy_qemu_kvm 0
%define force_fit_virtio_pxe_rom 1

%if 0%{?suse_version} > 1315
# cross-x86_64-gcc7 is available from SLE15/Leap15.0
%define build_rom_arch %ix86 x86_64 aarch64
%else
%define build_rom_arch %ix86 x86_64
%endif

%if "%{?distribution}" == ""
%define distro private-build
%else
%define distro %{distribution}
%endif

%ifarch %{build_rom_arch}
# choice of building all from source or using provided binary x86 blobs
%if 0%{?suse_version} > 1320 || ( 0%{?suse_version} == 1315 && 0%{?sle_version} > 120100 )
%define build_x86_firmware_from_source 1
%endif
%endif

%ifarch ppc64
%define build_skiboot_from_source 1
%define build_slof_from_source 1
%endif

%ifarch ppc64le
%if 0%{?suse_version} > 1320 ||  0%{?suse_version} == 1315
%define build_skiboot_from_source 1
%define build_slof_from_source 1
%endif
%endif

%ifarch %ix86 x86_64 ppc ppc64 ppc64le s390x armv7hl aarch64
%define kvm_available 1
%endif

%ifarch %ix86 x86_64 s390x
%define legacy_qemu_kvm 1
%endif

%if 0%{?suse_version} >= 1315 && 0%{?is_opensuse}
%define with_glusterfs 1
%endif

%ifarch x86_64
%if 0%{?suse_version} > 1320 || ( 0%{?suse_version} == 1315 && ( 0%{?is_opensuse} == 0 || 0%{?sle_version} > 120100 ) )
%define with_rbd 1
%endif
%endif

%ifarch aarch64
%if 0%{?suse_version} > 1320 || ( 0%{?is_opensuse} == 0 && 0%{?sle_version} > 120100 )
%define with_rbd 1
%endif
%endif

%ifarch ppc64le
%if 0%{?suse_version} > 1320 || ( 0%{?is_opensuse} == 0 && 0%{?sle_version} > 120200 )
%define with_rbd 1
%endif
%endif

%ifarch s390x
%if 0%{?is_opensuse} == 0 && 0%{?sle_version} > 120200
%define with_rbd 1
%endif
%endif

%ifarch ppc64
%if 0%{?is_opensuse} && 0%{?sle_version} > 120200
%define with_rbd 1
%endif
%endif

%if 0%{?suse_version} > 1320
%define with_seccomp 1
%endif

%ifarch %ix86 x86_64 s390x aarch64 ppc64le
%define with_seccomp 1
%endif

%if 0%( pkg-config --exists 'udev > 190' && echo '1' ) == 01
%define _udevrulesdir /usr/lib/udev/rules.d
%else
%define _udevrulesdir /lib/udev/rules.d
%endif

%define srcname qemu
Name:           qemu
Url:            https://www.qemu.org/
Summary:        Machine emulator and virtualizer
License:        BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Group:          System/Emulators/PC
%define qemuver 4.0.0
%define srcver  4.0.0
Version:        %qemuver
Release:        0
Source:         https://wiki.qemu.org/download/%{srcname}-%{srcver}.tar.xz
Source99:       https://wiki.qemu.org/download/%{srcname}-%{srcver}.tar.xz.sig
Source100:      %{srcname}.keyring
Source1:        80-kvm.rules
Source2:        kvm.conf
Source3:        qemu-ifup
Source4:        bridge.conf
Source5:        qemu-kvm.1.gz
Source6:        ksm.service
Source7:        qemu-ga@.service
Source8:        80-qemu-ga.rules
Source9:        qemu-supportconfig
Source10:       supported.arm.txt
Source11:       supported.ppc.txt
Source12:       supported.x86.txt
Source13:       supported.s390.txt
# this is to make lint happy
Source300:      qemu-rpmlintrc
Source301:      ipxe-stub-out-the-SAN-req-s-in-int13.patch
Source400:      update_git.sh
# Upstream First -- https://wiki.qemu.org/Contribute/SubmitAPatch
# This patch queue is auto-generated from https://github.com/openSUSE/qemu
Patch0001:      0001-XXX-dont-dump-core-on-sigabort.patch
Patch0002:      0002-qemu-binfmt-conf-Modify-default-pat.patch
Patch0003:      0003-qemu-cvs-gettimeofday.patch
Patch0004:      0004-qemu-cvs-ioctl_debug.patch
Patch0005:      0005-qemu-cvs-ioctl_nodirection.patch
Patch0006:      0006-linux-user-add-binfmt-wrapper-for-a.patch
Patch0007:      0007-PPC-KVM-Disable-mmu-notifier-check.patch
Patch0008:      0008-linux-user-binfmt-support-host-bina.patch
Patch0009:      0009-linux-user-Fake-proc-cpuinfo.patch
Patch0010:      0010-linux-user-use-target_ulong.patch
Patch0011:      0011-Make-char-muxer-more-robust-wrt-sma.patch
Patch0012:      0012-linux-user-lseek-explicitly-cast-no.patch
Patch0013:      0013-AIO-Reduce-number-of-threads-for-32.patch
Patch0014:      0014-xen_disk-Add-suse-specific-flush-di.patch
Patch0015:      0015-qemu-bridge-helper-reduce-security-.patch
Patch0016:      0016-qemu-binfmt-conf-use-qemu-ARCH-binf.patch
Patch0017:      0017-linux-user-properly-test-for-infini.patch
Patch0018:      0018-roms-Makefile-pass-a-packaging-time.patch
Patch0019:      0019-Raise-soft-address-space-limit-to-h.patch
Patch0020:      0020-increase-x86_64-physical-bits-to-42.patch
Patch0021:      0021-vga-Raise-VRAM-to-16-MiB-for-pc-0.1.patch
Patch0022:      0022-i8254-Fix-migration-from-SLE11-SP2.patch
Patch0023:      0023-acpi_piix4-Fix-migration-from-SLE11.patch
Patch0024:      0024-Switch-order-of-libraries-for-mpath.patch
Patch0025:      0025-Make-installed-scripts-explicitly-p.patch
Patch0026:      0026-hw-smbios-handle-both-file-formats-.patch
Patch0027:      0027-tests-test-thread-pool-is-racy-add-.patch
Patch0028:      0028-xen-add-block-resize-support-for-xe.patch
Patch0029:      0029-tests-qemu-iotests-Triple-timeout-o.patch
Patch0030:      0030-tests-block-io-test-130-needs-some-.patch
Patch0031:      0031-xen-ignore-live-parameter-from-xen-.patch
Patch0032:      0032-tests-Fix-Makefile-handling-of-chec.patch
Patch0033:      0033-Conditionalize-ui-bitmap-installati.patch
Patch0034:      0034-Revert-target-i386-kvm-add-VMX-migr.patch
Patch0035:      0035-tests-change-error-message-in-test-.patch
Patch0036:      0036-sockets-avoid-string-truncation-war.patch
Patch0037:      0037-hw-usb-hcd-xhci-Fix-GCC-9-build-war.patch
Patch0038:      0038-hw-usb-dev-mtp-Fix-GCC-9-build-warn.patch
Patch0039:      0039-linux-user-avoid-string-truncation-.patch
Patch0040:      0040-linux-user-elfload-Fix-GCC-9-build-.patch
Patch0041:      0041-qxl-avoid-unaligned-pointer-reads-w.patch
Patch0042:      0042-libvhost-user-fix-Waddress-of-packe.patch
Patch0043:      0043-target-i386-define-md-clear-bit.patch
Patch0044:      0044-hw-intc-exynos4210_gic-provide-more.patch
Patch0045:      0045-kbd-state-fix-autorepeat-handling.patch
Patch0046:      0046-target-ppc-ensure-we-get-null-termi.patch
Patch0047:      0047-configure-only-populate-roms-if-sof.patch
Patch0048:      0048-pc-bios-s390-ccw-net-avoid-warning-.patch
Patch0049:      0049-qxl-check-release-info-object.patch
Patch0050:      0050-qemu-bridge-helper-restrict-interfa.patch
Patch0051:      0051-linux-user-fix-to-handle-variably-s.patch
# Please do not add QEMU patches manually here.
# Run update_git.sh to regenerate this queue.

# SeaBIOS / SeaVGABIOS - path: roms/seabios (patch range 1100-1199)
Patch1100:      seabios-use-python2-explicitly-as-needed.patch
Patch1101:      seabios-switch-to-python3-as-needed.patch
Patch1102:      seabios-fix_cross_compilation.patch

# ipxe - path: roms/ipxe (patch range 1200-1299)
Patch1200:      ipxe-stable-buildid.patch
Patch1201:      ipxe-use-gcc6-for-more-compact-code.patch
Patch1202:      ipxe-efi-Simplify-diagnostic-for-NULL-handle.patch
Patch1203:      ipxe-build-Disable-gcc-address-of-packed-member-warning.patch
Patch1204:      ipxe-efi-Avoid-string-op-warning-with-cross-gcc-7-compile.patch

# sgabios - path: roms/sgabios (patch range 1300-1399)
Patch1300:      sgabios-stable-buildid.patch
Patch1301:      sgabios-fix-cross-build.patch

# SLOF - path: roms/SLOF (patch range 1400-1499) (Currently no patches)

# skiboot - path: roms/skiboot (patch range 1500-1599) (Currently no patches)
Patch1500:      skiboot-gcc9-compat.patch

# keycodemapdb - path: ui/keycodemapdb (patch range 1600-1699) (Currently no patches)
Patch1600:      keycodemapdb-make-keycode-gen-output-reproducible.patch

# openBIOS - path: roms/openbios (patch range 1700-1799) (Currently no patches)

# If for any reason we have any QEMU patches which are conditionally applied,
# "manually" include them here:

ExcludeArch:    s390
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{build_x86_firmware_from_source}
BuildRequires:  acpica
%endif
BuildRequires:  alsa-devel
%if %{build_x86_firmware_from_source}
BuildRequires:  binutils-devel
%endif
BuildRequires:  bison
BuildRequires:  bluez-devel
BuildRequires:  brlapi-devel
%if %{build_x86_firmware_from_source}
%ifnarch %{ix86} x86_64
# We must cross-compile on non-x86*
BuildRequires:  cross-x86_64-binutils
BuildRequires:  cross-x86_64-gcc7
%endif
%endif
BuildRequires:  curl-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  e2fsprogs-devel
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
%if %{build_x86_firmware_from_source}
%if 0%{?suse_version} <= 1320
BuildRequires:  gcc6
%endif
%endif
BuildRequires:  glib2-devel
%if 0%{?with_glusterfs}
BuildRequires:  glusterfs-devel
%endif
BuildRequires:  gtk3-devel
BuildRequires:  libaio-devel
BuildRequires:  libattr-devel
BuildRequires:  libbz2-devel
%if 0%{?is_opensuse}
BuildRequires:  libcacard-devel
%endif
BuildRequires:  libcap-devel
BuildRequires:  libcap-ng-devel
BuildRequires:  libdrm-devel
%if 0%{?suse_version} >= 1320 || ( 0%{?suse_version} == 1315 && 0%{?sle_version} > 120100 )
BuildRequires:  libepoxy-devel
%endif
%if 0%{?suse_version} > 1320 || ( 0%{?suse_version} == 1315 && 0%{?sle_version} > 120200 )
BuildRequires:  libfdt-devel
%else
BuildRequires:  libfdt1-devel
%endif
BuildRequires:  libgbm-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgnutls-devel
%if 0%{?suse_version} > 1320 || ( 0%{?suse_version} == 1315 && 0%{?sle_version} > 120100 )
BuildRequires:  libiscsi-devel
%endif
BuildRequires:  libjpeg-devel
%if 0%{?is_opensuse}
BuildRequires:  libnfs-devel
%endif
%ifarch %ix86 x86_64
%if 0%{?suse_version} > 1320 || 0%{?suse_version} == 1315
BuildRequires:  libnuma-devel
%endif
%else
%ifarch aarch64
%if 0%{?suse_version} > 1320 || ( 0%{?suse_version} == 1315 && 0%{?sle_version} > 120100 )
BuildRequires:  libnuma-devel
%endif
%endif
%else
%ifnarch %arm s390x
BuildRequires:  libnuma-devel
%endif
%endif
BuildRequires:  libpcap-devel
BuildRequires:  libpixman-1-0-devel
%ifarch x86_64
BuildRequires:  libpmem-devel
%endif
BuildRequires:  libpng-devel
BuildRequires:  libpulse-devel
%if 0%{?with_rbd}
%if 0%{?is_opensuse} || 0%{?sle_version} > 120100
BuildRequires:  librbd-devel
%else
BuildRequires:  ceph-devel
%endif
%endif
%if 0%{?suse_version} >= 1320 && 0%{?is_opensuse}
BuildRequires:  libSDL2-devel
BuildRequires:  libSDL2_image-devel
%endif
%if 0%{?with_seccomp}
BuildRequires:  libseccomp-devel
%endif
BuildRequires:  libspice-server-devel
BuildRequires:  libssh2-devel
BuildRequires:  libudev-devel
BuildRequires:  libusb-1_0-devel
%if 0%{?suse_version} > 1320
BuildRequires:  libvdeplug-devel
%else
BuildRequires:  libvdeplug3-devel
%endif
%if 0%{?is_opensuse}
BuildRequires:  lzfse-devel
%endif
BuildRequires:  Mesa-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  lzo-devel
BuildRequires:  makeinfo
%if 0%{?suse_version} > 1320
BuildRequires:  multipath-tools-devel
%endif
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  pwdutils
%if 0%{?suse_version} > 1320
BuildRequires:  python3-Sphinx
BuildRequires:  python3-base
%else
BuildRequires:  python-Sphinx
%endif
BuildRequires:  python-base
%if 0%{?suse_version} >= 1315
BuildRequires:  rdma-core-devel
%endif
BuildRequires:  snappy-devel
BuildRequires:  spice-protocol-devel
BuildRequires:  systemd
%{?systemd_requires}
%if %{kvm_available}
BuildRequires:  pkgconfig(udev)
%endif
BuildRequires:  usbredir-devel
%if 0%{?suse_version} >= 1320 || ( 0%{?suse_version} == 1315 && 0%{?sle_version} > 120100 )
BuildRequires:  virglrenderer-devel >= 0.4.1
%endif
BuildRequires:  vte-devel
%ifarch x86_64
BuildRequires:  xen-devel
%endif
BuildRequires:  xfsprogs-devel
%if %{build_x86_firmware_from_source}
BuildRequires:  xz-devel
%endif
BuildRequires:  zlib-devel
%if "%{name}" == "qemu-testsuite"
%if 0%{?suse_version} > 1320
BuildRequires:  python-base
%endif
BuildRequires:  bc
BuildRequires:  qemu-arm = %{qemuver}
BuildRequires:  qemu-audio-alsa = %{qemuver}
BuildRequires:  qemu-audio-pa = %{qemuver}
%if 0%{?suse_version} >= 1320 && 0%{?is_opensuse}
BuildRequires:  qemu-audio-sdl = %{qemuver}
%endif
BuildRequires:  qemu-block-curl = %{qemuver}
BuildRequires:  qemu-block-dmg = %{qemuver}
%if 0%{?with_glusterfs}
BuildRequires:  qemu-block-gluster = %{qemuver}
%endif
%if 0%{?suse_version} > 1320 || ( 0%{?suse_version} == 1315 && 0%{?sle_version} > 120100 )
BuildRequires:  qemu-block-iscsi = %{qemuver}
%endif
%if 0%{?is_opensuse}
BuildRequires:  qemu-block-nfs = %{qemuver}
%endif
%if 0%{?with_rbd}
BuildRequires:  qemu-block-rbd = %{qemuver}
%endif
BuildRequires:  qemu-block-ssh = %{qemuver}
BuildRequires:  qemu-extra = %{qemuver}
BuildRequires:  qemu-guest-agent = %{qemuver}
BuildRequires:  qemu-ipxe = 1.0.0+
%if 0%{?is_opensuse}
BuildRequires:  qemu-ksm = %{qemuver}
%endif
BuildRequires:  qemu-lang = %{qemuver}
BuildRequires:  qemu-ppc   = %{qemuver}
BuildRequires:  qemu-s390  = %{qemuver}
BuildRequires:  qemu-seabios = 1.12.1
BuildRequires:  qemu-sgabios = 8
BuildRequires:  qemu-tools = %{qemuver}
BuildRequires:  qemu-ui-curses = %{qemuver}
BuildRequires:  qemu-ui-gtk = %{qemuver}
%if 0%{?suse_version} >= 1320 && 0%{?is_opensuse}
BuildRequires:  qemu-ui-sdl = %{qemuver}
%endif
BuildRequires:  qemu-vgabios = 1.12.1
BuildRequires:  qemu-x86    = %{qemuver}
%endif
Requires(pre):  shadow
Requires(post): coreutils
%if %{kvm_available}
Requires(post): acl
Requires(post): udev
%ifarch s390x
Requires(post): procps
%endif
Recommends:     kvm_stat
%endif
Recommends:     qemu-block-curl
Recommends:     qemu-tools
Recommends:     qemu-ui-curses
Recommends:     qemu-ui-gtk
%if 0%{?suse_version} >= 1320 && 0%{?is_opensuse}
Recommends:     qemu-ui-sdl
%endif
Recommends:     qemu-x86
%ifarch ppc ppc64 ppc64le
Recommends:     qemu-ppc
%else
Suggests:       qemu-ppc
%endif
%ifarch s390x
Recommends:     qemu-s390
%else
Suggests:       qemu-s390
%endif
%ifarch %arm aarch64
Recommends:     qemu-arm
%else
Suggests:       qemu-arm
%endif
Suggests:       qemu-block-dmg
%if 0%{?with_glusterfs}
Suggests:       qemu-block-gluster
%endif
%if 0%{?suse_version} > 1320 || ( 0%{?suse_version} == 1315 && 0%{?sle_version} > 120100 )
Suggests:       qemu-block-iscsi
%endif
%if 0%{?is_opensuse}
Suggests:       qemu-block-nfs
%endif
%if 0%{?with_rbd}
Suggests:       qemu-block-rbd
%endif
Suggests:       qemu-block-ssh
Suggests:       qemu-extra
Suggests:       qemu-lang
%if 0%{?is_opensuse}
Recommends:     qemu-ksm = %{qemuver}
%endif
Provides:       qemu-audio-oss = %{qemuver}
Obsoletes:      qemu-audio-oss < %{qemuver}

# for the record, this set of firmware files is installed, but we don't
# build (yet): bamboo.dtb canyonlands.dtb hppa-firmware.img openbios-ppc openbios-sparc32
# openbios-sparc64 palcode-clipper petalogix-ml605.dtb petalogix-s3adsp1800.dtb ppc_rom.bin
# QEMU,cgthree.bin QEMU,tcx.bin qemu_vga.ndrv u-boot.e500 u-boot-sam460-20100605.bin

# This first list group isn't specific to what this instance builds
%define ppc_default_firmware {%nil}
%define ppc_extra_firmware {skiboot.lid slof.bin}
%define ppc64_only_default_firmware {spapr-rtas.bin}
%define ppc64_only_extra_firmware {%nil}
%define s390x_default_firmware {s390-ccw.img s390-netboot.img}
%define s390x_extra_firmware {%nil}
%define x86_default_firmware {linuxboot.bin linuxboot_dma.bin multiboot.bin \
kvmvapic.bin pvh.bin}
%define x86_extra_firmware {bios.bin bios-256k.bin pxe-e1000.rom pxe-eepro100.rom \
pxe-ne2k_pci.rom pxe-pcnet.rom pxe-rtl8139.rom pxe-virtio.rom sgabios.bin \
vgabios-bochs-display.bin vgabios.bin vgabios-cirrus.bin vgabios-qxl.bin \
vgabios-ramfb.bin vgabios-stdvga.bin vgabios-virtio.bin vgabios-vmware.bin}
%define x86_64_only_default_firmware {%nil}
%define x86_64_only_extra_firmware {efi-e1000.rom efi-e1000e.rom efi-eepro100.rom \
efi-ne2k_pci.rom efi-pcnet.rom efi-rtl8139.rom efi-virtio.rom efi-vmxnet3.rom}

%define firmware { \
%{?ppc_default_firmware} %{?ppc_extra_firmware} \
%{?ppc64_only_default_firmware} %{?ppc64_only_extra_firmware} \
%{?s390x_default_firmware} %{?s390x_extra_firmware} \
%{?x86_default_firmware} %{?x86_extra_firmware} \
%{?x86_64_only_default_firmware} %{?x86_64_only_extra_firmware} }

# This second list group is specific to what this instance builds
%define ppc_default_built_firmware %{ppc_default_firmware}
%if %{build_skiboot_from_source} && %{build_slof_from_source}
%define ppc_extra_built_firmware %{ppc_extra_firmware}
%else
%if %{build_skiboot_from_source}
%define ppc_extra_built_firmware {skiboot.lid}
%endif
%if %{build_slof_from_source}
%define ppc_extra_built_firmware {slof.bin}
%endif
%endif

%ifarch ppc64
%define ppc64_only_default_built_firmware %{ppc64_only_default_firmware}
%define ppc64_only_extra_built_firmware %{ppc64_only_extra_firmware}
%endif

%ifarch s390x
%define s390x_default_built_firmware %{s390x_default_firmware}
%define s390x_extra_built_firmware %{s390x_extra_firmware}
%endif

%ifarch %ix86 x86_64
%define x86_default_built_firmware %{x86_default_firmware}
%ifarch x86_64
%define x86_64_only_default_built_firmware %{x86_64_only_default_firmware}
%endif
%endif

%if %{build_x86_firmware_from_source}
%define x86_extra_built_firmware %{x86_extra_firmware}
%ifarch x86_64
%define x86_64_only_extra_built_firmware %{x86_64_only_extra_firmware}
%endif
%endif

%define built_firmware { \
%{?ppc_default_built_firmware} %{?ppc_extra_built_firmware} \
%{?ppc64_only_default_built_firmware} %{?ppc64_only_extra_built_firmware} \
%{?s390x_default_built_firmware} %{?s390x_extra_built_firmware} \
%{?x86_default_built_firmware} %{?x86_extra_built_firmware} \
%{?x86_64_only_default_built_firmware} %{?x86_64_only_extra_built_firmware} }

%description
QEMU provides full machine emulation and cross architecture usage. It closely
integrates with KVM and Xen virtualization, allowing for excellent performance.
Many options are available for defining the emulated environment, including 
traditional devices, direct host device access, and interfaces specific to
virtualization.

This package acts as an umbrella package to the other QEMU sub-packages.

%if "%{name}" != "qemu-testsuite"

%package x86
Summary:        Machine emulator and virtualizer for x86 architectures
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       %name = %{qemuver}
Requires:       qemu-ipxe
Requires:       qemu-seabios
Requires:       qemu-sgabios
Requires:       qemu-vgabios
Recommends:     ovmf
Recommends:     qemu-ovmf-x86_64

%description x86
QEMU provides full machine emulation and cross architecture usage. It closely
integrates with KVM and Xen virtualization, allowing for excellent performance.
Many options are available for defining the emulated environment, including 
traditional devices, direct host device access, and interfaces specific to
virtualization.

This package provides i386 and x86_64 emulation.

%package ppc
Summary:        Machine emulator and virtualizer for Power architectures
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       %name = %{qemuver}
Recommends:     qemu-ipxe
Recommends:     qemu-vgabios

%description ppc
QEMU provides full machine emulation and cross architecture usage. It closely
integrates with KVM and Xen virtualization, allowing for excellent performance.
Many options are available for defining the emulated environment, including 
traditional devices, direct host device access, and interfaces specific to
virtualization.

This package provides ppc and ppc64 emulation.

%package s390
Summary:        Machine emulator and virtualizer for S/390 architectures
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       %name = %{qemuver}

%description s390
QEMU provides full machine emulation and cross architecture usage. It closely
integrates with KVM and Xen virtualization, allowing for excellent performance.
Many options are available for defining the emulated environment, including 
traditional devices, direct host device access, and interfaces specific to
virtualization.

This package provides s390x emulation.

%package arm
Summary:        Machine emulator and virtualizer for ARM architectures
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       %name = %{qemuver}
Recommends:     qemu-ipxe
Recommends:     qemu-vgabios
Recommends:     ovmf
Recommends:     qemu-uefi-aarch64

%description arm
QEMU provides full machine emulation and cross architecture usage. It closely
integrates with KVM and Xen virtualization, allowing for excellent performance.
Many options are available for defining the emulated environment, including 
traditional devices, direct host device access, and interfaces specific to
virtualization.

This package provides arm emulation.

%package extra
Summary:        Machine emulator and virtualizer for "extra" architectures
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires:       %name = %{qemuver}
Recommends:     qemu-ipxe
Recommends:     qemu-vgabios

%description extra
QEMU provides full machine emulation and cross architecture usage. It closely
integrates with KVM and Xen virtualization, allowing for excellent performance.
Many options are available for defining the emulated environment, including 
traditional devices, direct host device access, and interfaces specific to
virtualization.

This package provides some lesser used emulations, including alpha, m68k,
mips, moxie, sparc, and xtensa. (The term "extra" is juxtapositioned against
more popular QEMU packages which are dedicated to a single architecture.)

%if %{legacy_qemu_kvm}
%package kvm
Summary:        Wrapper to enable KVM acceleration under QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%ifarch %ix86 x86_64
Requires:       qemu-x86 = %{qemuver}
%endif
%ifarch s390x
Requires:       qemu-s390 = %{qemuver}
%endif
Provides:       kvm = %{qemuver}
Obsoletes:      kvm < %{qemuver}

%description kvm
QEMU provides full machine emulation and cross architecture usage. It closely
integrates with KVM and Xen virtualization, allowing for excellent performance.
Many options are available for defining the emulated environment, including 
traditional devices, direct host device access, and interfaces specific to
virtualization.

This package simply provides a shell script wrapper for the QEMU program which
does the actual machine emulation and virtualization for this architecture. The
wrapper simply adds command-line parameters to ensure that the KVM accelerator
is invoked. It provides no additional benefit, and is considered deprecated.
%endif

%package lang
Summary:        Translations for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0

%description lang
This package contains a few language translations, particularly for the
graphical user interface components that come with QEMU. The bulk of strings
in QEMU are not localized.

# Modules need to match {qemu-system-*,qemu-img} version.
# We cannot have qemu and qemu-tools require them in the right version,
# as that would drag in the dependencies the modules are supposed to avoid.
# Nor can we have modules require the right version of qemu and qemu-tools
# as Xen reuses our qemu-tools but does not want our qemu and qemu-x86.
%define qemu_module_conflicts \
Conflicts:      %name < %{qemuver}-%{release} \
Conflicts:      %name > %{qemuver}-%{release} \
Conflicts:      qemu-tools < %{qemuver}-%{release} \
Conflicts:      qemu-tools > %{qemuver}-%{release}

%package block-curl
Summary:        cURL block support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Provides:       %name:%_libdir/%name/block-curl.so
%{qemu_module_conflicts}

%description block-curl
This package contains a module for accessing network-based image files over
a network connection from qemu-img tool and QEMU system emulation.

%package block-dmg
Summary:        DMG block support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description block-dmg
This package contains a module for accessing Mac OS X image files from
qemu-img tool and QEMU system emulation.

%if 0%{?with_glusterfs}
%package block-gluster
Summary:        GlusterFS block support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description block-gluster
This package contains a module for accessing network-based image files over a
GlusterFS network connection from qemu-img tool and QEMU system emulation.
%endif

%if 0%{?suse_version} > 1320 || ( 0%{?suse_version} == 1315 && 0%{?sle_version} > 120100 )
%package block-iscsi
Summary:        iSCSI block support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description block-iscsi
This package contains a module for accessing network-based image files over an
iSCSI network connection from qemu-img tool and QEMU system emulation.
%endif

%if 0%{?is_opensuse}
%package block-nfs
Summary:        direct Network File System support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description block-nfs
This package contains a module for directly accessing nfs based image files.
%endif

%if 0%{?with_rbd}
%package block-rbd
Summary:        Rados Block Device (Ceph) support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description block-rbd
This package contains a module for accessing ceph (rbd,rados) image files.
%endif

%package block-ssh
Summary:        SSH (SFTP) block support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description block-ssh
This package contains a module for accessing network-based image files over an
SSH network connection from qemu-img tool and QEMU system emulation.

%package ui-curses
Summary:        Curses based UI support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description ui-curses
This package contains a module for doing curses based UI for QEMU.

%package ui-gtk
Summary:        GTK based UI support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description ui-gtk
This package contains a module for doing GTK based UI for QEMU.

%if 0%{?suse_version} >= 1320 && 0%{?is_opensuse}
%package ui-sdl
Summary:        SDL based UI support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description ui-sdl
This package contains a module for doing SDL based UI for QEMU.
%endif

%package audio-alsa
Summary:        ALSA based audio support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description audio-alsa
This package contains a module for ALSA based audio support for QEMU.

%package audio-pa
Summary:        Pulse Audio based audio support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description audio-pa
This package contains a module for Pulse Audio based audio support for QEMU.

%if 0%{?suse_version} >= 1320 && 0%{?is_opensuse}
%package audio-sdl
Summary:        SDL based audio support for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
%{qemu_module_conflicts}

%description audio-sdl
This package contains a module for SDL based audio support for QEMU.
%endif

%package tools
Summary:        Tools for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Provides:       %name:%_libexecdir/qemu-bridge-helper
Requires(pre):  permissions
Requires(pre):  shadow
%if 0%{?suse_version} > 1320
Recommends:     multipath-tools
%endif
Recommends:     qemu-block-curl
%if 0%{?with_rbd}
Recommends:     qemu-block-rbd
%endif

%description tools
This package contains various QEMU related tools, including a bridge helper,
a virtfs helper, ivshmem, disk utilities and scripts for various purposes.

%package guest-agent
Summary:        Guest agent for QEMU
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Provides:       %name:%_bindir/qemu-ga
Requires(pre):  shadow
Requires(post): udev
Supplements:    modalias(acpi*:QEMU0002%3A*)
Supplements:    modalias(pci:v0000FFFDd00000101sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00005853d00000001sv*sd*bc*sc*i*)
%{?systemd_requires}

%description guest-agent
This package contains the QEMU guest agent. It is installed in the linux guest
to provide information and control at the guest OS level.

%ifarch %{build_rom_arch}
%package seabios
Summary:        x86 Legacy BIOS for QEMU
Group:          System/Emulators/PC
Version:        1.12.1
Release:        0
BuildArch:      noarch
Conflicts:      %name < 1.6.0

%description seabios
SeaBIOS is an open source implementation of a 16bit x86 BIOS. SeaBIOS
is the default and legacy BIOS for QEMU.

%package vgabios
Summary:        VGA BIOSes for QEMU
Group:          System/Emulators/PC
Version:        1.12.1
Release:        0
BuildArch:      noarch
Conflicts:      %name < 1.6.0

%description vgabios
VGABIOS provides the video ROM BIOSes for the following variants of VGA
emulated devices: Std VGA, QXL, Cirrus CLGD 5446 and VMware emulated
video card.

%package sgabios
Summary:        Serial Graphics Adapter BIOS for QEMU
Group:          System/Emulators/PC
Version:        8
Release:        0
BuildArch:      noarch
Conflicts:      %name < 1.6.0

%description sgabios
The Google Serial Graphics Adapter BIOS or SGABIOS provides a means for legacy
x86 software to communicate with an attached serial console as if a video card
were attached.

%package ipxe
Summary:        PXE ROMs for QEMU NICs
Group:          System/Emulators/PC
Version:        1.0.0+
Release:        0
BuildArch:      noarch
Conflicts:      %name < 1.6.0

%description ipxe
Provides Preboot Execution Environment (PXE) ROM support for various emulated
network adapters available with QEMU.
%endif

%if 0%{?is_opensuse}
%package ksm
Summary:        Kernel Samepage Merging services
Group:          System/Emulators/PC
Version:        %{qemuver}
Release:        0
Requires(pre):  coreutils
Requires(post): coreutils

%description ksm
Kernel Samepage Merging (KSM) is a memory-saving de-duplication feature, that
merges anonymous (private) pages (not pagecache ones).

This package provides a service file for starting and stopping KSM.
%endif

%endif # !qemu-testsuite

%prep
%setup -q -n %{srcname}-%{expand:%%(SV=%{srcver};echo ${SV%%%%+git*})}
%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1
%patch0009 -p1
%patch0010 -p1
%patch0011 -p1
%patch0012 -p1
%patch0013 -p1
%patch0014 -p1
%patch0015 -p1
%patch0016 -p1
%patch0017 -p1
%patch0018 -p1
%patch0019 -p1
%patch0020 -p1
%patch0021 -p1
%patch0022 -p1
%patch0023 -p1
%patch0024 -p1
%patch0025 -p1
%patch0026 -p1
%patch0027 -p1
%patch0028 -p1
%patch0029 -p1
%patch0030 -p1
%patch0031 -p1
%patch0032 -p1
%patch0033 -p1
%patch0034 -p1
%patch0035 -p1
%patch0036 -p1
%patch0037 -p1
%patch0038 -p1
%patch0039 -p1
%patch0040 -p1
%patch0041 -p1
%patch0042 -p1
%patch0043 -p1
%patch0044 -p1
%patch0045 -p1
%patch0046 -p1
%patch0047 -p1
%patch0048 -p1
%patch0049 -p1
%patch0050 -p1
%patch0051 -p1

pushd roms/seabios
%patch1100 -p1
%if 0%{?suse_version} > 1320
%patch1101 -p1
%endif
%patch1102 -p1
popd

pushd roms/ipxe
%patch1200 -p1
%if 0%{?suse_version} <= 1320
%patch1201 -p1
%endif
%patch1202 -p1
%patch1203 -p1
%ifarch aarch64
%patch1204 -p1
%endif
popd

pushd roms/sgabios
%patch1300 -p1
%patch1301 -p1
popd

pushd roms/SLOF
popd

pushd roms/skiboot
%patch1500 -p1
popd

pushd ui/keycodemapdb
%patch1600 -p1
popd

pushd roms/openbios
popd

%if "%{name}" != "qemu-testsuite"
# delete the firmware files that we intend to build
for i in %built_firmware
%else
# delete the firmware files that we intend to link from built packages
for i in %firmware
%endif
do
  unlink pc-bios/$i
done

%build
%define _lto_cflags %{nil}

%if %build_in_tree
%define mybuilddir %{_builddir}/%buildsubdir
%else
%define mybuilddir %{_builddir}/mybuilddir
mkdir -p %mybuilddir
cd %mybuilddir
%endif

%{_builddir}/%buildsubdir/configure \
	--prefix=%_prefix \
	--sysconfdir=%_sysconfdir \
	--libdir=%_libdir \
	--libexecdir=%_libexecdir \
	--localstatedir=%_localstatedir \
	--docdir=%_docdir/%name \
	--firmwarepath=%_datadir/%name \
%if 0%{?suse_version} > 1320
        --python=%_bindir/python3 \
%else
        --python=%_bindir/python2 \
%endif
	--extra-cflags="%{optflags}" \
	--disable-stack-protector \
	--disable-strip \
	--with-pkgversion="%(echo '%{distro}' | sed 's/ (.*)//')" \
	--with-default-devices \
	--enable-system --disable-linux-user \
	--enable-tools --enable-guest-agent \
	--enable-modules \
	--enable-pie \
	--enable-docs \
%if 0%{?suse_version} >= 1320 && 0%{?is_opensuse}
	--audio-drv-list="pa alsa sdl" \
%else
	--audio-drv-list="pa alsa" \
%endif
	--enable-attr \
	--disable-auth-pam \
	--enable-bluez \
	--enable-bochs \
	--enable-brlapi \
	--enable-bzip2 \
	--enable-cap-ng \
	--disable-capstone \
	--enable-cloop \
	--enable-coroutine-pool \
	--disable-crypto-afalg \
	--enable-curl \
	--enable-curses \
	--enable-dmg \
	--enable-fdt \
	--enable-gcrypt \
%if 0%{?with_glusterfs}
	--enable-glusterfs \
%else
	--disable-glusterfs \
%endif
	--enable-gnutls \
	--enable-gtk \
	--disable-hax \
	--disable-hvf \
	--enable-iconv \
	--disable-jemalloc \
%if %{kvm_available}
	--enable-kvm \
%else
	--disable-kvm \
%endif
%if 0%{?suse_version} > 1320 || ( 0%{?suse_version} == 1315 && 0%{?sle_version} > 120100 )
	--enable-libiscsi \
%else
	--disable-libiscsi \
%endif
%if 0%{?is_opensuse}
	--enable-libnfs \
%else
	--disable-libnfs \
%endif
%ifarch x86_64
	--enable-libpmem \
%else
	--disable-libpmem \
%endif
	--enable-libssh2 \
	--enable-libusb \
	--disable-libxml2 \
	--enable-linux-aio \
%if 0%{?is_opensuse}
	--enable-lzfse \
%else
	--disable-lzfse \
%endif
	--enable-lzo \
	--disable-malloc-trim \
	--enable-membarrier \
%if 0%{?suse_version} > 1320
	--enable-mpath \
%else
	--disable-mpath \
%endif
	--disable-netmap \
	--disable-nettle \
%ifarch %ix86 x86_64
%if 0%{?suse_version} > 1320 || 0%{?suse_version} == 1315
	--enable-numa \
%else
	--disable-numa \
%endif
%else
%ifarch aarch64
%if 0%{?suse_version} > 1320 || ( 0%{?suse_version} == 1315 && 0%{?sle_version} > 120100 )
	--enable-numa \
%endif
%else
	--disable-numa \
%endif
%else
%ifarch %arm s390x
	--disable-numa \
%else
	--enable-numa \
%endif
%endif
%if 0%{?suse_version} >= 1320 || ( 0%{?suse_version} == 1315 && 0%{?sle_version} > 120100 )
	--enable-opengl \
%endif
	--enable-parallels \
%if 0%{?suse_version} >= 1315
	--enable-pvrdma \
%else
	--disable-pvrdma \
%endif
	--enable-qcow1 \
	--enable-qed \
%if 0%{?with_rbd}
	--enable-rbd \
%else
	--disable-rbd \
%endif
%if 0%{?suse_version} >= 1315
	--enable-rdma \
%else
	--disable-rdma \
%endif
	--enable-replication \
	--disable-sanitizers \
%if 0%{?suse_version} >= 1320 && 0%{?is_opensuse}
	--enable-sdl \
	--enable-sdl-image \
%else
	--disable-sdl \
	--disable-sdl-image \
%endif
%if 0%{?with_seccomp}
	--enable-seccomp \
%else
	--disable-seccomp \
%endif
	--enable-sheepdog \
%if 0%{?is_opensuse}
	--enable-smartcard \
%else
	--disable-smartcard \
%endif
	--enable-snappy \
	--enable-spice \
	--disable-tcmalloc \
	--enable-tpm \
	--enable-usb-redir \
	--enable-vde \
	--enable-vdi \
	--enable-vhost-crypto \
	--enable-vhost-kernel \
	--enable-vhost-net \
	--enable-vhost-scsi \
	--enable-vhost-user \
	--enable-vhost-vsock \
%if 0%{?suse_version} >= 1320 || ( 0%{?suse_version} == 1315 && 0%{?sle_version} > 120100 )
	--enable-virglrenderer \
%endif
	--enable-virtfs \
	--enable-vnc \
	--enable-vnc-jpeg \
	--enable-vnc-png \
	--enable-vnc-sasl \
%if 0%{?suse_version} == 1320
	--disable-vte \
%else
	--enable-vte \
%endif
	--enable-vvfat \
	--enable-werror \
	--disable-whpx \
%ifarch x86_64
	--enable-xen \
	--enable-xen-pci-passthrough \
%else
	--disable-xen \
%endif
	--enable-xfsctl \

%if "%{name}" != "qemu-testsuite"

make %{?_smp_mflags} V=1

# Firmware

%ifarch s390x
for i in %s390x_default_built_firmware
do
  cp pc-bios/s390-ccw/$i %{_builddir}/%buildsubdir/pc-bios/
done
%endif

%ifarch ppc64
for i in %ppc64_only_default_built_firmware
do
  cp pc-bios/spapr-rtas/$i %{_builddir}/%buildsubdir/pc-bios/
done
%endif

%ifarch %ix86 x86_64
for i in %x86_default_built_firmware
do
  cp pc-bios/optionrom/$i %{_builddir}/%buildsubdir/pc-bios/
done
%ifarch x86_64
for i in %x86_64_only_default_built_firmware
do
  cp pc-bios/optionrom/$i %{_builddir}/%buildsubdir/pc-bios/
done
%endif
%endif

%if %{build_x86_firmware_from_source}
%ifnarch %{ix86} x86_64
export CC=x86_64-suse-linux-gcc
export LD=x86_64-suse-linux-ld
%endif

make %{?_smp_mflags} -C %{_builddir}/%buildsubdir/roms bios \
%ifnarch %ix86 x86_64
  HOSTCC=cc \
%endif

make %{?_smp_mflags} -C %{_builddir}/%buildsubdir/roms seavgabios \
%ifnarch %ix86 x86_64
  HOSTCC=cc \
%endif

make %{?_smp_mflags} -C %{_builddir}/%buildsubdir/roms pxerom

%ifnarch %ix86
make %{?_smp_mflags} -C %{_builddir}/%buildsubdir/roms efirom \
  EDK2_BASETOOLS_OPTFLAGS='-fPIE'
%endif

make                 -C %{_builddir}/%buildsubdir/roms sgabios \
  HOSTCC=cc

%if %{force_fit_virtio_pxe_rom}
pushd %{_builddir}/%buildsubdir/roms/ipxe
patch -p1 < %{SOURCE301}
popd
make %{?_smp_mflags} -C %{_builddir}/%buildsubdir/roms pxerom_variants=virtio pxerom_targets=1af41000 pxerom
%endif

# enforce pxe rom sizes for migration compatability from SLE 11 SP3 forward
# the following need to be > 64K
%define supported_nics_large {e1000 rtl8139}
# the following need to be <= 64K
%define supported_nics_small {virtio}
# Though not required, make unsupported pxe roms migration compatable as well
%define unsupported_nics {eepro100 ne2k_pci pcnet}

for i in %supported_nics_large %unsupported_nics
  do
    if test "`stat -c '%s' %{_builddir}/%buildsubdir/pc-bios/pxe-$i.rom`" -gt "131072" ; then
    echo "pxe rom is too large"
    exit 1
  fi
  if test "`stat -c '%s' %{_builddir}/%buildsubdir/pc-bios/pxe-$i.rom`" -le "65536" ; then
    ./%{_builddir}/%buildsubdir/roms/ipxe/src/util/padimg.pl %{_builddir}/%buildsubdir/pc-bios/pxe-$i.rom -s 65536 -b 255
    echo -ne "SEGMENT OVERAGE\0" >> %{_builddir}/%buildsubdir/pc-bios/pxe-$i.rom
  fi
done
for i in %supported_nics_small
  do
    if test "`stat -c '%s' %{_builddir}/%buildsubdir/pc-bios/pxe-$i.rom`" -gt "65536" ; then
    echo "pxe rom is too large"
    exit 1
  fi
done
%ifnarch %{ix86} x86_64
unset CC
unset LD
%endif
%endif

%if %{build_skiboot_from_source}
make %{?_smp_mflags} -C %{_builddir}/%buildsubdir/roms skiboot CROSS=
%endif

%if %{build_slof_from_source}
make %{?_smp_mflags} -C %{_builddir}/%buildsubdir/roms slof
%endif

%else # qemu-testsuite

ln -s %_bindir/qemu-img qemu-img
ln -s %_bindir/qemu-ga qemu-ga
ln -s %_bindir/qemu-io qemu-io
# And what about these binaries: qemu-nbd, elf2dmp, ivshmem-client, ivshmem-server, qemu-edid, qemu-keymap, qemu-pr-helper, virtfs-proxy-helper

for i in %firmware
do
  ln -s %_datadir/%name/$i pc-bios/$i
done

for conf in %{_builddir}/%buildsubdir/default-configs/*-softmmu.mak; do
  arch=`echo "$conf" | sed -e 's|%{_builddir}/%buildsubdir/default-configs/\(.*\)-softmmu.mak|\1|g'`
  ln -s %_bindir/qemu-system-$arch $arch-softmmu/qemu-system-$arch
done

# Compile the QOM test binary first, so that ...
touch -r config-host.mak pc-bios
make %{?_smp_mflags} tests/qom-test %{?_smp_mflags} V=1
# ... make comes in fresh and has lots of address space (needed for 32bit, bsc#957379)
make %{?_smp_mflags} check-report.tap V=1

%endif

%check
cd %mybuilddir
%if "%{name}" == "qemu-testsuite"

export QEMU_PROG=%_bindir/qemu-system-x86_64
export QEMU_IMG_PROG=%_bindir/qemu-img
export QEMU_IO_PROG=%_bindir/qemu-io
export QEMU_NBD_PROG=%_bindir/qemu-nbd
make %{?_smp_mflags} check-block V=1

%endif # qemu-testsuite

%install
cd %mybuilddir
%if "%{name}" != "qemu-testsuite"

make %{?_smp_mflags} install DESTDIR=%{buildroot}
%ifnarch %{build_rom_arch}
for f in %{x86_extra_firmware} \
         %{x86_64_only_extra_firmware}; do
  unlink %{buildroot}%_datadir/%name/$f
done
%endif
%find_lang %name
install -d -m 0755 %{buildroot}%_datadir/%name/firmware
install -d -m 0755 %{buildroot}%_libexecdir/supportconfig/plugins
install -d -m 0755 %{buildroot}%_sysconfdir/%name/firmware
install -D -m 0644 %{SOURCE4} %{buildroot}%_sysconfdir/%name/bridge.conf
install -D -m 0755 %{SOURCE3} %{buildroot}%_datadir/%name/qemu-ifup
install -D -p -m 0644 %{SOURCE8} %{buildroot}%{_udevrulesdir}/80-qemu-ga.rules
install -D -m 0755 scripts/analyze-migration.py  %{buildroot}%_bindir/analyze-migration.py
install -D -m 0755 scripts/vmstate-static-checker.py  %{buildroot}%_bindir/vmstate-static-checker.py
install -D -m 0755 %{SOURCE9} %{buildroot}%_libexecdir/supportconfig/plugins/%name
%if 0%{?is_opensuse} == 0
install -D -m 0644 %{SOURCE10} %{buildroot}%_docdir/qemu-arm/supported.txt
install -D -m 0644 %{SOURCE11} %{buildroot}%_docdir/qemu-ppc/supported.txt
install -D -m 0644 %{SOURCE12} %{buildroot}%_docdir/qemu-x86/supported.txt
install -D -m 0644 %{SOURCE13} %{buildroot}%_docdir/qemu-s390/supported.txt
%endif
%if %{legacy_qemu_kvm}
cat > %{buildroot}%_bindir/qemu-kvm << 'EOF'
#!/bin/sh

%ifarch s390x
exec %_bindir/qemu-system-s390x -machine accel=kvm "$@"
%else
exec %_bindir/qemu-system-x86_64 -machine accel=kvm "$@"
%endif
EOF
chmod 755 %{buildroot}%_bindir/qemu-kvm
install -D -m 0644 %{SOURCE5} %{buildroot}%_mandir/man1/qemu-kvm.1.gz
%if 0%{?is_opensuse} == 0
install -d %{buildroot}%_docdir/qemu-kvm
%ifarch s390x
ln -s ../qemu-s390/supported.txt %{buildroot}%_docdir/qemu-kvm/kvm-supported.txt
%else
ln -s ../qemu-x86/supported.txt %{buildroot}%_docdir/qemu-kvm/kvm-supported.txt
%endif
%endif
%endif
%if %{kvm_available}
install -D -m 0644 %{SOURCE1} %{buildroot}%{_udevrulesdir}/80-kvm.rules
%endif
install -D -p -m 0644 %{SOURCE7} %{buildroot}%{_unitdir}/qemu-ga@.service
%if 0%{?is_opensuse}
install -D -p -m 0644 %{SOURCE6} %{buildroot}%{_unitdir}/ksm.service
%endif
%ifarch s390x
install -D -m 0644 %{SOURCE2} %{buildroot}%_libexecdir/modules-load.d/kvm.conf
%endif
%fdupes -s %{buildroot}

%else # qemu-testsuite

install -D -m 0644 check-report.tap %{buildroot}%_datadir/qemu/check-report.tap

%endif

%if "%{name}" != "qemu-testsuite"

%pre
%_bindir/getent group kvm >/dev/null || %_sbindir/groupadd -r kvm
%_bindir/getent group qemu >/dev/null || %_sbindir/groupadd -r qemu
%_bindir/getent passwd qemu >/dev/null ||
  %_sbindir/useradd -r -g qemu -G kvm -d / -s /sbin/nologin \
  -c "qemu user" qemu

%if %{kvm_available}
%post
# Do not execute operations affecting host devices while running in a chroot
if [ $(stat -L -c "%i" /proc/1/root/) = $(stat -L -c "%i" /) ]; then
  setfacl --remove-all /dev/kvm &> /dev/null || :
%ifarch s390x
  if [ -c /dev/kvm ]; then
    %_bindir/chmod 0666 /dev/kvm
    %_bindir/chgrp kvm /dev/kvm
  fi
%endif
  %udev_rules_update
  %_bindir/udevadm trigger -y kvm || :
%ifarch s390x
  sysctl vm.allocate_pgste=1 || :
%endif
fi
%endif

%pre tools
%_bindir/getent group kvm >/dev/null || %_sbindir/groupadd -r kvm
%post tools
%set_permissions %_libexecdir/qemu-bridge-helper

%verifyscript tools
%verify_permissions %_libexecdir/qemu-bridge-helper

%pre guest-agent
%_bindir/getent group kvm >/dev/null || %_sbindir/groupadd -r kvm
%service_add_pre qemu-ga@.service

%post guest-agent
%service_add_post qemu-ga@.service
if [ -e /dev/virtio-ports/org.qemu.guest_agent.0 ]; then
  /usr/bin/systemctl start qemu-ga@virtio\\x2dports-org.qemu.guest_agent.0.service || :
fi

%preun guest-agent
if [ -e /dev/virtio-ports/org.qemu.guest_agent.0 ]; then
  /usr/bin/systemctl stop qemu-ga@virtio\\x2dports-org.qemu.guest_agent.0.service || :
fi

%postun guest-agent
%service_del_postun qemu-ga@.service

%if 0%{?is_opensuse}
%pre ksm
%service_add_pre ksm.service

%post ksm
%service_add_post ksm.service

%preun ksm
%service_del_preun ksm.service

%postun ksm
%service_del_postun ksm.service
%endif

%endif # !qemu-testsuite

%files
%defattr(-, root, root)
%if "%{name}" != "qemu-testsuite"
%doc Changelog README VERSION
%license COPYING COPYING.LIB LICENSE
%dir %_docdir/%name/interop
%dir %_docdir/%name/interop/_static
%_docdir/%name/interop/.buildinfo
%_docdir/%name/interop/_static/*
%_docdir/%name/interop/bitmaps.html
%_docdir/%name/interop/genindex.html
%_docdir/%name/interop/index.html
%_docdir/%name/interop/live-block-operations.html
%_docdir/%name/interop/objects.inv
%_docdir/%name/interop/pr-helper.html
%_docdir/%name/interop/search.html
%_docdir/%name/interop/searchindex.js
%_docdir/%name/qemu-doc.txt
%_docdir/%name/qemu-doc.html
%_docdir/%name/qemu-qmp-ref.txt
%_docdir/%name/qemu-qmp-ref.html
%_docdir/%name/qemu-ga-ref.txt
%_docdir/%name/qemu-ga-ref.html
%_mandir/man1/%name.1.gz
%_mandir/man7/qemu-block-drivers.7.gz
%_mandir/man7/qemu-cpu-models.7.gz
%_mandir/man7/qemu-qmp-ref.7.gz
%_mandir/man7/qemu-ga-ref.7.gz
%dir %_datadir/%name
%dir %_datadir/%name/firmware
%_datadir/%name/keymaps
%_datadir/%name/trace-events-all
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/firmware
%_datadir/%name/qemu-ifup
%dir %_libexecdir/supportconfig
%dir %_libexecdir/supportconfig/plugins
%_libexecdir/supportconfig/plugins/%name
%if %{kvm_available}
%{_udevrulesdir}/80-kvm.rules
%ifarch s390x
%_libexecdir/modules-load.d/kvm.conf
%endif
%endif
%dir %_datadir/icons/hicolor
%dir %_datadir/icons/hicolor/*/
%dir %_datadir/icons/hicolor/*/apps
%_datadir/icons/hicolor/16x16/apps/qemu.png
%_datadir/icons/hicolor/24x24/apps/qemu.png
%_datadir/icons/hicolor/32x32/apps/qemu.bmp
%_datadir/icons/hicolor/32x32/apps/qemu.png
%_datadir/icons/hicolor/48x48/apps/qemu.png
%_datadir/icons/hicolor/64x64/apps/qemu.png
%_datadir/icons/hicolor/128x128/apps/qemu.png
%_datadir/icons/hicolor/256x256/apps/qemu.png
%_datadir/icons/hicolor/512x512/apps/qemu.png
%_datadir/icons/hicolor/scalable/apps/qemu.svg
%_datadir/applications/qemu.desktop

%files x86
%defattr(-, root, root)
%_bindir/qemu-system-i386
%_bindir/qemu-system-x86_64
%_datadir/%name/kvmvapic.bin
%_datadir/%name/linuxboot.bin
%_datadir/%name/linuxboot_dma.bin
%_datadir/%name/multiboot.bin
%_datadir/%name/pvh.bin
%if 0%{?is_opensuse} == 0
%dir %_docdir/qemu-x86
%_docdir/qemu-x86/supported.txt
%endif

%files ppc
%defattr(-, root, root)
%_bindir/qemu-system-ppc
%_bindir/qemu-system-ppc64
%_datadir/%name/bamboo.dtb
%_datadir/%name/canyonlands.dtb
%_datadir/%name/openbios-ppc
%_datadir/%name/ppc_rom.bin
%_datadir/%name/qemu_vga.ndrv
%_datadir/%name/skiboot.lid
%_datadir/%name/slof.bin
%_datadir/%name/spapr-rtas.bin
%_datadir/%name/u-boot.e500
%_datadir/%name/u-boot-sam460-20100605.bin
%if 0%{?is_opensuse} == 0
%dir %_docdir/qemu-ppc
%_docdir/qemu-ppc/supported.txt
%endif

%files s390
%defattr(-, root, root)
%_bindir/qemu-system-s390x
%_datadir/%name/s390-ccw.img
%_datadir/%name/s390-netboot.img
%if 0%{?is_opensuse} == 0
%dir %_docdir/qemu-s390
%_docdir/qemu-s390/supported.txt
%endif

%files arm
%defattr(-, root, root)
%_bindir/qemu-system-arm
%_bindir/qemu-system-aarch64
%if 0%{?is_opensuse} == 0
%dir %_docdir/qemu-arm
%_docdir/qemu-arm/supported.txt
%endif

%files extra
%defattr(-, root, root)
%_bindir/qemu-system-alpha
%_bindir/qemu-system-cris
%_bindir/qemu-system-hppa
%_bindir/qemu-system-lm32
%_bindir/qemu-system-m68k
%_bindir/qemu-system-microblaze
%_bindir/qemu-system-microblazeel
%_bindir/qemu-system-mips
%_bindir/qemu-system-mipsel
%_bindir/qemu-system-mips64
%_bindir/qemu-system-mips64el
%_bindir/qemu-system-moxie
%_bindir/qemu-system-nios2
%_bindir/qemu-system-or1k
%_bindir/qemu-system-riscv32
%_bindir/qemu-system-riscv64
%_bindir/qemu-system-sh4
%_bindir/qemu-system-sh4eb
%_bindir/qemu-system-sparc
%_bindir/qemu-system-sparc64
%_bindir/qemu-system-tricore
%_bindir/qemu-system-unicore32
%_bindir/qemu-system-xtensa
%_bindir/qemu-system-xtensaeb
%_datadir/%name/hppa-firmware.img
%_datadir/%name/openbios-sparc32
%_datadir/%name/openbios-sparc64
%_datadir/%name/palcode-clipper
%_datadir/%name/petalogix-ml605.dtb
%_datadir/%name/petalogix-s3adsp1800.dtb
%_datadir/%name/QEMU,cgthree.bin
%_datadir/%name/QEMU,tcx.bin

%if %{legacy_qemu_kvm}
%files kvm
%defattr(-,root,root)
%_bindir/qemu-kvm
%_mandir/man1/qemu-kvm.1.gz
%if 0%{?is_opensuse} == 0
%dir %_docdir/qemu-kvm
%_docdir/qemu-kvm/kvm-supported.txt
%endif
%endif

%files block-curl
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-curl.so

%files block-dmg
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-dmg-bz2.so
%if 0%{?is_opensuse}
%_libdir/%name/block-dmg-lzfse.so
%endif

%if 0%{?with_glusterfs}
%files block-gluster
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-gluster.so
%endif

%if 0%{?suse_version} > 1320 || ( 0%{?suse_version} == 1315 && 0%{?sle_version} > 120100 )
%files block-iscsi
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-iscsi.so
%endif

%if 0%{?is_opensuse}
%files block-nfs
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-nfs.so
%endif

%if 0%{?with_rbd}
%files block-rbd
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-rbd.so
%endif

%files block-ssh
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/block-ssh.so

%files ui-curses
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/ui-curses.so

%files ui-gtk
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/ui-gtk.so

%if 0%{?suse_version} >= 1320 && 0%{?is_opensuse}
%files ui-sdl
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/ui-sdl.so
%endif

%files audio-alsa
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/audio-alsa.so

%files audio-pa
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/audio-pa.so

%if 0%{?suse_version} >= 1320 && 0%{?is_opensuse}
%files audio-sdl
%defattr(-, root, root)
%dir %_libdir/%name
%_libdir/%name/audio-sdl.so
%endif

%files lang -f %mybuilddir/%name.lang
%defattr(-, root, root)

%ifarch %{build_rom_arch}
%files seabios
%defattr(-, root, root)
%dir %_datadir/%name
%_datadir/%name/bios.bin
%_datadir/%name/bios-256k.bin

%files vgabios
%defattr(-, root, root)
%dir %_datadir/%name
%_datadir/%name/vgabios.bin
%_datadir/%name/vgabios-cirrus.bin
%_datadir/%name/vgabios-qxl.bin
%_datadir/%name/vgabios-stdvga.bin
%_datadir/%name/vgabios-virtio.bin
%_datadir/%name/vgabios-vmware.bin
%_datadir/%name/vgabios-bochs-display.bin
%_datadir/%name/vgabios-ramfb.bin

%files sgabios
%defattr(-, root, root)
%dir %_datadir/%name
%_datadir/%name/sgabios.bin

%files ipxe
%defattr(-, root, root)
%dir %_datadir/%name
%_datadir/%name/pxe-e1000.rom
%_datadir/%name/pxe-eepro100.rom
%_datadir/%name/pxe-ne2k_pci.rom
%_datadir/%name/pxe-pcnet.rom
%_datadir/%name/pxe-rtl8139.rom
%_datadir/%name/pxe-virtio.rom
%_datadir/%name/efi-e1000.rom
%_datadir/%name/efi-e1000e.rom
%_datadir/%name/efi-eepro100.rom
%_datadir/%name/efi-ne2k_pci.rom
%_datadir/%name/efi-pcnet.rom
%_datadir/%name/efi-rtl8139.rom
%_datadir/%name/efi-virtio.rom
%_datadir/%name/efi-vmxnet3.rom
%endif

%files tools
%defattr(-, root, root)
%_mandir/man1/qemu-img.1.gz
%_mandir/man1/virtfs-proxy-helper.1.gz
%_mandir/man8/qemu-nbd.8.gz
%_bindir/elf2dmp
%_bindir/ivshmem-client
%_bindir/ivshmem-server
%_bindir/qemu-edid
%_bindir/qemu-io
%_bindir/qemu-img
%_bindir/qemu-keymap
%_bindir/qemu-nbd
%_bindir/qemu-pr-helper
%_bindir/virtfs-proxy-helper
%verify(not mode) %attr(4750,root,kvm) %_libexecdir/qemu-bridge-helper
%dir %_sysconfdir/%name
%config %_sysconfdir/%name/bridge.conf
%_bindir/analyze-migration.py
%_bindir/vmstate-static-checker.py

%files guest-agent
%defattr(-, root, root)
%_mandir/man8/qemu-ga.8.gz
%attr(0755,root,kvm) %_bindir/qemu-ga
%{_unitdir}/qemu-ga@.service
%{_udevrulesdir}/80-qemu-ga.rules

%if 0%{?is_opensuse}
%files ksm
%defattr(-, root, root)
%{_unitdir}/ksm.service
%endif

%else # qemu-testsuite
%_datadir/qemu/check-report.tap
%endif

%changelog
