#
# spec file for package python-nltk
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


%{!?python_module:%define python_module() python-%{**} python3-%{**}}
%define interps python python3
%define pyname nltk
Name:           python-nltk
Version:        3.4.4
Release:        0
Summary:        Natural Language Toolkit
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://nltk.org/
Source:         https://files.pythonhosted.org/packages/source/n/nltk/%{pyname}-%{version}.zip
BuildRequires:  %{interps}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python-singledispatch
BuildRequires:  unzip
Requires:       python-six
Recommends:     python-gensim
Recommends:     python-matplotlib
Recommends:     python-numpy
Recommends:     python-pyparsing
Recommends:     python-python-crfsuite
Recommends:     python-requests
Recommends:     python-scikit-learn
Recommends:     python-scipy
Recommends:     python-twython
BuildArch:      noarch
%ifpython2
Requires:       python-singledispatch
%endif
%ifpython2
Requires:       python2-singledispatch
%endif
%python_subpackages

%description
NLTK -- the Natural Language Toolkit -- is a suite of
Python modules, data sets and tutorials supporting research and
development in Natural Language Processing.

%prep
%setup -q -n %{pyname}-%{version}

sed -i "1,4{/\/usr\/bin\/env/d}" nltk/corpus/reader/knbc.py
sed -i "1,4{/\/usr\/bin\/env/d}" nltk/test/runtests.py
sed -i "1,4{/\/usr\/bin\/env/d}" nltk/test/unit/test_tgrep.py
sed -i "1,4{/\/usr\/bin\/env/d}" nltk/tgrep.py
sed -i "1,4{/\/usr\/bin\/env/d}" nltk/tokenize/stanford_segmenter.py

%build
%python_build

%install
%python_install

%{python_expand %fdupes -s %{buildroot}%{$python_sitelib}/
chmod -x %{buildroot}%{$python_sitelib}/nltk/test/dependency.doctest
}

%check
# FOLLOWING http://www.nltk.org/install.html
%python_exec -c "import nltk" || exit 1

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/%{pyname}/
%{python_sitelib}/%{pyname}-%{version}-py%{py_ver}.egg-info/

%changelog
