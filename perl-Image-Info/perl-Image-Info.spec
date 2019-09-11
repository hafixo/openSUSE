#
# spec file for package perl-Image-Info
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Image-Info
Version:        1.41
Release:        0
%define cpan_name Image-Info
Summary:        Extract meta information from image files
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Image-Info/
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::Scalar)
Requires:       perl(IO::Scalar)
Recommends:     perl(Bundle::Image::Info::PNG)
Recommends:     perl(Bundle::Image::Info::SVG)
Recommends:     perl(Bundle::Image::Info::XBM)
Recommends:     perl(Bundle::Image::Info::XPM)
%{perl_requires}

%description
This module provides functions to extract various kinds of meta information
from image files.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc CHANGES CREDITS exifdump imgdump README TODO

%changelog
