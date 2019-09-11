#
# spec file for package perl-Inline
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


Name:           perl-Inline
Version:        0.83
Release:        0
%define cpan_name Inline
Summary:        Write Perl Subroutines in Other Programming Languages
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TINITA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warn) >= 0.23
BuildRequires:  perl(version) >= 0.82
Requires:       perl(version) >= 0.82
%{perl_requires}
# MANUAL BEGIN
Requires:       gcc
Requires:       make
Provides:       perl-Inline-C = 0.20
Obsoletes:      perl-Inline-C < 0.20
# MANUAL END

%description
The Inline module allows you to put source code from other programming
languages directly "inline" in a Perl script or module. The code is
automatically compiled as needed, and then loaded for immediate access from
Perl.

Inline saves you from the hassle of having to write and compile your own
glue code using facilities like XS or SWIG. Simply type the code where you
want it and run your Perl as normal. All the hairy details are handled for
you. The compilation and installation of your code chunks all happen
transparently; all you will notice is the delay of compilation on the first
run.

The Inline code only gets compiled the first time you run it (or whenever
it is modified) so you only take the performance hit once. Code that is
Inlined into distributed modules (like on the CPAN) will get compiled when
the module is installed, so the end user will never notice the compilation
time.

Best of all, it works the same on both Unix and Microsoft Windows. See
Inline- Support for support information.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING example README
%license LICENSE

%changelog
