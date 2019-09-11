#
# spec file for package perl-Crypt-SSLeay
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


Name:           perl-Crypt-SSLeay
Version:        0.72
Release:        0
%define cpan_name Crypt-SSLeay
Summary:        OpenSSL support for LWP
License:        Artistic-2.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Crypt-SSLeay/
Source0:        https://cpan.metacpan.org/authors/id/N/NA/NANIS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         no-dot-inc.patch
Patch1:         Crypt-SSLeay-use_TLS_instead_of_SSL.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.280205
BuildRequires:  perl(LWP::Protocol::https) >= 6.02
BuildRequires:  perl(Path::Class) >= 0.26
BuildRequires:  perl(Try::Tiny) >= 0.19
Requires:       perl(LWP::Protocol::https) >= 6.02
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  openssl-devel
Requires:       openssl
# MANUAL END

%description
This Perl module provides support for the HTTPS protocol under LWP, to
allow an LWP::UserAgent object to perform GET, HEAD, and POST requests over
encrypted socket connections. Please see LWP for more information on POST
requests.

The 'Crypt::SSLeay' package provides 'Net::SSL', which, if requested, is
loaded by 'LWP::Protocol::https' for https requests and provides the
necessary SSL glue.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644
%patch0 -p1
%patch1 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README.md TODO

%changelog
