#
# spec file for package yomi-formula
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


%define fname yomi
%define fdir  %{_datadir}/salt-formulas

Name:           yomi-formula
Version:        0.0.1+git.1565191883.64eabeb
Release:        0
Summary:        Yomi - Yet one more installer
License:        Apache-2.0
Group:          System/Packages
Requires:       python3-base
BuildArch:      noarch
URL:            https://github.com/openSUSE/yomi
Source0:        %{fname}-%{version}.tar.xz

# On SLE/Leap 15-SP1 and TW requires the new salt-formula configuration location.
%if ! (0%{?sle_version:1} && 0%{?sle_version} < 150100)
Requires(pre):  salt-formulas-configuration
%else
Requires(pre):  salt-master
%endif

%description
Yomi (yet one more installer) is a new proposal for an installer for
the [open]SUSE family. It is designed as a SaltStack state, and
expected to be used in situations were unattended installations for
heterogeneous nodes is required, and where some bits of intelligence
in the configuration file, can help to customize the installation.

Being also a Salt state makes the installation process one more step
during the provisioning stage, making on Yomi a good candidate for
integration in any workflow were SaltStack is used.

%prep
%setup -q -n %{fname}-%{version}

%build

%install
# States, modules and grains inside Yomi namespace
mkdir -p %{buildroot}%{fdir}/states/%{fname}/
cp -R salt/* %{buildroot}%{fdir}/states/

# Remove the top.sls, as can overwrite the one from the user
rm %{buildroot}%{fdir}/states/top.sls

# Example of pillars
mkdir -p %{buildroot}%{_datadir}/%{fname}/
cp -R pillar %{buildroot}%{_datadir}/%{fname}/

# Monitoring CLI
mkdir -p %{buildroot}%{_bindir}/
cp -a monitor %{buildroot}%{_bindir}/

# Pillars examples
cat <<EOF > %{buildroot}%{_datadir}/%{fname}/pillar.conf
pillar_roots:
  base:
    - /usr/share/yomi/pillar
    - /srv/pillar
EOF

# Configuration and UUIDs for autosign
echo "autosign_grains_dir: /usr/share/yomi/autosign_grains" > %{buildroot}%{_datadir}/%{fname}/autosign.conf
mkdir -p %{buildroot}%{_datadir}/%{fname}/autosign_grains/
for i in $(seq 0 9); do
    echo $(uuidgen --md5 --namespace @dns --name http://opensuse.org/$i)
done > %{buildroot}%{_datadir}/%{fname}/autosign_grains/uuid

# Salt-API configuration
cat <<EOF > %{buildroot}%{_datadir}/%{fname}/salt-api.conf
rest_cherrypy:
  port: 8000
  debug: no
  disable_ssl: yes
  # ssl_crt: /etc/ssl/server.crt
  # ssl_key: /etc/ssl/server.key
EOF

# Eauth configuration and example user-list.txt
cat <<EOF > %{buildroot}%{_datadir}/%{fname}/eauth.conf
external_auth: 
  file:
    ^filename: /usr/share/yomi/user-list.txt
    salt:
      - .*
      - '@wheel'
      - '@runner'
      - '@jobs'
EOF
echo 'salt:linux' > %{buildroot}%{_datadir}/%{fname}/user-list.txt

# Examples of integration
cp -a docs/examples/* %{buildroot}%{_datadir}/%{fname}
cat <<EOF > %{buildroot}%{_datadir}/%{fname}/kubic-file.conf
file_roots:
  base:
    - /usr/share/yomi/kubic
    - /usr/share/salt-formulas/states
    - /srv/salt
EOF

%files
%defattr(0640,root,salt,0750)
%license LICENSE
%doc README.md docs/*
%dir %{fdir}/
%dir %{fdir}/states/
%dir %{fdir}/states/%{fname}
%dir %{_datadir}/%{fname}
%{fdir}/states/
%{_datadir}/%{fname}
%attr(755,root,root) %{_bindir}/monitor

%changelog
