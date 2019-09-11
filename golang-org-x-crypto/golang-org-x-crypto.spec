#
# spec file for package golang-org-x
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


%global provider        github
%global provider_tld    com
%global project         golang
%global repo            crypto
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     golang.org/x/crypto

Name:           golang-org-x-%{repo}
Version:        1.5.2+git20171021.edd5e9b
Release:        0
Summary:        Go supplementary cryptography libraries
License:        BSD-3-Clause
Group:          Development/Languages/Golang
Url:            https://%{provider_prefix}
Source0:        %{repo}-%{version}.tar.xz
Source1:        rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  golang-packaging
BuildRequires:  xz

BuildRequires:  golang-org-x-net-context
Requires:       golang-org-x-net-context
BuildRequires:  golang(golang.org/x/sys/unix)
Requires:       golang(golang.org/x/sys/unix)

%{go_nostrip}
%{go_provides}

%description
Go supplementary cryptography libraries.

%prep
%setup -q -n %{repo}-%{version}

%build
%goprep %{import_path}
%gobuild ...

%install
%goinstall
%gosrc
%gofilelist

%files -f file.lst
%defattr(-,root,root,-)
%doc README.md LICENSE PATENTS AUTHORS CONTRIBUTORS

%changelog
