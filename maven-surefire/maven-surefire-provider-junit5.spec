#
# spec file for package maven
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


%global base_name maven-surefire
Name:           %{base_name}-provider-junit5
Version:        2.22.0
Release:        0
Summary:        JUnit 5 provider for Maven Surefire
License:        Apache-2.0 AND CPL-1.0
Group:          Development/Libraries/Java
URL:            http://maven.apache.org/surefire/
# ./generate-tarball.sh
Source0:        %{base_name}-%{version}.tar.gz
# Remove bundled binaries which cannot be easily verified for licensing
Source1:        generate-tarball.sh
Source2:        http://junit.sourceforge.net/cpl-v10.html
Patch0:         0001-Maven-3.patch
Patch1:         0002-Port-to-current-doxia.patch
Patch2:         0003-Port-to-TestNG-6.11.patch
Patch3:         0004-Port-to-current-maven-shared-utils.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.surefire:common-java5)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher)
# PpidChecker relies on /usr/bin/ps to check process uptime
Requires:       procps
BuildArch:      noarch

%description
JUnit 5 provider for Maven Surefire.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n surefire-%{version}
cp -p %{SOURCE2} .

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Disable strict doclint
sed -i /-Xdoclint:all/d pom.xml

%pom_disable_module surefire-shadefire

%pom_add_dep org.apiguardian:apiguardian-api::provided surefire-providers/surefire-junit-platform

%pom_remove_dep -r org.apache.maven.surefire:surefire-shadefire

# Help plugin is needed only to evaluate effective Maven settings.
# For building RPM package default settings will suffice.
%pom_remove_plugin :maven-help-plugin surefire-setup-integration-tests

# QA plugin useful only for upstream
%pom_remove_plugin -r :jacoco-maven-plugin

# Not in Fedora
%pom_remove_plugin -r :animal-sniffer-maven-plugin
# Complains
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
# We don't need site-source
%pom_remove_plugin :maven-assembly-plugin maven-surefire-plugin
%pom_remove_dep -r ::::site-source

%pom_xpath_set pom:mavenVersion 3.3.3
%pom_remove_dep :maven-project maven-surefire-report-plugin
%pom_remove_dep :maven-project maven-surefire-common
%pom_remove_dep :maven-plugin-descriptor maven-surefire-common
%pom_remove_dep :maven-toolchain maven-surefire-common

%pom_xpath_remove -r "pom:execution[pom:id='shared-logging-generated-sources']"

%pom_add_dep com.google.code.findbugs:jsr305 surefire-api

%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_plugin -r :build-helper-maven-plugin

%pom_add_dep org.apache.commons:commons-lang3::runtime maven-surefire-plugin
%pom_add_dep commons-io:commons-io::runtime maven-surefire-plugin

%build
pushd surefire-providers/surefire-junit-platform
%mvn_build -f
popd

%install
pushd surefire-providers/surefire-junit-platform
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}
popd

%files -f surefire-providers/surefire-junit-platform/.mfiles
%doc README.md
%license LICENSE NOTICE cpl-v10.html

%files javadoc -f surefire-providers/surefire-junit-platform/.mfiles-javadoc
%license LICENSE NOTICE cpl-v10.html

%changelog
