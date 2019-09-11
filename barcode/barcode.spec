#
# spec file for package barcode
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           barcode
Version:        0.99
Release:        0
Summary:        Text-Mode Barcode Creation Utility
License:        GPL-3.0+
Group:          Productivity/Graphics/Other
Url:            http://www.gnu.org/software/barcode
Source0:        ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
# PATCH-FIX-OPENSUSE barcode-0.99-info.patch
Patch2:         %{name}-0.99-info.patch
# PATCH-FIX-UPSTREAM barcode-0.98-leak-fix.patch bnc#537525 -- Fix memory leak by adding call to free.
Patch5:         %{name}-0.98-leak-fix.patch
# PATCH-FIX-UPSTREAM barcode-fix-renamed-include.patch malcolmlewis@opensuse.org -- Fix renamed gettext include header reference.
Patch6:         barcode-fix-renamed-include.patch
BuildRequires:  xz
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} <= 1220
BuildRequires:  texlive
%else
BuildRequires:  makeinfo
BuildRequires:  texinfo
BuildRequires:  texlive-dvips
BuildRequires:  texlive-tex
BuildRequires:  texlive-texinfo
%endif

%description
GNU Barcode is meant to meet most barcode creation needs with a
conventional printer. It can create printouts for the conventional
product tagging standards: UPC-A, UPC-E, EAN-13, EAN-8, ISBN, as well
as a few other formats. Output is generated in either PostScript or
Encapsulated PostScript format.

%package devel
Summary:        Text-Mode Barcode Creation Utility - Development files
Group:          Development/Libraries

%description devel
GNU Barcode is meant to meet most barcode creation needs with a
conventional printer. It can create printouts for the conventional
product tagging standards: UPC-A, UPC-E, EAN-13, EAN-8, ISBN, as well
as a few other formats. Output is generated in either PostScript or
Encapsulated PostScript format.

%prep
%setup -q
%patch2
%patch5
%patch6 -p1

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
install -Dm0644 barcode.h %{buildroot}%{_includedir}/barcode.h
install -Dm0644 .libs/libbarcode.a %{buildroot}%{_libdir}/libbarcode.a

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files
%defattr(-,root,root)
%doc COPYING README TODO
%{_bindir}/barcode
%{_bindir}/sample
%{_infodir}/%{name}.info.gz

%files devel
%defattr(-,root,root)
%{_includedir}/barcode.h
%{_libdir}/libbarcode.a

%changelog
