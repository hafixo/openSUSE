#
# spec file for package ocaml-jsonm
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _name   jsonm
Name:           ocaml-jsonm
Version:        1.0.1
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Non-blocking streaming JSON codec for OCaml
License:        ISC
Group:          Development/Languages/OCaml
Url:            http://erratique.ch/software/jsonm 
Source:         http://erratique.ch/software/jsonm/releases/%{_name}-%{version}.tbz
BuildRequires:  ocaml
BuildRequires:  ocaml-oasis
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.03
BuildRequires:  ocamlfind(uutf)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Jsonm is an OCaml non-blocking streaming codec to decode and encode the JSON
data format. It can process JSON text without blocking on IO and without a
complete in-memory representation of the data.

The uncut codec also processes whitespace and (non-standard) JSON with
JavaScript comments.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{_name}-%{version}

%build
rm -fv setup.ml myocamlbuild.ml META* _* */_* 
# obs service changes every ^Version line ...
sh -c "sed 's/^Version.*/Version: %{version}/' | tee _oasis" <<_EOF_
OASISFormat: 0.4
Name:        jsonm
Version:     0
Synopsis:    Non-blocking streaming JSON codec
Authors:     Daniel Bünzli <daniel.buenzl i@erratique.ch>
License:     %{license}
LicenseFile: LICENSE.md
Plugins:     META(`oasis version`)
BuildTools:  ocamlbuild

Library jsonm
 Path: src
 Install: true
 Modules: Jsonm
 BuildDepends: uutf

Document jsonm
 Title:                API reference for jsonm
 Type:                 ocamlbuild
 BuildTools+:          ocamldoc
 InstallDir:           \$htmldir
 Install:              true
 XOCamlbuildPath:      .
 XOCamlbuildLibraries: jsonm
_EOF_
%oasis_setup
%ocaml_oasis_configure --enable-docs
%ocaml_oasis_build
%ocaml_oasis_doc

%install
%ocaml_oasis_findlib_install

%files
%defattr(-,root,root)
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%endif

%files devel
%defattr(-,root,root,-)
%{oasis_docdir_html}
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%endif
%{_libdir}/ocaml/*/*.annot
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.cmt
%{_libdir}/ocaml/*/*.cmti
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/META

%changelog
