#
# spec file for package rubygem-shoes
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           rubygem-shoes
Version:        3.0.1
Release:        0
%define mod_name shoes
%define mod_full_name %{mod_name}-%{version}

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 1
Url:            http://github.com/shoes/shoes
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Summary:        Shoes is the best little GUI toolkit for Ruby
License:        MIT
Group:          Development/Languages/Ruby

%description
Shoes is the best little GUI toolkit for Ruby. This gem is currently a
placeholder until we properly gemfiy Shoes.

%package doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       %{name} = %{version}

%description doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%package testsuite
Summary:        Test suite for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       %{name} = %{version}

%description testsuite
Test::Unit or RSpec files, useful for developers.
kl
%prep
#gem_unpack
#if you need patches, apply them here and replace the # with a % sign in the surrounding lines
#gem_build

%build

%install
%gem_install -f
mkdir -p %{buildroot}%{_docdir}/%{name}
ln -s %{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_full_name}/CHANGELOG %buildroot/%{_docdir}/%{name}/CHANGELOG
ln -s %{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_full_name}/COPYING %buildroot/%{_docdir}/%{name}/COPYING
ln -s %{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_full_name}/README.md %buildroot/%{_docdir}/%{name}/README.md

%files
%defattr(-,root,root,-)
%{_docdir}/%{name}
%{_libdir}/ruby/gems/%{rb_ver}/cache/%{mod_full_name}.gem
%{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_full_name}/
%exclude %{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_full_name}/test
%{_libdir}/ruby/gems/%{rb_ver}/specifications/%{mod_full_name}.gemspec

%files doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/%{rb_ver}/doc/%{mod_full_name}/

%files testsuite
%defattr(-,root,root,-)
%{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_full_name}/test

%changelog


