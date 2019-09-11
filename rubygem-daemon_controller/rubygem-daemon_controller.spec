#
# spec file for package rubygem-daemon_controller
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


Name:           rubygem-daemon_controller
Version:        1.2.0
Release:        0
%define mod_name daemon_controller
%define mod_full_name %{mod_name}-%{version}

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
Url:            https://github.com/FooBarWidget/daemon_controller
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Summary:        A library for implementing daemon management capabilities
License:        MIT
Group:          Development/Languages/Ruby

%description
A library for robust daemon management.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="LICENSE.txt" \
  -f

%gem_packages

%changelog
