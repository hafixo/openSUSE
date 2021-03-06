#
# spec file for package rubygem-pry_debug
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           rubygem-pry_debug
Version:        0.1.0
Release:        0
%define mod_name pry_debug
%define mod_full_name %{mod_name}-%{version}

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
Url:            http://github.com/Mon-Ouie/pry_debug
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Summary:        A pure-ruby debugger
License:        Zlib
Group:          Development/Languages/Ruby
%define mod_branch -%{version}
%define mod_weight 0
PreReq:         update-alternatives

%description
A pure-ruby debugger. No more puts "HERE!!!" or p :var => var, :other => other
until you find what caused the bug. Just add a breakpoint and see the value of
any variable.


%prep
%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="LICENSE README.md" \
  -f

%gem_packages

%changelog
