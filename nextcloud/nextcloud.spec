#
# spec file for package nextcloud
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


#
%if 0%{?suse_version}
%define apache_serverroot /srv/www/htdocs
%define apache_confdir /etc/apache2/conf.d
%define apache_docdir /usr/share/doc/packages
%define apache_user wwwrun
%define apache_group www
%else
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
%define apache_serverroot /var/www/html
%define apache_confdir /etc/httpd/conf.d
%define apache_user apache
%define apache_group apache
%define __jar_repack 0
%else
%define apache_serverroot /var/www
%define apache_confdir /etc/httpd/conf.d
%define apache_user www
%define apache_group www
%endif
%endif

%define oc_user 	%{apache_user}
%define oc_dir  	%{apache_serverroot}/%{name}
%define ocphp_bin	/usr/bin

%if 0%{?rhel} == 600 || 0%{?rhel_version} == 600 || 0%{?centos_version} == 600
%define statedir	/var/run
%else
%define statedir	/run
%endif

Name:           nextcloud
Version:        16.0.3
Release:        0
Summary:        File hosting service
License:        AGPL-3.0-only
Group:          Productivity/Networking/Web/Utilities
Url:            https://nextcloud.com
Source0:        https://download.nextcloud.com/server/releases/%{name}-%{version}.tar.bz2
Source1:        apache_secure_data
Source2:        README
Source3:        README.SELinux
Source4:        README.SUSE
Source5:        robots.txt
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%if 0%{?suse_version}
BuildRequires:  apache2 >= 2.4
%if 0%{?suse_version} > 1020
BuildRequires:  fdupes
%endif
BuildRequires:  unzip
%endif
#
Requires:       curl
Requires:       libxml2-2
Requires:       mysql
Requires:       php-bz2
Requires:       php-dom
Requires:       php-gd
Requires:       php-intl
Requires:       php-json
Requires:       php-mbstring
Requires:       php-mysql
Requires:       php-posix
Requires:       php-zip
#
%if 0%{?fedora_version} || 0%{?rhel} || 0%{?rhel_version} || 0%{?centos_version}
Requires:       php <= 7.3.0
Requires:       php >= 7.0.0
Requires:       php-process
Requires:       php-xml
#
Recommends:     sqlite
%endif
#
%if 0%{?suse_version}
Requires:       apache2
Requires:       mod_php_any < 7.4.0
Requires:       mod_php_any >= 7.0.0
Requires:       php-ctype
Requires:       php-curl
# SUSE does not include the fileinfo module in php-common.
Requires:       php-fileinfo
Requires:       php-iconv
Requires:       php-openssl
Requires:       php-pear
Requires:       php-xmlreader
Requires:       php-xmlwriter
Requires:       php-zlib
Recommends:     sqlite3
%endif
# Database connectors:
Recommends:     php-sqlite
#Recommends:     php-pgsql
# For preview generation: 
Recommends:     php-imagick 
Recommends:     php-ffmpeg
#Recommends:     libreoffice
# Require for specific apps:
Recommends:     php-ldap
Recommends:     php-ftp
#Recommends:     php-smbclient
#Recommends:     php-imap
# Recommend for specific apps:
Recommends:     php-exif
Recommends:     php-gmp
# For enhanced server performance:
Recommends:     php-APCu

%description
Nextcloud is a suite of client-server software for creating file
hosting services and using them.

%prep
%setup -q -n %{name}
cp %{SOURCE2} .
cp %{SOURCE3} .
cp %{SOURCE4} .
cp %{SOURCE5} .
### Don't remove git files!! 
### git files should not be removed, otherwise nextcloud rise up integrity check failure in some situations.
###
## delete unneeded gitfiles 
#rm -r `find . -name ".gitignore" -or -name ".gitkeep" -or -name ".github"`
## remove entries in signature.json to prevent integrity check failure
#find . -iname signature.json \
#    -exec sed -i "/\/.gitignore\": ./d" "{}" \;  \
#    -exec sed -i "/\/.gitkeep\": ./d" "{}" \; \
#    -exec sed -i "/\/.github\": ./d" "{}" \;
#rm -f 3rdparty/symfony/debug/Resources/ext/*.{c,h}

%build

%install
# no server side java code contained, alarm is false
idir=$RPM_BUILD_ROOT/%{apache_serverroot}/%{name}
mkdir -p $idir
mkdir -p $idir/data
mkdir -p $idir/search
cp -aRf * $idir
cp -aRf .htaccess $idir
cp -aRf .user.ini $idir
# $idir/l10n to disappear in future
#rm -f $idir/l10n/l10n.pl

if [ ! -f $idir/robots.txt ]; then
  install -p -D -m 644 %{SOURCE5} $idir/robots.txt
fi

# create the AllowOverride directive
install -p -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT/%{apache_confdir}/nextcloud.conf
ocpath="%{apache_serverroot}/%{name}"
sed -i -e"s|@DATAPATH@|${ocpath}|g" $RPM_BUILD_ROOT/%{apache_confdir}/nextcloud.conf

# not needed for distro packages
rm -f ${idir}/indie.json

%if 0%{?suse_version}
# link duplicate doc files
%fdupes -s $RPM_BUILD_ROOT/%{apache_serverroot}/%{name}
%endif

%pre
# avoid fatal php errors, while we are changing files
# https://github.com/nextcloud
#
# We don't do this for new installs. Only for updates.
# If the first argument to pre is 1, the RPM operation is an initial installation. If the argument is 2, 
# the operation is an upgrade from an existing version to a new one.
if [ $1 -gt 1 -a ! -s %{statedir}/apache_stopped_during_nextcloud_install ]; then	
  echo "%{name} update: Checking for running Apache"
  # FIXME: this above should make it idempotent -- a requirement with openSUSE.
  # it does not work.
%if 0%{?suse_version} && 0
%if 0%{?suse_version} <= 1110
  rcapache2 status       | grep running > %{statedir}/apache_stopped_during_nextcloud_install
  rcapache2 stop
%else
  service apache2 status | grep running > %{statedir}/apache_stopped_during_nextcloud_install
  service apache2 stop
%endif
%endif
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
  service httpd status | grep running > %{statedir}/apache_stopped_during_nextcloud_install
  service httpd stop
%endif
fi
if [ -s %{statedir}/apache_stopped_during_nextcloud_install ]; then
  echo "%{name} pre-install: Stopping Apache"
fi

if [ $1 -eq 1 ]; then
    echo "%{name}-server: First install starting"
else
    echo "%{name}-server: installing upgrade ..."
fi
# https://github.com/nextcloud
if [ -x %{ocphp_bin}/php -a -f %{oc_dir}/occ ]; then
  echo "%{name}: occ maintenance:mode --on"
  su %{oc_user} -s /bin/sh -c "cd %{oc_dir}; PATH=%{ocphp_bin}:$PATH php ./occ maintenance:mode --on" || true
  echo yes > %{statedir}/occ_maintenance_mode_during_nextcloud_install
fi

%post
if [ $1 -eq 1 ]; then
    echo "%{name} First install complete"
else
    echo "%{name} Upgrade complete"
fi

%if 0%{?suse_version}
%if 0%{?suse_version} >= 1500
# make sure php7 is not in APACHE_MODULES, so that we don't create dups.
perl -pani -e 's@^(APACHE_MODULES=".*)\bphp7\b@$1@' /etc/sysconfig/apache2
# add php7 to APACHE_MODULES
perl -pani -e 's@^(APACHE_MODULES=")@${1}php7 @' /etc/sysconfig/apache2
%else
# make sure php5 is not in APACHE_MODULES, so that we don't create dups.
perl -pani -e 's@^(APACHE_MODULES=".*)\bphp5\b@$1@' /etc/sysconfig/apache2
# add php5 to APACHE_MODULES
perl -pani -e 's@^(APACHE_MODULES=")@${1}php5 @' /etc/sysconfig/apache2
%endif
%endif

if [ -s %{statedir}/apache_stopped_during_nextcloud_install ]; then
  echo "%{name} post-install: Restarting Apache"
  ## If we stopped apache in pre section, we now should restart. -- but *ONLY* then!
  ## Maybe delegate that task to occ upgrade? They also need to handle this, somehow.
%if 0%{?suse_version}
%if 0%{?suse_version} <= 1310
  rcapache2 start
%else
  rcapache2 restart apache2.service
%endif
%endif
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
  service httpd start
%endif
fi

if [ -s %{statedir}/occ_maintenance_mode_during_nextcloud_install ]; then
echo "%{name}: occ upgrade"
su %{oc_user} -s /bin/sh -c "cd %{oc_dir}; PATH=%{ocphp_bin}:$PATH php ./occ upgrade" || true
echo "%{name}: occ maintenance:mode --off"
su %{oc_user} -s /bin/sh -c "cd %{oc_dir}; PATH=%{ocphp_bin}:$PATH php ./occ maintenance:mode --off" || true
fi

rm -f %{statedir}/apache_stopped_during_nextcloud_install
rm -f %{statedir}/occ_maintenance_mode_during_nextcloud_install

%files
%defattr(644,root,root,755)
%exclude %{apache_serverroot}/%{name}/README
%exclude %{apache_serverroot}/%{name}/README.SUSE
%exclude %{apache_serverroot}/%{name}/README.SELinux
%doc README README.SUSE README.SELinux
%{apache_serverroot}/%{name}
%attr(-,wwwrun,www) %{apache_serverroot}/%{name}/occ
%config(noreplace) %{apache_confdir}/nextcloud.conf
%config(noreplace) %{apache_serverroot}/%{name}/.user.ini
%defattr(664,wwwrun,www,775)
%{apache_serverroot}/%{name}/apps
%defattr(660,wwwrun,www,770)
%{apache_serverroot}/%{name}/config
%{apache_serverroot}/%{name}/data

%changelog
