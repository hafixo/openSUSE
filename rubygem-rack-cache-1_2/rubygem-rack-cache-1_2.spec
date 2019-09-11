#
# spec file for package rubygem-rack-cache-1_2
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


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-rack-cache-1_2
Version:        1.2
Release:        0
%define mod_name rack-cache
%define mod_full_name %{mod_name}-%{version}
%define mod_version_suffix -1_2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
Url:            http://tomayko.com/src/rack-cache/
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        HTTP Caching for Rack
License:        MIT
Group:          Development/Languages/Ruby

%description
Rack::Cache is suitable as a quick drop-in component to enable HTTP caching
for Rack-based applications that produce freshness (Expires, Cache-Control)
and/or validation (Last-Modified, ETag) information.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGES COPYING README" \
  -f

%gem_packages

%changelog
