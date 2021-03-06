#
# spec file for package rubygem-rubocop
#
# Copyright (c) 2020 SUSE LLC
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


%define mod_name rubocop
%define mod_full_name %{mod_name}-%{version}
#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#
Name:           rubygem-rubocop
Version:        0.86.0
Release:        0
Summary:        Automatic Ruby code style checking tool
License:        MIT
Group:          Development/Languages/Ruby
URL:            https://github.com/rubocop-hq/rubocop
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
BuildRequires:  %{ruby >= 2.4.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         update-alternatives
# MANUAL
Patch0:         0001-Use-usr-bin-bash-instead-of-env-as-the-shebang.patch
# /MANUAL

%description
RuboCop is a Ruby code style checking and code formatting tool.
It aims to enforce the community-driven Ruby Style Guide.

%prep
%gem_unpack
%patch0 -p1
find -type f -print0 | xargs -0 touch -r %{SOURCE0}
%{gem_build}

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="LICENSE.txt README.md" \
  -f

%gem_packages

%changelog
