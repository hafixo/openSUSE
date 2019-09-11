#
# spec file for package patterns-base
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


%bcond_with betatest
Name:           patterns-base
Version:        20190612
Release:        0
Summary:        Patterns for Installation (base patterns)
License:        MIT
Group:          Metapackages
URL:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
Source1:        pattern-definition-32bit.txt
Source2:        create_32bit-patterns_file.pl
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains all the base / core patterns (and those that don't fit well anywhere else).

################################################################################

# bsc#1088669 - only provide 32bit pattern for 64bit intel
%ifarch x86_64
%package 32bit
%pattern_basetechnologies
Summary:        32-Bit Runtime Environment
Group:          Metapackages
Provides:       pattern() = 32bit
Provides:       pattern-icon() = pattern-cli
Provides:       pattern-order() = 1180
Provides:       pattern-visible()
%if 0%{?is_opensuse}
Provides:       patterns-openSUSE-32bit = %{version}
Provides:       patterns-openSUSE-x86 = %{version}
Obsoletes:      patterns-openSUSE-32bit < %{version}
Obsoletes:      patterns-openSUSE-x86 < %{version}
%else
Provides:       patterns-sled-32bit = %{version}
Provides:       patterns-sles-32bit = %{version}
Obsoletes:      patterns-sled-32bit < %{version}
Obsoletes:      patterns-sles-32bit < %{version}
%endif

%description 32bit
This will install the 32-bit variant of all selected patterns. This allows to execute 32-bit software.

%files 32bit
%dir %{_docdir}/patterns
%{_docdir}/patterns/32bit.txt
%endif

################################################################################

%package apparmor
%pattern_basetechnologies
Summary:        AppArmor
Group:          Metapackages
Provides:       pattern() = apparmor
Provides:       pattern-icon() = pattern-apparmor
Provides:       pattern-order() = 1100
Provides:       pattern-visible()
%if 0%{?is_opensuse}
Provides:       patterns-openSUSE-apparmor = %{version}
Obsoletes:      patterns-openSUSE-apparmor < %{version}
%else
Provides:       patterns-sled-apparmor = %{version}
Provides:       patterns-sles-apparmor = %{version}
Obsoletes:      patterns-sled-apparmor < %{version}
Obsoletes:      patterns-sles-apparmor < %{version}
%endif
Requires:       pattern() = minimal_base
%if 0%{?is_opensuse}
Recommends:     pattern() = apparmor_opt
%endif

Requires:       apparmor-abstractions
Requires:       apparmor-parser
Requires:       apparmor-profiles
Recommends:     apparmor-docs
Recommends:     apparmor-utils
Recommends:     yast2-apparmor
Suggests:       pam_apparmor
%if 0%{?is_opensuse}
Requires:       audit
%else
Recommends:     audit
%endif

%description apparmor
AppArmor is an application security framework that provides mandatory access control for programs. It protects from exploitation of software flaws and compromised systems. It offers an advanced tool set that automates the development of per-program application security without requiring additional knowledge.

%files apparmor
%dir %{_docdir}/patterns
%{_docdir}/patterns/apparmor.txt

################################################################################

%if 0%{?is_opensuse}
%package apparmor_opt
%pattern_basetechnologies
Summary:        AppArmor
Group:          Metapackages
Provides:       pattern() = apparmor_opt
Provides:       pattern-extends() = apparmor
Provides:       pattern-icon() = pattern-apparmor
Provides:       pattern-order() = 1080
# Keep these grouped
Provides:       patterns-openSUSE-apparmor_opt = %{version}
Obsoletes:      patterns-openSUSE-apparmor_opt < %{version}
Requires:       pattern() = minimal_base

Requires:       apparmor-docs

%description apparmor_opt
AppArmor is an application security framework that provides mandatory access control for programs. It protects from exploitation of software flaws and compromised systems. It offers an advanced tool set that automates the development of per-program application security without requiring additional knowledge.

%files apparmor_opt
%dir %{_docdir}/patterns
%{_docdir}/patterns/apparmor_opt.txt
%endif

################################################################################

%package basesystem
%pattern_basetechnologies
Summary:        Minimal Base System (alias pattern for base)
Group:          Metapackages
Provides:       pattern() = basesystem
Provides:       pattern-icon() = pattern-basis
Requires:       pattern() = minimal_base

%description basesystem
This is the base runtime system.  It contains only a minimal multiuser booting system. For running on real hardware, you need to add additional packages and pattern to make this pattern useful on its own.

%files basesystem
%dir %{_docdir}/patterns
%{_docdir}/patterns/basesystem.txt

################################################################################

%package base
%pattern_basetechnologies
Summary:        Minimal Base System
Group:          Metapackages
Provides:       pattern() = base
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1030
Provides:       pattern-visible()
%if 0%{?is_opensuse}
Provides:       patterns-openSUSE-base = %{version}
Obsoletes:      patterns-openSUSE-base < %{version}
%else
Provides:       patterns-sles-base
Provides:       patterns-sles-minimal
Obsoletes:      patterns-sles-base < %{version}
Obsoletes:      patterns-sles-minimal < %{version}
%endif
Requires:       pattern() = minimal_base

Requires:       e2fsprogs
Requires:       kmod
Requires:       openssh
Requires:       polkit
Requires:       polkit-default-privs
Requires:       shadow
Requires:       util-linux
Requires:       which
%if ! 0%{?is_opensuse}
Requires:       systemd-coredump
%endif
# Add some static base tool in case system explodes; Recommend only, as users are free to uninstall it
Recommends:     busybox-static
Recommends:     bash-completion
Recommends:     btrfsprogs
Recommends:     ca-certificates-mozilla
Recommends:     chrony
Recommends:     cron
# we rely on cron for daily/hourly
Recommends:     cronie
Recommends:     grub2
Recommends:     glibc-locale
Recommends:     systemd-sysvinit
Recommends:     snapper

%if 0%{?is_opensuse}
# get it branded
Recommends:     branding-openSUSE
%else
Recommends:     branding-SLE
%endif
%ifarch x86_64
Recommends:     efibootmgr
Recommends:     shim
Recommends:     grub2-x86_64-efi
%endif
%ifarch aarch64
Recommends:     shim
Recommends:     grub2-arm64-efi
%endif
%ifarch %arm
Recommends:     efibootmgr
Recommends:     grub2-arm-efi
%endif
%ifarch ppc ppc64 ppc64le
%if !0%{?is_opensuse}
Recommends:     lshw
Recommends:     lsvpd
%endif
%endif
%ifarch ppc64 ppc64le
# bsc#1098849
Requires:       ppc64-diag
%endif
# Current systems suffer from entropy starvation (bsc#1131369)
%ifarch aarch64 %ix86 x86_64 ppc64 ppc64le s390x
Recommends:     haveged
%endif
# issue-generator is not used on Leap so far
%if !(0%{?is_opensuse} && 0%{?sle_version})
Recommends:     issue-generator
%endif

%description base
This is the base runtime system.  It contains only a minimal multiuser booting system. For running on real hardware, you need to add additional packages and pattern to make this pattern useful on its own.

%files base
%dir %{_docdir}/patterns
%{_docdir}/patterns/base.txt

################################################################################

# This pattern contains everything the SLES x11 package used to have that
# doesn't need to be in the openSUSE x11 package
%package basic_desktop
%pattern_graphicalenvironments
Summary:        A very basic desktop (previously part of x11 pattern)
Group:          Metapackages
Provides:       pattern() = basic_desktop
Provides:       pattern-icon() = pattern-desktop
Provides:       pattern-order() = 1802
Provides:       pattern-visible()
# We want SLES-15 systems to install this pattern on upgrade to SLES-16
%if !0%{?is_opensuse}
Obsoletes:      patterns-base-x11 < %{version}
%endif
Requires:       pattern() = x11

# choose icewm-default if you have a choice
# icewm-lite is too lightweight in new release
Requires:       icewm-default
Requires:       icewm-theme-branding
Recommends:     libgnomesu
Recommends:     openssh-askpass-gnome

%description basic_desktop
This pattern installs a rather basic desktop (icewm) 

%files basic_desktop
%dir %{_docdir}/patterns
%{_docdir}/patterns/basic_desktop.txt

################################################################################

%if 0%{?is_opensuse}
%package console
%pattern_basetechnologies
Summary:        Console Tools
Group:          Metapackages
Provides:       pattern() = console
Provides:       pattern-icon() = pattern-cli
Provides:       pattern-order() = 1120
Provides:       pattern-visible()
# Keep these grouped
Provides:       patterns-openSUSE-console = %{version}
Obsoletes:      patterns-openSUSE-console < %{version}
Requires:       pattern() = enhanced_base
Recommends:     pattern() = yast2_basis

Recommends:     at
Recommends:     bc
Recommends:     ed
Recommends:     emacs-nox
Recommends:     libyui-ncurses
Recommends:     libyui-ncurses-pkg
Recommends:     mc
Recommends:     mosh
Recommends:     mtools
Recommends:     sensors
Recommends:     susepaste
Recommends:     susepaste-screenshot
Recommends:     tmux
Recommends:     w3m
Suggests:       alpine
Suggests:       bsd-games
Suggests:       cnetworkmanager
Suggests:       convert
Suggests:       dar
Suggests:       ding
Suggests:       gcal
Suggests:       grepmail
Suggests:       irssi
Suggests:       lftp
Suggests:       links
Suggests:       lynx
Suggests:       minicom
Suggests:       mlocate
Suggests:       mutt
Suggests:       ncftp
Suggests:       pico
Suggests:       pinfo
Suggests:       slrn
Suggests:       units
Suggests:       vlock

%description console
Applications useful for those using the console and no graphical desktop environment.

%files console
%dir %{_docdir}/patterns
%{_docdir}/patterns/console.txt
%endif

################################################################################

%package documentation
%pattern_documentation
Summary:        Help and Support Documentation
Group:          Metapackages
Provides:       pattern() = documentation
Provides:       pattern-icon() = pattern-documentation
Provides:       pattern-order() = 1005
Provides:       pattern-visible()
Requires:       pattern() = basesystem
%if !0%{?is_opensuse}
Provides:       patterns-sled-documentation
Obsoletes:      patterns-sles-documentation < %{version}
%endif

Recommends:     info2html
Recommends:     man-pages
# note pam is in every install so no point in using packageand
Recommends:     pam-doc
Recommends:     susehelp
Recommends:     susehelp_en
%if !0%{?is_opensuse}
Recommends:     sled-admin_en-pdf
Recommends:     sled-gnomeuser_en-pdf
Recommends:     sled-manuals_en-pdf
Recommends:     sled-security_en-pdf
Recommends:     sled-tuning_en-pdf
%endif

%description documentation
Help and Support Documentation

%files documentation
%dir %{_docdir}/patterns
%{_docdir}/patterns/documentation.txt

################################################################################

%package enhanced_base
%pattern_basetechnologies
Summary:        Enhanced Base System
Group:          Metapackages
Provides:       pattern() = enhanced_base
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1060
Provides:       pattern-visible()
%if 0%{?is_opensuse}
Provides:       patterns-openSUSE-enhanced_base = %{version}
Obsoletes:      patterns-openSUSE-enhanced_base < %{version}
%endif
Requires:       pattern() = base
Recommends:     pattern() = apparmor
Recommends:     pattern() = sw_management
Recommends:     pattern() = yast2_basis
%if 0%{?is_opensuse}
Recommends:     pattern() = enhanced_base_opt
%endif

Recommends:     aaa_base-extras
# getfacl and setfacl
Recommends:     acl
# #302569
Recommends:     alsa-plugins
# getattr and setattr
Recommends:     attr
Recommends:     autofs
Recommends:     bind-utils
Recommends:     binutils
# compressor is interesting
Recommends:     bzip2
# #375103
Recommends:     cifs-utils
Recommends:     command-not-found
Recommends:     cpio
Recommends:     cpupower
Recommends:     cronie
Recommends:     cryptsetup
# cups server for remote printing queues
Recommends:     cups
# printing considered cool
Recommends:     cups-client
Recommends:     curl
Recommends:     cyrus-sasl
Recommends:     cyrus-sasl-crammd5
Recommends:     cyrus-sasl-digestmd5
Recommends:     cyrus-sasl-gssapi
Recommends:     cyrus-sasl-plain
# bnc#430895
# cyrus-sasl-saslauthd
# delta rpms are considered cool for updates
Recommends:     deltarpm
Recommends:     diffutils
Recommends:     dos2unix
Recommends:     e2fsprogs
Recommends:     ethtool
Recommends:     file
Recommends:     fillup
Recommends:     findutils
# firewall by default
Recommends:     firewalld
Recommends:     fuse
Recommends:     gawk
Recommends:     gettext-runtime
Recommends:     glibc-locale
Recommends:     gpart
Recommends:     gpg2
Recommends:     gpm
Recommends:     grep
Recommends:     gzip
Recommends:     hdparm
Recommends:     hwinfo
Recommends:     info
Recommends:     initviocons
# /bin/ip considered useful
Recommends:     iproute2
# ping is required for network tests
Recommends:     iputils
Recommends:     irqbalance
Recommends:     joe
Recommends:     kmod-compat
# #303857
Recommends:     kpartx
Recommends:     krb5
# pager
Recommends:     less
Recommends:     logrotate
Recommends:     lsscsi
Recommends:     mailx
# man by default (#304687)
Recommends:     man
# needed for detecting software raid - required by yast2-storage too
Recommends:     mdadm
Recommends:     multipath-tools
# split out of ncurses
Recommends:     ncurses-utils
Recommends:     net-snmp
Recommends:     netcat-openbsd
Recommends:     netcfg
Recommends:     nfs-client
Recommends:     nfsidmap
Recommends:     nscd
# mount NTFS rw (bsc#1087242)
Recommends:     ntfs-3g
Recommends:     ntfsprogs
Recommends:     openslp
# we want a ssh server to be available
Recommends:     openssh
# TODO: should this be in more places
Recommends:     pam-config
Recommends:     parted
Recommends:     pciutils
Recommends:     pciutils-ids
Recommends:     perl-Bootloader
Recommends:     perl-base
Recommends:     pinentry
Recommends:     postfix
# fuser (psmisc) by default (#304694)
Recommends:     psmisc
Recommends:     rsync
%if 0%{?sle_version}
# in SLE we still want /var/log/messages as all of the docu refers to it
# TODO: if we still want it everywhere it should move back to base
Recommends:     rsyslog
%else
# go for journal in TW (boo#1143144)
Recommends:     systemd-logger
%endif
# Bug 424707 - Feature "Command not found" for openSUSE by default
Recommends:     scout
Recommends:     screen
Recommends:     sed
Recommends:     sg3_utils
Recommends:     smartmontools
Recommends:     sudo
Recommends:     sysconfig
#SUSE hardware tunings
Recommends:     system-tuning-common-SUSE
Recommends:     systemd-sysvinit
Recommends:     time
Recommends:     timezone
Recommends:     translation-update
Recommends:     udev
# autoconfig new printers - bnc#808014
Recommends:     udev-configure-printer
# lsusb is good for debugging USB devices - #401593
Recommends:     usbutils
# Our editor of choice
Recommends:     vim
Recommends:     wget
Recommends:     xz
Recommends:     zisofs-tools
# DELL computers mainly #403270, but #441079
Suggests:       biosdevname
Suggests:       cpupower
# #437252
Suggests:       pam_ssh
Suggests:       xfsprogs
Suggests:       zip
%ifarch aarch64 %ix86 x86_64
Recommends:     dmidecode
%endif
%ifarch ppc
Recommends:     hfsutils
%endif
%ifarch ppc
# #303737
Recommends:     mouseemu
Recommends:     pdisk
Recommends:     powerpc32
%endif
# openSUSE Branding packages first
%if 0%{?is_opensuse}
# we want a branded grub2 too #757683
Recommends:     grub2-branding-openSUSE
Recommends:     plymouth
Recommends:     plymouth-branding-openSUSE
Recommends:     release-notes-openSUSE
%else
Recommends:     grub2-branding-SLE
Recommends:     plymouth
%endif
# Other packages we have in openSUSE and not SLE-15
%if 0%{?is_opensuse}
Recommends:     dmraid
Recommends:     dosfstools
Recommends:     ifplugd
Recommends:     klogd
# boo#1034493
Recommends:     nano
Recommends:     openldap2-client
Recommends:     prctl
# fuser (psmisc) by default (#304694)
Recommends:     psmisc
Recommends:     smp_utils
# useful for debugging
Recommends:     strace
Recommends:     syslinux
# having a ftp command line client is good for moving log files
Recommends:     tnftp
Recommends:     tuned
Recommends:     wireless-tools
Recommends:     wol
%ifarch %ix86 x86_64
Recommends:     acpica
%endif
%ifarch x86_64
Recommends:     mcelog
%endif
%ifarch aarch64 x86_64
Recommends:     numactl
%endif
%ifarch %ix86 x86_64
Recommends:     ucode-amd
Recommends:     ucode-intel
%endif
%endif

%description enhanced_base
This is the enhanced base runtime system with lots of convenience packages.

%files enhanced_base
%dir %{_docdir}/patterns
%{_docdir}/patterns/enhanced_base.txt

################################################################################

%if 0%{?is_opensuse}
%package enhanced_base_opt
%pattern_basetechnologies
Summary:        Enhanced Base System
Group:          Metapackages
Provides:       pattern() = enhanced_base_opt
Provides:       pattern-extends() = enhanced_base
Provides:       pattern-icon() = pattern-software-management
Provides:       pattern-order() = 1040
# Keep these grouped
Provides:       patterns-openSUSE-enhanced_base_opt = %{version}
Obsoletes:      patterns-openSUSE-enhanced_base_opt < %{version}

Recommends:     joe
Recommends:     mpt-status
Recommends:     perl-TermReadLine-Gnu
Recommends:     prctl
Recommends:     procinfo
Recommends:     procmail
Recommends:     providers
Recommends:     setserial
Recommends:     sharutils
Recommends:     spax
Recommends:     strace
Recommends:     tcpdump
Recommends:     telnet
Recommends:     terminfo
Recommends:     vlan
Recommends:     wol
Suggests:       acpid
Suggests:       cracklib-dict-full
# needed as soon as you want to do kerberos authentication
Suggests:       cyrus-sasl-gssapi
Suggests:       delayacct-utils
Suggests:       groff
Suggests:       hfsutils
# bnc#388570
Suggests:       kerneloops
Suggests:       man-pages
Suggests:       man-pages-posix
Suggests:       ocfs2-tools
Suggests:       pwgen
Suggests:       unzip
Suggests:       w3m-el
# delta apply
Suggests:       xdelta
# tool for xfs
Suggests:       xfsdump
# #754959
%ifarch %ix86 x86_64
Suggests:       hyper-v
%endif

%description enhanced_base_opt
This is the enhanced base runtime system with lots of convenience packages.

%files enhanced_base_opt
%dir %{_docdir}/patterns
%{_docdir}/patterns/enhanced_base_opt.txt
%endif

################################################################################

%package minimal_base
%pattern_basetechnologies
Summary:        Minimal Appliance Base
Group:          Metapackages
Provides:       pattern() = minimal_base
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 5190
Provides:       pattern-visible()
# Keep these grouped
Provides:       patterns-openSUSE-minimal_base = %{version}
Obsoletes:      patterns-openSUSE-minimal_base < %{version}

Requires:       aaa_base
Requires:       bash
Requires:       coreutils
Requires:       device-mapper
Requires:       distribution-release
Requires:       dracut
Requires:       filesystem
Requires:       glibc
Requires:       iproute2
Requires:       kbd
Requires:       pam
Requires:       procps
Requires:       rpm
Requires:       sysconfig
Requires:       system-group-hardware
Requires:       system-group-wheel
Requires:       system-user-bin
Requires:       system-user-daemon
Requires:       system-user-nobody
Requires:       systemd
Requires:       udev
Requires:       zypper
# Note it makes no sense to recommend packages in minimal_base as it can't
# be installed with --no-recommends if your package can be Recommended rather
# then required it likely belongs in base and not here.
# rollback-helper is useful on Leap / SLE but not tumbleweed
%if 0%{?sle_version}
Requires:       rollback-helper
%endif
%if 0%{?is_opensuse}
Requires:       openSUSE-build-key
# There are two release packages in the repo, pick this over openSUSE-Tumbleweed-Kubic-release
Suggests:       openSUSE-release
%else
Requires:       SUSEConnect
Requires:       rollback_helper
Requires:       suse-build-key
%endif

%if 0%{?is_opensuse}
%description minimal_base
This is the minimal openSUSE runtime system. It is really a minimal system, you can login and a shell will be started, that's all. It is intended as base for Appliances.
%else
%description minimal_base
This is the minimal SLE runtime system. It is really a minimal system, you can login and a shell will be started, that's all. It is intended as base for Appliances.
%endif

%files minimal_base
%dir %{_docdir}/patterns
%{_docdir}/patterns/minimal_base.txt

################################################################################

%package transactional_base
%pattern_basetechnologies
Summary:        Transactional Base System
Group:          Metapackages
Provides:       pattern() = transactional_base
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 1050
Obsoletes:      pattern() = readonly_root_tools
Requires:       pattern() = base

Requires:       read-only-root-fs
Requires:       rebootmgr
Requires:       systemd-presets-branding-transactional-server
Requires:       transactional-update
Requires:       transactional-update-zypp-config
Recommends:     pattern() = enhanced_base
Suggests:       health-checker

%description transactional_base
This is the base system for a host updated by Transactional Updates. Includes Tools for systems with a read-only root filesystem.

%files transactional_base
%dir %{_docdir}/patterns
%{_docdir}/patterns/transactional_base.txt

################################################################################

%package sw_management
%pattern_basetechnologies
Summary:        Software Management
Group:          Metapackages
Provides:       pattern() = sw_management
Provides:       pattern-icon() = pattern-software-management
Provides:       pattern-order() = 1360
Provides:       pattern-visible()
%if 0%{?is_opensuse}
Provides:       patterns-openSUSE-sw_management = %{version}
Obsoletes:      patterns-openSUSE-sw_management < %{version}
%endif
%if 0%{?sle_version}
Recommends:     pattern() = sw_management_x11

# Zypper is the basic sw_management stack for *SUSE
Requires:       zypper
Recommends:     lifecycle-data
Recommends:     zypper-lifecycle-plugin
%endif

%description sw_management
This pattern provides a graphical application and a command line tool for keeping your system up to date.

%files sw_management
%dir %{_docdir}/patterns
%{_docdir}/patterns/sw_management.txt

################################################################################

%if 0%{?is_opensuse}
%package update_test
%pattern_basetechnologies
Summary:        Tests for the Update Stack
Group:          Metapackages
Provides:       pattern() = update_test
Provides:       pattern-icon() = pattern-tests
Provides:       pattern-order() = 1380
Provides:       pattern-visible()
# Keep these grouped
Provides:       patterns-openSUSE-update_test = %{version}
Obsoletes:      patterns-openSUSE-update_test < %{version}

Recommends:     update-test-affects-package-manager
Recommends:     update-test-interactive
Recommends:     update-test-optional
Recommends:     update-test-reboot-needed
Recommends:     update-test-security
Recommends:     update-test-trival
%if %{with betatest}
Recommends:     aaa_base-malloccheck
Supplements:    %{name}-base
%endif

%description update_test
Packages used for testing that the update stack works.  These tiny packages do not have any functionality themselves.

%files update_test
%dir %{_docdir}/patterns
%{_docdir}/patterns/update_test.txt
%endif

################################################################################

%package x11
%pattern_graphicalenvironments
Summary:        X Window System
Group:          Metapackages
Provides:       pattern() = x11
Provides:       pattern-icon() = pattern-x11
Provides:       pattern-order() = 1800
Provides:       pattern-visible()
%if 0%{?is_opensuse}
Provides:       patterns-openSUSE-x11 = %{version}
Obsoletes:      patterns-openSUSE-x11 < %{version}
%endif
Requires:       pattern() = base
%if 0%{?is_opensuse}
Recommends:     pattern() = x11_enhanced
Recommends:     pattern() = x11_opt
%endif

Requires:       xorg-x11-fonts-core
Requires:       xorg-x11-server
Requires:       yast2-qt
Recommends:     dejavu-fonts
Recommends:     libyui-qt
Recommends:     libyui-qt-pkg
# Recommend lightdm so it gets installed by default
# rather then xdm bsc#1081760
# Todo: Require DisplayManger and suggest lightdm
Recommends:     lightdm
Recommends:     noto-sans-fonts
Recommends:     tigervnc
Recommends:     x11-tools
Recommends:     xdmbgrd
Recommends:     xorg-x11-Xvnc
Recommends:     xorg-x11-driver-video
Recommends:     xorg-x11-essentials
Recommends:     xorg-x11-fonts
Recommends:     xorg-x11-server-extra
Recommends:     xterm
Recommends:     xtermset
Recommends:     yast2-control-center

# bsc#1071953
%ifnarch s390 s390x
Requires:       xf86-input-libinput
Recommends:     xf86-input-vmmouse
Recommends:     xf86-input-wacom
%endif

%description x11
The X Window System provides the only standard platform-independent networked graphical window system bridging the heterogeneous platforms in today's enterprise: from network servers to desktops, thin clients, laptops, and handhelds, independent of operating system and hardware.

%files x11
%dir %{_docdir}/patterns
%{_docdir}/patterns/x11.txt

################################################################################

%package x11_enhanced
%pattern_graphicalenvironments
Summary:        X Window System
Group:          Metapackages
Provides:       pattern() = x11_enhanced
Provides:       pattern-icon() = pattern-x11
Provides:       pattern-order() = 1801
%if 0%{?is_opensuse}
Obsoletes:      patterns-openSUSE-x11 < %{version}
%else
Provides:       patterns-sled-minimal
Obsoletes:      patterns-sled-minimal < %{version}
%endif
Requires:       pattern() = enhanced_base
Requires:       pattern() = fonts
Requires:       pattern() = x11
Recommends:     pattern() = x11_yast
%if 0%{?is_opensuse}
Recommends:     pattern() = x11_opt
%endif

# 1057377
Requires:       glibc-locale
Requires:       xkeyboard-config
Requires:       xorg-x11-essentials
# make it possible to install firefox or chromium
Recommends:     web_browser
Recommends:     cabextract
Recommends:     command-not-found
Recommends:     dbus-1-glib
Recommends:     dbus-1-x11
Recommends:     dialog
Recommends:     fontconfig
Recommends:     fonts-config
Recommends:     fribidi
Recommends:     ghostscript-x11
Recommends:     numlockx
Recommends:     opensuse-welcome
# #353229 - drag in empty replacements
Recommends:     translation-update
Recommends:     xauth
Recommends:     xdmbgrd
Recommends:     xkeyboard-config
Recommends:     xorg-x11-fonts
Recommends:     xorg-x11-fonts-core
Recommends:     yast2-control-center-gnome
Recommends:     yast2-scanner
# This will install Firefox if no other browser is selected
Suggests:       MozillaFirefox
Suggests:       MozillaFirefox-translations

%if 0%{?is_opensuse}
# #394406
Suggests:       desktop-data-openSUSE-extra
%else
Recommends:     MozillaFirefox-branding-SLE
Recommends:     desktop-data-SLE
%endif
%if 0%{?is_opensuse}
# people love having numlock configurable
Recommends:     numlockx
Recommends:     openssh-askpass
Recommends:     susepaste
Recommends:     susepaste-screenshot
Suggests:       gvim
Suggests:       hexchat
Suggests:       wpa_supplicant-gui
%endif

%description x11_enhanced
The X Window System provides the only standard platform-independent networked graphical window system bridging the heterogeneous platforms in today's enterprise: from network servers to desktops, thin clients, laptops, and handhelds, independent of operating system and hardware.

%files x11_enhanced
%dir %{_docdir}/patterns
%{_docdir}/patterns/x11_enhanced.txt

################################################################################

%if 0%{?is_opensuse}
%package x11_opt
%pattern_graphicalenvironments
Summary:        X Window System
Group:          Metapackages
Provides:       pattern() = x11_opt
Provides:       pattern-extends() = x11
Provides:       pattern-icon() = pattern-x11
Provides:       pattern-order() = 1680
# Keep these grouped
Provides:       patterns-openSUSE-x11_opt = %{version}
Obsoletes:      patterns-openSUSE-x11_opt < %{version}
Requires:       pattern() = enhanced_base
Requires:       pattern() = fonts
# needed e.g. for nvidia drivers
# #302566
Recommends:     x11-tools
Recommends:     xorg-x11-libX11-ccache
Suggests:       MozillaThunderbird
Suggests:       WindowMaker
Suggests:       WindowMaker-applets
Suggests:       WindowMaker-themes
Suggests:       unclutter
Suggests:       xlockmore
Suggests:       xorg-x11-driver-video-radeonhd
Suggests:       xorg-x11-driver-video-unichrome
# #389816
Suggests:       xorg-x11-server-sdk

%description x11_opt
The X Window System provides the only standard platform-independent networked graphical window system bridging the heterogeneous platforms in today's enterprise: from network servers to desktops, thin clients, laptops, and handhelds, independent of operating system and hardware.

%files x11_opt
%dir %{_docdir}/patterns
%{_docdir}/patterns/x11_opt.txt
%endif

################################################################################

%ifarch armv6hl armv7hl aarch64
%package x11_raspberrypi
%pattern_graphicalenvironments
Summary:        X Window System
Group:          Metapackages
Provides:       pattern() = x11_raspberrypi
Provides:       pattern-icon() = pattern-x11
Provides:       pattern-order() = 1803
Provides:       pattern-visible()
# Use only Requires - it's meant to be used on JeOS, which ignores Recommends
# Based on SUSE:SLE-15:GA:RaspberryPI/kiwi-templates-SLES15-JeOS/JeOS.kiwi
# Patterns
Requires:       pattern() = base
Requires:       pattern() = x11
# Drivers
Requires:       xf86-input-evdev
Requires:       xf86-input-libinput
Requires:       xf86-video-fbdev
# Other X11 packages
Requires:       gconf2
Requires:       gtk2-metatheme-adwaita
Requires:       gtk3-metatheme-adwaita
Requires:       x11-tools
Requires:       x11perf
Requires:       xauth
Requires:       xbacklight
Requires:       xclock
Requires:       xconsole
Requires:       xcursor-themes
Requires:       xcursorgen
Requires:       xdg-user-dirs
Requires:       xdg-user-dirs-gtk
Requires:       xdg-user-dirs-gtk-lang
Requires:       xdg-utils
Requires:       xdm
Requires:       xdmbgrd
Requires:       xdpyinfo
Requires:       xev
Requires:       xeyes
Requires:       xfd
Requires:       xfontsel
Requires:       xgamma
Requires:       xhost
Requires:       xinit
Requires:       xinput
Requires:       xkbcomp
Requires:       xkbevd
Requires:       xkbprint
Requires:       xkbutils
Requires:       xkeyboard-config
Requires:       xkill
Requires:       xlogo
Requires:       xlsatoms
Requires:       xlsclients
Requires:       xlsfonts
Requires:       xmag
Requires:       xmessage
Requires:       xmodmap
Requires:       xorg-x11
Requires:       xorg-x11-fonts-core
Requires:       xorg-x11-server
Requires:       xorg-x11-server-extra
Requires:       xprop
Requires:       xrandr
Requires:       xrdb
Requires:       xrestop
Requires:       xscope
Requires:       xscreensaver
Requires:       xscreensaver-data
Requires:       xset
Requires:       xsetmode
Requires:       xsetpointer
Requires:       xsetroot
Requires:       xterm
Requires:       xtermset
Requires:       xvinfo
Requires:       xwd
Requires:       xwininfo
Requires:       yast2-packager
Requires:       yast2-snapper
Requires:       yast2-x11
# bsc#1095870
Requires:       libyui-ncurses-pkg
Requires:       libyui-qt-pkg
Requires:       yast2-control-center-qt
# Branding
%if ! 0%{?is_opensuse}
Requires:       MozillaFirefox-branding-SLE
%endif
# X11/IceWM-specific packages
Requires:       icewm
Requires:       icewm-default
Requires:       icewm-lite
Requires:       icewm-theme-branding
Requires:       polkit-default-privs
Requires:       polkit-gnome-lang
# for IceWM taskbar mailbox icon (bsc#1093913)
Requires:       mutt
Requires:       mutt-lang

%description x11_raspberrypi
The X Window System provides the only standard platform-independent networked graphical window system bridging the heterogeneous platforms in today's enterprise: from network servers to desktops, thin clients, laptops, and handhelds, independent of operating system and hardware.

%files x11_raspberrypi
%dir %{_docdir}/patterns
%{_docdir}/patterns/x11_raspberrypi.txt
%endif

################################################################################

%prep

%build

%install
mkdir -p %{buildroot}%{_docdir}/patterns
%if 0%{?is_opensuse}
for i in apparmor base enhanced_base minimal_base \
     sw_management x11 x11_enhanced; do
%else
for i in apparmor base basic_desktop enhanced_base  minimal_base sw_management x11 x11_enhanced; do
%endif
    echo "This file marks the pattern $i to be installed." \
    >"%{buildroot}%{_docdir}/patterns/$i.txt"
    echo "This file marks the pattern $i to be installed." \
    >"%{buildroot}%{_docdir}/patterns/$i-32bit.txt"
done

# These packages don't generate a 32bit pattern
for i in \
%if 0%{?is_opensuse}
apparmor_opt basesystem basic_desktop console documentation enhanced_base_opt transactional_base update_test x11_opt \
%else
%ifnarch s390 s390x
32bit \
%endif
basesystem basic_desktop documentation \
%endif
%ifarch armv6hl armv7hl aarch64
x11_raspberrypi \
%endif
; do
    echo "This file marks the pattern $i to be installed." \
    >"%{buildroot}%{_docdir}/patterns/$i.txt"
done

%ifarch x86_64
echo "This file marks the pattern 32bit to be installed." \
>"%{buildroot}%{_docdir}/patterns/32bit.txt"
%endif

#
# This file is created at check-in time. Sorry for the inconsistent workflow :(
#
%include %{SOURCE1}

%changelog
