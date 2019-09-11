#
# spec file for package python-GitPython
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
Name:           python-GitPython
Version:        2.1.11.1531661757.92a4819
Release:        0
Summary:        Python Git Library
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/gitpython-developers/GitPython
Source:         GitPython-%{version}.tar.xz
Patch0:         test-skips.patch
# Subset and rebase of merged https://github.com/gitpython-developers/GitPython/pull/793
Patch1:         merged_pr_793.patch
Patch2:         test_blocking_lock_file-extra-time.patch
BuildRequires:  %{python_module ddt >= 1.1.1}
BuildRequires:  %{python_module gitdb2 >= 2.0.0}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module smmap2 >= 2.0.0}
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  python-rpm-macros
BuildRequires:  python2-mock
Requires:       git-core
Requires:       python-gitdb2 >= 2.0.0
BuildArch:      noarch
%python_subpackages

%description
GitPython is a python library used to interact with Git repositories.

GitPython provides object model read and write access to your git repository.
Access repository information conveniently, alter the index directly, handle
remotes, or go down to low-level object database access with big-files support.

With the new object database abstraction added in 0.3, its even possible to
implement your own storage mechanisms, the currently available implementations
are 'cgit' and pure python, which is the default.

%prep
%setup -q -n GitPython-%{version}
echo y | ./init-tests-after-clone.sh
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/git/test/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# While SKIP_GITHUB is fine, the two tests skipped with SKIP_LOCALHOST
# should work as the test runner sets up a git daemon.
export SKIP_GITHUB=true
export SKIP_LOCALHOST=true
export TRAVIS=true

export LANG=en_US.UTF-8
export GIT_PYTHON_TEST_GIT_REPO_BASE=${PWD}

git config --global user.email "you@example.com"
git config --global user.name "Your Name"

%python_exec setup.py test --test-suite=git.test

%files %{python_files}
%license LICENSE
%doc AUTHORS CHANGES README.md doc/source/*.rst
%{python_sitelib}/*

%changelog
