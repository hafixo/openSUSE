#
# spec file for package glassfish-jsp-api
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


%global artifactId javax.servlet.jsp-api
Name:           glassfish-jsp-api
Version:        2.3.3
Release:        0
Summary:        Glassfish J2EE JSP API specification
License:        (CDDL-1.1 OR GPL-2.0-only WITH Classpath-exception-2.0) AND Apache-2.0
Group:          Development/Libraries/Java
URL:            http://java.net/jira/browse/JSP
Source0:        %{artifactId}-%{version}.tar.xz
# Generate API tarball from a git tag
Source1:        generate_tarball.sh
Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source3:        https://javaee.github.io/glassfish/LICENSE.html
Source4:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  glassfish-el-api
BuildRequires:  glassfish-servlet-api
BuildRequires:  javapackages-local
Requires:       mvn(javax.el:javax.el-api)
Requires:       mvn(javax.servlet:javax.servlet-api)
BuildArch:      noarch

%description
This project provides a container independent specification of JSP
2.2. Note that this package doesn't contain implementation of this
specification. See glassfish-jsp for one of implementations

%package javadoc
Summary:        API documentation for %{name}
Group:          Development/Libraries/Java
BuildArch:      noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{artifactId}-%{version}

cp -p %{SOURCE2} LICENSE-ASL-2.0.txt
cp -p %{SOURCE3} LICENSE-CDDL+GPLv2.html
cp -p %{SOURCE4} build.xml

# Submited upstream: http://java.net/jira/browse/JSP-31
sed -i "/<bundle.symbolicName>/s/-api//" pom.xml

%pom_xpath_set "pom:project/pom:version" %{version}

%pom_remove_parent

%pom_xpath_remove "pom:dependency[pom:groupId='javax.el' or pom:groupId='javax.servlet']/pom:scope"

%build
mkdir -p lib
build-jar-repository -s lib glassfish-el-api glassfish-servlet-api
%{ant} jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 target/%{artifactId}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{artifactId}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{artifactId}.pom
%add_maven_depmap %{name}/%{artifactId}.pom %{name}/%{artifactId}.jar -a javax.servlet:jsp-api
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE-ASL-2.0.txt LICENSE-CDDL+GPLv2.html

%files javadoc
%license LICENSE-ASL-2.0.txt LICENSE-CDDL+GPLv2.html
%{_javadocdir}/%{name}

%changelog
