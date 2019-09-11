#
# spec file for package shadow
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


Name:           shadow
Version:        4.7
Release:        0
Summary:        Utilities to Manage User and Group Accounts
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          System/Base
URL:            https://github.com/shadow-maint/shadow
Source:         https://github.com/shadow-maint/shadow/releases/download/%{version}/shadow-%{version}.tar.xz
Source1:        pamd.tar.bz2
Source2:        README.changes-pwdutils
Source3:        useradd.local
Source4:        userdel-pre.local
Source5:        userdel-post.local
Source6:        shadow.service
Source7:        shadow.timer
Source42:       https://github.com/shadow-maint/shadow/releases/download/%{version}/shadow-%{version}.tar.xz.asc
Source43:       %{name}.keyring
# SOURCE-FEATURE-SUSE shadow-login_defs-check.sh sbrabec@suse.com -- Supplementary script that verifies coverage of variables in shadow-login_defs-unused-by-pam.patch and other patches.
Source44:       shadow-login_defs-check.sh
# PATCH-FIX-SUSE shadow-login_defs-unused-by-pam.patch kukuk@suse.com -- Remove variables that have no use with PAM.
Patch0:         shadow-login_defs-unused-by-pam.patch
# PATCH-FEATURE-SUSE userdel-script.patch kukuk@suse.com -- Add support for USERDEL_PRECMD and USERDEL_POSTCMD.
Patch1:         userdel-script.patch
# PATCH-FEATURE-SUSE useradd-script.patch kukuk@suse.com -- Add support for USERADD_CMD.
Patch2:         useradd-script.patch
# PATCH-FEATURE-SUSE chkname-regex.patch kukuk@suse.com -- Username restriction by regex.
Patch3:         chkname-regex.patch
# PATCH-FEATURE-SUSE useradd-default.patch kukuk@suse.com -- Change useradd defaults group to 1000.
Patch4:         useradd-default.patch
# PATCH-FEATURE-SUSE shadow-util-linux.patch sbrabec@suse.com -- Add support for util-linux specific variables, delete shadow login, su runuser specific.
Patch5:         shadow-util-linux.patch
# PATCH-FEATURE-FEDORA shadow-4.1.5.1-userdel-helpfix.patch christian.brauner@mailbox.org -- Give a hint about what happens when you force the removal of a user.
Patch6:         shadow-4.1.5.1-userdel-helpfix.patch
# PATCH-FIX-FEDORA shadow-4.1.5.1-logmsg.patch kukuk@suse.com -- Fix error message.
Patch7:         shadow-4.1.5.1-logmsg.patch
# PATCH-FEATURE-SUSE encryption_method_nis.patch kukuk@suse.com -- Add support for ENCRYPT_METHOD_NIS used by SUSE patch in pam (pam_unix).
Patch10:        encryption_method_nis.patch
# PATCH-FEATURE-SUSE shadow-login_defs-comments.patch kukuk@suse.com -- Adjust login.defs comments.
Patch13:        shadow-login_defs-comments.patch
# PATCH-FEATURE-SUSE shadow-login_defs-suse.patch kukuk@suse.com -- Customize login.defs.
Patch14:        shadow-login_defs-suse.patch
# PATCH-FIX-SUSE disable_new_audit_function.patch adam.majer@suse.de -- Disable newer libaudit functionality for older distributions.
Patch20:        disable_new_audit_function.patch
# PATCH-FIX-UPSTREAM shadow-usermod-variable.patch https://github.com/shadow-maint/shadow/pull/170 sbrabec@suse.com -- Fix variable name.
Patch21:        shadow-usermod-variable.patch
BuildRequires:  audit-devel > 2.3
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  libselinux-devel
BuildRequires:  libsemanage-devel
BuildRequires:  libtool
BuildRequires:  pam-devel
BuildRequires:  xz
Requires(pre):  group(root)
Requires(pre):  group(shadow)
Requires(pre):  permissions
Requires(pre):  user(root)
Provides:       pwdutils = 3.2.20
Obsoletes:      pwdutils <= 3.2.19
# Virtual provides for supported variables in login.defs.
# It prevents references to unknown variables.
# Upgrade them only if shadow-util-linux.patch or
# encryption_method_nis.patch has to be ported!
# Call shadow-login_defs-check.sh before!
Provides:       login_defs-support-for-pam = 1.3.1
Provides:       login_defs-support-for-util-linux = 2.33.1
Provides:       useradd_or_adduser_dep

%description
This package includes the necessary programs for converting plain
password files to the shadow password format and to manage user and
group accounts.

%prep
%setup -q -a 1
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
%patch10
%patch13
%patch14
%if 0%{?suse_version} < 1330
%patch20 -p1
%endif
%patch21 -p1

iconv -f ISO88591 -t utf-8  doc/HOWTO > doc/HOWTO.utf8
mv -v doc/HOWTO.utf8 doc/HOWTO

%build
export CFLAGS="%{optflags} -fpie"
export LDFLAGS="-pie"

autoreconf -fvi
%configure \
  --disable-shadowgrp \
  --enable-account-tools-setuid \
  --with-audit \
  --with-libpam \
  --with-sha-crypt \
  --with-acl \
  --with-attr \
  --with-nscd \
  --with-selinux \
  --without-libcrack \
  --disable-shared \
  --with-group-name-max-length=32
make %{?_smp_mflags} V=1

%install
cp %{SOURCE2} .
%make_install gnulocaledir=%{buildroot}/%{_datadir}/locale MKINSTALLDIRS=`pwd`/mkinstalldirs

# install useradd.local, userdel.local, ...
install -m 0755 %{SOURCE3} %{buildroot}/%{_sbindir}/
install -m 0755 %{SOURCE4} %{buildroot}/%{_sbindir}/
install -m 0755 %{SOURCE5} %{buildroot}/%{_sbindir}/
install -Dm644 %{SOURCE6} %{buildroot}%{_unitdir}/shadow.service
install -Dm644 %{SOURCE7} %{buildroot}%{_unitdir}/shadow.timer

# add empty /etc/sub{u,g}id files
touch %{buildroot}/%{_sysconfdir}/subuid
touch %{buildroot}/%{_sysconfdir}/subgid

# Remove binaries we don't use.
rm %{buildroot}/%{_bindir}/groups
rm %{buildroot}/%{_mandir}/man1/groups.*
rm %{buildroot}/%{_mandir}/*/man1/groups.*

rm %{buildroot}/%{_sbindir}/grpconv
rm %{buildroot}/%{_mandir}/man8/grpconv.*
rm %{buildroot}/%{_mandir}/*/man8/grpconv.*
rm %{buildroot}/%{_sbindir}/grpunconv
rm %{buildroot}/%{_mandir}/man8/grpunconv.*
rm %{buildroot}/%{_mandir}/*/man8/grpunconv.*

rm %{buildroot}/%{_sbindir}/groupmems
rm %{buildroot}/%{_mandir}/man8/groupmems.*
rm %{buildroot}/%{_mandir}/*/man8/groupmems.*
rm %{buildroot}%{_sysconfdir}/pam.d/groupmems

rm %{buildroot}/%{_bindir}/login
rm %{buildroot}/%{_mandir}/man1/login.*
rm %{buildroot}/%{_mandir}/*/man1/login.*
rm %{buildroot}%{_sysconfdir}/pam.d/login

rm %{buildroot}/%{_bindir}/su
rm %{buildroot}/%{_mandir}/man1/su.*
rm %{buildroot}/%{_mandir}/*/man1/su.*
rm %{buildroot}/%{_mandir}/man5/suauth.*
rm %{buildroot}/%{_mandir}/*/man5/suauth.*
rm %{buildroot}%{_sysconfdir}/pam.d/su

rm %{buildroot}/%{_bindir}/faillog
rm %{buildroot}/%{_mandir}/man5/faillog.*
rm %{buildroot}/%{_mandir}/*/man5/faillog.*
rm %{buildroot}/%{_mandir}/man8/faillog.*
rm %{buildroot}/%{_mandir}/*/man8/faillog.*

rm %{buildroot}/%{_sbindir}/logoutd
rm %{buildroot}/%{_mandir}/man8/logoutd.*
rm %{buildroot}/%{_mandir}/*/man8/logoutd.*
rm %{buildroot}/%{_sbindir}/nologin
rm %{buildroot}/%{_mandir}/man8/nologin.*
rm %{buildroot}/%{_mandir}/*/man8/nologin.*

rm %{buildroot}/%{_sbindir}/chgpasswd
rm %{buildroot}/%{_mandir}/man8/chgpasswd.*
rm %{buildroot}/%{_mandir}/*/man8/chgpasswd.*
rm %{buildroot}%{_sysconfdir}/pam.d/chgpasswd

rm %{buildroot}/%{_mandir}/man3/getspnam.*
rm %{buildroot}/%{_mandir}/*/man3/getspnam.*
rm %{buildroot}/%{_mandir}/man5/gshadow.5*
rm %{buildroot}/%{_mandir}/*/man5/gshadow.5*
rm %{buildroot}/%{_mandir}/man5/passwd.5*
rm %{buildroot}/%{_mandir}/*/man5/passwd.5*

rm -rf %{buildroot}%{_mandir}/{??,??_??}

%find_lang shadow

%pre
%service_add_pre shadow.service shadow.timer

%post
%set_permissions %{_bindir}/chage
%set_permissions %{_bindir}/chfn
%set_permissions %{_bindir}/chsh
%set_permissions %{_bindir}/expiry
%set_permissions %{_bindir}/gpasswd
%set_permissions %{_bindir}/newgrp
%set_permissions %{_bindir}/passwd
%set_permissions %{_bindir}/newgidmap
%set_permissions %{_bindir}/newuidmap

%service_add_post shadow.service shadow.timer

%verifyscript
%verify_permissions %{_bindir}/chage
%verify_permissions %{_bindir}/chfn
%verify_permissions %{_bindir}/chsh
%verify_permissions %{_bindir}/expiry
%verify_permissions %{_bindir}/gpasswd
%verify_permissions %{_bindir}/newgrp
%verify_permissions %{_bindir}/passwd
%verify_permissions %{_bindir}/newgidmap
%verify_permissions %{_bindir}/newuidmap

%preun
%service_del_preun shadow.service shadow.timer

%postun
%service_del_postun shadow.service shadow.timer

%files -f shadow.lang
%license COPYING
%doc NEWS doc/HOWTO README README.changes-pwdutils
%attr(0644,root,root) %config %{_sysconfdir}/login.defs
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/default/useradd
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/subuid
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/subgid
%config %{_sysconfdir}/pam.d/chage
%config %{_sysconfdir}/pam.d/chfn
%config %{_sysconfdir}/pam.d/chsh
%config %{_sysconfdir}/pam.d/passwd
%config %{_sysconfdir}/pam.d/useradd
%config %{_sysconfdir}/pam.d/chpasswd
%config %{_sysconfdir}/pam.d/groupadd
%config %{_sysconfdir}/pam.d/groupdel
%config %{_sysconfdir}/pam.d/groupmod
%config %{_sysconfdir}/pam.d/newusers
%config %{_sysconfdir}/pam.d/useradd
%config %{_sysconfdir}/pam.d/userdel
%config %{_sysconfdir}/pam.d/usermod
%verify(not mode) %attr(2755,root,shadow) %{_bindir}/chage
%verify(not mode) %attr(4755,root,shadow) %{_bindir}/chfn
%verify(not mode) %attr(4755,root,shadow) %{_bindir}/chsh
%verify(not mode) %attr(4755,root,shadow) %{_bindir}/expiry
%verify(not mode) %attr(4755,root,shadow) %{_bindir}/gpasswd
%verify(not mode) %attr(4755,root,root) %{_bindir}/newgrp
%verify(not mode) %attr(4755,root,shadow) %{_bindir}/passwd
%verify(not mode) %attr(4755,root,shadow) %{_bindir}/newgidmap
%verify(not mode) %attr(4755,root,shadow) %{_bindir}/newuidmap
%{_bindir}/lastlog
%{_bindir}/sg
%{_sbindir}/groupadd
%{_sbindir}/groupdel
%{_sbindir}/groupmod
%{_sbindir}/grpck
%{_sbindir}/pwck
%{_sbindir}/useradd
%{_sbindir}/userdel
%{_sbindir}/usermod
%{_sbindir}/pwconv
%{_sbindir}/pwunconv
%{_sbindir}/chpasswd
%{_sbindir}/newusers
%{_sbindir}/vipw
%{_sbindir}/vigr
%verify(not md5 size mtime) %config(noreplace) %{_sbindir}/useradd.local
%verify(not md5 size mtime) %config(noreplace) %{_sbindir}/userdel-pre.local
%verify(not md5 size mtime) %config(noreplace) %{_sbindir}/userdel-post.local
%{_mandir}/man1/chage.1%{?ext_man}
%{_mandir}/man1/chfn.1%{?ext_man}
%{_mandir}/man1/chsh.1%{?ext_man}
%{_mandir}/man1/expiry.1%{?ext_man}
%{_mandir}/man1/gpasswd.1%{?ext_man}
%{_mandir}/man1/newgrp.1%{?ext_man}
%{_mandir}/man1/passwd.1%{?ext_man}
%{_mandir}/man1/sg.1%{?ext_man}
%{_mandir}/man3/shadow.3%{?ext_man}
%{_mandir}/man5/login.defs.5%{?ext_man}
%{_mandir}/man5/shadow.5%{?ext_man}
%{_mandir}/man8/chpasswd.8%{?ext_man}
%{_mandir}/man8/groupadd.8%{?ext_man}
%{_mandir}/man8/groupdel.8%{?ext_man}
%{_mandir}/man8/groupmod.8%{?ext_man}
%{_mandir}/man8/grpck.8%{?ext_man}
%{_mandir}/man8/lastlog.8%{?ext_man}
%{_mandir}/man8/newusers.8%{?ext_man}
%{_mandir}/man8/pwck.8%{?ext_man}
%{_mandir}/man8/pwconv.8%{?ext_man}
%{_mandir}/man8/pwunconv.8%{?ext_man}
%{_mandir}/man8/useradd.8%{?ext_man}
%{_mandir}/man8/userdel.8%{?ext_man}
%{_mandir}/man8/usermod.8%{?ext_man}
%{_mandir}/man8/vigr.8%{?ext_man}
%{_mandir}/man8/vipw.8%{?ext_man}
%{_mandir}/man5/subuid.5%{?ext_man}
%{_mandir}/man5/subgid.5%{?ext_man}
%{_mandir}/man1/newgidmap.1%{?ext_man}
%{_mandir}/man1/newuidmap.1%{?ext_man}

%{_unitdir}/*

%changelog
