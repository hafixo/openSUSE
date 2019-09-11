#
# spec file for package python-astor
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}

Name:           python-astor
Version:        0.8
Release:        0
Summary:        Read/rewrite/write Python ASTs
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/berkerpeksag/astor
Source:         https://github.com/berkerpeksag/astor/archive/%{version}.tar.gz#/astor-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module nose}
BuildRequires:  python2-unittest2
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
astor is designed to allow easy manipulation of Python source via the AST.
There are some other similar libraries, but astor focuses on the following areas:
- Round-trip an AST back to Python:
  - Modified AST doesn't need linenumbers, ctx, etc. or otherwise
    be directly compileable for the round-trip to work.
  - Easy to read generated code as, well, code
  - Can round-trip two different source trees to compare for functional
    differences, using the astor.rtrip tool (for example, after PEP8 edits).
- Dump pretty-printing of AST
  - Harder to read than round-tripped code, but more accurate to figure out what
    is going on.
  - Easier to read than dump from built-in AST module
- Non-recursive treewalk
  - Sometimes you want a recursive treewalk (and astor supports that, starting
    at any node on the tree), but sometimes you don't need to do that.  astor
    doesn't require you to explicitly visit sub-nodes unless you want to:
  - You can add code that executes before a node's children are visited, and/or
  - You can add code that executes after a node's children are visited, and/or
  - You can add code that executes and keeps the node's children from being
    visited (and optionally visit them yourself via a recursive call)
  - Write functions to access the tree based on object names and/or attribute names
  - Enjoy easy access to parent node(s) for tree rewriting

%prep
%setup -q -n astor-%{version}
# ugly fix for the use of /usr/bin/env
sed -i 's@env @@' astor/rtrip.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# fix executeable bits
%python_expand chmod 755 %{buildroot}%{$python_sitelib}/astor/rtrip.py

%check
%python_expand nosetests-%{$python_bin_suffix} -v

%files %{python_files}
%doc AUTHORS README.rst docs/*.rst
%license LICENSE 
%{python_sitelib}/*

%changelog
