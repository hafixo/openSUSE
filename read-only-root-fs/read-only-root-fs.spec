#
# spec file for package read-only-root-fs
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           read-only-root-fs
Version:        1.0+git20190206.586e9f1
Release:        0
Summary:        Files and Scripts for a RO root fileystem
License:        GPL-2.0-or-later
Group:          System/Fhs
Url:            https://github.com/openSUSE/read-only-root-fs
Source:         read-only-root-fs-%{version}.tar.xz
Source1:        README.packaging.txt
BuildRequires:  dracut
Requires:       dracut
Requires(post): coreutils
Requires(post): gawk
# Required if system with new /etc/fstab entries is supposed to be updated
Conflicts:      transactional-update < 2.12
BuildArch:      noarch

%description
Files, scripts and directories to run the system with a
read-only root filesystem with %{_sysconfdir} writeable via overlayfs.

This package should never be installed in an already running
system! It should only be selected by a system role for a
read-only root filesystem with transactional updates.
The package will create / modify entries for mounting /etc and /var.
Those entries are used by dracut to mount the overlay file systems
during the early boot phase.

%package volatile
Summary:        Dracut Module to mount a tmpfs overlay on a RO root
Group:          System/Fhs
Requires:       dracut

%description volatile
A dracut module which mounts an overlayfs each on /etc and /var, with the upper
layer in a tmpfs mount. This is the minimal setup to get a booting system, to
have a writable /root or /home, additional fstab entries can be added.

%prep
%setup -q

%build

%install
cp -a usr %{buildroot}
mkdir -p %{buildroot}%{_localstatedir}/lib/overlay/work-etc

%post
if [ "$1" = 1 ] ; then
    %{_sbindir}/setup-fstab-for-overlayfs
    mkdir -p %{_localstatedir}/lib/overlay/1/etc
fi

%posttrans
if [ -f /etc/zypp/zypp.conf ]; then
    sed -i 's/^multiversion =.*/multiversion =/g' /etc/zypp/zypp.conf
fi
exit 0

%files
%license COPYING
%{_sbindir}/setup-fstab-for-overlayfs
%{_localstatedir}/lib/overlay
%{_prefix}/lib/dracut/dracut.conf.d/10-read-only-root-fs.conf
%{_prefix}/lib/systemd/system-preset/*

%files volatile
%license COPYING
%{_prefix}/lib/dracut/modules.d/99volatile-overlay/

%changelog
