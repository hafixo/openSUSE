#
# spec file for package grpc-httpjson-transcoding
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define sover 0
%define libname libgrpc-httpjson-transcoding%{sover}
%define src_install_dir /usr/src/%{name}

Name:           grpc-httpjson-transcoding
Version:        20181128
Release:        0
Summary:        Library for transcoding HTTP/JSON to gRPC
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Url:            https://github.com/grpc-ecosystem/%{name}
Source0:        %{name}-%{version}.tar.xz
Source1:        repositories.bzl
Source2:        BUILD
Source3:        WORKSPACE
Source100:      grpc-httpjson-transcoding-rpmlintrc
BuildRequires:  abseil-cpp-devel
BuildRequires:  bazel
BuildRequires:  gcc-c++
BuildRequires:  googleapis-source
BuildRequires:  patchelf
BuildRequires:  protobuf-source
ExcludeArch:    %ix86

%description
grpc-httpjson-transcoding is a library that supports transcoding so that
HTTP/JSON can be converted to gRPC. It allows to provide APIs in both gRPC and
REST style at the same time.

%package -n %{libname}
Summary:        Library for transcoding HTTP/JSON to gRPC
Group:          System/Libraries

%description -n %{libname}
grpc-httpjson-transcoding is a library that supports transcoding so that
HTTP/JSON can be converted to gRPC. It allows to provide APIs in both gRPC and
REST style at the same time.

%package devel
Summary:        Development files for grpc-httpjson-transcoding
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Development files for grpc-httpjson-transcoding - a library that supports
transcoding so that HTTP/JSON can be converted to gRPC. It allows to provide
APIs in both gRPC and REST style at the same time.

%package source
Summary:        Source code of grpc-httpjson-transcoding
Group:          Development/Sources
BuildArch:      noarch

%description source
Source code of grpc-httpjson-transcoding - a library that supports transcoding
so that HTTP/JSON can be converted to gRPC. It allows to provide APIs in both
gRPC and REST style at the same time.

%prep
# Upstream sources of googleapis do not export servicecontrol protobufs for
# Bazel builds which use googleapis as a dependency. This custom BUILD file
# expots them.
mkdir googleapis
cp -r /usr/src/googleapis/* googleapis/

%setup -q
cp %{SOURCE1} .
cp %{SOURCE2} .
cp %{SOURCE3} .
# Unit tests in grpc-httpjson-transcoding are not able to use gtest as a shared
# library. We don't run tests in this spec, so let's just get rid of them...
rm test/BUILD

sed -i 's|@com_google_absl//absl/strings|//:abseil_strings|g' ./src/BUILD

%build
# TODO(mrostecki): Create a macro in bazel package.
bazel build \
    -c dbg \
    --color=no \
    %(for opt in %{optflags}; do echo -e "--copt=${opt} \c"; done) \
    --curses=no \
    --distdir=%{_sourcedir} \
    --genrule_strategy=standalone \
    --spawn_strategy=standalone \
    --strip=never \
    --verbose_failures \
    //...
bazel shutdown

%install
install -D -m0755 bazel-bin/src/libmessage_stream.so %{buildroot}%{_libdir}/libmessage_stream.so.%{sover}
install -D -m0755 bazel-bin/src/libjson_request_translator.so %{buildroot}%{_libdir}/libjson_request_translator.so.%{sover}
install -D -m0755 bazel-bin/src/libpath_matcher.so %{buildroot}%{_libdir}/libpath_matcher.so.%{sover}
install -D -m0755 bazel-bin/src/libhttp_template.so %{buildroot}%{_libdir}/libhttp_template.so.%{sover}
install -D -m0755 bazel-bin/src/libmessage_reader.so %{buildroot}%{_libdir}/libmessage_reader.so.%{sover}
install -D -m0755 bazel-bin/src/librequest_weaver.so %{buildroot}%{_libdir}/librequest_weaver.so.%{sover}
install -D -m0755 bazel-bin/src/librequest_stream_translator.so %{buildroot}%{_libdir}/librequest_stream_translator.so.%{sover}
install -D -m0755 bazel-bin/src/libresponse_to_json_translator.so %{buildroot}%{_libdir}/libresponse_to_json_translator.so.%{sover}
install -D -m0755 bazel-bin/src/librequest_message_translator.so %{buildroot}%{_libdir}/librequest_message_translator.so.%{sover}
install -D -m0755 bazel-bin/src/libprefix_writer.so %{buildroot}%{_libdir}/libprefix_writer.so.%{sover}
install -D -m0755 bazel-bin/src/libtype_helper.so %{buildroot}%{_libdir}/libtype_helper.so.%{sover}
# We can't patchelf libraries in the build step, because bazel saves the build
# output in protected read-only directory.
patchelf --set-soname libmessage_stream.so.%{sover} %{buildroot}%{_libdir}/libmessage_stream.so.%{sover}
patchelf --set-soname libjson_request_translator.so.%{sover} %{buildroot}%{_libdir}/libjson_request_translator.so.%{sover}
patchelf --set-soname libpath_matcher.so.%{sover} %{buildroot}%{_libdir}/libpath_matcher.so.%{sover}
patchelf --set-soname libhttp_template.so.%{sover} %{buildroot}%{_libdir}/libhttp_template.so.%{sover}
patchelf --set-soname libmessage_reader.so.%{sover} %{buildroot}%{_libdir}/libmessage_reader.so.%{sover}
patchelf --set-soname librequest_weaver.so.%{sover} %{buildroot}%{_libdir}/librequest_weaver.so.%{sover}
patchelf --set-soname librequest_stream_translator.so.%{sover} %{buildroot}%{_libdir}/librequest_stream_translator.so.%{sover}
patchelf --set-soname libresponse_to_json_translator.so.%{sover} %{buildroot}%{_libdir}/libresponse_to_json_translator.so.%{sover}
patchelf --set-soname librequest_message_translator.so.%{sover} %{buildroot}%{_libdir}/librequest_message_translator.so.%{sover}
patchelf --set-soname libprefix_writer.so.%{sover} %{buildroot}%{_libdir}/libprefix_writer.so.%{sover}
patchelf --set-soname libtype_helper.so.%{sover} %{buildroot}%{_libdir}/libtype_helper.so.%{sover}
ln -sf libmessage_stream.so.%{sover} %{buildroot}%{_libdir}/libmessage_stream.so
ln -sf libjson_request_translator.so.%{sover} %{buildroot}%{_libdir}/libjson_request_translator.so
ln -sf libpath_matcher.so.%{sover} %{buildroot}%{_libdir}/libpath_matcher.so
ln -sf libhttp_template.so.%{sover} %{buildroot}%{_libdir}/libhttp_template.so
ln -sf libmessage_reader.so.%{sover} %{buildroot}%{_libdir}/libmessage_reader.so
ln -sf librequest_weaver.so.%{sover} %{buildroot}%{_libdir}/librequest_weaver.so
ln -sf librequest_stream_translator.so.%{sover} %{buildroot}%{_libdir}/librequest_stream_translator.so
ln -sf libresponse_to_json_translator.so.%{sover} %{buildroot}%{_libdir}/libresponse_to_json_translator.so
ln -sf librequest_message_translator.so.%{sover} %{buildroot}%{_libdir}/librequest_message_translator.so
ln -sf libprefix_writer.so.%{sover} %{buildroot}%{_libdir}/libprefix_writer.so
ln -sf libtype_helper.so.%{sover} %{buildroot}%{_libdir}/libtype_helper.so
for header in $(find src/include -name "*.h" -printf "%%P\n"); do
    install -D -m0644 src/include/$header %{buildroot}%{_includedir}/$header
done

# Install sources
mkdir -p %{buildroot}%{src_install_dir}
tar -xf %{SOURCE0} --strip-components=1 -C %{buildroot}%{src_install_dir}
pushd %{buildroot}%{src_install_dir}
sed -i 's|@com_google_absl//absl/strings|//:abseil_strings|g' ./src/BUILD
cp %{SOURCE1} .
cp %{SOURCE2} .
cp %{SOURCE3} .
popd

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/libhttp_template.so.0
%{_libdir}/libjson_request_translator.so.0
%{_libdir}/libmessage_reader.so.0
%{_libdir}/libmessage_stream.so.0
%{_libdir}/libpath_matcher.so.0
%{_libdir}/libprefix_writer.so.0
%{_libdir}/librequest_message_translator.so.0
%{_libdir}/librequest_stream_translator.so.0
%{_libdir}/librequest_weaver.so.0
%{_libdir}/libresponse_to_json_translator.so.0
%{_libdir}/libtype_helper.so.0

%files devel
%{_includedir}/grpc_transcoding
%{_libdir}/libhttp_template.so
%{_libdir}/libjson_request_translator.so
%{_libdir}/libmessage_reader.so
%{_libdir}/libmessage_stream.so
%{_libdir}/libpath_matcher.so
%{_libdir}/libprefix_writer.so
%{_libdir}/librequest_message_translator.so
%{_libdir}/librequest_stream_translator.so
%{_libdir}/librequest_weaver.so
%{_libdir}/libresponse_to_json_translator.so
%{_libdir}/libtype_helper.so

%files source
%{src_install_dir}

%changelog
