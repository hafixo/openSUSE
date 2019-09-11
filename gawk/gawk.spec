#
# spec file for package gawk
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gawk
Version:        4.2.1
Release:        0
Summary:        GNU awk
License:        GPL-3.0+
Group:          Productivity/Text/Utilities
Url:            http://www.gnu.org/software/gawk/
Source:         http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source2:        http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source3:        http://savannah.gnu.org/people/viewgpg.php?user_id=80653#/gawk.keyring
Source4:        gawk.rpmlintrc
BuildRequires:  update-alternatives
Requires(post): %{install_info_prereq}
Requires(post): update-alternatives
Requires(preun): %{install_info_prereq}
Requires(preun): update-alternatives
Provides:       awk
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
GNU awk is upwardly compatible with the System V Release 4 awk.  It is
almost completely POSIX 1003.2 compliant.

%prep
%setup -q

%build
%configure --libexecdir=%{_libdir}
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

#UsrMerge
install -d %{buildroot}/bin
ln -sf %{_bindir}/gawk %{buildroot}/bin
ln -s %{_sysconfdir}/alternatives/awk %{buildroot}/bin/awk
#EndUsrMerge
rm -f %{buildroot}%{_bindir}/*-%{version} %{buildroot}%{_bindir}/awk

# create symlinks for update-alternatives
ln -s %{_sysconfdir}/alternatives/usr-bin-awk %{buildroot}%{_bindir}/awk
ln -s %{_sysconfdir}/alternatives/awk.1%{?ext_man} %{buildroot}%{_mandir}/man1/awk.1%{?ext_man}

%find_lang %{name}

%post
%{_sbindir}/update-alternatives \
  --install /bin/awk awk %{_bindir}/gawk 20 \
  --slave %{_bindir}/awk usr-bin-awk %{_bindir}/gawk \
  --slave %{_mandir}/man1/awk.1.gz awk.1%{?ext_man} %{_mandir}/man1/gawk.1%{?ext_man}
%install_info --info-dir=%{_infodir} %{_infodir}/gawk.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/gawkinet.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/gawk.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/gawkinet.info.gz
if [ $1 -eq 0 ]; then
    %{_sbindir}/update-alternatives --remove awk %{_bindir}/gawk
fi

%files -f %{name}.lang
%defattr(-,root,root)
%config %{_sysconfdir}/profile.d/gawk.csh
%config %{_sysconfdir}/profile.d/gawk.sh
#UsrMerge
/bin/awk
#EndUsrMerge
%{_bindir}/awk
%{_mandir}/man1/awk.1%{?ext_man}
%ghost %{_sysconfdir}/alternatives/awk
%ghost %{_sysconfdir}/alternatives/usr-bin-awk
%ghost %{_sysconfdir}/alternatives/awk.1%{?ext_man}
%license COPYING*
%doc AUTHORS NEWS POSIX.STD README ChangeLog*
#UsrMerge
/bin/gawk
#EndUsrMerge
%{_bindir}/gawk
%{_libdir}/awk
%{_libdir}/gawk
%{_datadir}/awk
%{_includedir}/gawkapi.h
%{_infodir}/*.info.gz
%{_mandir}/man1/gawk.1%{?ext_man}
%{_mandir}/man3/*%{?ext_man}

%changelog
