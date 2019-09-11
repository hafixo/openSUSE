#
# spec file for package cadabra2
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


Name:           cadabra2
Version:        2.2.7
Release:        0
Summary:        A computer algebra system for solving problems in field theory
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
Url:            http://cadabra.science/
Source0:        https://github.com/kpeeters/cadabra2/archive/%{version}.tar.gz
Source1:        %{name}-rpmlintrc
Source2:        %{name}-gtk.appdata.xml
# PATCH-FIX-OPENSUSE add -pthread to CMAKE_CXX_FLAGS (as adivised in https://github.com/potree/PotreeConverter/issues/136) kkaempf@suse.de
Patch1:         cadabra2-add-pthread-to-cxxflags.patch
BuildRequires:  appstream-glib
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++ >= 4.9
BuildRequires:  gmp-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libuuid-devel
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig
BuildRequires:  texlive-dvipng
BuildRequires:  texlive-dvipng-bin
BuildRequires:  texlive-epstopdf
BuildRequires:  texlive-latex-bin
BuildRequires:  texlive-makeindex-bin
BuildRequires:  texlive-metafont-bin
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  tex(8r.enc)
BuildRequires:  tex(adjustbox.sty)
BuildRequires:  tex(caption.sty)
BuildRequires:  tex(colortbl.sty)
BuildRequires:  tex(fancyhdr.sty)
BuildRequires:  tex(float.sty)
BuildRequires:  tex(geometry.sty)
BuildRequires:  tex(helvet.sty)
BuildRequires:  tex(hyperref.sty)
BuildRequires:  tex(multirow.sty)
BuildRequires:  tex(natbib.sty)
BuildRequires:  tex(pcrr8t.tfm)
BuildRequires:  tex(phvr8t.tfm)
BuildRequires:  tex(psyr.tfm)
BuildRequires:  tex(rsfs10.tfm)
BuildRequires:  tex(sectsty.sty)
BuildRequires:  tex(tabu.sty)
BuildRequires:  tex(textcomp.sty)
BuildRequires:  tex(tocloft.sty)
BuildRequires:  tex(wasy7.tfm)
BuildRequires:  tex(wasysym.sty)
BuildRequires:  tex(xtab.sty)
BuildRequires:  tex(zptmcm7t.tfm)
Requires(post): texlive-kpathsea-bin
Requires(postun): texlive-kpathsea-bin
Recommends:     %{name}-doc
Recommends:     %{name}-examples
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} > 1320
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_python3-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  python3-devel
BuildRequires:  python3-matplotlib
BuildRequires:  python3-sympy
%else
BuildRequires:  boost-devel
BuildRequires:  python-devel
BuildRequires:  python-matplotlib
BuildRequires:  python-sympy
%endif

%description
Cadabra2 is a computer algebra system (CAS) designed specifically for
the solution of problems encountered in field theory. It has extensive
functionality for tensor computer algebra, tensor polynomial
simplification including multi-term symmetries, fermions and
anti-commuting variables, Clifford algebras and Fierz transformations,
implicit coordinate dependence, multiple index types and many more.
The input format is a subset of TeX. Both a command-line and a
graphical interface are available.

Key features of Cadabra2:
- Input and output using TeX notation.
- Designed for field-theory problems, with handling of anti-commuting
  and non-commuting objects without special notations for their
  products, gamma matrix algebra, Fierz identities, Dirac conjugation,
  vielbeine, flat and curved, covariant and contravariant indices,
  implicit dependence of tensors on coordinates, partial and covariant
  derivatives...
- Powerful tensor simplification algorithms, not just for mono-term
  symmetries but also for multi-terms symmetries like the Bianchi
  identity, or dimensionally-dependent symmetries like the Schouten
  identity.

%package gui
Summary:        GUI for cadabra2: computer algebra system for problems in field theory
Group:          Productivity/Scientific/Math
Requires:       %{name} = %{version}
Obsoletes:      cadabra < 2.0
Provides:       cadabra = %{version}

%description gui
Cadabra2 is a computer algebra system (CAS) designed specifically for
the solution of problems encountered in field theory.

This package provides the GUI for %{name} and it's desktop menu integration.

%package examples
Summary:        A computer algebra system for solving problems in field theory
Group:          Productivity/Scientific/Math
Requires:       %{name} = %{version}

%description examples
Cadabra2 is a computer algebra system (CAS) designed specifically for
the solution of problems encountered in field theory.

This package provides examples for %{name}.

%package doc
Summary:        A computer algebra system for solving problems in field theory
Group:          Documentation/HTML
Obsoletes:      cadabra-doc < 2.0
Provides:       cadabra-doc = %{version}

%description doc
Cadabra2 is a computer algebra system (CAS) designed specifically for
the solution of problems encountered in field theory.

This package provides html documentation for %{name}.

%prep
%setup -q
%patch1 -p1
rm examples/.gitignore

%build

# FIXME: you should use %%cmake macro but it doesn't work
mkdir build && pushd build
cmake \\\
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \\\
  -DCMAKE_MANDIR=%{_mandir} \\\
  -DPACKAGING_MODE=ON \\\
%if 0%{?suse_version} <= 1320
  -DUSE_PYTHON_3=OFF \\\
%endif
  -DINSTALL_LATEX_DIR=%{_datadir}/texmf \\\
  -DENABLE_FRONTEND=ON \\\
  -DENABLE_MATHEMATICA=OFF \\\
  ..

make %{?_smp_mflags}
popd
make %{?_smp_mflags} doc

%install
%cmake_install DESTDIR=%{buildroot}

%suse_update_desktop_file cadabra2-gtk

# INSTALL APPDATA TO /usr/share/metainfo
install -D -m0644 %{S:2} %{buildroot}%{_datadir}/metainfo/%{name}-gtk.appdata.xml

# Replace "/usr/bin/env python3" hashbang by "/usr/bin/python3"
sed -E -i "s|^#!/usr/bin/env python3|#!/usr/bin/python3|" %{buildroot}%{_bindir}/cadabra2

mkdir -p %{buildroot}%{_datadir}/texmf/tex/latex/cadabra2/
ln %{buildroot}%{_datadir}/cadabra2/latex/* %{buildroot}%{_datadir}/texmf/tex/latex/cadabra2/

# Move man files to proper %%_mandir
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_prefix}/man/man1/* %{buildroot}%{_mandir}/man1/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%if 0%{?suse_version} <= 1320
%post gui
%icon_theme_cache_post
%desktop_database_post

%postun gui
%icon_theme_cache_postun
%desktop_database_postun
%endif

%files
%doc README.rst
%license doc/license.txt
%{_bindir}/cadabra2cadabra
%{_bindir}/cadabra-server
%{_bindir}/%{name}
%{_bindir}/%{name}python
%{_bindir}/%{name}html
%{_datadir}/%{name}/
%{_datadir}/texmf/tex/latex/cadabra2/
%{_mandir}/man1/cadabra*.1%{?ext_man}

%files gui
%{_bindir}/%{name}-gtk
%{_datadir}/icons/hicolor/*/apps/cadabra2-gtk.*
%{_datadir}/applications/cadabra2-gtk.desktop
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/*.appdata.xml

%files examples
%doc examples/

%files doc
%doc doxygen/html

%changelog
