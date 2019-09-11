#
# spec file for package perl-Parse-PMFile
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Parse-PMFile
Version:        0.41
Release:        0
%define cpan_name Parse-PMFile
Summary:        Parses .Pm File As Pause Does
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Parse-PMFile/
Source0:        http://www.cpan.org/authors/id/I/IS/ISHIGAKI/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker::CPANfile) >= 0.07
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(JSON::PP) >= 2.00
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(version) >= 0.83
Requires:       perl(JSON::PP) >= 2.00
Requires:       perl(version) >= 0.83
%{perl_requires}

%description
The most of the code of this module is taken from the PAUSE code as of
April 2013 almost verbatim. Thus, the heart of this module should be quite
stable. However, I made it not to use pipe ("-|") as well as I stripped
database-related code. If you encounter any issue, that's most probably
because of my modification.

This module doesn't provide features to extract a distribution or parse
meta files intentionally.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes README

%changelog

