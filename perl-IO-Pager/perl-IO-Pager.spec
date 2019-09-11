#
# spec file for package perl-IO-Pager
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           perl-IO-Pager
Version:        0.40
Release:        0
%define cpan_name IO-Pager
Summary:        Select a pager and pipe text to it if destination is a TTY
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JP/JPIERCE/%{cpan_name}-%{version}.tgz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(File::Which)
%{perl_requires}

%description
IO::Pager can be used to locate an available pager and set the _PAGER_
environment variable (see NOTES). It is also a factory for creating I/O
objects such as IO::Pager::Buffered and IO::Pager::Unbuffered.

IO::Pager subclasses are designed to programmatically decide whether or not
to pipe a filehandle's output to a program specified in _PAGER_. Subclasses
may implement only the IO handle methods desired and inherit the remainder
of those outlined below from IO::Pager. For anything else, YMMV. See the
appropriate subclass for implementation specific details.

%prep
%setup -q -n %{cpan_name}-0.4

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
%doc CHANGES README TODO

%changelog
