#
# spec file for package hawtjni-runtime
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


%global base_name hawtjni
# That is the maven-release-plugin generated commit, but it's not tagged for some reason
# https://github.com/fusesource/hawtjni/issues/46
%global commit    fa1fd5dfdd0a1a5a67b61fa7d7ee7126b300c8f0
Name:           hawtjni-runtime
Version:        1.16
Release:        0
Summary:        HawtJNI Runtime
License:        Apache-2.0 AND EPL-1.0 AND BSD-3-Clause
Group:          Development/Libraries/Java
URL:            http://hawtjni.fusesource.org/
Source0:        https://github.com/fusesource/hawtjni/archive/%{commit}/hawtjni-%{commit}.tar.gz
BuildRequires:  apache-commons-cli
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  objectweb-asm >= 5
BuildRequires:  xbean

%description
This package provides API that projects using HawtJNI should build
against.

%package -n hawtjni-javadoc
Summary:        Javadocs for hawtjni
Group:          Documentation/HTML
BuildArch:      noarch

%description -n hawtjni-javadoc
This package contains the API documentation for hawtjni.

%package -n hawtjni
Summary:        Code generator that produces the JNI code
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}
Requires:       apache-commons-cli
Requires:       javapackages-tools
Requires:       objectweb-asm >= 5
Requires:       xbean
BuildArch:      noarch

%description -n hawtjni
HawtJNI is a code generator that produces the JNI code needed to
implement java native methods. It is based on the jnigen code generator
that is part of the SWT Tools project which is used to generate all the
JNI code which powers the eclipse platform.

%prep
%setup -q -n hawtjni-%{commit}

%pom_disable_module hawtjni-example
%pom_disable_module hawtjni-maven-plugin
%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_plugin -r :maven-eclipse-plugin

%pom_remove_parent .

%build
mkdir -p hawtjni-runtime/build/classes
javac -d hawtjni-runtime/build/classes -source 6 -target 6 \
  $(find hawtjni-runtime/src/main/java/ -name *.java | xargs)
jar cf hawtjni-runtime.jar -C hawtjni-runtime/build/classes .
mkdir -p  hawtjni-generator/build/classes
javac -d hawtjni-generator/build/classes \
  -source 6 -target 6 \
  -cp $(build-classpath commons-cli objectweb-asm/asm objectweb-asm/asm-commons xbean/xbean-finder xbean/xbean-asm-util):hawtjni-runtime.jar \
  $(find hawtjni-generator/src/main/java/ -name *.java | xargs)
jar cf hawtjni-generator.jar -C hawtjni-generator/build/classes .
jar uf hawtjni-generator.jar -C hawtjni-generator/src/main/resources .
mkdir -p hawtjni-runtime/build/apidoc
javadoc -d hawtjni-runtime/build/apidoc -source 6 \
  -classpath $(build-classpath commons-cli objectweb-asm/asm objectweb-asm/asm-commons xbean/xbean-finder xbean/xbean-asm-util) \
  $(find hawtjni-runtime/src/main/java/ -name *.java && \
    find hawtjni-generator/src/main/java/ -name *.java| xargs)

%install
# jars
install -dm 755 %{buildroot}%{_javadir}/hawtjni
install -dm 755 %{buildroot}%{_jnidir}/hawtjni
install -m 0644 hawtjni-runtime.jar %{buildroot}%{_jnidir}/hawtjni/
install -m 0644 hawtjni-generator.jar %{buildroot}%{_javadir}/hawtjni/

# poms
install -dm 755 %{buildroot}%{_mavenpomdir}/hawtjni
install -m 0644 pom.xml %{buildroot}%{_mavenpomdir}/hawtjni/hawtjni-project.pom
install -m 0644 hawtjni-runtime/pom.xml %{buildroot}%{_mavenpomdir}/hawtjni/hawtjni-runtime.pom
install -m 0644 hawtjni-generator/pom.xml %{buildroot}%{_mavenpomdir}/hawtjni/hawtjni-generator.pom
%add_maven_depmap hawtjni/hawtjni-project.pom
%add_maven_depmap hawtjni/hawtjni-generator.pom hawtjni/hawtjni-generator.jar -f generator
%add_maven_depmap hawtjni/hawtjni-runtime.pom hawtjni/hawtjni-runtime.jar

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/hawtjni
cp -pr  hawtjni-runtime/build/apidoc/* %{buildroot}%{_javadocdir}/hawtjni/
%fdupes -s %{buildroot}%{_javadocdir}/hawtjni/

%{jpackage_script org.fusesource.hawtjni.generator.HawtJNI "" "" commons-cli:objectweb-asm/asm:objectweb-asm/asm-commons:xbean/xbean-finder:xbean/xbean-asm-util:hawtjni/hawtjni-runtime:hawtjni/hawtjni-generator hawtjni-generator true}

%files -f .mfiles
%license license.txt
%doc readme.md changelog.md

%files -n hawtjni -f .mfiles-generator
%{_bindir}/hawtjni-generator

%files -n hawtjni-javadoc
%{_javadocdir}/hawtjni
%license license.txt

%changelog
