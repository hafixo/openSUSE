#
# spec file for package texlive-specs-t
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


%bcond_with	zypper_posttrans

%define texlive_version  2019
%define texlive_previous 2018
%define texlive_release  20190407
%define texlive_noarch   163

#!BuildIgnore:          texlive

%global _varlib         %{_localstatedir}/lib
%global _libexecdir     %{_prefix}/lib

%define _texmfdistdir   %{_datadir}/texmf
%if 0%{texlive_version} >= 2013
%define _texmfmaindir   %{_texmfdistdir}
%define _texmfdirs      %{_texmfdistdir}
%else
%define _texmfmaindir   %{_libexecdir}/texmf
%define _texmfdirs      \{%{_texmfdistdir},%{_texmfmaindir}\}
%endif

%define _texmfconfdir   %{_sysconfdir}/texmf
%define _texmfvardir    %{_varlib}/texmf
%define _texmfcache     %{_localstatedir}/cache/texmf
%define _fontcache      %{_texmfcache}/fonts
#
%define _x11bin         %{_prefix}/bin
%define _x11lib         %{_libdir}
%define _x11data        %{_datadir}/X11
%define _x11inc         %{_includedir}
%define _appdefdir      %{_x11data}/app-defaults

Name:           texlive-specs-t
Version:        2019
Release:        0
BuildRequires:  ed
BuildRequires:  fontconfig
BuildRequires:  fontpackages-devel
BuildRequires:  t1utils
BuildRequires:  texlive-filesystem
BuildRequires:  xz
BuildArch:      noarch
Summary:        Meta package for t
License:        Apache-1.0 and BSD-3-Clause and GPL-2.0+ and LGPL-2.1+ and LPPL-1.0 and OFL-1.1 and SUSE-Public-Domain and SUSE-TeX
Group:          Productivity/Publishing/TeX/Base
Url:            https://build.opensuse.org/package/show/Publishing:TeXLive/Meta
Source0:        texlive-specs-t-rpmlintrc

%description
Meta package to build tons of noarch texlive packages.

%package -n texlive-pst-pdf
Version:        %{texlive_version}.%{texlive_noarch}.1.2dsvn44665
Release:        0
Summary:        Make PDF versions of graphics by processing between runs
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive-pst-pdf-bin >= %{texlive_version}
#!BuildIgnore: texlive-pst-pdf-bin
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-pdf-doc >= %{texlive_version}
Provides:       tex(pst-pdf.sty)
Requires:       tex(dvips.def)
Requires:       tex(environ.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifvtex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(luatex85.sty)
Requires:       tex(pdftex.def)
Requires:       tex(preview.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source1:        pst-pdf.tar.xz
Source2:        pst-pdf.doc.tar.xz

%description -n texlive-pst-pdf
The package pst-pdf simplifies the use of graphics from
PSTricks and other PostScript code in PDF documents. As in
building a bibliography with BibTeX, additional external
programmes are invoked. In this case they are used to create a
PDF file (\PDFcontainer) that will contain all the graphics
material. In the final document these contents will be inserted
instead of the original PostScript code. The package works with
pstricks and requires a recent version of the preview package.

date: 2018-09-15 11:05:45 +0000


%package -n texlive-pst-pdf-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2dsvn44665
Release:        0
Summary:        Documentation for texlive-pst-pdf
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-pst-pdf-doc:de;en)

%description -n texlive-pst-pdf-doc
This package includes the documentation for texlive-pst-pdf

%post -n texlive-pst-pdf
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-pdf 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-pdf
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-pdf-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pst-pdf/CHANGES
%{_texmfdistdir}/doc/latex/pst-pdf/Makefile
%{_texmfdistdir}/doc/latex/pst-pdf/README.md
%{_texmfdistdir}/doc/latex/pst-pdf/pst-pdf-DE.pdf
%{_texmfdistdir}/doc/latex/pst-pdf/pst-pdf-example.pdf
%{_texmfdistdir}/doc/latex/pst-pdf/pst-pdf-example.tex
%{_texmfdistdir}/doc/latex/pst-pdf/pst-pdf.pdf

%files -n texlive-pst-pdf
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/pst-pdf/ps4pdf
%{_texmfdistdir}/scripts/pst-pdf/ps4pdf.bat.noMiKTeX
%{_texmfdistdir}/scripts/pst-pdf/ps4pdf.bat.w95
%{_texmfdistdir}/tex/latex/pst-pdf/pst-pdf.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-pdf-%{texlive_version}.%{texlive_noarch}.1.2dsvn44665-%{release}-zypper
%endif

%package -n texlive-pst-pdgr
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn45875
Release:        0
Summary:        Draw medical pedigrees using PSTricks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-pdgr-doc >= %{texlive_version}
Provides:       tex(pst-pdgr.cfg)
Provides:       tex(pst-pdgr.sty)
Provides:       tex(pst-pdgr.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source3:        pst-pdgr.tar.xz
Source4:        pst-pdgr.doc.tar.xz

%description -n texlive-pst-pdgr
The package provides a set of macros based on PSTricks to draw
medical pedigrees according to the recommendations for
standardized human pedigree nomenclature. The drawing commands
place the symbols on a pspicture canvas. An interface for
making trees is also provided. The package may be used both
with LaTeX and PlainTeX. A separate Perl program for generating
TeX files from spreadsheets is available.

date: 2017-11-20 22:58:47 +0000


%package -n texlive-pst-pdgr-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn45875
Release:        0
Summary:        Documentation for texlive-pst-pdgr
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pst-pdgr-doc
This package includes the documentation for texlive-pst-pdgr

%post -n texlive-pst-pdgr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-pdgr 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-pdgr
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-pdgr-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-pdgr/NEWS
%{_texmfdistdir}/doc/generic/pst-pdgr/README
%{_texmfdistdir}/doc/generic/pst-pdgr/pst-pdgr.bib
%{_texmfdistdir}/doc/generic/pst-pdgr/pst-pdgr.pdf

%files -n texlive-pst-pdgr
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-pdgr/pst-pdgr.tex
%{_texmfdistdir}/tex/latex/pst-pdgr/pst-pdgr.cfg
%{_texmfdistdir}/tex/latex/pst-pdgr/pst-pdgr.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-pdgr-%{texlive_version}.%{texlive_noarch}.0.0.4svn45875-%{release}-zypper
%endif

%package -n texlive-pst-perspective
Version:        %{texlive_version}.%{texlive_noarch}.1.05svn39585
Release:        0
Summary:        Draw perspective views using PSTricks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-perspective-doc >= %{texlive_version}
Provides:       tex(pst-perspective.sty)
Provides:       tex(pst-perspective.tex)
Requires:       tex(pst-grad.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source5:        pst-perspective.tar.xz
Source6:        pst-perspective.doc.tar.xz

%description -n texlive-pst-perspective
The package provides the means to draw an orthogonal parallel
projection with an arbitrarily chosen angle and a variable
shortening factor.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-pst-perspective-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.05svn39585
Release:        0
Summary:        Documentation for texlive-pst-perspective
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-pst-perspective-doc:de;en)

%description -n texlive-pst-perspective-doc
This package includes the documentation for texlive-pst-perspective

%post -n texlive-pst-perspective
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-perspective 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-perspective
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-perspective-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-perspective/Parallelprojektion-Kreis.pdf
%{_texmfdistdir}/doc/generic/pst-perspective/Parallelprojektion-Kreis.tex
%{_texmfdistdir}/doc/generic/pst-perspective/README
%{_texmfdistdir}/doc/generic/pst-perspective/pst-perspective-doc.pdf
%{_texmfdistdir}/doc/generic/pst-perspective/pst-perspective-doc.tex
%{_texmfdistdir}/doc/generic/pst-perspective/pst-perspective-docEN.pdf
%{_texmfdistdir}/doc/generic/pst-perspective/pst-perspective-docEN.tex

%files -n texlive-pst-perspective
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-perspective/pst-perspective.tex
%{_texmfdistdir}/tex/latex/pst-perspective/pst-perspective.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-perspective-%{texlive_version}.%{texlive_noarch}.1.05svn39585-%{release}-zypper
%endif

%package -n texlive-pst-platon
Version:        %{texlive_version}.%{texlive_noarch}.0.0.01svn16538
Release:        0
Summary:        Platonic solids in PSTricks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-platon-doc >= %{texlive_version}
Provides:       tex(pst-platon.sty)
Requires:       tex(pst-3d.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source7:        pst-platon.tar.xz
Source8:        pst-platon.doc.tar.xz

%description -n texlive-pst-platon
The package adds to PSTricks the ability to draw 3-dimensional
views of the five Platonic solids.

date: 2018-09-15 11:08:05 +0000


%package -n texlive-pst-platon-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.01svn16538
Release:        0
Summary:        Documentation for texlive-pst-platon
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pst-platon-doc
This package includes the documentation for texlive-pst-platon

%post -n texlive-pst-platon
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-platon 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-platon
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-platon-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-platon/Changes
%{_texmfdistdir}/doc/generic/pst-platon/README
%{_texmfdistdir}/doc/generic/pst-platon/pst-platon-doc.bib
%{_texmfdistdir}/doc/generic/pst-platon/pst-platon-doc.pdf
%{_texmfdistdir}/doc/generic/pst-platon/pst-platon-doc.tex

%files -n texlive-pst-platon
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pst-platon/pst-platon.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-platon-%{texlive_version}.%{texlive_noarch}.0.0.01svn16538-%{release}-zypper
%endif

%package -n texlive-pst-plot
Version:        %{texlive_version}.%{texlive_noarch}.1.91svn48526
Release:        0
Summary:        Plot data using PSTricks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-plot-doc >= %{texlive_version}
Provides:       tex(pst-plot.sty)
Provides:       tex(pst-plot.tex)
Provides:       tex(pst-plot97.tex)
Requires:       tex(multido.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source9:        pst-plot.tar.xz
Source10:       pst-plot.doc.tar.xz

%description -n texlive-pst-plot
The package provides plotting of data (typically from external
files), using PSTricks. Plots may be configured using a wide
variety of parameters.

date: 2018-08-31 17:10:21 +0000


%package -n texlive-pst-plot-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.91svn48526
Release:        0
Summary:        Documentation for texlive-pst-plot
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-pst-plot-doc:en)

%description -n texlive-pst-plot-doc
This package includes the documentation for texlive-pst-plot

%post -n texlive-pst-plot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-plot 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-plot
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-plot-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-plot/Changes
%{_texmfdistdir}/doc/generic/pst-plot/README
%{_texmfdistdir}/doc/generic/pst-plot/data/Data.dat
%{_texmfdistdir}/doc/generic/pst-plot/data/LSM.data
%{_texmfdistdir}/doc/generic/pst-plot/data/LSM2.data
%{_texmfdistdir}/doc/generic/pst-plot/data/boxplot.data
%{_texmfdistdir}/doc/generic/pst-plot/data/data.data
%{_texmfdistdir}/doc/generic/pst-plot/data/data1.dat
%{_texmfdistdir}/doc/generic/pst-plot/data/data3.data
%{_texmfdistdir}/doc/generic/pst-plot/data/dataMul.data
%{_texmfdistdir}/doc/generic/pst-plot/data/demo.txt
%{_texmfdistdir}/doc/generic/pst-plot/data/demo0.data
%{_texmfdistdir}/doc/generic/pst-plot/data/demo1.data
%{_texmfdistdir}/doc/generic/pst-plot/data/demo2.data
%{_texmfdistdir}/doc/generic/pst-plot/data/demo3.data
%{_texmfdistdir}/doc/generic/pst-plot/data/dotmatrix.data
%{_texmfdistdir}/doc/generic/pst-plot/data/pst-plot-doc.eps
%{_texmfdistdir}/doc/generic/pst-plot/data/pstricks-add-data9.data
%{_texmfdistdir}/doc/generic/pst-plot/data/test.data
%{_texmfdistdir}/doc/generic/pst-plot/pst-plot-doc.bib
%{_texmfdistdir}/doc/generic/pst-plot/pst-plot-doc.pdf
%{_texmfdistdir}/doc/generic/pst-plot/pst-plot-doc.tex

%files -n texlive-pst-plot
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-plot/pst-plot.tex
%{_texmfdistdir}/tex/generic/pst-plot/pst-plot97.tex
%{_texmfdistdir}/tex/latex/pst-plot/pst-plot.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-plot-%{texlive_version}.%{texlive_noarch}.1.91svn48526-%{release}-zypper
%endif

%package -n texlive-pst-poker
Version:        %{texlive_version}.%{texlive_noarch}.0.0.03svn48347
Release:        0
Summary:        Drawing poker cards
License:        LGPL-2.1-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-poker-doc >= %{texlive_version}
Provides:       tex(pst-poker.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(multido.sty)
Requires:       tex(pst-blur.sty)
Requires:       tex(pst-fill.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source11:       pst-poker.tar.xz
Source12:       pst-poker.doc.tar.xz

%description -n texlive-pst-poker
This PSTricks related package can create poker cards in various
manners.

date: 2018-08-03 19:43:01 +0000


%package -n texlive-pst-poker-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.03svn48347
Release:        0
Summary:        Documentation for texlive-pst-poker
License:        LGPL-2.1-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pst-poker-doc
This package includes the documentation for texlive-pst-poker

%post -n texlive-pst-poker
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-poker 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-poker
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-poker-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pst-poker/Changes
%{_texmfdistdir}/doc/latex/pst-poker/README
%{_texmfdistdir}/doc/latex/pst-poker/pst-poker-doc.bib
%{_texmfdistdir}/doc/latex/pst-poker/pst-poker-doc.pdf
%{_texmfdistdir}/doc/latex/pst-poker/pst-poker-doc.tex

%files -n texlive-pst-poker
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pst-poker/Jack-club-bw.eps
%{_texmfdistdir}/tex/latex/pst-poker/Jack-club-color.eps
%{_texmfdistdir}/tex/latex/pst-poker/Jack-diamond-bw.eps
%{_texmfdistdir}/tex/latex/pst-poker/Jack-diamond-color.eps
%{_texmfdistdir}/tex/latex/pst-poker/Jack-heart-bw.eps
%{_texmfdistdir}/tex/latex/pst-poker/Jack-heart-color.eps
%{_texmfdistdir}/tex/latex/pst-poker/Jack-spade-bw.eps
%{_texmfdistdir}/tex/latex/pst-poker/Jack-spade-color.eps
%{_texmfdistdir}/tex/latex/pst-poker/King-club-bw.eps
%{_texmfdistdir}/tex/latex/pst-poker/King-club-color.eps
%{_texmfdistdir}/tex/latex/pst-poker/King-diamond-bw.eps
%{_texmfdistdir}/tex/latex/pst-poker/King-diamond-color.eps
%{_texmfdistdir}/tex/latex/pst-poker/King-heart-bw.eps
%{_texmfdistdir}/tex/latex/pst-poker/King-heart-color.eps
%{_texmfdistdir}/tex/latex/pst-poker/King-spade-bw.eps
%{_texmfdistdir}/tex/latex/pst-poker/King-spade-color.eps
%{_texmfdistdir}/tex/latex/pst-poker/Queen-club-bw.eps
%{_texmfdistdir}/tex/latex/pst-poker/Queen-club-color.eps
%{_texmfdistdir}/tex/latex/pst-poker/Queen-diamond-bw.eps
%{_texmfdistdir}/tex/latex/pst-poker/Queen-diamond-color.eps
%{_texmfdistdir}/tex/latex/pst-poker/Queen-heart-bw.eps
%{_texmfdistdir}/tex/latex/pst-poker/Queen-heart-color.eps
%{_texmfdistdir}/tex/latex/pst-poker/Queen-spade-bw.eps
%{_texmfdistdir}/tex/latex/pst-poker/Queen-spade-color.eps
%{_texmfdistdir}/tex/latex/pst-poker/pst-poker.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-poker-%{texlive_version}.%{texlive_noarch}.0.0.03svn48347-%{release}-zypper
%endif

%package -n texlive-pst-poly
Version:        %{texlive_version}.%{texlive_noarch}.1.63svn35062
Release:        0
Summary:        Polygons with PSTricks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-poly-doc >= %{texlive_version}
Provides:       tex(pst-poly.sty)
Provides:       tex(pst-poly.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source13:       pst-poly.tar.xz
Source14:       pst-poly.doc.tar.xz

%description -n texlive-pst-poly
This PSTricks package provides a really rather simple command
\PstPolygon that will draw various regular and non-regular
polygons (according to command parameters); various shortcuts
to commonly-used polygons are provided, as well as a command
\pspolygonbox that frames text with a polygon. The package uses
the xkeyval package for argument decoding.

date: 2018-09-15 11:09:48 +0000


%package -n texlive-pst-poly-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.63svn35062
Release:        0
Summary:        Documentation for texlive-pst-poly
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pst-poly-doc
This package includes the documentation for texlive-pst-poly

%post -n texlive-pst-poly
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-poly 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-poly
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-poly-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-poly/Changes
%{_texmfdistdir}/doc/generic/pst-poly/README
%{_texmfdistdir}/doc/generic/pst-poly/pst-poly-doc.bib
%{_texmfdistdir}/doc/generic/pst-poly/pst-poly-doc.pdf
%{_texmfdistdir}/doc/generic/pst-poly/pst-poly-doc.tex

%files -n texlive-pst-poly
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-poly/pst-poly.tex
%{_texmfdistdir}/tex/latex/pst-poly/pst-poly.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-poly-%{texlive_version}.%{texlive_noarch}.1.63svn35062-%{release}-zypper
%endif

%package -n texlive-pst-pulley
Version:        %{texlive_version}.%{texlive_noarch}.0.0.02svn45316
Release:        0
Summary:        Plot pulleys, using PSTricks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-pulley-doc >= %{texlive_version}
Provides:       tex(pst-pulley.sty)
Provides:       tex(pst-pulley.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source15:       pst-pulley.tar.xz
Source16:       pst-pulley.doc.tar.xz

%description -n texlive-pst-pulley
The package enables the user to draw pulley systems with up to
6 pulleys. The pulley diagrams are labelled with the physical
properties of the system. The package uses pstricks and
requires several PSTricks-related packages.

date: 2018-09-15 11:11:53 +0000


%package -n texlive-pst-pulley-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.02svn45316
Release:        0
Summary:        Documentation for texlive-pst-pulley
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pst-pulley-doc
This package includes the documentation for texlive-pst-pulley

%post -n texlive-pst-pulley
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-pulley 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-pulley
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-pulley-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-pulley/Changes
%{_texmfdistdir}/doc/generic/pst-pulley/README.md
%{_texmfdistdir}/doc/generic/pst-pulley/pst-pulley-doc.bib
%{_texmfdistdir}/doc/generic/pst-pulley/pst-pulley-doc.pdf
%{_texmfdistdir}/doc/generic/pst-pulley/pst-pulley-doc.tex

%files -n texlive-pst-pulley
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-pulley/pst-pulley.tex
%{_texmfdistdir}/tex/latex/pst-pulley/pst-pulley.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-pulley-%{texlive_version}.%{texlive_noarch}.0.0.02svn45316-%{release}-zypper
%endif

%package -n texlive-pst-qtree
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Simple syntax for trees
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-qtree-doc >= %{texlive_version}
Provides:       tex(pst-qtree.sty)
Provides:       tex(pst-qtree.tex)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source17:       pst-qtree.tar.xz
Source18:       pst-qtree.doc.tar.xz

%description -n texlive-pst-qtree
The package provides a qtree-like front end for PSTricks.

date: 2018-09-15 11:13:35 +0000


%package -n texlive-pst-qtree-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-pst-qtree
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pst-qtree-doc
This package includes the documentation for texlive-pst-qtree

%post -n texlive-pst-qtree
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-qtree 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-qtree
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-qtree-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-qtree/CHANGES
%{_texmfdistdir}/doc/generic/pst-qtree/LICENSE
%{_texmfdistdir}/doc/generic/pst-qtree/pst-qtree-manual.pdf
%{_texmfdistdir}/doc/generic/pst-qtree/pst-qtree-manual.tex

%files -n texlive-pst-qtree
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-qtree/pst-qtree.tex
%{_texmfdistdir}/tex/latex/pst-qtree/pst-qtree.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-qtree-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-pst-rputover
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn44724
Release:        0
Summary:        Place text over objects without obscuring background colors
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-rputover-doc >= %{texlive_version}
Provides:       tex(pst-rputover.sty)
Provides:       tex(pst-rputover.tex)
Requires:       tex(pst-node.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source19:       pst-rputover.tar.xz
Source20:       pst-rputover.doc.tar.xz

%description -n texlive-pst-rputover
This is a PSTricks package which allows to place text over
objects without obscuring background colors.

date: 2017-07-01 03:09:50 +0000


%package -n texlive-pst-rputover-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn44724
Release:        0
Summary:        Documentation for texlive-pst-rputover
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pst-rputover-doc
This package includes the documentation for texlive-pst-rputover

%post -n texlive-pst-rputover
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-rputover 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-rputover
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-rputover-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-rputover/Changes.txt
%{_texmfdistdir}/doc/generic/pst-rputover/README.md
%{_texmfdistdir}/doc/generic/pst-rputover/pst-rputover-doc.pdf
%{_texmfdistdir}/doc/generic/pst-rputover/pst-rputover-doc.tex

%files -n texlive-pst-rputover
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-rputover/pst-rputover.tex
%{_texmfdistdir}/tex/latex/pst-rputover/pst-rputover.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-rputover-%{texlive_version}.%{texlive_noarch}.1.0svn44724-%{release}-zypper
%endif

%package -n texlive-pst-rubans
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn23464
Release:        0
Summary:        Draw three-dimensional ribbons
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-rubans-doc >= %{texlive_version}
Provides:       tex(pst-rubans.sty)
Provides:       tex(pst-rubans.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source21:       pst-rubans.tar.xz
Source22:       pst-rubans.doc.tar.xz

%description -n texlive-pst-rubans
The package uses PStricks and pst-solides3d to draw three
dimensional ribbons on a cylinder, torus, sphere, cone or
paraboloid. The width of the ribbon, the number of turns, the
colour of the outer and the inner surface of the ribbon may be
set. In the case of circular and conical helices, one may also
choose the number of ribbons.

date: 2018-09-15 11:15:39 +0000


%package -n texlive-pst-rubans-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn23464
Release:        0
Summary:        Documentation for texlive-pst-rubans
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pst-rubans-doc
This package includes the documentation for texlive-pst-rubans

%post -n texlive-pst-rubans
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-rubans 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-rubans
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-rubans-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-rubans/Changes
%{_texmfdistdir}/doc/generic/pst-rubans/README
%{_texmfdistdir}/doc/generic/pst-rubans/pst-rubans-doc.bib
%{_texmfdistdir}/doc/generic/pst-rubans/pst-rubans-doc.pdf
%{_texmfdistdir}/doc/generic/pst-rubans/pst-rubans-doc.tex

%files -n texlive-pst-rubans
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-rubans/pst-rubans.tex
%{_texmfdistdir}/tex/latex/pst-rubans/pst-rubans.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-rubans-%{texlive_version}.%{texlive_noarch}.1.2svn23464-%{release}-zypper
%endif

%package -n texlive-pst-shell
Version:        %{texlive_version}.%{texlive_noarch}.0.0.03svn42840
Release:        0
Summary:        Pst-shell: plotting sea shells
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-shell-doc >= %{texlive_version}
Provides:       tex(pst-shell.sty)
Provides:       tex(pst-shell.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source23:       pst-shell.tar.xz
Source24:       pst-shell.doc.tar.xz

%description -n texlive-pst-shell
pst-shell is a PSTricks related package to draw seashells in 3D
view: Argonauta, Epiteonium, Lyria, Turritella, Tonna,
Achatina, Oxystele, Conus, Ammonite, Codakia, Escalaria,
Helcion, Natalina, Planorbis, and Nautilus, all with different
parameters. pst-shell needs pst-solides3d and an up-to-date
PSTricks, which should be part of your local TeX installation,
otherwise get it from a CTAN server.

date: 2016-12-29 04:38:19 +0000


%package -n texlive-pst-shell-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.03svn42840
Release:        0
Summary:        Documentation for texlive-pst-shell
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pst-shell-doc
This package includes the documentation for texlive-pst-shell

%post -n texlive-pst-shell
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-shell 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-shell
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-shell-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-shell/Changes
%{_texmfdistdir}/doc/generic/pst-shell/README.md
%{_texmfdistdir}/doc/generic/pst-shell/data/cockle-2-couleurs.dat
%{_texmfdistdir}/doc/generic/pst-shell/data/cockle-2-faces.dat
%{_texmfdistdir}/doc/generic/pst-shell/data/cockle-2-io.dat
%{_texmfdistdir}/doc/generic/pst-shell/data/cockle-2-sommets.dat
%{_texmfdistdir}/doc/generic/pst-shell/data/cockle-couleurs.dat
%{_texmfdistdir}/doc/generic/pst-shell/data/cockle-faces.dat
%{_texmfdistdir}/doc/generic/pst-shell/data/cockle-io.dat
%{_texmfdistdir}/doc/generic/pst-shell/data/cockle-sommets.dat
%{_texmfdistdir}/doc/generic/pst-shell/data/nautile-180-24-couleurs.dat
%{_texmfdistdir}/doc/generic/pst-shell/data/nautile-180-24-faces.dat
%{_texmfdistdir}/doc/generic/pst-shell/data/nautile-180-24-io.dat
%{_texmfdistdir}/doc/generic/pst-shell/data/nautile-180-24-sommets.dat
%{_texmfdistdir}/doc/generic/pst-shell/data/nautile-360-36-couleurs.dat
%{_texmfdistdir}/doc/generic/pst-shell/data/nautile-360-36-faces.dat
%{_texmfdistdir}/doc/generic/pst-shell/data/nautile-360-36-io.dat
%{_texmfdistdir}/doc/generic/pst-shell/data/nautile-360-36-sommets.dat
%{_texmfdistdir}/doc/generic/pst-shell/data/testnautile-360-36-couleurs.dat
%{_texmfdistdir}/doc/generic/pst-shell/data/testnautile-360-36-faces.dat
%{_texmfdistdir}/doc/generic/pst-shell/data/testnautile-360-36-io.dat
%{_texmfdistdir}/doc/generic/pst-shell/data/testnautile-360-36-sommets.dat
%{_texmfdistdir}/doc/generic/pst-shell/images/shell.eps
%{_texmfdistdir}/doc/generic/pst-shell/images/shell.pdf
%{_texmfdistdir}/doc/generic/pst-shell/pst-shell-doc.bib
%{_texmfdistdir}/doc/generic/pst-shell/pst-shell-doc.pdf
%{_texmfdistdir}/doc/generic/pst-shell/pst-shell-doc.tex
%{_texmfdistdir}/doc/generic/pst-shell/zz.tex

%files -n texlive-pst-shell
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-shell/pst-shell.pro
%{_texmfdistdir}/tex/generic/pst-shell/pst-shell.tex
%{_texmfdistdir}/tex/latex/pst-shell/pst-shell.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-shell-%{texlive_version}.%{texlive_noarch}.0.0.03svn42840-%{release}-zypper
%endif

%package -n texlive-pst-sigsys
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn21667
Release:        0
Summary:        Support of signal processing-related disciplines
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-sigsys-doc >= %{texlive_version}
Provides:       tex(pst-sigsys.sty)
Provides:       tex(pst-sigsys.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source25:       pst-sigsys.tar.xz
Source26:       pst-sigsys.doc.tar.xz

%description -n texlive-pst-sigsys
The package offers a collection of useful macros for
disciplines related to signal processing. It defines macros for
plotting a sequence of numbers, drawing the pole-zero diagram
of a system, shading the region of convergence, creating an
adder or a multiplier node, placing a framed node at a given
coordinate, creating an up-sampler or a down-sampler node,
drawing the block diagram of a system, drawing adaptive
systems, sequentially connecting a list of nodes, and
connecting a list of nodes using any node-connecting macro.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-pst-sigsys-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn21667
Release:        0
Summary:        Documentation for texlive-pst-sigsys
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pst-sigsys-doc
This package includes the documentation for texlive-pst-sigsys

%post -n texlive-pst-sigsys
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-sigsys 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-sigsys
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-sigsys-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-sigsys/Changes
%{_texmfdistdir}/doc/generic/pst-sigsys/README
%{_texmfdistdir}/doc/generic/pst-sigsys/pst-sigsys-doc.bib
%{_texmfdistdir}/doc/generic/pst-sigsys/pst-sigsys-doc.pdf
%{_texmfdistdir}/doc/generic/pst-sigsys/pst-sigsys-doc.tex

%files -n texlive-pst-sigsys
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-sigsys/pst-sigsys.tex
%{_texmfdistdir}/tex/latex/pst-sigsys/pst-sigsys.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-sigsys-%{texlive_version}.%{texlive_noarch}.1.4svn21667-%{release}-zypper
%endif

%package -n texlive-pst-slpe
Version:        %{texlive_version}.%{texlive_noarch}.1.31svn24391
Release:        0
Summary:        Sophisticated colour gradients
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-slpe-doc >= %{texlive_version}
Provides:       tex(pst-slpe.sty)
Provides:       tex(pst-slpe.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source27:       pst-slpe.tar.xz
Source28:       pst-slpe.doc.tar.xz

%description -n texlive-pst-slpe
This PStricks package covers all the colour gradient
functionality of pst-grad (part of the base PSTricks
distribution), and provides the following facilities: it
permits the user to specify an arbitrary number of colours,
along with the points at which they are to be reached; it
converts between RGB and HSV behind the scenes; it provides
concentric and radial gradients; it provides a command \psBall
that generates bullets with a three-dimensional appearance; and
uses the xkeyval package for the extended key handling.

date: 2018-09-15 11:19:48 +0000


%package -n texlive-pst-slpe-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.31svn24391
Release:        0
Summary:        Documentation for texlive-pst-slpe
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pst-slpe-doc
This package includes the documentation for texlive-pst-slpe

%post -n texlive-pst-slpe
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-slpe 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-slpe
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-slpe-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-slpe/Changes
%{_texmfdistdir}/doc/generic/pst-slpe/README
%{_texmfdistdir}/doc/generic/pst-slpe/pst-slpe.pdf

%files -n texlive-pst-slpe
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-slpe/pst-slpe.pro
%{_texmfdistdir}/tex/generic/pst-slpe/pst-slpe.tex
%{_texmfdistdir}/tex/latex/pst-slpe/pst-slpe.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-slpe-%{texlive_version}.%{texlive_noarch}.1.31svn24391-%{release}-zypper
%endif

%package -n texlive-pst-solarsystem
Version:        %{texlive_version}.%{texlive_noarch}.0.0.13svn45097
Release:        0
Summary:        Plot the solar system for a specific date
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-solarsystem-doc >= %{texlive_version}
Provides:       tex(pst-solarsystem.sty)
Provides:       tex(pst-solarsystem.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source29:       pst-solarsystem.tar.xz
Source30:       pst-solarsystem.doc.tar.xz

%description -n texlive-pst-solarsystem
The package uses pstricks to produce diagrams of the visible
planets, projected on the plane of the ecliptic. It is not
possible to represent all the planets in their real
proportions, so only Mercury, Venus, Earth and Mars have their
orbits in correct proportions and their relative sizes are
observed. Saturn and Jupiter are in the right direction, but
not in the correct size.

date: 2018-09-15 11:22:10 +0000


%package -n texlive-pst-solarsystem-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.13svn45097
Release:        0
Summary:        Documentation for texlive-pst-solarsystem
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pst-solarsystem-doc
This package includes the documentation for texlive-pst-solarsystem

%post -n texlive-pst-solarsystem
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-solarsystem 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-solarsystem
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-solarsystem-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-solarsystem/Changes
%{_texmfdistdir}/doc/generic/pst-solarsystem/README
%{_texmfdistdir}/doc/generic/pst-solarsystem/pst-solarsystem-doc.bib
%{_texmfdistdir}/doc/generic/pst-solarsystem/pst-solarsystem-doc.pdf
%{_texmfdistdir}/doc/generic/pst-solarsystem/pst-solarsystem-doc.tex

%files -n texlive-pst-solarsystem
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-solarsystem/pst-solarsystem.pro
%{_texmfdistdir}/tex/generic/pst-solarsystem/pst-solarsystem.tex
%{_texmfdistdir}/tex/latex/pst-solarsystem/pst-solarsystem.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-solarsystem-%{texlive_version}.%{texlive_noarch}.0.0.13svn45097-%{release}-zypper
%endif

%package -n texlive-pst-solides3d
Version:        %{texlive_version}.%{texlive_noarch}.4.34asvn49520
Release:        0
Summary:        Draw perspective views of 3D solids
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-solides3d-doc >= %{texlive_version}
Provides:       tex(pst-solides3d.sty)
Provides:       tex(pst-solides3d.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source31:       pst-solides3d.tar.xz
Source32:       pst-solides3d.doc.tar.xz

%description -n texlive-pst-solides3d
The package is designed to draw solids in 3d perspective.
Features include: create primitive solids; create solids by
including a list of its vertices and faces; faces of solids and
surfaces can be colored by choosing from a very large palette
of colors; draw parametric surfaces in algebraic and reverse
polish notation; create explicit and parameterized algebraic
functions drawn in 2 or 3 dimensions; project text onto a plane
or onto the faces of a solid; support for including external
database files.

date: 2018-12-27 16:25:55 +0000


%package -n texlive-pst-solides3d-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.34asvn49520
Release:        0
Summary:        Documentation for texlive-pst-solides3d
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-pst-solides3d-doc:en)

%description -n texlive-pst-solides3d-doc
This package includes the documentation for texlive-pst-solides3d

%post -n texlive-pst-solides3d
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-solides3d 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-solides3d
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-solides3d-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-solides3d/Changes
%{_texmfdistdir}/doc/generic/pst-solides3d/README
%{_texmfdistdir}/doc/generic/pst-solides3d/data/Pyramid-couleurs.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/Pyramid-faces.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/Pyramid-io.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/Pyramid-sommets.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/cubeHexagone-couleurs.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/cubeHexagone-faces.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/cubeHexagone-io.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/cubeHexagone-sommets.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/cubecolor-couleurs.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/cubecolor-faces.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/cubecolor-io.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/cubecolor-sommets.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/faces_nefer.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/faces_nefer_levres.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/faces_nefer_sourcils.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/faces_nefer_yeux.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/fusee62-couleurs.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/fusee62-faces.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/fusee62-io.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/fusee62-sommets.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/geodedual44-couleurs.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/geodedual44-faces.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/geodedual44-io.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/geodedual44-sommets.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/horoptere-couleurs.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/horoptere-faces.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/horoptere-io.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/horoptere-sommets.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/paraboloid-couleurs.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/paraboloid-faces.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/paraboloid-io.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/paraboloid-sommets.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/rocket.obj
%{_texmfdistdir}/doc/generic/pst-solides3d/data/slicePyramid-couleurs.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/slicePyramid-faces.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/slicePyramid-io.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/slicePyramid-sommets.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/sommets_nefer.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/tore1836-couleurs.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/tore1836-faces.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/tore1836-io.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/tore1836-sommets.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/tore1860-couleurs.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/tore1860-faces.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/tore1860-io.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/tore1860-sommets.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/tore1860lemniscate-couleurs.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/tore1860lemniscate-faces.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/tore1860lemniscate-io.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/tore1860lemniscate-sommets.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/tore1860ovales-couleurs.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/tore1860ovales-faces.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/tore1860ovales-io.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/tore1860ovales-sommets.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/tore1860part-couleurs.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/tore1860part-faces.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/tore1860part-io.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/data/tore1860part-sommets.dat
%{_texmfdistdir}/doc/generic/pst-solides3d/images/kepler.eps
%{_texmfdistdir}/doc/generic/pst-solides3d/images/parrot.eps
%{_texmfdistdir}/doc/generic/pst-solides3d/images/tiger.eps
%{_texmfdistdir}/doc/generic/pst-solides3d/pst-solides3d-doc.bib
%{_texmfdistdir}/doc/generic/pst-solides3d/pst-solides3d-doc.pdf
%{_texmfdistdir}/doc/generic/pst-solides3d/pst-solides3d-doc.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/chapter-1-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/chapter-2-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-acknowledgements-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-affinage-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-anneaux-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-annoterschema-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-axes3D-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-chanfrein-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-codejps-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-colorierfacettes-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-commandestrace-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-couleurs-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-courbeR3-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-cylindres-cones-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-datfile-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-definirfonction-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-definirplanquelconque-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-definitionmaillage-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-eclairageponctuel-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-enleverfacettes-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-extensions-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-face-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-fusion-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-fusionjps-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-geode-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-grille-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-image2d-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-implicitsurface-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-keywords-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-ligne3D-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-lignedeniveau-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-modes-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-new-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-nommersolide-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-numeroterfacettes-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-opacity-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-parametres-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-plan-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-poems-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-point-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-pointagesommets-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-positionnerpointconnu-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-positionnersolide-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-prisme-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-projectionangledroit-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-projectioncercle-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-projectioncourbe-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-projectiondroite-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-projectionligne-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-projectionpoint-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-projectionpolygone-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-projectiontexte-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-projectionvecteur-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-projectionvisibility-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-projpresentation-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-ruban-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-section-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-solidescreux-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-solidespredefinis-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-surfaces-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-surfacesparametrees-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-tracerpolygone-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-transform-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-transformpointconnu-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-tronque-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-tube-en.tex
%{_texmfdistdir}/doc/generic/pst-solides3d/text/par-vecteur-en.tex

%files -n texlive-pst-solides3d
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-solides3d/pst-implicitsurface.pro
%{_texmfdistdir}/dvips/pst-solides3d/pst-solides3d.pro
%{_texmfdistdir}/tex/generic/pst-solides3d/pst-solides3d.tex
%{_texmfdistdir}/tex/latex/pst-solides3d/pst-solides3d.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-solides3d-%{texlive_version}.%{texlive_noarch}.4.34asvn49520-%{release}-zypper
%endif

%package -n texlive-pst-soroban
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Draw a Soroban using PSTricks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-soroban-doc >= %{texlive_version}
Provides:       tex(pst-soroban.sty)
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pstricks-add.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source33:       pst-soroban.tar.xz
Source34:       pst-soroban.doc.tar.xz

%description -n texlive-pst-soroban
The package uses PSTricks to draw a Japanese abacus, or
soroban. The soroban is still used in Japan today.

date: 2018-09-15 11:24:17 +0000


%package -n texlive-pst-soroban-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-pst-soroban
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pst-soroban-doc
This package includes the documentation for texlive-pst-soroban

%post -n texlive-pst-soroban
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-soroban 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-soroban
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-soroban-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-soroban/Changes
%{_texmfdistdir}/doc/generic/pst-soroban/README
%{_texmfdistdir}/doc/generic/pst-soroban/pst-soroban-doc.bib
%{_texmfdistdir}/doc/generic/pst-soroban/pst-soroban-doc.pdf
%{_texmfdistdir}/doc/generic/pst-soroban/pst-soroban-doc.tex

%files -n texlive-pst-soroban
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pst-soroban/pst-soroban.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-soroban-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif

%package -n texlive-pst-spectra
Version:        %{texlive_version}.%{texlive_noarch}.0.0.91svn15878
Release:        0
Summary:        Draw continuum, emission and absorption spectra with PSTricks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-spectra-doc >= %{texlive_version}
Provides:       tex(pst-spectra.sty)
Provides:       tex(pst-spectra.tex)
Requires:       tex(multido.sty)
Requires:       tex(pstricks.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source35:       pst-spectra.tar.xz
Source36:       pst-spectra.doc.tar.xz

%description -n texlive-pst-spectra
The package is a PSTricks extension, based on a NASA lines
database. It allows you to draw continuum, emission and
absorption spectra. A Total of 16 880 visible lines from 99
elements can be displayed. The package requires the xkeyval
package for decoding its arguments.

date: 2018-09-15 11:26:13 +0000


%package -n texlive-pst-spectra-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.91svn15878
Release:        0
Summary:        Documentation for texlive-pst-spectra
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-pst-spectra-doc:fr;en)

%description -n texlive-pst-spectra-doc
This package includes the documentation for texlive-pst-spectra

%post -n texlive-pst-spectra
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-spectra 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-spectra
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-spectra-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-spectra/README
%{_texmfdistdir}/doc/generic/pst-spectra/pst-spectra.pdf
%{_texmfdistdir}/doc/generic/pst-spectra/pst-spectraEN.pdf

%files -n texlive-pst-spectra
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-spectra/pst-spectra.pro
%{_texmfdistdir}/tex/generic/pst-spectra/pst-spectra.tex
%{_texmfdistdir}/tex/latex/pst-spectra/pst-spectra.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-spectra-%{texlive_version}.%{texlive_noarch}.0.0.91svn15878-%{release}-zypper
%endif

%package -n texlive-pst-spinner
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn44507
Release:        0
Summary:        Drawing a fidget spinner
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-spinner-doc >= %{texlive_version}
Provides:       tex(pst-spinner.sty)
Provides:       tex(pst-spinner.tex)
Requires:       tex(pst-node.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source37:       pst-spinner.tar.xz
Source38:       pst-spinner.doc.tar.xz

%description -n texlive-pst-spinner
This package aims to propose a model of the fidget spinner
gadget. It exists under different forms with 2, 3 poles and
even more. We chose the most popular model: the triple Fidget
Spinner. You can run the PSTricks related documents with
XeLaTeX.

date: 2017-06-06 17:56:03 +0000


%package -n texlive-pst-spinner-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn44507
Release:        0
Summary:        Documentation for texlive-pst-spinner
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pst-spinner-doc
This package includes the documentation for texlive-pst-spinner

%post -n texlive-pst-spinner
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-spinner 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-spinner
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-spinner-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-spinner/Changes
%{_texmfdistdir}/doc/generic/pst-spinner/README
%{_texmfdistdir}/doc/generic/pst-spinner/images/cercle-chromatique.eps
%{_texmfdistdir}/doc/generic/pst-spinner/images/spirales-hsb.eps
%{_texmfdistdir}/doc/generic/pst-spinner/pst-spinner-doc.bib
%{_texmfdistdir}/doc/generic/pst-spinner/pst-spinner-doc.pdf
%{_texmfdistdir}/doc/generic/pst-spinner/pst-spinner-doc.tex

%files -n texlive-pst-spinner
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-spinner/pst-spinner.pro
%{_texmfdistdir}/tex/generic/pst-spinner/pst-spinner.tex
%{_texmfdistdir}/tex/latex/pst-spinner/pst-spinner.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-spinner-%{texlive_version}.%{texlive_noarch}.1.02svn44507-%{release}-zypper
%endif

%package -n texlive-pst-spirograph
Version:        %{texlive_version}.%{texlive_noarch}.0.0.41svn35026
Release:        0
Summary:        Drawing hypotrochoids as with a spirograph
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-spirograph-doc >= %{texlive_version}
Provides:       tex(pst-spirograph.sty)
Provides:       tex(pst-spirograph.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source39:       pst-spirograph.tar.xz
Source40:       pst-spirograph.doc.tar.xz

%description -n texlive-pst-spirograph
The package simulates the action of a spirograph, which is a
geometric drawing toy that produces mathematical roulette
curves (technically known as hypotrochoids and epitrochoids).

date: 2016-06-24 17:18:15 +0000


%package -n texlive-pst-spirograph-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.41svn35026
Release:        0
Summary:        Documentation for texlive-pst-spirograph
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pst-spirograph-doc
This package includes the documentation for texlive-pst-spirograph

%post -n texlive-pst-spirograph
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-spirograph 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-spirograph
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-spirograph-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-spirograph/Changes
%{_texmfdistdir}/doc/generic/pst-spirograph/README
%{_texmfdistdir}/doc/generic/pst-spirograph/animation/README.anim
%{_texmfdistdir}/doc/generic/pst-spirograph/animation/anim1.tex
%{_texmfdistdir}/doc/generic/pst-spirograph/animation/anim2.tex
%{_texmfdistdir}/doc/generic/pst-spirograph/animation/anim3.tex
%{_texmfdistdir}/doc/generic/pst-spirograph/animation/anim4.tex
%{_texmfdistdir}/doc/generic/pst-spirograph/animation/anim5.tex
%{_texmfdistdir}/doc/generic/pst-spirograph/animation/anim6.tex
%{_texmfdistdir}/doc/generic/pst-spirograph/animation/anim7.tex
%{_texmfdistdir}/doc/generic/pst-spirograph/animation/anim8.tex
%{_texmfdistdir}/doc/generic/pst-spirograph/animation/runall.sh
%{_texmfdistdir}/doc/generic/pst-spirograph/pst-spirograph-doc.bib
%{_texmfdistdir}/doc/generic/pst-spirograph/pst-spirograph-doc.pdf
%{_texmfdistdir}/doc/generic/pst-spirograph/pst-spirograph-doc.tex

%files -n texlive-pst-spirograph
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-spirograph/pst-spirograph.pro
%{_texmfdistdir}/tex/generic/pst-spirograph/pst-spirograph.tex
%{_texmfdistdir}/tex/latex/pst-spirograph/pst-spirograph.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-spirograph-%{texlive_version}.%{texlive_noarch}.0.0.41svn35026-%{release}-zypper
%endif

%package -n texlive-pst-stru
Version:        %{texlive_version}.%{texlive_noarch}.0.0.13svn38613
Release:        0
Summary:        Civil engineering diagrams, using PSTricks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-stru-doc >= %{texlive_version}
Provides:       tex(pst-stru.sty)
Provides:       tex(pst-stru.tex)
Requires:       tex(multido.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source41:       pst-stru.tar.xz
Source42:       pst-stru.doc.tar.xz

%description -n texlive-pst-stru
This PSTricks-based package provides facilities to draw
structural schemes in civil engineering analysis, for beams,
portals, arches and piles.

date: 2018-09-15 11:29:54 +0000


%package -n texlive-pst-stru-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.13svn38613
Release:        0
Summary:        Documentation for texlive-pst-stru
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pst-stru-doc
This package includes the documentation for texlive-pst-stru

%post -n texlive-pst-stru
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-stru 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-stru
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-stru-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-stru/Changes
%{_texmfdistdir}/doc/generic/pst-stru/README
%{_texmfdistdir}/doc/generic/pst-stru/pst-stru-doc.bib
%{_texmfdistdir}/doc/generic/pst-stru/pst-stru-doc.pdf
%{_texmfdistdir}/doc/generic/pst-stru/pst-stru-doc.tex

%files -n texlive-pst-stru
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-stru/pst-stru.tex
%{_texmfdistdir}/tex/latex/pst-stru/pst-stru.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-stru-%{texlive_version}.%{texlive_noarch}.0.0.13svn38613-%{release}-zypper
%endif

%package -n texlive-pst-support
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Assorted support files for use with PSTricks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source43:       pst-support.doc.tar.xz

%description -n texlive-pst-support
An appropriate set of job options, together with process
scripts for use with TeXnicCenter/

date: 2016-06-24 17:18:15 +0000

%post -n texlive-pst-support
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-support 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-support
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-support
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-support/README
%{_texmfdistdir}/doc/generic/pst-support/Standard_transparency.joboptions
%{_texmfdistdir}/doc/generic/pst-support/latex-ps-pdf.tco
%{_texmfdistdir}/doc/generic/pst-support/latex-pstpdf-pdf.tco
%{_texmfdistdir}/doc/generic/pst-support/pdflatex-autopstpdf.tco
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-support-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-pst-text
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn49542
Release:        0
Summary:        Text and character manipulation in PSTricks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-text-doc >= %{texlive_version}
Provides:       tex(pst-char.sty)
Provides:       tex(pst-text.sty)
Provides:       tex(pst-text.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source44:       pst-text.tar.xz
Source45:       pst-text.doc.tar.xz

%description -n texlive-pst-text
Pst-text is a PSTricks based package for plotting text along a
different path and manipulating characters. It includes the
functionality of the old package pst-char.

date: 2018-12-29 21:53:50 +0000


%package -n texlive-pst-text-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn49542
Release:        0
Summary:        Documentation for texlive-pst-text
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pst-text-doc
This package includes the documentation for texlive-pst-text

%post -n texlive-pst-text
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-text 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-text
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-text-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-text/Changes
%{_texmfdistdir}/doc/generic/pst-text/README
%{_texmfdistdir}/doc/generic/pst-text/pst-text-doc.bib
%{_texmfdistdir}/doc/generic/pst-text/pst-text-doc.pdf
%{_texmfdistdir}/doc/generic/pst-text/pst-text-doc.tex

%files -n texlive-pst-text
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-text/pst-text.pro
%{_texmfdistdir}/tex/generic/pst-text/pst-text.tex
%{_texmfdistdir}/tex/latex/pst-text/pst-char.sty
%{_texmfdistdir}/tex/latex/pst-text/pst-text.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-text-%{texlive_version}.%{texlive_noarch}.1.02svn49542-%{release}-zypper
%endif

%package -n texlive-pst-thick
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn16369
Release:        0
Summary:        Drawing very thick lines and curves
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-thick-doc >= %{texlive_version}
Provides:       tex(pst-thick.sty)
Provides:       tex(pst-thick.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source46:       pst-thick.tar.xz
Source47:       pst-thick.doc.tar.xz

%description -n texlive-pst-thick
The package supports drawing of very thick lines and curves in
PSTricks, with various fillings for the body of the lines.

date: 2018-09-15 11:33:51 +0000


%package -n texlive-pst-thick-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn16369
Release:        0
Summary:        Documentation for texlive-pst-thick
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-pst-thick-doc:fr)

%description -n texlive-pst-thick-doc
This package includes the documentation for texlive-pst-thick

%post -n texlive-pst-thick
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-thick 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-thick
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-thick-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-thick/Changes
%{_texmfdistdir}/doc/generic/pst-thick/README
%{_texmfdistdir}/doc/generic/pst-thick/pst-thick-doc.bib
%{_texmfdistdir}/doc/generic/pst-thick/pst-thick-doc.pdf
%{_texmfdistdir}/doc/generic/pst-thick/pst-thick-doc.tex

%files -n texlive-pst-thick
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-thick/pst-thick.tex
%{_texmfdistdir}/tex/latex/pst-thick/pst-thick.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-thick-%{texlive_version}.%{texlive_noarch}.1.0svn16369-%{release}-zypper
%endif

%package -n texlive-pst-tools
Version:        %{texlive_version}.%{texlive_noarch}.0.0.09bsvn45978
Release:        0
Summary:        PSTricks support functions
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-tools-doc >= %{texlive_version}
Provides:       tex(pst-tools.sty)
Provides:       tex(pst-tools.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source48:       pst-tools.tar.xz
Source49:       pst-tools.doc.tar.xz

%description -n texlive-pst-tools
The package provides helper functions for other PSTricks
related packages.

date: 2017-12-03 11:35:57 +0000


%package -n texlive-pst-tools-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.09bsvn45978
Release:        0
Summary:        Documentation for texlive-pst-tools
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pst-tools-doc
This package includes the documentation for texlive-pst-tools

%post -n texlive-pst-tools
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-tools 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-tools
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-tools-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-tools/Changes
%{_texmfdistdir}/doc/generic/pst-tools/README
%{_texmfdistdir}/doc/generic/pst-tools/pst-tools-doc.bib
%{_texmfdistdir}/doc/generic/pst-tools/pst-tools-doc.pdf
%{_texmfdistdir}/doc/generic/pst-tools/pst-tools-doc.tex

%files -n texlive-pst-tools
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-tools/pst-tools.pro
%{_texmfdistdir}/tex/generic/pst-tools/pst-tools.tex
%{_texmfdistdir}/tex/latex/pst-tools/pst-tools.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-tools-%{texlive_version}.%{texlive_noarch}.0.0.09bsvn45978-%{release}-zypper
%endif

%package -n texlive-pst-tree
Version:        %{texlive_version}.%{texlive_noarch}.1.13svn43272
Release:        0
Summary:        Trees, using PSTricks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-tree-doc >= %{texlive_version}
Provides:       tex(pst-tree.sty)
Provides:       tex(pst-tree.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source50:       pst-tree.tar.xz
Source51:       pst-tree.doc.tar.xz

%description -n texlive-pst-tree
pst-tree is a pstricks package that defines a macro \pstree
which offers a structured way of joining nodes created using
pst-node in order to draw trees.

date: 2018-09-15 11:35:58 +0000


%package -n texlive-pst-tree-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.13svn43272
Release:        0
Summary:        Documentation for texlive-pst-tree
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-pst-tree-doc:en)

%description -n texlive-pst-tree-doc
This package includes the documentation for texlive-pst-tree

%post -n texlive-pst-tree
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-tree 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-tree
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-tree-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-tree/Changes
%{_texmfdistdir}/doc/generic/pst-tree/README
%{_texmfdistdir}/doc/generic/pst-tree/pst-tree-doc.bib
%{_texmfdistdir}/doc/generic/pst-tree/pst-tree-doc.pdf
%{_texmfdistdir}/doc/generic/pst-tree/pst-tree-doc.tex

%files -n texlive-pst-tree
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-tree/pst-tree.tex
%{_texmfdistdir}/tex/latex/pst-tree/pst-tree.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-tree-%{texlive_version}.%{texlive_noarch}.1.13svn43272-%{release}-zypper
%endif

%package -n texlive-pst-tvz
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn23451
Release:        0
Summary:        Draw trees with more than one root node, using PSTricks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-tvz-doc >= %{texlive_version}
Provides:       tex(pst-tvz.sty)
Provides:       tex(pst-tvz.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source52:       pst-tvz.tar.xz
Source53:       pst-tvz.doc.tar.xz

%description -n texlive-pst-tvz
The package uses PSTricks to draw trees with more than one root
node. It is similar to pst-tree, though it uses a different
placement algorithm.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-pst-tvz-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn23451
Release:        0
Summary:        Documentation for texlive-pst-tvz
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pst-tvz-doc
This package includes the documentation for texlive-pst-tvz

%post -n texlive-pst-tvz
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-tvz 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-tvz
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-tvz-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-tvz/Changes
%{_texmfdistdir}/doc/generic/pst-tvz/README
%{_texmfdistdir}/doc/generic/pst-tvz/pst-tvz-doc.bib
%{_texmfdistdir}/doc/generic/pst-tvz/pst-tvz-doc.pdf
%{_texmfdistdir}/doc/generic/pst-tvz/pst-tvz-doc.tex

%files -n texlive-pst-tvz
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-tvz/pst-tvz.tex
%{_texmfdistdir}/tex/latex/pst-tvz/pst-tvz.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-tvz-%{texlive_version}.%{texlive_noarch}.1.01svn23451-%{release}-zypper
%endif

%package -n texlive-pst-uml
Version:        %{texlive_version}.%{texlive_noarch}.0.0.83svn15878
Release:        0
Summary:        UML diagrams with PSTricks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires:       texlive-multido >= %{texlive_version}
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-uml-doc >= %{texlive_version}
Provides:       tex(pst-uml.sty)
Requires:       tex(calc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(multido.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pst-tree.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source54:       pst-uml.tar.xz
Source55:       pst-uml.doc.tar.xz

%description -n texlive-pst-uml
This a PSTricks package that provides support for drawing
moderately complex UML (Universal Modelling Language) diagrams.
(The PDF documentation is written in French.)

date: 2018-09-15 11:38:22 +0000


%package -n texlive-pst-uml-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.83svn15878
Release:        0
Summary:        Documentation for texlive-pst-uml
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-pst-uml-doc:fr)

%description -n texlive-pst-uml-doc
This package includes the documentation for texlive-pst-uml

%post -n texlive-pst-uml
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-uml 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-uml
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-uml-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-uml/Changes
%{_texmfdistdir}/doc/generic/pst-uml/README
%{_texmfdistdir}/doc/generic/pst-uml/diagCase.tex
%{_texmfdistdir}/doc/generic/pst-uml/diagClass.tex
%{_texmfdistdir}/doc/generic/pst-uml/diagClass1.tex
%{_texmfdistdir}/doc/generic/pst-uml/diagSeq.tex
%{_texmfdistdir}/doc/generic/pst-uml/diagState.tex
%{_texmfdistdir}/doc/generic/pst-uml/pst-uml-doc.pdf
%{_texmfdistdir}/doc/generic/pst-uml/pst-uml-doc.tex
%{_texmfdistdir}/doc/generic/pst-uml/pst-uml-encapsuled-pdf-fig.pdf
%{_texmfdistdir}/doc/generic/pst-uml/pst-uml-encapsuled-pdf-fig.tex
%{_texmfdistdir}/doc/generic/pst-uml/pst-uml-exemples.pdf
%{_texmfdistdir}/doc/generic/pst-uml/pst-uml-exemples.tex

%files -n texlive-pst-uml
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pst-uml/pst-uml.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-uml-%{texlive_version}.%{texlive_noarch}.0.0.83svn15878-%{release}-zypper
%endif

%package -n texlive-pst-vectorian
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn28801
Release:        0
Summary:        Printing ornaments
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-vectorian-doc >= %{texlive_version}
Provides:       tex(psvectorian.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source56:       pst-vectorian.tar.xz
Source57:       pst-vectorian.doc.tar.xz

%description -n texlive-pst-vectorian
The package uses PSTricks to draw ornaments (a substantial
repertoire of ornaments is provided).

date: 2016-06-24 17:18:15 +0000


%package -n texlive-pst-vectorian-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn28801
Release:        0
Summary:        Documentation for texlive-pst-vectorian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-pst-vectorian-doc:fr)

%description -n texlive-pst-vectorian-doc
This package includes the documentation for texlive-pst-vectorian

%post -n texlive-pst-vectorian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-vectorian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-vectorian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-vectorian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pst-vectorian/README
%{_texmfdistdir}/doc/latex/pst-vectorian/psvectorian.pdf
%{_texmfdistdir}/doc/latex/pst-vectorian/psvectorian.tex

%files -n texlive-pst-vectorian
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-vectorian/psvectorian.pro
%{_texmfdistdir}/tex/latex/pst-vectorian/psvectorian.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-vectorian-%{texlive_version}.%{texlive_noarch}.0.0.4svn28801-%{release}-zypper
%endif

%package -n texlive-pst-vehicle
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn45320
Release:        0
Summary:        A PSTricks package for rolling vehicles on graphs of mathematical functions
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-vehicle-doc >= %{texlive_version}
Provides:       tex(ListVehicles.tex)
Provides:       tex(pst-vehicle.sty)
Provides:       tex(pst-vehicle.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source58:       pst-vehicle.tar.xz
Source59:       pst-vehicle.doc.tar.xz

%description -n texlive-pst-vehicle
This package permits to represent vehicles rolling without
slipping on mathematical curves. Different types of vehicles
are proposed, the shape of the curve is to be defined by its
equation "y=f(x)" in algebraic notation.

date: 2017-09-16 18:11:01 +0000


%package -n texlive-pst-vehicle-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn45320
Release:        0
Summary:        Documentation for texlive-pst-vehicle
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-pst-vehicle-doc:fr)

%description -n texlive-pst-vehicle-doc
This package includes the documentation for texlive-pst-vehicle

%post -n texlive-pst-vehicle
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-vehicle 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-vehicle
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-vehicle-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-vehicle/Changes.txt
%{_texmfdistdir}/doc/generic/pst-vehicle/README.md
%{_texmfdistdir}/doc/generic/pst-vehicle/pst-vehicle-doc-fr.pdf
%{_texmfdistdir}/doc/generic/pst-vehicle/pst-vehicle-doc-fr.tex
%{_texmfdistdir}/doc/generic/pst-vehicle/pst-vehicle-doc.pdf
%{_texmfdistdir}/doc/generic/pst-vehicle/pst-vehicle-doc.tex

%files -n texlive-pst-vehicle
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-vehicle/ListVehicles.tex
%{_texmfdistdir}/tex/generic/pst-vehicle/pst-vehicle.tex
%{_texmfdistdir}/tex/latex/pst-vehicle/pst-vehicle.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-vehicle-%{texlive_version}.%{texlive_noarch}.1.2svn45320-%{release}-zypper
%endif

%package -n texlive-pst-venn
Version:        %{texlive_version}.%{texlive_noarch}.0.0.01svn49316
Release:        0
Summary:        A PSTricks package for drawing Venn sets
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-venn-doc >= %{texlive_version}
Provides:       tex(pst-venn.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source60:       pst-venn.tar.xz
Source61:       pst-venn.doc.tar.xz

%description -n texlive-pst-venn
This is a PSTricks related package for drawing Venn diagrams
with three circles.

date: 2018-12-06 06:51:50 +0000


%package -n texlive-pst-venn-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.01svn49316
Release:        0
Summary:        Documentation for texlive-pst-venn
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pst-venn-doc
This package includes the documentation for texlive-pst-venn

%post -n texlive-pst-venn
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-venn 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-venn
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-venn-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-venn/Changes
%{_texmfdistdir}/doc/generic/pst-venn/README
%{_texmfdistdir}/doc/generic/pst-venn/pst-venn-doc.bib
%{_texmfdistdir}/doc/generic/pst-venn/pst-venn-doc.pdf
%{_texmfdistdir}/doc/generic/pst-venn/pst-venn-doc.tex

%files -n texlive-pst-venn
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pst-venn/pst-venn.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-venn-%{texlive_version}.%{texlive_noarch}.0.0.01svn49316-%{release}-zypper
%endif

%package -n texlive-pst-vowel
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn25228
Release:        0
Summary:        Enable arrows showing diphthongs on vowel charts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-vowel-doc >= %{texlive_version}
Provides:       tex(pst-vowel.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(vowel.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source62:       pst-vowel.tar.xz
Source63:       pst-vowel.doc.tar.xz

%description -n texlive-pst-vowel
The package extends the vowel package (distributed as part of
the tipa bundle) by allowing the user to draw arrows between
vowels to show relationships such as diphthong membership. The
package depends on use of pstricks.

date: 2018-09-15 11:40:17 +0000


%package -n texlive-pst-vowel-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn25228
Release:        0
Summary:        Documentation for texlive-pst-vowel
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pst-vowel-doc
This package includes the documentation for texlive-pst-vowel

%post -n texlive-pst-vowel
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-vowel 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-vowel
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-vowel-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pst-vowel/README
%{_texmfdistdir}/doc/latex/pst-vowel/pst-vowel.pdf
%{_texmfdistdir}/doc/latex/pst-vowel/pst-vowel.tex

%files -n texlive-pst-vowel
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pst-vowel/pst-vowel.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-vowel-%{texlive_version}.%{texlive_noarch}.1.0svn25228-%{release}-zypper
%endif

%package -n texlive-pst-vue3d
Version:        %{texlive_version}.%{texlive_noarch}.1.24svn15878
Release:        0
Summary:        Draw perspective views of three dimensional objects
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst-vue3d-doc >= %{texlive_version}
Provides:       tex(pst-vue3d.sty)
Provides:       tex(pst-vue3d.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source64:       pst-vue3d.tar.xz
Source65:       pst-vue3d.doc.tar.xz

%description -n texlive-pst-vue3d
With pst-vue3d three dimensional objects like cubes, spheres
and others can be viewed from different points. The
distribution includes a comprehensive set of examples of usage.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-pst-vue3d-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.24svn15878
Release:        0
Summary:        Documentation for texlive-pst-vue3d
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pst-vue3d-doc
This package includes the documentation for texlive-pst-vue3d

%post -n texlive-pst-vue3d
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-vue3d 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-vue3d
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-vue3d-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-vue3d/Changes
%{_texmfdistdir}/doc/generic/pst-vue3d/README
%{_texmfdistdir}/doc/generic/pst-vue3d/pst-vue3d-doc.bib
%{_texmfdistdir}/doc/generic/pst-vue3d/pst-vue3d-doc.pdf
%{_texmfdistdir}/doc/generic/pst-vue3d/pst-vue3d-doc.tex

%files -n texlive-pst-vue3d
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-vue3d/pst-vue3d.pro
%{_texmfdistdir}/tex/generic/pst-vue3d/pst-vue3d.tex
%{_texmfdistdir}/tex/latex/pst-vue3d/pst-vue3d.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst-vue3d-%{texlive_version}.%{texlive_noarch}.1.24svn15878-%{release}-zypper
%endif

%package -n texlive-pst2pdf
Version:        %{texlive_version}.%{texlive_noarch}.0.0.18svn45476
Release:        0
Summary:        A script to compile PSTricks documents via pdfTeX
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive-pst2pdf-bin >= %{texlive_version}
#!BuildIgnore: texlive-pst2pdf-bin
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pst2pdf-doc >= %{texlive_version}
Requires:       perl(Config)
#!BuildIgnore:  perl(Config)
Requires:       perl(File::Basename)
#!BuildIgnore:  perl(File::Basename)
Requires:       perl(File::Copy)
#!BuildIgnore:  perl(File::Copy)
Requires:       perl(File::Find)
#!BuildIgnore:  perl(File::Find)
Requires:       perl(File::Path)
#!BuildIgnore:  perl(File::Path)
Requires:       perl(File::Spec)
#!BuildIgnore:  perl(File::Spec)
Requires:       perl(Getopt::Long)
#!BuildIgnore:  perl(Getopt::Long)
Requires:       perl(IO::File)
#!BuildIgnore:  perl(IO::File)
Requires:       perl(autodie)
#!BuildIgnore:  perl(autodie)
Requires:       perl(re)
#!BuildIgnore:  perl(re)
Requires:       perl(strict)
#!BuildIgnore:  perl(strict)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source66:       pst2pdf.tar.xz
Source67:       pst2pdf.doc.tar.xz

%description -n texlive-pst2pdf
The script extracts the preamble of the document and runs all
\begin{postscript}...\end{postscript}
\begin{pspicture}...\end{pspicture} and
\pspicture...\endpspicture separately through LaTeX with the
same preamble as the original document; thus it creates EPS,
PNG and PDF files of these snippets. In a final pdfLaTeX run
the script replaces the environments with \includegraphics to
include the processed snippets. Detail documentation is
acquired from the document itself via Perldoc.

date: 2017-10-04 13:33:08 +0000


%package -n texlive-pst2pdf-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.18svn45476
Release:        0
Summary:        Documentation for texlive-pst2pdf
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pst2pdf-doc
This package includes the documentation for texlive-pst2pdf

%post -n texlive-pst2pdf
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst2pdf 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst2pdf
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst2pdf-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pst2pdf/Changes
%{_texmfdistdir}/doc/latex/pst2pdf/README
%{_texmfdistdir}/doc/latex/pst2pdf/pst2pdf-doc.bib
%{_texmfdistdir}/doc/latex/pst2pdf/pst2pdf-doc.pdf
%{_texmfdistdir}/doc/latex/pst2pdf/pst2pdf-doc.tex
%{_texmfdistdir}/doc/latex/pst2pdf/test1-pdf.pdf
%{_texmfdistdir}/doc/latex/pst2pdf/test1.tex
%{_texmfdistdir}/doc/latex/pst2pdf/test2-pdf.pdf
%{_texmfdistdir}/doc/latex/pst2pdf/test2.tex
%{_texmfdistdir}/doc/latex/pst2pdf/test3-pdf.pdf
%{_texmfdistdir}/doc/latex/pst2pdf/test3.tex
%{_texmfdistdir}/doc/latex/pst2pdf/tux.jpg

%files -n texlive-pst2pdf
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/pst2pdf/pst2pdf.pl
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pst2pdf-%{texlive_version}.%{texlive_noarch}.0.0.18svn45476-%{release}-zypper
%endif

%package -n texlive-pstool
Version:        %{texlive_version}.%{texlive_noarch}.1.5esvn46393
Release:        0
Summary:        Support for psfrag within pdfLaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pstool-doc >= %{texlive_version}
Provides:       tex(pstool.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source68:       pstool.tar.xz
Source69:       pstool.doc.tar.xz

%description -n texlive-pstool
The package works in the same sort of way as pst-pdf, but it
also processes the PostScript graphics with psfrag to add
labels within the graphic, before conversion. Thus the bundle
replaces two steps of an ordinary workflow. (Naturally, the
package requires that \write 18 is enabled.) Pstool ensures
that each version of each graphic is compiled once only (the
graphic is (re-)compiled only if it has changed since the
previous compilation of the document). This drastically speeds
up the running of the package in the typical case (though the
first run of any document is inevitably just as slow as with
any similar package).

date: 2018-01-20 09:12:28 +0000


%package -n texlive-pstool-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5esvn46393
Release:        0
Summary:        Documentation for texlive-pstool
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pstool-doc
This package includes the documentation for texlive-pstool

%post -n texlive-pstool
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pstool 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pstool
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pstool-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pstool/README.md
%{_texmfdistdir}/doc/latex/pstool/pstool.pdf
%{_texmfdistdir}/doc/latex/pstool/pstool.tex

%files -n texlive-pstool
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pstool/pstool.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pstool-%{texlive_version}.%{texlive_noarch}.1.5esvn46393-%{release}-zypper
%endif

%package -n texlive-pstools
Version:        %{texlive_version}.%{texlive_noarch}.1.68svn50602
Release:        0
Summary:        Produce Encapsulated PostScript from PostScript
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires:       psutils
Requires(pre): texlive-pstools-bin >= %{texlive_version}
#!BuildIgnore: texlive-pstools-bin
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pstools-doc >= %{texlive_version}
Requires:       perl(Getopt::Long)
#!BuildIgnore:  perl(Getopt::Long)
Requires:       perl(POSIX)
#!BuildIgnore:  perl(POSIX)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source70:       pstools.tar.xz
Source71:       pstools.doc.tar.xz

%description -n texlive-pstools
Produce Encapsulated PostScript Files (EPS/EPSF) from a
one-page PostScript document, or any PostScript document. A
correct Bounding Box is calculated for the EPS files and some
PostScript command sequences that can produce errorneous
results on printers are filtered. The input is cropped to
include just the image contained in the PostScript file. The
EPS files can then be included into TeX documents. Other
programs like ps2epsi (a script distributed with ghostscript)
don't always calculate the correct bounding box (because the
values are put on the PostScript stack which may get corrupted
by bad PostScript code) or they round it off, resulting in
clipping the image. Therefore ps2eps uses a resolution of 144
dpi to get the correct bounding box. The bundle includes
binaries for Linux, Solaris, Digital Unix or Windows
2000/9x/NT; for other platforms, the user needs perl,
ghostscript and an ANSI-C compiler. Included in the
distribution is the bbox program, an application to produce
Bounding Box values for rawppm or rawpbm format files.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-pstools-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.68svn50602
Release:        0
Summary:        Documentation for texlive-pstools
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pstools-doc
This package includes the documentation for texlive-pstools

%post -n texlive-pstools
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pstools 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pstools
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pstools-doc
%defattr(-,root,root,755)
%{_mandir}/man1/bbox.1*
%{_mandir}/man1/ps2eps.1*
%{_mandir}/man1/ps2frag.1*
%{_mandir}/man1/pslatex.1*

%files -n texlive-pstools
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/ps2eps/ps2eps.pl
%{_texmfdistdir}/scripts/texlive/ps2frag.sh
%{_texmfdistdir}/scripts/texlive/pslatex.sh
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pstools-%{texlive_version}.%{texlive_noarch}.1.68svn50602-%{release}-zypper
%endif

%package -n texlive-pstricks
Version:        %{texlive_version}.%{texlive_noarch}.2.96svn50101
Release:        0
Summary:        PostScript macros for TeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pstricks-doc >= %{texlive_version}
Provides:       tex(README.cfg)
Provides:       tex(distiller.cfg)
Provides:       tex(dvips.cfg)
Provides:       tex(dvipsone.cfg)
Provides:       tex(gastex.cfg)
Provides:       tex(pst-all.sty)
Provides:       tex(pst-doc.cls)
Provides:       tex(pst-fp.tex)
Provides:       tex(pst-key.sty)
Provides:       tex(pst-key.tex)
Provides:       tex(pst-platform.sty)
Provides:       tex(pstcol.sty)
Provides:       tex(pstricks-pdf.sty)
Provides:       tex(pstricks-tex.def)
Provides:       tex(pstricks-xetex.def)
Provides:       tex(pstricks.sty)
Provides:       tex(pstricks.tex)
Provides:       tex(pstricks97.tex)
Provides:       tex(textures.cfg)
Provides:       tex(vtex.cfg)
Provides:       tex(xdvipdfmx.cfg)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(babel.sty)
Requires:       tex(bera.sty)
Requires:       tex(biblatex.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(breakurl.sty)
Requires:       tex(calc.sty)
Requires:       tex(caption.sty)
Requires:       tex(catchfile.sty)
Requires:       tex(eso-pic.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(filecontents.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(footmisc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(lscape.sty)
Requires:       tex(makeidx.sty)
Requires:       tex(multido.sty)
Requires:       tex(nameref.sty)
Requires:       tex(paralist.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(pst-3d.sty)
Requires:       tex(pst-coil.sty)
Requires:       tex(pst-eps.sty)
Requires:       tex(pst-fill.sty)
Requires:       tex(pst-grad.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pst-pdf.sty)
Requires:       tex(pst-plot.sty)
Requires:       tex(pst-text.sty)
Requires:       tex(pst-tree.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks-add.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(scrartcl.cls)
Requires:       tex(scrlayer-scrpage.sty)
Requires:       tex(setspace.sty)
Requires:       tex(shellesc.sty)
Requires:       tex(showexpl.sty)
Requires:       tex(subfig.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(varioref.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xkvview.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source72:       pstricks.tar.xz
Source73:       pstricks.doc.tar.xz

%description -n texlive-pstricks
PSTricks offers an extensive collection of macros for
generating PostScript that is usable with most TeX macro
formats, including Plain TeX, LaTeX, AMS-TeX, and AMS-LaTeX.
Included are macros for colour, graphics, pie charts, rotation,
trees and overlays. It has many special features, including a
wide variety of graphics (picture drawing) macros, with a
flexible interface and with colour support. There are macros
for colouring or shading the cells of tables. The package
pstricks-add contains bug-fixes and additions for PSTricks
(among other things). PSTricks ordinarily uses PostScript
\special commands, which are not supported by pdf(La)TeX. This
limitation may be overcome by using either the pst-pdf or the
pdftricks package, to generate a PDF inclusion from a PSTricks
diagram. PSTricks macros can also generate PDF output when the
document is processed XeTeX, without the need for other
supporting packages.

date: 2019-02-23 15:30:24 +0000


%package -n texlive-pstricks-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.96svn50101
Release:        0
Summary:        Documentation for texlive-pstricks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pstricks-doc
This package includes the documentation for texlive-pstricks

%post -n texlive-pstricks
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pstricks 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pstricks
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pstricks-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pstricks/PSTricks.bib
%{_texmfdistdir}/doc/generic/pstricks/README
%{_texmfdistdir}/doc/generic/pstricks/ctandir.sty
%{_texmfdistdir}/doc/generic/pstricks/images/flowers.eps
%{_texmfdistdir}/doc/generic/pstricks/images/tiger.eps
%{_texmfdistdir}/doc/generic/pstricks/images/tiger.pdf
%{_texmfdistdir}/doc/generic/pstricks/pst-doc.bst
%{_texmfdistdir}/doc/generic/pstricks/pst-doc.ist
%{_texmfdistdir}/doc/generic/pstricks/pst-doc.pdf
%{_texmfdistdir}/doc/generic/pstricks/pst-news.sty
%{_texmfdistdir}/doc/generic/pstricks/pst-news.tex
%{_texmfdistdir}/doc/generic/pstricks/pst-news05.pdf
%{_texmfdistdir}/doc/generic/pstricks/pst-news05.tex
%{_texmfdistdir}/doc/generic/pstricks/pst-news06.pdf
%{_texmfdistdir}/doc/generic/pstricks/pst-news06.tex
%{_texmfdistdir}/doc/generic/pstricks/pst-news08.pdf
%{_texmfdistdir}/doc/generic/pstricks/pst-news08.tex
%{_texmfdistdir}/doc/generic/pstricks/pst-news09.pdf
%{_texmfdistdir}/doc/generic/pstricks/pst-news09.tex
%{_texmfdistdir}/doc/generic/pstricks/pst-news10.pdf
%{_texmfdistdir}/doc/generic/pstricks/pst-news10.tex
%{_texmfdistdir}/doc/generic/pstricks/pst-news11.pdf
%{_texmfdistdir}/doc/generic/pstricks/pst-news11.tex
%{_texmfdistdir}/doc/generic/pstricks/pst-news12.pdf
%{_texmfdistdir}/doc/generic/pstricks/pst-news12.tex
%{_texmfdistdir}/doc/generic/pstricks/pst-news13.pdf
%{_texmfdistdir}/doc/generic/pstricks/pst-news13.tex
%{_texmfdistdir}/doc/generic/pstricks/pst-news14.pdf
%{_texmfdistdir}/doc/generic/pstricks/pst-news14.tex
%{_texmfdistdir}/doc/generic/pstricks/pst-news15.pdf
%{_texmfdistdir}/doc/generic/pstricks/pst-news15.tex
%{_texmfdistdir}/doc/generic/pstricks/pst-news16.pdf
%{_texmfdistdir}/doc/generic/pstricks/pst-news16.tex
%{_texmfdistdir}/doc/generic/pstricks/pst-news17.pdf
%{_texmfdistdir}/doc/generic/pstricks/pst-news17.tex
%{_texmfdistdir}/doc/generic/pstricks/pst-news18.pdf
%{_texmfdistdir}/doc/generic/pstricks/pst-news18.tex
%{_texmfdistdir}/doc/generic/pstricks/pst-news19.pdf
%{_texmfdistdir}/doc/generic/pstricks/pst-news19.tex
%{_texmfdistdir}/doc/generic/pstricks/pst-user.pdf
%{_texmfdistdir}/doc/generic/pstricks/pst-user.tgz
%{_texmfdistdir}/doc/generic/pstricks/pstricks-bug.tex
%{_texmfdistdir}/doc/generic/pstricks/pstricks-doc.pdf
%{_texmfdistdir}/doc/generic/pstricks/test-pst.pdf
%{_texmfdistdir}/doc/generic/pstricks/test-pst.tex

%files -n texlive-pstricks
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pstricks/pst-algparser.pro
%{_texmfdistdir}/dvips/pstricks/pst-dots.pro
%{_texmfdistdir}/dvips/pstricks/pst-dots97.pro
%{_texmfdistdir}/dvips/pstricks/pstricks-fonts-lm.pro
%{_texmfdistdir}/dvips/pstricks/pstricks-fonts-ps.pro
%{_texmfdistdir}/dvips/pstricks/pstricks-fonts-urw.pro
%{_texmfdistdir}/dvips/pstricks/pstricks.pro
%{_texmfdistdir}/dvips/pstricks/pstricks97.pro
%{_texmfdistdir}/tex/generic/pstricks/config/README.cfg
%{_texmfdistdir}/tex/generic/pstricks/config/distiller.cfg
%{_texmfdistdir}/tex/generic/pstricks/config/dvips.cfg
%{_texmfdistdir}/tex/generic/pstricks/config/dvipsone.cfg
%{_texmfdistdir}/tex/generic/pstricks/config/gastex.cfg
%{_texmfdistdir}/tex/generic/pstricks/config/textures.cfg
%{_texmfdistdir}/tex/generic/pstricks/config/vtex.cfg
%{_texmfdistdir}/tex/generic/pstricks/config/xdvipdfmx.cfg
%{_texmfdistdir}/tex/generic/pstricks/pst-fp.tex
%{_texmfdistdir}/tex/generic/pstricks/pst-key.tex
%{_texmfdistdir}/tex/generic/pstricks/pstricks-tex.def
%{_texmfdistdir}/tex/generic/pstricks/pstricks-xetex.def
%{_texmfdistdir}/tex/generic/pstricks/pstricks.con
%{_texmfdistdir}/tex/generic/pstricks/pstricks.tex
%{_texmfdistdir}/tex/generic/pstricks/pstricks97.tex
%{_texmfdistdir}/tex/latex/pstricks/pst-all.sty
%{_texmfdistdir}/tex/latex/pstricks/pst-doc.cls
%{_texmfdistdir}/tex/latex/pstricks/pst-key.sty
%{_texmfdistdir}/tex/latex/pstricks/pst-platform.sty
%{_texmfdistdir}/tex/latex/pstricks/pstcol.sty
%{_texmfdistdir}/tex/latex/pstricks/pstricks-pdf.sty
%{_texmfdistdir}/tex/latex/pstricks/pstricks.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pstricks-%{texlive_version}.%{texlive_noarch}.2.96svn50101-%{release}-zypper
%endif

%package -n texlive-pstricks-add
Version:        %{texlive_version}.%{texlive_noarch}.3.87svn49680
Release:        0
Summary:        A collection of add-ons and bugfixes for PSTricks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pstricks-add-doc >= %{texlive_version}
Provides:       tex(pstricks-add.sty)
Provides:       tex(pstricks-add.tex)
Requires:       tex(multido.sty)
Requires:       tex(pst-3d.sty)
Requires:       tex(pst-calculate.sty)
Requires:       tex(pst-math.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pst-plot.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source74:       pstricks-add.tar.xz
Source75:       pstricks-add.doc.tar.xz

%description -n texlive-pstricks-add
Collects together examples that have been posted to the
PSTricks mailing list, together with many additional features
for the basic pstricks, pst-plot and pst-node, including:
bugfixes; new options for the pspicture environment; arrows;
braces as node connection/linestyle; extended axes for plots
(e.g., logarithm axes); polar plots; plotting tangent lines of
curves or functions; solving and printing differential
equations; box plots; matrix plots; and pie charts. The package
makes use of PostScript routines provided by pst-math.

date: 2019-01-12 18:39:00 +0000


%package -n texlive-pstricks-add-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.87svn49680
Release:        0
Summary:        Documentation for texlive-pstricks-add
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pstricks-add-doc
This package includes the documentation for texlive-pstricks-add

%post -n texlive-pstricks-add
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pstricks-add 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pstricks-add
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pstricks-add-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pstricks-add/Changes
%{_texmfdistdir}/doc/generic/pstricks-add/README
%{_texmfdistdir}/doc/generic/pstricks-add/data/contourN.data
%{_texmfdistdir}/doc/generic/pstricks-add/data/data.data
%{_texmfdistdir}/doc/generic/pstricks-add/data/data3.data
%{_texmfdistdir}/doc/generic/pstricks-add/data/dataMul.data
%{_texmfdistdir}/doc/generic/pstricks-add/data/demo0.data
%{_texmfdistdir}/doc/generic/pstricks-add/data/demo1.data
%{_texmfdistdir}/doc/generic/pstricks-add/data/demo2.data
%{_texmfdistdir}/doc/generic/pstricks-add/data/demo3.data
%{_texmfdistdir}/doc/generic/pstricks-add/data/dotmatrix.data
%{_texmfdistdir}/doc/generic/pstricks-add/data/matrix.data
%{_texmfdistdir}/doc/generic/pstricks-add/data/matrix1.data
%{_texmfdistdir}/doc/generic/pstricks-add/data/matrix2.data
%{_texmfdistdir}/doc/generic/pstricks-add/data/olympic.eps
%{_texmfdistdir}/doc/generic/pstricks-add/data/olympic.pdf
%{_texmfdistdir}/doc/generic/pstricks-add/data/olympic.tex
%{_texmfdistdir}/doc/generic/pstricks-add/data/pstricks-add-doc.data
%{_texmfdistdir}/doc/generic/pstricks-add/pstricks-add-doc.bib
%{_texmfdistdir}/doc/generic/pstricks-add/pstricks-add-doc.pdf
%{_texmfdistdir}/doc/generic/pstricks-add/pstricks-add-doc.tex

%files -n texlive-pstricks-add
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pstricks-add/pstricks-add.pro
%{_texmfdistdir}/tex/generic/pstricks-add/pstricks-add.tex
%{_texmfdistdir}/tex/latex/pstricks-add/pstricks-add.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pstricks-add-%{texlive_version}.%{texlive_noarch}.3.87svn49680-%{release}-zypper
%endif

%package -n texlive-pstricks_calcnotes
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn34363
Release:        0
Summary:        Use of PSTricks in calculus lecture notes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source76:       pstricks_calcnotes.doc.tar.xz

%description -n texlive-pstricks_calcnotes
The bundle shows the construction of PSTricks macros to draw
Riemann sums of an integral and to draw the vector field of an
ordinary differential equation. The results are illustrated in
a fragment of lecture notes.

date: 2018-09-16 13:47:34 +0000

%post -n texlive-pstricks_calcnotes
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pstricks_calcnotes 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pstricks_calcnotes
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pstricks_calcnotes
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/AppThreePDF.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/Convert_PstricksCode_To_Pdf/Readme.txt
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/Convert_PstricksCode_To_Pdf/convert.tex
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/Convert_PstricksCode_To_Pdf/test.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/AppThreePDF.tex
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/BZ1.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/BZ10.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/BZ2.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/BZ3.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/BZ4.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/BZ5.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/BZ6.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/BZ7.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/BZ8.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/BZ9.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig13.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig14.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig1a.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig1b.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig1c.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig2a.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig2b.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig3.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig4.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig5.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig6.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig7.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig8.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig9.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/ThreeAppsPDF.tex
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/b6of1.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/b6of2.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/b6of3.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/b6of4.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/vecb1.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/vecb2.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/vecb3.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/vecb4.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/vecb5.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/vecb6.pdf
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/AppThreePS.tex
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/BZ10.eps
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/BZ6.eps
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/BZ7.eps
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/BZ8.eps
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/BZ9.eps
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/ThreeAppsPS.tex
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/b6of1.eps
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/b6of2.eps
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/b6of3.eps
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/b6of4.eps
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/vecb1.eps
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/vecb2.eps
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/vecb3.eps
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/vecb4.eps
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/vecb5.eps
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/vecb6.eps
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/README
%{_texmfdistdir}/doc/latex/pstricks_calcnotes/ThreeAppsPDF.pdf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pstricks_calcnotes-%{texlive_version}.%{texlive_noarch}.1.2svn34363-%{release}-zypper
%endif

%package -n texlive-pstring
Version:        %{texlive_version}.%{texlive_noarch}.svn42857
Release:        0
Summary:        Typeset sequences with justification pointers
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pstring-doc >= %{texlive_version}
Provides:       tex(pstring.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(pgfcore.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source77:       pstring.tar.xz
Source78:       pstring.doc.tar.xz

%description -n texlive-pstring
This package lets you typeset justified sequences, also called
pointing strings. It's used for instance, in research papers
about Game Semantics to represent sequence of game moves with
their associated justification pointers. Depending on wether
using LaTeX or pdfLaTeX, the package uses PSTricks and pst-node
respectively pgf/TikZ.

date: 2018-09-15 11:51:14 +0000


%package -n texlive-pstring-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn42857
Release:        0
Summary:        Documentation for texlive-pstring
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pstring-doc
This package includes the documentation for texlive-pstring

%post -n texlive-pstring
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pstring 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pstring
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pstring-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pstring/README.md
%{_texmfdistdir}/doc/latex/pstring/pgfmanual-en-macros.tex
%{_texmfdistdir}/doc/latex/pstring/pstring-doc.pdf
%{_texmfdistdir}/doc/latex/pstring/pstring-doc.pre
%{_texmfdistdir}/doc/latex/pstring/pstring-doc.tex

%files -n texlive-pstring
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pstring/pstring.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pstring-%{texlive_version}.%{texlive_noarch}.svn42857-%{release}-zypper
%endif

%package -n texlive-ptex
Version:        %{texlive_version}.%{texlive_noarch}.svn50664
Release:        0
Summary:        A TeX system for publishing in Japanese
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires:       texlive-cm >= %{texlive_version}
Requires:       texlive-etex >= %{texlive_version}
Requires:       texlive-hyphen-base >= %{texlive_version}
Requires:       texlive-knuth-lib >= %{texlive_version}
Requires:       texlive-plain >= %{texlive_version}
Requires:       texlive-ptex-base >= %{texlive_version}
Requires:       texlive-ptex-fonts >= %{texlive_version}
Requires(pre): texlive-ptex-bin >= %{texlive_version}
#!BuildIgnore: texlive-ptex-bin
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source79:       ptex.doc.tar.xz

%description -n texlive-ptex
pTeX adds features related to vertical writing, and deals with
other problems in typesetting Japanese. A set of additions to a
TEXMF tree, for use with pTeX, may be found in package
pTeX-texmf. pTeX is distributed as WEB change files. A manual
(in Japanese) is distributed as package pTeX-manual.

date: 2019-01-08 19:07:01 +0000

%post -n texlive-ptex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.ptex
sed -ri 's/^\#\![[= =]]+ptex\b.*/ptex ptex - ptex.ini/' %{_texmfconfdir}/web2c/fmtutil.cnf || :
> /var/run/texlive/run-fmtutil.eptex
sed -ri 's/^\#\![[= =]]+eptex\b.*/eptex eptex language.def *eptex.ini/' %{_texmfconfdir}/web2c/fmtutil.cnf || :
echo 'addKanjiMap ptex-@jaEmbed@@jaVariant@.map' >> /var/run/texlive/run-updmap

%postun -n texlive-ptex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    sed -ri 's/^(ptex\b)/\#\!\ \1/' %{_texmfconfdir}/web2c/fmtutil.cnf || :
    rm -f %{_texmfvardir}/web2c/ptex/ptex.*
    sed -ri 's/^(eptex\b)/\#\!\ \1/' %{_texmfconfdir}/web2c/fmtutil.cnf || :
    rm -f %{_texmfvardir}/web2c/eptex/eptex.*
    echo 'deleteKanjiMap ptex-@jaEmbed@@jaVariant@.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%triggerin -n texlive-ptex -- texlive-cm
> /var/run/texlive/run-fmtutil.ptex
> /var/run/texlive/run-fmtutil.eptex

%triggerun -n texlive-ptex -- texlive-cm
> /var/run/texlive/run-fmtutil.ptex
> /var/run/texlive/run-fmtutil.eptex

%triggerin -n texlive-ptex -- texlive-hyphen-base
> /var/run/texlive/run-fmtutil.ptex
> /var/run/texlive/run-fmtutil.eptex

%triggerun -n texlive-ptex -- texlive-hyphen-base
> /var/run/texlive/run-fmtutil.ptex
> /var/run/texlive/run-fmtutil.eptex

%triggerin -n texlive-ptex -- texlive-knuth-lib
> /var/run/texlive/run-fmtutil.ptex
> /var/run/texlive/run-fmtutil.eptex

%triggerun -n texlive-ptex -- texlive-knuth-lib
> /var/run/texlive/run-fmtutil.ptex
> /var/run/texlive/run-fmtutil.eptex

%triggerin -n texlive-ptex -- texlive-plain
> /var/run/texlive/run-fmtutil.ptex
> /var/run/texlive/run-fmtutil.eptex

%triggerun -n texlive-ptex -- texlive-plain
> /var/run/texlive/run-fmtutil.ptex
> /var/run/texlive/run-fmtutil.eptex

%triggerin -n texlive-ptex -- texlive-ptex-base
> /var/run/texlive/run-fmtutil.ptex
> /var/run/texlive/run-fmtutil.eptex

%triggerun -n texlive-ptex -- texlive-ptex-base
> /var/run/texlive/run-fmtutil.ptex
> /var/run/texlive/run-fmtutil.eptex

%triggerin -n texlive-ptex -- texlive-ptex-fonts
> /var/run/texlive/run-fmtutil.ptex
> /var/run/texlive/run-fmtutil.eptex

%triggerun -n texlive-ptex -- texlive-ptex-fonts
> /var/run/texlive/run-fmtutil.ptex
> /var/run/texlive/run-fmtutil.eptex

%triggerin -n texlive-ptex -- texlive-etex
> /var/run/texlive/run-fmtutil.ptex
> /var/run/texlive/run-fmtutil.eptex

%triggerun -n texlive-ptex -- texlive-etex
> /var/run/texlive/run-fmtutil.ptex
> /var/run/texlive/run-fmtutil.eptex

%posttrans -n texlive-ptex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ptex
%defattr(-,root,root,755)
%{_mandir}/man1/eptex.1*
%{_mandir}/man1/makejvf.1*
%{_mandir}/man1/mendex.1*
%{_mandir}/man1/ppltotf.1*
%{_mandir}/man1/ptex.1*
%{_mandir}/man1/ptftopl.1*
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ptex-%{texlive_version}.%{texlive_noarch}.svn50664-%{release}-zypper
%endif

%package -n texlive-ptex-base
Version:        %{texlive_version}.%{texlive_noarch}.svn50731
Release:        0
Summary:        Plain TeX format for pTeX and e-pTeX
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-ptex-base-doc >= %{texlive_version}
Provides:       tex(ascii-jplain.tex)
Provides:       tex(kinsoku.tex)
Provides:       tex(ptex.tex)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source80:       ptex-base.tar.xz
Source81:       ptex-base.doc.tar.xz

%description -n texlive-ptex-base
The bundle contains the plain TeX format for pTeX and e-pTeX.

date: 2019-04-03 13:55:31 +0000


%package -n texlive-ptex-base-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn50731
Release:        0
Summary:        Documentation for texlive-ptex-base
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-ptex-base-doc
This package includes the documentation for texlive-ptex-base

%post -n texlive-ptex-base
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ptex-base 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ptex-base
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ptex-base-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/ptex/ptex-base/LICENSE
%{_texmfdistdir}/doc/ptex/ptex-base/README.md

%files -n texlive-ptex-base
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/ptex/ptex-base/ascii-jplain.tex
%{_texmfdistdir}/tex/ptex/ptex-base/eptex.ini
%{_texmfdistdir}/tex/ptex/ptex-base/eptex.src
%{_texmfdistdir}/tex/ptex/ptex-base/eptexdefs.lib
%{_texmfdistdir}/tex/ptex/ptex-base/kinsoku.tex
%{_texmfdistdir}/tex/ptex/ptex-base/ptex.ini
%{_texmfdistdir}/tex/ptex/ptex-base/ptex.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ptex-base-%{texlive_version}.%{texlive_noarch}.svn50731-%{release}-zypper
%endif

%package -n texlive-ptex-fontmaps
Version:        %{texlive_version}.%{texlive_noarch}.20190318.0svn50446
Release:        0
Summary:        Font maps and configuration tools for Japanese/Chinese/Korean fonts with (u)ptex
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires:       texlive-arphic-ttf >= %{texlive_version}
Requires:       texlive-baekmuk >= %{texlive_version}
Requires:       texlive-ipaex >= %{texlive_version}
Requires(pre): texlive-ptex-fontmaps-bin >= %{texlive_version}
#!BuildIgnore: texlive-ptex-fontmaps-bin
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-ptex-fontmaps-doc >= %{texlive_version}
Requires:       perl(Cwd)
#!BuildIgnore:  perl(Cwd)
Requires:       perl(Getopt::Long)
#!BuildIgnore:  perl(Getopt::Long)
Requires:       perl(Pod::Usage)
#!BuildIgnore:  perl(Pod::Usage)
Requires:       perl(Tk)
#!BuildIgnore:  perl(Tk)
Requires:       perl(Tk::Dialog)
#!BuildIgnore:  perl(Tk::Dialog)
Requires:       perl(Tk::NoteBook)
#!BuildIgnore:  perl(Tk::NoteBook)
Requires:       perl(strict)
#!BuildIgnore:  perl(strict)
Provides:       tex(otf-canon.map)
Provides:       tex(otf-hiragino-pron.map)
Provides:       tex(otf-hiragino.map)
Provides:       tex(otf-ipa.map)
Provides:       tex(otf-ipaex.map)
Provides:       tex(otf-ko-adobe.map)
Provides:       tex(otf-ko-apple.map)
Provides:       tex(otf-ko-baekmuk.map)
Provides:       tex(otf-ko-ms.map)
Provides:       tex(otf-ko-noEmbed.map)
Provides:       tex(otf-ko-noto-otc.map)
Provides:       tex(otf-ko-noto.map)
Provides:       tex(otf-ko-solaris.map)
Provides:       tex(otf-ko-sourcehan-otc.map)
Provides:       tex(otf-ko-sourcehan.map)
Provides:       tex(otf-ko-unfonts.map)
Provides:       tex(otf-kozuka-pr6.map)
Provides:       tex(otf-kozuka-pr6n.map)
Provides:       tex(otf-kozuka.map)
Provides:       tex(otf-moga-mobo-ex.map)
Provides:       tex(otf-moga-mobo.map)
Provides:       tex(otf-morisawa-pr6n.map)
Provides:       tex(otf-morisawa.map)
Provides:       tex(otf-ms-osx.map)
Provides:       tex(otf-ms.map)
Provides:       tex(otf-noEmbed.map)
Provides:       tex(otf-noto-otc.map)
Provides:       tex(otf-noto.map)
Provides:       tex(otf-sc-adobe.map)
Provides:       tex(otf-sc-arphic.map)
Provides:       tex(otf-sc-cjkunifonts-ttf.map)
Provides:       tex(otf-sc-cjkunifonts.map)
Provides:       tex(otf-sc-fandol.map)
Provides:       tex(otf-sc-founder.map)
Provides:       tex(otf-sc-ms-osx.map)
Provides:       tex(otf-sc-ms.map)
Provides:       tex(otf-sc-noEmbed.map)
Provides:       tex(otf-sc-noto-otc.map)
Provides:       tex(otf-sc-noto.map)
Provides:       tex(otf-sc-sourcehan-otc.map)
Provides:       tex(otf-sc-sourcehan.map)
Provides:       tex(otf-sourcehan-otc.map)
Provides:       tex(otf-sourcehan.map)
Provides:       tex(otf-tc-adobe.map)
Provides:       tex(otf-tc-arphic.map)
Provides:       tex(otf-tc-cjkunifonts-ttf.map)
Provides:       tex(otf-tc-cjkunifonts.map)
Provides:       tex(otf-tc-dynacomware.map)
Provides:       tex(otf-tc-ms-win10.map)
Provides:       tex(otf-tc-ms.map)
Provides:       tex(otf-tc-noEmbed.map)
Provides:       tex(otf-tc-noto-otc.map)
Provides:       tex(otf-tc-noto.map)
Provides:       tex(otf-tc-sourcehan-otc.map)
Provides:       tex(otf-tc-sourcehan.map)
Provides:       tex(otf-ume.map)
Provides:       tex(otf-up-canon.map)
Provides:       tex(otf-up-hiragino-pron.map)
Provides:       tex(otf-up-hiragino.map)
Provides:       tex(otf-up-ipa.map)
Provides:       tex(otf-up-ipaex.map)
Provides:       tex(otf-up-kozuka-pr6.map)
Provides:       tex(otf-up-kozuka-pr6n.map)
Provides:       tex(otf-up-kozuka.map)
Provides:       tex(otf-up-moga-mobo-ex.map)
Provides:       tex(otf-up-moga-mobo.map)
Provides:       tex(otf-up-morisawa-pr6n.map)
Provides:       tex(otf-up-morisawa.map)
Provides:       tex(otf-up-ms-osx.map)
Provides:       tex(otf-up-ms.map)
Provides:       tex(otf-up-noEmbed.map)
Provides:       tex(otf-up-noto-otc.map)
Provides:       tex(otf-up-noto.map)
Provides:       tex(otf-up-sourcehan-otc.map)
Provides:       tex(otf-up-sourcehan.map)
Provides:       tex(otf-up-ume.map)
Provides:       tex(otf-up-yu-osx.map)
Provides:       tex(otf-up-yu-win.map)
Provides:       tex(otf-up-yu-win10.map)
Provides:       tex(otf-yu-osx.map)
Provides:       tex(otf-yu-win.map)
Provides:       tex(otf-yu-win10.map)
Provides:       tex(ptex-canon.map)
Provides:       tex(ptex-fontmaps-data.dat)
Provides:       tex(ptex-hiragino-04.map)
Provides:       tex(ptex-hiragino-pron-04.map)
Provides:       tex(ptex-hiragino-pron.map)
Provides:       tex(ptex-hiragino.map)
Provides:       tex(ptex-ipa.map)
Provides:       tex(ptex-ipaex.map)
Provides:       tex(ptex-kozuka-04.map)
Provides:       tex(ptex-kozuka-pr6-04.map)
Provides:       tex(ptex-kozuka-pr6.map)
Provides:       tex(ptex-kozuka-pr6n-04.map)
Provides:       tex(ptex-kozuka-pr6n.map)
Provides:       tex(ptex-kozuka.map)
Provides:       tex(ptex-moga-mobo-04.map)
Provides:       tex(ptex-moga-mobo-ex-04.map)
Provides:       tex(ptex-moga-mobo-ex.map)
Provides:       tex(ptex-moga-mobo.map)
Provides:       tex(ptex-morisawa-04.map)
Provides:       tex(ptex-morisawa-pr6n-04.map)
Provides:       tex(ptex-morisawa-pr6n.map)
Provides:       tex(ptex-morisawa.map)
Provides:       tex(ptex-ms-osx.map)
Provides:       tex(ptex-ms.map)
Provides:       tex(ptex-noEmbed-04.map)
Provides:       tex(ptex-noEmbed.map)
Provides:       tex(ptex-noto-04.map)
Provides:       tex(ptex-noto-otc-04.map)
Provides:       tex(ptex-noto-otc.map)
Provides:       tex(ptex-noto.map)
Provides:       tex(ptex-sourcehan-04.map)
Provides:       tex(ptex-sourcehan-otc-04.map)
Provides:       tex(ptex-sourcehan-otc.map)
Provides:       tex(ptex-sourcehan.map)
Provides:       tex(ptex-ume.map)
Provides:       tex(ptex-yu-osx-04.map)
Provides:       tex(ptex-yu-osx.map)
Provides:       tex(ptex-yu-win.map)
Provides:       tex(ptex-yu-win10.map)
Provides:       tex(uptex-canon.map)
Provides:       tex(uptex-hiragino-04.map)
Provides:       tex(uptex-hiragino-pron-04.map)
Provides:       tex(uptex-hiragino-pron.map)
Provides:       tex(uptex-hiragino.map)
Provides:       tex(uptex-ipa.map)
Provides:       tex(uptex-ipaex.map)
Provides:       tex(uptex-ko-adobe.map)
Provides:       tex(uptex-ko-apple.map)
Provides:       tex(uptex-ko-baekmuk.map)
Provides:       tex(uptex-ko-ms.map)
Provides:       tex(uptex-ko-noEmbed.map)
Provides:       tex(uptex-ko-noto-otc.map)
Provides:       tex(uptex-ko-noto.map)
Provides:       tex(uptex-ko-solaris.map)
Provides:       tex(uptex-ko-sourcehan-otc.map)
Provides:       tex(uptex-ko-sourcehan.map)
Provides:       tex(uptex-ko-unfonts.map)
Provides:       tex(uptex-kozuka-04.map)
Provides:       tex(uptex-kozuka-pr6-04.map)
Provides:       tex(uptex-kozuka-pr6.map)
Provides:       tex(uptex-kozuka-pr6n-04.map)
Provides:       tex(uptex-kozuka-pr6n.map)
Provides:       tex(uptex-kozuka.map)
Provides:       tex(uptex-moga-mobo-04.map)
Provides:       tex(uptex-moga-mobo-ex-04.map)
Provides:       tex(uptex-moga-mobo-ex.map)
Provides:       tex(uptex-moga-mobo.map)
Provides:       tex(uptex-morisawa-04.map)
Provides:       tex(uptex-morisawa-pr6n-04.map)
Provides:       tex(uptex-morisawa-pr6n.map)
Provides:       tex(uptex-morisawa.map)
Provides:       tex(uptex-ms-osx.map)
Provides:       tex(uptex-ms.map)
Provides:       tex(uptex-noEmbed-04.map)
Provides:       tex(uptex-noEmbed.map)
Provides:       tex(uptex-noto-04.map)
Provides:       tex(uptex-noto-otc-04.map)
Provides:       tex(uptex-noto-otc.map)
Provides:       tex(uptex-noto.map)
Provides:       tex(uptex-sc-adobe.map)
Provides:       tex(uptex-sc-arphic.map)
Provides:       tex(uptex-sc-cjkunifonts-ttf.map)
Provides:       tex(uptex-sc-cjkunifonts.map)
Provides:       tex(uptex-sc-fandol.map)
Provides:       tex(uptex-sc-founder.map)
Provides:       tex(uptex-sc-ms-osx.map)
Provides:       tex(uptex-sc-ms.map)
Provides:       tex(uptex-sc-noEmbed.map)
Provides:       tex(uptex-sc-noto-otc.map)
Provides:       tex(uptex-sc-noto.map)
Provides:       tex(uptex-sc-sourcehan-otc.map)
Provides:       tex(uptex-sc-sourcehan.map)
Provides:       tex(uptex-sourcehan-04.map)
Provides:       tex(uptex-sourcehan-otc-04.map)
Provides:       tex(uptex-sourcehan-otc.map)
Provides:       tex(uptex-sourcehan.map)
Provides:       tex(uptex-tc-adobe.map)
Provides:       tex(uptex-tc-arphic.map)
Provides:       tex(uptex-tc-cjkunifonts-ttf.map)
Provides:       tex(uptex-tc-cjkunifonts.map)
Provides:       tex(uptex-tc-dynacomware.map)
Provides:       tex(uptex-tc-ms-win10.map)
Provides:       tex(uptex-tc-ms.map)
Provides:       tex(uptex-tc-noEmbed.map)
Provides:       tex(uptex-tc-noto-otc.map)
Provides:       tex(uptex-tc-noto.map)
Provides:       tex(uptex-tc-sourcehan-otc.map)
Provides:       tex(uptex-tc-sourcehan.map)
Provides:       tex(uptex-ume.map)
Provides:       tex(uptex-yu-osx-04.map)
Provides:       tex(uptex-yu-osx.map)
Provides:       tex(uptex-yu-win.map)
Provides:       tex(uptex-yu-win10.map)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source82:       ptex-fontmaps.tar.xz
Source83:       ptex-fontmaps.doc.tar.xz

%description -n texlive-ptex-fontmaps
This package provides font maps and setup tools for Japanese,
Korean, Traditional Chinese, and Simplified Chinese. It is the
successor of the jfontmaps package. The files in this package
contain font maps for dvipdfmx to make various
Japanese/Chinese/Korean fonts available for (u)ptex and related
programs and formats.

date: 2019-03-18 13:57:35 +0000


%package -n texlive-ptex-fontmaps-doc
Version:        %{texlive_version}.%{texlive_noarch}.20190318.0svn50446
Release:        0
Summary:        Documentation for texlive-ptex-fontmaps
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-ptex-fontmaps-doc
This package includes the documentation for texlive-ptex-fontmaps

%post -n texlive-ptex-fontmaps
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ptex-fontmaps 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ptex-fontmaps
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ptex-fontmaps-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/ptex-fontmaps/README
%{_texmfdistdir}/doc/fonts/ptex-fontmaps/examples/otf-sample-04.tex
%{_texmfdistdir}/doc/fonts/ptex-fontmaps/examples/otf-sample.tex
%{_texmfdistdir}/doc/fonts/ptex-fontmaps/examples/ptex-sample.tex
%{_texmfdistdir}/doc/fonts/ptex-fontmaps/examples/series-compare.tex

%files -n texlive-ptex-fontmaps
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/cmap/ptex-fontmaps/2004-H
%{_texmfdistdir}/fonts/cmap/ptex-fontmaps/2004-V
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/adobe/otf-ko-adobe.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/adobe/otf-sc-adobe.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/adobe/otf-tc-adobe.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/adobe/uptex-ko-adobe.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/adobe/uptex-sc-adobe.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/adobe/uptex-tc-adobe.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/apple/otf-ko-apple.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/apple/uptex-ko-apple.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/arphic/otf-sc-arphic.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/arphic/otf-tc-arphic.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/arphic/uptex-sc-arphic.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/arphic/uptex-tc-arphic.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/baekmuk/otf-ko-baekmuk.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/baekmuk/uptex-ko-baekmuk.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/canon/otf-canon.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/canon/otf-up-canon.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/canon/ptex-canon.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/canon/uptex-canon.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/cjkunifonts-ttf/otf-sc-cjkunifonts-ttf.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/cjkunifonts-ttf/otf-tc-cjkunifonts-ttf.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/cjkunifonts-ttf/uptex-sc-cjkunifonts-ttf.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/cjkunifonts-ttf/uptex-tc-cjkunifonts-ttf.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/cjkunifonts/otf-sc-cjkunifonts.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/cjkunifonts/otf-tc-cjkunifonts.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/cjkunifonts/uptex-sc-cjkunifonts.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/cjkunifonts/uptex-tc-cjkunifonts.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/dynacomware/otf-tc-dynacomware.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/dynacomware/uptex-tc-dynacomware.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/fandol/otf-sc-fandol.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/fandol/uptex-sc-fandol.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/founder/otf-sc-founder.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/founder/uptex-sc-founder.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/hiragino-pron/otf-hiragino-pron.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/hiragino-pron/otf-up-hiragino-pron.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/hiragino-pron/ptex-hiragino-pron-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/hiragino-pron/ptex-hiragino-pron.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/hiragino-pron/uptex-hiragino-pron-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/hiragino-pron/uptex-hiragino-pron.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/hiragino/otf-hiragino.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/hiragino/otf-up-hiragino.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/hiragino/ptex-hiragino-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/hiragino/ptex-hiragino.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/hiragino/uptex-hiragino-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/hiragino/uptex-hiragino.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ipa/otf-ipa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ipa/otf-up-ipa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ipa/ptex-ipa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ipa/uptex-ipa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ipaex/otf-ipaex.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ipaex/otf-up-ipaex.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ipaex/ptex-ipaex.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ipaex/uptex-ipaex.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/kozuka-pr6/otf-kozuka-pr6.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/kozuka-pr6/otf-up-kozuka-pr6.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/kozuka-pr6/ptex-kozuka-pr6-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/kozuka-pr6/ptex-kozuka-pr6.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/kozuka-pr6/uptex-kozuka-pr6-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/kozuka-pr6/uptex-kozuka-pr6.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/kozuka-pr6n/otf-kozuka-pr6n.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/kozuka-pr6n/otf-up-kozuka-pr6n.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/kozuka-pr6n/ptex-kozuka-pr6n-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/kozuka-pr6n/ptex-kozuka-pr6n.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/kozuka-pr6n/uptex-kozuka-pr6n-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/kozuka-pr6n/uptex-kozuka-pr6n.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/kozuka/otf-kozuka.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/kozuka/otf-up-kozuka.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/kozuka/ptex-kozuka-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/kozuka/ptex-kozuka.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/kozuka/uptex-kozuka-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/kozuka/uptex-kozuka.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/moga-mobo-ex/otf-moga-mobo-ex.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/moga-mobo-ex/otf-up-moga-mobo-ex.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/moga-mobo-ex/ptex-moga-mobo-ex-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/moga-mobo-ex/ptex-moga-mobo-ex.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/moga-mobo-ex/uptex-moga-mobo-ex-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/moga-mobo-ex/uptex-moga-mobo-ex.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/moga-mobo/otf-moga-mobo.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/moga-mobo/otf-up-moga-mobo.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/moga-mobo/ptex-moga-mobo-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/moga-mobo/ptex-moga-mobo.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/moga-mobo/uptex-moga-mobo-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/moga-mobo/uptex-moga-mobo.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/morisawa-pr6n/otf-morisawa-pr6n.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/morisawa-pr6n/otf-up-morisawa-pr6n.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/morisawa-pr6n/ptex-morisawa-pr6n-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/morisawa-pr6n/ptex-morisawa-pr6n.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/morisawa-pr6n/uptex-morisawa-pr6n-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/morisawa-pr6n/uptex-morisawa-pr6n.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/morisawa/otf-morisawa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/morisawa/otf-up-morisawa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/morisawa/ptex-morisawa-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/morisawa/ptex-morisawa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/morisawa/uptex-morisawa-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/morisawa/uptex-morisawa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ms-osx/otf-ms-osx.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ms-osx/otf-sc-ms-osx.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ms-osx/otf-up-ms-osx.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ms-osx/ptex-ms-osx.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ms-osx/uptex-ms-osx.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ms-osx/uptex-sc-ms-osx.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ms-win10/otf-tc-ms-win10.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ms-win10/uptex-tc-ms-win10.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ms/otf-ko-ms.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ms/otf-ms.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ms/otf-sc-ms.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ms/otf-tc-ms.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ms/otf-up-ms.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ms/ptex-ms.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ms/uptex-ko-ms.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ms/uptex-ms.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ms/uptex-sc-ms.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ms/uptex-tc-ms.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noEmbed/otf-ko-noEmbed.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noEmbed/otf-noEmbed.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noEmbed/otf-sc-noEmbed.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noEmbed/otf-tc-noEmbed.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noEmbed/otf-up-noEmbed.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noEmbed/ptex-noEmbed-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noEmbed/ptex-noEmbed.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noEmbed/uptex-ko-noEmbed.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noEmbed/uptex-noEmbed-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noEmbed/uptex-noEmbed.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noEmbed/uptex-sc-noEmbed.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noEmbed/uptex-tc-noEmbed.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto-otc/otf-ko-noto-otc.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto-otc/otf-noto-otc.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto-otc/otf-sc-noto-otc.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto-otc/otf-tc-noto-otc.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto-otc/otf-up-noto-otc.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto-otc/ptex-noto-otc-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto-otc/ptex-noto-otc.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto-otc/uptex-ko-noto-otc.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto-otc/uptex-noto-otc-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto-otc/uptex-noto-otc.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto-otc/uptex-sc-noto-otc.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto-otc/uptex-tc-noto-otc.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto/otf-ko-noto.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto/otf-noto.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto/otf-sc-noto.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto/otf-tc-noto.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto/otf-up-noto.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto/ptex-noto-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto/ptex-noto.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto/uptex-ko-noto.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto/uptex-noto-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto/uptex-noto.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto/uptex-sc-noto.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/noto/uptex-tc-noto.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/solaris/otf-ko-solaris.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/solaris/uptex-ko-solaris.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan-otc/otf-ko-sourcehan-otc.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan-otc/otf-sc-sourcehan-otc.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan-otc/otf-sourcehan-otc.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan-otc/otf-tc-sourcehan-otc.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan-otc/otf-up-sourcehan-otc.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan-otc/ptex-sourcehan-otc-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan-otc/ptex-sourcehan-otc.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan-otc/uptex-ko-sourcehan-otc.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan-otc/uptex-sc-sourcehan-otc.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan-otc/uptex-sourcehan-otc-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan-otc/uptex-sourcehan-otc.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan-otc/uptex-tc-sourcehan-otc.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan/otf-ko-sourcehan.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan/otf-sc-sourcehan.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan/otf-sourcehan.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan/otf-tc-sourcehan.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan/otf-up-sourcehan.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan/ptex-sourcehan-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan/ptex-sourcehan.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan/uptex-ko-sourcehan.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan/uptex-sc-sourcehan.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan/uptex-sourcehan-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan/uptex-sourcehan.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/sourcehan/uptex-tc-sourcehan.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ume/otf-ume.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ume/otf-up-ume.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ume/ptex-ume.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/ume/uptex-ume.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/unfonts/otf-ko-unfonts.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/unfonts/uptex-ko-unfonts.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/yu-osx/otf-up-yu-osx.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/yu-osx/otf-yu-osx.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/yu-osx/ptex-yu-osx-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/yu-osx/ptex-yu-osx.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/yu-osx/uptex-yu-osx-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/yu-osx/uptex-yu-osx.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/yu-win/otf-up-yu-win.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/yu-win/otf-yu-win.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/yu-win/ptex-yu-win.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/yu-win/uptex-yu-win.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/yu-win10/otf-up-yu-win10.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/yu-win10/otf-yu-win10.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/yu-win10/ptex-yu-win10.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ptex-fontmaps/yu-win10/uptex-yu-win10.map
%{_texmfdistdir}/fonts/misc/ptex-fontmaps/ptex-fontmaps-data.dat
%{_texmfdistdir}/scripts/ptex-fontmaps/kanji-config-updmap-sys.sh
%{_texmfdistdir}/scripts/ptex-fontmaps/kanji-config-updmap-user.sh
%{_texmfdistdir}/scripts/ptex-fontmaps/kanji-config-updmap.pl
%{_texmfdistdir}/scripts/ptex-fontmaps/kanji-fontmap-creator.pl
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ptex-fontmaps-%{texlive_version}.%{texlive_noarch}.20190318.0svn50446-%{release}-zypper
%endif

%package -n texlive-ptex-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn46940
Release:        0
Summary:        Fonts for use with pTeX
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-ptex-fonts-doc >= %{texlive_version}
Provides:       tex(gbm.tfm)
Provides:       tex(gbmv.tfm)
Provides:       tex(goth10.tfm)
Provides:       tex(goth10.vf)
Provides:       tex(goth5.tfm)
Provides:       tex(goth5.vf)
Provides:       tex(goth6.tfm)
Provides:       tex(goth6.vf)
Provides:       tex(goth7.tfm)
Provides:       tex(goth7.vf)
Provides:       tex(goth8.tfm)
Provides:       tex(goth8.vf)
Provides:       tex(goth9.tfm)
Provides:       tex(goth9.vf)
Provides:       tex(jis-v.tfm)
Provides:       tex(jis-v.vf)
Provides:       tex(jis.tfm)
Provides:       tex(jis.vf)
Provides:       tex(jisg-v.tfm)
Provides:       tex(jisg-v.vf)
Provides:       tex(jisg.tfm)
Provides:       tex(jisg.vf)
Provides:       tex(jisgn-v.tfm)
Provides:       tex(jisgn-v.vf)
Provides:       tex(jisgn.tfm)
Provides:       tex(jisgn.vf)
Provides:       tex(jisn-v.tfm)
Provides:       tex(jisn-v.vf)
Provides:       tex(jisn.tfm)
Provides:       tex(jisn.vf)
Provides:       tex(min10.tfm)
Provides:       tex(min10.vf)
Provides:       tex(min5.tfm)
Provides:       tex(min5.vf)
Provides:       tex(min6.tfm)
Provides:       tex(min6.vf)
Provides:       tex(min7.tfm)
Provides:       tex(min7.vf)
Provides:       tex(min8.tfm)
Provides:       tex(min8.vf)
Provides:       tex(min9.tfm)
Provides:       tex(min9.vf)
Provides:       tex(ngoth10.tfm)
Provides:       tex(ngoth10.vf)
Provides:       tex(ngoth5.tfm)
Provides:       tex(ngoth5.vf)
Provides:       tex(ngoth6.tfm)
Provides:       tex(ngoth6.vf)
Provides:       tex(ngoth7.tfm)
Provides:       tex(ngoth7.vf)
Provides:       tex(ngoth8.tfm)
Provides:       tex(ngoth8.vf)
Provides:       tex(ngoth9.tfm)
Provides:       tex(ngoth9.vf)
Provides:       tex(nmin10.tfm)
Provides:       tex(nmin10.vf)
Provides:       tex(nmin5.tfm)
Provides:       tex(nmin5.vf)
Provides:       tex(nmin6.tfm)
Provides:       tex(nmin6.vf)
Provides:       tex(nmin7.tfm)
Provides:       tex(nmin7.vf)
Provides:       tex(nmin8.tfm)
Provides:       tex(nmin8.vf)
Provides:       tex(nmin9.tfm)
Provides:       tex(nmin9.vf)
Provides:       tex(rml.tfm)
Provides:       tex(rmlv.tfm)
Provides:       tex(tgoth10.tfm)
Provides:       tex(tgoth10.vf)
Provides:       tex(tgoth5.tfm)
Provides:       tex(tgoth5.vf)
Provides:       tex(tgoth6.tfm)
Provides:       tex(tgoth6.vf)
Provides:       tex(tgoth7.tfm)
Provides:       tex(tgoth7.vf)
Provides:       tex(tgoth8.tfm)
Provides:       tex(tgoth8.vf)
Provides:       tex(tgoth9.tfm)
Provides:       tex(tgoth9.vf)
Provides:       tex(tmin10.tfm)
Provides:       tex(tmin10.vf)
Provides:       tex(tmin5.tfm)
Provides:       tex(tmin5.vf)
Provides:       tex(tmin6.tfm)
Provides:       tex(tmin6.vf)
Provides:       tex(tmin7.tfm)
Provides:       tex(tmin7.vf)
Provides:       tex(tmin8.tfm)
Provides:       tex(tmin8.vf)
Provides:       tex(tmin9.tfm)
Provides:       tex(tmin9.vf)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source84:       ptex-fonts.tar.xz
Source85:       ptex-fonts.doc.tar.xz

%description -n texlive-ptex-fonts
The bundle contains fonts for use with pTeX and the documents
for the makejvf program. This is a redistribution derived from
the ptex-texmf distribution by ASCII MEDIA WORKS.

date: 2018-03-09 15:42:25 +0000


%package -n texlive-ptex-fonts-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn46940
Release:        0
Summary:        Documentation for texlive-ptex-fonts
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-ptex-fonts-doc
This package includes the documentation for texlive-ptex-fonts

%post -n texlive-ptex-fonts
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ptex-fonts 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ptex-fonts
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ptex-fonts-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/ptex-fonts/Changes_makejvf
%{_texmfdistdir}/doc/fonts/ptex-fonts/LICENSE
%{_texmfdistdir}/doc/fonts/ptex-fonts/README.md
%{_texmfdistdir}/doc/fonts/ptex-fonts/README_makejvf

%files -n texlive-ptex-fonts
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/ptex-fonts/jis/jis-v.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/jis/jis.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/jis/jisn-v.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/jis/jisn.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/nmin-ngoth/ngoth10.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/nmin-ngoth/ngoth5.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/nmin-ngoth/ngoth6.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/nmin-ngoth/ngoth7.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/nmin-ngoth/ngoth8.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/nmin-ngoth/ngoth9.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/nmin-ngoth/nmin10.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/nmin-ngoth/nmin5.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/nmin-ngoth/nmin6.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/nmin-ngoth/nmin7.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/nmin-ngoth/nmin8.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/nmin-ngoth/nmin9.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/goth10.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/goth5.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/goth6.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/goth7.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/goth8.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/goth9.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/min10.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/min5.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/min6.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/min7.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/min8.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/min9.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/tgoth10.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/tgoth5.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/tgoth6.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/tgoth7.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/tgoth8.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/tgoth9.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/tmin10.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/tmin5.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/tmin6.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/tmin7.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/tmin8.pl
%{_texmfdistdir}/fonts/source/ptex-fonts/standard/tmin9.pl
%{_texmfdistdir}/fonts/tfm/ptex-fonts/dvips/gbm.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/dvips/gbmv.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/dvips/rml.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/dvips/rmlv.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/jis/jis-v.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/jis/jis.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/jis/jisg-v.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/jis/jisg.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/jis/jisgn-v.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/jis/jisgn.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/jis/jisn-v.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/jis/jisn.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/nmin-ngoth/ngoth10.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/nmin-ngoth/ngoth5.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/nmin-ngoth/ngoth6.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/nmin-ngoth/ngoth7.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/nmin-ngoth/ngoth8.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/nmin-ngoth/ngoth9.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/nmin-ngoth/nmin10.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/nmin-ngoth/nmin5.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/nmin-ngoth/nmin6.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/nmin-ngoth/nmin7.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/nmin-ngoth/nmin8.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/nmin-ngoth/nmin9.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/goth10.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/goth5.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/goth6.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/goth7.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/goth8.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/goth9.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/min10.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/min5.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/min6.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/min7.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/min8.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/min9.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/tgoth10.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/tgoth5.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/tgoth6.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/tgoth7.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/tgoth8.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/tgoth9.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/tmin10.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/tmin5.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/tmin6.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/tmin7.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/tmin8.tfm
%{_texmfdistdir}/fonts/tfm/ptex-fonts/standard/tmin9.tfm
%{_texmfdistdir}/fonts/vf/ptex-fonts/jis/jis-v.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/jis/jis.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/jis/jisg-v.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/jis/jisg.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/jis/jisgn-v.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/jis/jisgn.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/jis/jisn-v.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/jis/jisn.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/nmin-ngoth/ngoth10.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/nmin-ngoth/ngoth5.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/nmin-ngoth/ngoth6.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/nmin-ngoth/ngoth7.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/nmin-ngoth/ngoth8.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/nmin-ngoth/ngoth9.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/nmin-ngoth/nmin10.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/nmin-ngoth/nmin5.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/nmin-ngoth/nmin6.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/nmin-ngoth/nmin7.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/nmin-ngoth/nmin8.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/nmin-ngoth/nmin9.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/goth10.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/goth5.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/goth6.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/goth7.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/goth8.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/goth9.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/min10.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/min5.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/min6.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/min7.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/min8.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/min9.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/tgoth10.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/tgoth5.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/tgoth6.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/tgoth7.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/tgoth8.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/tgoth9.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/tmin10.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/tmin5.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/tmin6.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/tmin7.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/tmin8.vf
%{_texmfdistdir}/fonts/vf/ptex-fonts/standard/tmin9.vf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ptex-fonts-%{texlive_version}.%{texlive_noarch}.svn46940-%{release}-zypper
%endif

%package -n texlive-ptex-manual
Version:        %{texlive_version}.%{texlive_noarch}.svn50733
Release:        0
Summary:        Japanese pTeX manual
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-ptex-manual-doc >= %{texlive_version}
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source86:       ptex-manual.source.tar.xz
Source87:       ptex-manual.doc.tar.xz

%description -n texlive-ptex-manual
This package contains the Japanese pTeX manual. Feedback is
welcome!

date: 2019-04-03 13:24:53 +0000


%package -n texlive-ptex-manual-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn50733
Release:        0
Summary:        Documentation for texlive-ptex-manual
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-ptex-manual-doc:ja)

%description -n texlive-ptex-manual-doc
This package includes the documentation for texlive-ptex-manual

%post -n texlive-ptex-manual
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ptex-manual 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ptex-manual
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ptex-manual-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/ptex/ptex-manual/LICENSE
%{_texmfdistdir}/doc/ptex/ptex-manual/README.md
%{_texmfdistdir}/doc/ptex/ptex-manual/eptex_resume.pdf
%{_texmfdistdir}/doc/ptex/ptex-manual/eptex_resume.tex
%{_texmfdistdir}/doc/ptex/ptex-manual/eptexdoc.pdf
%{_texmfdistdir}/doc/ptex/ptex-manual/eptexdoc.tex
%{_texmfdistdir}/doc/ptex/ptex-manual/fam256d.tex
%{_texmfdistdir}/doc/ptex/ptex-manual/fam256p.tex
%{_texmfdistdir}/doc/ptex/ptex-manual/jfm.pdf
%{_texmfdistdir}/doc/ptex/ptex-manual/jfm.tex
%{_texmfdistdir}/doc/ptex/ptex-manual/jtex_asciimw.pdf
%{_texmfdistdir}/doc/ptex/ptex-manual/jtex_asciimw.tex
%{_texmfdistdir}/doc/ptex/ptex-manual/jtexdoc_asciimw.pdf
%{_texmfdistdir}/doc/ptex/ptex-manual/jtexdoc_asciimw.tex
%{_texmfdistdir}/doc/ptex/ptex-manual/ptex-manual.pdf
%{_texmfdistdir}/doc/ptex/ptex-manual/ptex-manual.tex
%{_texmfdistdir}/doc/ptex/ptex-manual/ptexdoc_asciimw.pdf
%{_texmfdistdir}/doc/ptex/ptex-manual/ptexdoc_asciimw.tex
%{_texmfdistdir}/doc/ptex/ptex-manual/ptexskip_asciimw.pdf
%{_texmfdistdir}/doc/ptex/ptex-manual/ptexskip_asciimw.tex

%files -n texlive-ptex-manual
%defattr(-,root,root,755)
%{_texmfdistdir}/source/latex/ptex-manual/Makefile
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ptex-manual-%{texlive_version}.%{texlive_noarch}.svn50733-%{release}-zypper
%endif

%package -n texlive-ptex2pdf
Version:        %{texlive_version}.%{texlive_noarch}.20181212.0svn49396
Release:        0
Summary:        Convert Japanese TeX documents to PDF
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive-ptex2pdf-bin >= %{texlive_version}
#!BuildIgnore: texlive-ptex2pdf-bin
Requires(post): perl = %{perl_version}
Requires(post): perl(TeXLive::TLUtils)
Requires(post): tex(texmf.cnf)
Requires(post): texlive-kpathsea-bin >= %{texlive_version}
Requires(post): texlive-texlive.infra >= %{texlive_version}
#!BuildIgnore: texlive-kpathsea
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-ptex2pdf-doc >= %{texlive_version}
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source88:       ptex2pdf.tar.xz
Source89:       ptex2pdf.doc.tar.xz

%description -n texlive-ptex2pdf
The Lua script provides system-independent support of Japanese
typesetting engines in TeXworks. As TeXworks typesetting setup
does not allow for multistep processing, this script runs one
of the ptex-based programs (ptex, uptex, eptex, platex,
uplatex) followed by dvipdfmx.

date: 2018-12-12 16:43:43 +0000


%package -n texlive-ptex2pdf-doc
Version:        %{texlive_version}.%{texlive_noarch}.20181212.0svn49396
Release:        0
Summary:        Documentation for texlive-ptex2pdf
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-ptex2pdf-doc
This package includes the documentation for texlive-ptex2pdf

%post -n texlive-ptex2pdf
/usr/bin/perl %{_texmfmaindir}/tlpkg/tlpostcode/ptex2pdf-tlpost.pl install %{_texmfmaindir}
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ptex2pdf 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ptex2pdf
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ptex2pdf-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ptex2pdf/COPYING
%{_texmfdistdir}/doc/latex/ptex2pdf/README.md

%files -n texlive-ptex2pdf
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/ptex2pdf/ptex2pdf.lua
%{_texmfmaindir}/tlpkg/tlpostcode/ptex2pdf-tlpost.pl
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ptex2pdf-%{texlive_version}.%{texlive_noarch}.20181212.0svn49396-%{release}-zypper
%endif

%package -n texlive-ptext
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn30171
Release:        0
Summary:        A 'lipsum' for Persian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-ptext-doc >= %{texlive_version}
Provides:       tex(ptext.sty)
Requires:       tex(biditools.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source90:       ptext.tar.xz
Source91:       ptext.doc.tar.xz

%description -n texlive-ptext
The package provides lipsum-like facilities for the Persian
language. The source of the filling text is the Persian epic
"the Shanameh" (100 paragraphs are used.) The package needs to
be run under XeLaTeX.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-ptext-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn30171
Release:        0
Summary:        Documentation for texlive-ptext
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-ptext-doc:fa)

%description -n texlive-ptext-doc
This package includes the documentation for texlive-ptext

%post -n texlive-ptext
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ptext 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ptext
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ptext-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/xelatex/ptext/README
%{_texmfdistdir}/doc/xelatex/ptext/ptext.pdf
%{_texmfdistdir}/doc/xelatex/ptext/ptext.tex

%files -n texlive-ptext
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/xelatex/ptext/ptext.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ptext-%{texlive_version}.%{texlive_noarch}.1.1svn30171-%{release}-zypper
%endif

%package -n texlive-ptolemaicastronomy
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn50810
Release:        0
Summary:        Diagrams of sphere models for variably strict conditionals (Lewis counterfactuals)
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-ptolemaicastronomy-doc >= %{texlive_version}
Provides:       tex(ptolemaicastronomy.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source92:       ptolemaicastronomy.tar.xz
Source93:       ptolemaicastronomy.doc.tar.xz

%description -n texlive-ptolemaicastronomy
David K. Lewis (Counterfactuals, Blackwell 1973) introduced a
sphere semantics for counterfactual conditionals. He jokingly
referred to the diagrams depicting such sphere models as
Ptolemaic astronomy, hence the name of this package. The macros
provided in this package aid in the construction of sphere
model diagrams in the style of Lewis. The macros all make use
of TikZ.

date: 2019-04-06 05:05:41 +0000


%package -n texlive-ptolemaicastronomy-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn50810
Release:        0
Summary:        Documentation for texlive-ptolemaicastronomy
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-ptolemaicastronomy-doc
This package includes the documentation for texlive-ptolemaicastronomy

%post -n texlive-ptolemaicastronomy
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ptolemaicastronomy 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ptolemaicastronomy
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ptolemaicastronomy-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ptolemaicastronomy/README.md
%{_texmfdistdir}/doc/latex/ptolemaicastronomy/README.txt
%{_texmfdistdir}/doc/latex/ptolemaicastronomy/ptolemaicastronomy.pdf

%files -n texlive-ptolemaicastronomy
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ptolemaicastronomy/ptolemaicastronomy.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ptolemaicastronomy-%{texlive_version}.%{texlive_noarch}.1.0svn50810-%{release}-zypper
%endif

%package -n texlive-ptptex
Version:        %{texlive_version}.%{texlive_noarch}.0.0.91svn19440
Release:        0
Summary:        Macros for 'Progress of Theoretical Physics'
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-ptptex-doc >= %{texlive_version}
Provides:       tex(ptp-prep.clo)
Provides:       tex(ptptex.cls)
Provides:       tex(wrapft.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(overcite.sty)
Requires:       tex(wrapfig.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source94:       ptptex.tar.xz
Source95:       ptptex.doc.tar.xz

%description -n texlive-ptptex
The distribution contains the class (which offers an option
file for preprints), and a template. The class requires the
cite, overcite and wrapfig packages.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-ptptex-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.91svn19440
Release:        0
Summary:        Documentation for texlive-ptptex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-ptptex-doc
This package includes the documentation for texlive-ptptex

%post -n texlive-ptptex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ptptex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ptptex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ptptex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ptptex/README
%{_texmfdistdir}/doc/latex/ptptex/README.TEXLIVE
%{_texmfdistdir}/doc/latex/ptptex/manptp.pdf
%{_texmfdistdir}/doc/latex/ptptex/manptp.tex
%{_texmfdistdir}/doc/latex/ptptex/template.tex

%files -n texlive-ptptex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ptptex/ptp-prep.clo
%{_texmfdistdir}/tex/latex/ptptex/ptptex.cls
%{_texmfdistdir}/tex/latex/ptptex/wrapft.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ptptex-%{texlive_version}.%{texlive_noarch}.0.0.91svn19440-%{release}-zypper
%endif

%package -n texlive-punk
Version:        %{texlive_version}.%{texlive_noarch}.svn27388
Release:        0
Summary:        Donald Knuth's punk font
License:        SUSE-TeX
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-punk-doc >= %{texlive_version}
Provides:       tex(punk10.tfm)
Provides:       tex(punk12.tfm)
Provides:       tex(punk20.tfm)
Provides:       tex(punkbx20.tfm)
Provides:       tex(punksl20.tfm)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source96:       punk.tar.xz
Source97:       punk.doc.tar.xz

%description -n texlive-punk
A response to the assertion in a lecture that "typography tends
to lag behind other stylistic changes by about 10 years". Knuth
felt it was (in 1988) time to design a replacement for his
designs of the 1970s, and came up with this font! The fonts are
distributed as Metafont source. The package offers LaTeX
support by Rohit Grover, from an original by Sebastian Rahtz,
which is slightly odd in claiming that the fonts are
T1-encoded. A (possibly) more rational support package is to be
found in punk-latex

date: 2016-06-24 17:18:15 +0000


%package -n texlive-punk-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn27388
Release:        0
Summary:        Documentation for texlive-punk
License:        SUSE-TeX
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-punk-doc
This package includes the documentation for texlive-punk

%post -n texlive-punk
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-punk 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-punk
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-punk-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/punk/punk.sty
%{_texmfdistdir}/doc/fonts/punk/punktest.tex

%files -n texlive-punk
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/punk/punk.mf
%{_texmfdistdir}/fonts/source/public/punk/punk10.mf
%{_texmfdistdir}/fonts/source/public/punk/punk12.mf
%{_texmfdistdir}/fonts/source/public/punk/punk20.mf
%{_texmfdistdir}/fonts/source/public/punk/punka.mf
%{_texmfdistdir}/fonts/source/public/punk/punkae.mf
%{_texmfdistdir}/fonts/source/public/punk/punkbx20.mf
%{_texmfdistdir}/fonts/source/public/punk/punkd.mf
%{_texmfdistdir}/fonts/source/public/punk/punkg.mf
%{_texmfdistdir}/fonts/source/public/punk/punkl.mf
%{_texmfdistdir}/fonts/source/public/punk/punkp.mf
%{_texmfdistdir}/fonts/source/public/punk/punksl.mf
%{_texmfdistdir}/fonts/source/public/punk/punksl20.mf
%{_texmfdistdir}/fonts/tfm/public/punk/punk10.tfm
%{_texmfdistdir}/fonts/tfm/public/punk/punk12.tfm
%{_texmfdistdir}/fonts/tfm/public/punk/punk20.tfm
%{_texmfdistdir}/fonts/tfm/public/punk/punkbx20.tfm
%{_texmfdistdir}/fonts/tfm/public/punk/punksl20.tfm
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-punk-%{texlive_version}.%{texlive_noarch}.svn27388-%{release}-zypper
%endif

%package -n texlive-punk-latex
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn27389
Release:        0
Summary:        LaTeX support for punk fonts
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-punk-latex-doc >= %{texlive_version}
Provides:       tex(ot1pnk.fd)
Provides:       tex(punk.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source98:       punk-latex.tar.xz
Source99:       punk-latex.doc.tar.xz

%description -n texlive-punk-latex
The package and .fd file provide support for Knuth's punk
fonts. That bundle also offers support within LaTeX; the
present package is to be preferred.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-punk-latex-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn27389
Release:        0
Summary:        Documentation for texlive-punk-latex
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-punk-latex-doc
This package includes the documentation for texlive-punk-latex

%post -n texlive-punk-latex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-punk-latex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-punk-latex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-punk-latex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/punk-latex/README
%{_texmfdistdir}/doc/latex/punk-latex/punk.pdf
%{_texmfdistdir}/doc/latex/punk-latex/punk.tex

%files -n texlive-punk-latex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/punk-latex/ot1pnk.fd
%{_texmfdistdir}/tex/latex/punk-latex/punk.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-punk-latex-%{texlive_version}.%{texlive_noarch}.1.1svn27389-%{release}-zypper
%endif

%package -n texlive-punknova
Version:        %{texlive_version}.%{texlive_noarch}.1.003svn24649
Release:        0
Summary:        OpenType version of Knuth's Punk font
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires:       texlive-punknova-fonts >= %{texlive_version}
Recommends:     texlive-punknova-doc >= %{texlive_version}
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source100:      punknova.tar.xz
Source101:      punknova.doc.tar.xz

%description -n texlive-punknova
The font was generated from a MetaPost version of the sources
of the 'original' punk font. Knuth's original fonts generated
different shapes at random. This isn't actually possible in an
OpenType font; rather, the font contains several variants of
each glyph, and uses the OpenType randomize function to select
a variant for each invocation.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-punknova-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.003svn24649
Release:        0
Summary:        Documentation for texlive-punknova
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-punknova-doc
This package includes the documentation for texlive-punknova


%package -n texlive-punknova-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.003svn24649
Release:        0
Summary:        Severed fonts for texlive-punknova
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
Url:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-punknova-fonts
The  separated fonts package for texlive-punknova
%post -n texlive-punknova
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-punknova 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-punknova
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-punknova-fonts
%files -n texlive-punknova-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/punknova/Makefile
%{_texmfdistdir}/doc/fonts/punknova/NEWS
%{_texmfdistdir}/doc/fonts/punknova/README
%{_texmfdistdir}/doc/fonts/punknova/documentation/documentation-sources/sample.tex
%{_texmfdistdir}/doc/fonts/punknova/documentation/sample.pdf
%{_texmfdistdir}/doc/fonts/punknova/source/punkfont-bold.mp
%{_texmfdistdir}/doc/fonts/punknova/source/punkfont-boldslanted.mp
%{_texmfdistdir}/doc/fonts/punknova/source/punkfont-regular.mp
%{_texmfdistdir}/doc/fonts/punknova/source/punkfont-slanted.mp
%{_texmfdistdir}/doc/fonts/punknova/tools/build.py

%files -n texlive-punknova
%defattr(-,root,root,755)
%verify(link) %{_texmfdistdir}/fonts/opentype/public/punknova/punknova-bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/punknova/punknova-boldslanted.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/punknova/punknova-regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/punknova/punknova-slanted.otf

%files -n texlive-punknova-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-punknova
%config %{_sysconfdir}/fonts/conf.avail/58-texlive-punknova.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-punknova/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-punknova/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-punknova/fonts.scale
%{_datadir}/fonts/texlive-punknova/punknova-bold.otf
%{_datadir}/fonts/texlive-punknova/punknova-boldslanted.otf
%{_datadir}/fonts/texlive-punknova/punknova-regular.otf
%{_datadir}/fonts/texlive-punknova/punknova-slanted.otf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-punknova-fonts-%{texlive_version}.%{texlive_noarch}.1.003svn24649-%{release}-zypper
%endif

%package -n texlive-purifyeps
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn29725
Release:        0
Summary:        Make EPS work with both LaTeX/dvips and pdfLaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive-purifyeps-bin >= %{texlive_version}
#!BuildIgnore: texlive-purifyeps-bin
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-purifyeps-doc >= %{texlive_version}
Requires:       perl(Cwd)
#!BuildIgnore:  perl(Cwd)
Requires:       perl(English)
#!BuildIgnore:  perl(English)
Requires:       perl(File::Basename)
#!BuildIgnore:  perl(File::Basename)
Requires:       perl(File::Spec)
#!BuildIgnore:  perl(File::Spec)
Requires:       perl(File::Temp)
#!BuildIgnore:  perl(File::Temp)
Requires:       perl(File::Which)
#!BuildIgnore:  perl(File::Which)
Requires:       perl(FindBin)
#!BuildIgnore:  perl(FindBin)
Requires:       perl(Getopt::Long)
#!BuildIgnore:  perl(Getopt::Long)
Requires:       perl(POSIX)
#!BuildIgnore:  perl(POSIX)
Requires:       perl(Pod::Man)
#!BuildIgnore:  perl(Pod::Man)
Requires:       perl(Pod::Usage)
#!BuildIgnore:  perl(Pod::Usage)
Requires:       perl(strict)
#!BuildIgnore:  perl(strict)
Requires:       perl(warnings)
#!BuildIgnore:  perl(warnings)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source102:      purifyeps.tar.xz
Source103:      purifyeps.doc.tar.xz

%description -n texlive-purifyeps
While pdfLaTeX has a number of nice features, its primary
shortcoming relative to standard LaTeX+dvips is that it is
unable to read ordinary Encapsulated PostScript (EPS) files,
the most common graphics format in the LaTeX world. Purifyeps
converts EPS files into a 'purified' form that can be read by
both LaTeX+dvips and pdfLaTeX. The trick is that the standard
LaTeX2e graphics packages can parse MetaPost-produced EPS
directly. Hence, purifyeps need only convert an arbitrary EPS
file into the same stylized format that MetaPost outputs.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-purifyeps-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn29725
Release:        0
Summary:        Documentation for texlive-purifyeps
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-purifyeps-doc
This package includes the documentation for texlive-purifyeps

%post -n texlive-purifyeps
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-purifyeps 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-purifyeps
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-purifyeps-doc
%defattr(-,root,root,755)
%{_mandir}/man1/purifyeps.1*
%{_texmfdistdir}/doc/support/purifyeps/README

%files -n texlive-purifyeps
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/purifyeps/purifyeps
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-purifyeps-%{texlive_version}.%{texlive_noarch}.1.1svn29725-%{release}-zypper
%endif

%package -n texlive-pxbase
Version:        %{texlive_version}.%{texlive_noarch}.1.1bsvn44756
Release:        0
Summary:        Tools for use with (u)pLaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pxbase-doc >= %{texlive_version}
Provides:       tex(pxbabel.sty)
Provides:       tex(pxbase.def)
Provides:       tex(pxbase.sty)
Provides:       tex(pxbasenc.def)
Provides:       tex(pxbsjc.def)
Provides:       tex(pxbsjc1.def)
Provides:       tex(pxjsfenc.def)
Provides:       tex(upkcat.sty)
Requires:       tex(ifptex.sty)
Requires:       tex(ifuptex.sty)
Requires:       tex(rlbabel.def)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source104:      pxbase.tar.xz
Source105:      pxbase.doc.tar.xz

%description -n texlive-pxbase
The main purpose of this package is to provide auxiliary
functions which are utilized by other packages created by the
same author. It also provides a few user commands to assist in
creating Japanese documents using (u)pLaTeX.

date: 2017-07-06 08:05:14 +0000


%package -n texlive-pxbase-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1bsvn44756
Release:        0
Summary:        Documentation for texlive-pxbase
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-pxbase-doc:ja)

%description -n texlive-pxbase-doc
This package includes the documentation for texlive-pxbase

%post -n texlive-pxbase
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pxbase 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pxbase
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pxbase-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/platex/pxbase/LICENSE
%{_texmfdistdir}/doc/platex/pxbase/README-ja.md
%{_texmfdistdir}/doc/platex/pxbase/README.md
%{_texmfdistdir}/doc/platex/pxbase/pxbabel.pdf
%{_texmfdistdir}/doc/platex/pxbase/pxbabel.tex

%files -n texlive-pxbase
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/platex/pxbase/pxbabel.sty
%{_texmfdistdir}/tex/platex/pxbase/pxbase.def
%{_texmfdistdir}/tex/platex/pxbase/pxbase.sty
%{_texmfdistdir}/tex/platex/pxbase/pxbasenc.def
%{_texmfdistdir}/tex/platex/pxbase/pxbsjc.def
%{_texmfdistdir}/tex/platex/pxbase/pxbsjc1.def
%{_texmfdistdir}/tex/platex/pxbase/pxjsfenc.def
%{_texmfdistdir}/tex/platex/pxbase/upkcat.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pxbase-%{texlive_version}.%{texlive_noarch}.1.1bsvn44756-%{release}-zypper
%endif

%package -n texlive-pxchfon
Version:        %{texlive_version}.%{texlive_noarch}.1.4asvn50556
Release:        0
Summary:        Japanese font setup for pLaTeX and upLaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pxchfon-doc >= %{texlive_version}
Provides:       tex(cfjam-r-l0j.tfm)
Provides:       tex(cfjam-r-l0j.vf)
Provides:       tex(cfjar-b-l0j.tfm)
Provides:       tex(cfjar-b-l0j.vf)
Provides:       tex(cfjar-l-l0j.tfm)
Provides:       tex(cfjar-l-l0j.vf)
Provides:       tex(cfjar-r-l0j.tfm)
Provides:       tex(cfjar-r-l0j.vf)
Provides:       tex(cfjas-b-l0j.tfm)
Provides:       tex(cfjas-b-l0j.vf)
Provides:       tex(cfjas-r-l0j.tfm)
Provides:       tex(cfjas-r-l0j.vf)
Provides:       tex(cfjas-x-l0j.tfm)
Provides:       tex(cfjas-x-l0j.vf)
Provides:       tex(pxchfon.sty)
Provides:       tex(pxchfon0.def)
Provides:       tex(pxjafont.sty)
Provides:       tex(r-cfjam-r-l0j.tfm)
Provides:       tex(r-cfjam-rz-l0j.tfm)
Provides:       tex(r-cfjar-b-l0j.tfm)
Provides:       tex(r-cfjar-bz-l0j.tfm)
Provides:       tex(r-cfjar-l-l0j.tfm)
Provides:       tex(r-cfjar-lz-l0j.tfm)
Provides:       tex(r-cfjar-r-l0j.tfm)
Provides:       tex(r-cfjar-rz-l0j.tfm)
Provides:       tex(r-cfjas-b-l0j.tfm)
Provides:       tex(r-cfjas-bz-l0j.tfm)
Provides:       tex(r-cfjas-r-l0j.tfm)
Provides:       tex(r-cfjas-rz-l0j.tfm)
Provides:       tex(r-cfjas-x-l0j.tfm)
Provides:       tex(r-cfjas-xz-l0j.tfm)
Requires:       tex(atbegshi.sty)
Requires:       tex(pxufont-ruby.sty)
Requires:       tex(pxufont.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source106:      pxchfon.tar.xz
Source107:      pxchfon.doc.tar.xz

%description -n texlive-pxchfon
This package enables users to declare in their document which
physical fonts should be used for the standard Japanese
(logical) fonts of pLaTeX and upLaTeX. Font setup is realized
by changing the font mapping of dvipdfmx, and thus users can
use any (monospaced) physical fonts they like, once they
properly install this package, without creating helper files
for each new font. This package also supports setup for the
fonts used in the japanese-otf package. System requirements:
TeX format: LaTeX. TeX engine: pTeX or upTeX. DVIware:
dvipdfmx. Prerequisite packages: atbegshi.

date: 2019-03-23 18:05:32 +0000


%package -n texlive-pxchfon-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4asvn50556
Release:        0
Summary:        Documentation for texlive-pxchfon
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-pxchfon-doc:ja)

%description -n texlive-pxchfon-doc
This package includes the documentation for texlive-pxchfon

%post -n texlive-pxchfon
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pxchfon 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pxchfon
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pxchfon-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/platex/pxchfon/LICENSE
%{_texmfdistdir}/doc/platex/pxchfon/README-ja.md
%{_texmfdistdir}/doc/platex/pxchfon/README.md
%{_texmfdistdir}/doc/platex/pxchfon/pxchfon.pdf
%{_texmfdistdir}/doc/platex/pxchfon/pxchfon.tex
%{_texmfdistdir}/doc/platex/pxchfon/sample-2000jis.pdf
%{_texmfdistdir}/doc/platex/pxchfon/sample-2000jis.tex
%{_texmfdistdir}/doc/platex/pxchfon/sample-2004jis.pdf
%{_texmfdistdir}/doc/platex/pxchfon/sample-2004jis.tex
%{_texmfdistdir}/doc/platex/pxchfon/sample-pxchfon.pdf
%{_texmfdistdir}/doc/platex/pxchfon/sample-pxchfon.tex

%files -n texlive-pxchfon
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/sfd/pxchfon/PXcjk0.sfd
%{_texmfdistdir}/fonts/tfm/public/pxchfon/cfjam-r-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/cfjar-b-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/cfjar-l-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/cfjar-r-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/cfjas-b-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/cfjas-r-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/cfjas-x-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/r-cfjam-r-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/r-cfjam-rz-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/r-cfjar-b-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/r-cfjar-bz-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/r-cfjar-l-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/r-cfjar-lz-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/r-cfjar-r-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/r-cfjar-rz-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/r-cfjas-b-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/r-cfjas-bz-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/r-cfjas-r-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/r-cfjas-rz-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/r-cfjas-x-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/r-cfjas-xz-l0j.tfm
%{_texmfdistdir}/fonts/vf/public/pxchfon/cfjam-r-l0j.vf
%{_texmfdistdir}/fonts/vf/public/pxchfon/cfjar-b-l0j.vf
%{_texmfdistdir}/fonts/vf/public/pxchfon/cfjar-l-l0j.vf
%{_texmfdistdir}/fonts/vf/public/pxchfon/cfjar-r-l0j.vf
%{_texmfdistdir}/fonts/vf/public/pxchfon/cfjas-b-l0j.vf
%{_texmfdistdir}/fonts/vf/public/pxchfon/cfjas-r-l0j.vf
%{_texmfdistdir}/fonts/vf/public/pxchfon/cfjas-x-l0j.vf
%{_texmfdistdir}/tex/platex/pxchfon/pxchfon.sty
%{_texmfdistdir}/tex/platex/pxchfon/pxchfon0.def
%{_texmfdistdir}/tex/platex/pxchfon/pxjafont.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pxchfon-%{texlive_version}.%{texlive_noarch}.1.4asvn50556-%{release}-zypper
%endif

%package -n texlive-pxcjkcat
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47266
Release:        0
Summary:        LaTeX interface for the CJK category codes of upTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pxcjkcat-doc >= %{texlive_version}
Provides:       tex(pxcjkcat.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source108:      pxcjkcat.tar.xz
Source109:      pxcjkcat.doc.tar.xz

%description -n texlive-pxcjkcat
The package provides management of the CJK category code
('kcatcode'> table of the upTeX extended TeX engine. Package
options are available for tailored use in the cases of
documents that are principally written in Japanese, or
principally written in English or other Western languages.

date: 2018-04-03 08:18:00 +0000


%package -n texlive-pxcjkcat-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47266
Release:        0
Summary:        Documentation for texlive-pxcjkcat
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-pxcjkcat-doc:ja;en)

%description -n texlive-pxcjkcat-doc
This package includes the documentation for texlive-pxcjkcat

%post -n texlive-pxcjkcat
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pxcjkcat 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pxcjkcat
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pxcjkcat-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pxcjkcat/LICENSE
%{_texmfdistdir}/doc/latex/pxcjkcat/README-ja.md
%{_texmfdistdir}/doc/latex/pxcjkcat/README.md
%{_texmfdistdir}/doc/latex/pxcjkcat/pxcjkcat.pdf
%{_texmfdistdir}/doc/latex/pxcjkcat/pxcjkcat.tex

%files -n texlive-pxcjkcat
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pxcjkcat/pxcjkcat.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pxcjkcat-%{texlive_version}.%{texlive_noarch}.1.1svn47266-%{release}-zypper
%endif

%package -n texlive-pxfonts
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Palatino-like fonts in support of mathematics
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires:       texlive-pxfonts-fonts >= %{texlive_version}
Recommends:     texlive-pxfonts-doc >= %{texlive_version}
Provides:       tex(omlpxmi.fd)
Provides:       tex(omlpxr.fd)
Provides:       tex(omspxr.fd)
Provides:       tex(omspxsy.fd)
Provides:       tex(omxpxex.fd)
Provides:       tex(ot1pxr.fd)
Provides:       tex(ot1pxss.fd)
Provides:       tex(ot1pxtt.fd)
Provides:       tex(p1xb.tfm)
Provides:       tex(p1xb.vf)
Provides:       tex(p1xbi.tfm)
Provides:       tex(p1xbi.vf)
Provides:       tex(p1xbsc.tfm)
Provides:       tex(p1xbsc.vf)
Provides:       tex(p1xbsl.tfm)
Provides:       tex(p1xbsl.vf)
Provides:       tex(p1xi.tfm)
Provides:       tex(p1xi.vf)
Provides:       tex(p1xr.tfm)
Provides:       tex(p1xr.vf)
Provides:       tex(p1xsc.tfm)
Provides:       tex(p1xsc.vf)
Provides:       tex(p1xsl.tfm)
Provides:       tex(p1xsl.vf)
Provides:       tex(pcxb.tfm)
Provides:       tex(pcxb.vf)
Provides:       tex(pcxbi.tfm)
Provides:       tex(pcxbi.vf)
Provides:       tex(pcxbsl.tfm)
Provides:       tex(pcxbsl.vf)
Provides:       tex(pcxi.tfm)
Provides:       tex(pcxi.vf)
Provides:       tex(pcxr.tfm)
Provides:       tex(pcxr.vf)
Provides:       tex(pcxsl.tfm)
Provides:       tex(pcxsl.vf)
Provides:       tex(pxb.tfm)
Provides:       tex(pxb.vf)
Provides:       tex(pxbex.tfm)
Provides:       tex(pxbexa.tfm)
Provides:       tex(pxbi.tfm)
Provides:       tex(pxbi.vf)
Provides:       tex(pxbmi.tfm)
Provides:       tex(pxbmi.vf)
Provides:       tex(pxbmi1.tfm)
Provides:       tex(pxbmi1.vf)
Provides:       tex(pxbmia.tfm)
Provides:       tex(pxbsc.tfm)
Provides:       tex(pxbsc.vf)
Provides:       tex(pxbsl.tfm)
Provides:       tex(pxbsl.vf)
Provides:       tex(pxbsy.tfm)
Provides:       tex(pxbsya.tfm)
Provides:       tex(pxbsyb.tfm)
Provides:       tex(pxbsyc.tfm)
Provides:       tex(pxex.tfm)
Provides:       tex(pxexa.tfm)
Provides:       tex(pxfonts.map)
Provides:       tex(pxfonts.sty)
Provides:       tex(pxi.tfm)
Provides:       tex(pxi.vf)
Provides:       tex(pxmi.tfm)
Provides:       tex(pxmi.vf)
Provides:       tex(pxmi1.tfm)
Provides:       tex(pxmi1.vf)
Provides:       tex(pxmia.tfm)
Provides:       tex(pxr.map)
Provides:       tex(pxr.tfm)
Provides:       tex(pxr.vf)
Provides:       tex(pxr1.map)
Provides:       tex(pxr2.map)
Provides:       tex(pxr3.map)
Provides:       tex(pxsc.tfm)
Provides:       tex(pxsc.vf)
Provides:       tex(pxsl.tfm)
Provides:       tex(pxsl.vf)
Provides:       tex(pxsy.tfm)
Provides:       tex(pxsya.tfm)
Provides:       tex(pxsyb.tfm)
Provides:       tex(pxsyc.tfm)
Provides:       tex(rpcxb.tfm)
Provides:       tex(rpcxbi.tfm)
Provides:       tex(rpcxbsl.tfm)
Provides:       tex(rpcxi.tfm)
Provides:       tex(rpcxr.tfm)
Provides:       tex(rpcxsl.tfm)
Provides:       tex(rpxb.tfm)
Provides:       tex(rpxbi.tfm)
Provides:       tex(rpxbmi.tfm)
Provides:       tex(rpxbsc.tfm)
Provides:       tex(rpxbsl.tfm)
Provides:       tex(rpxi.tfm)
Provides:       tex(rpxmi.tfm)
Provides:       tex(rpxpplb.tfm)
Provides:       tex(rpxpplbi.tfm)
Provides:       tex(rpxpplbo.tfm)
Provides:       tex(rpxpplr.tfm)
Provides:       tex(rpxpplri.tfm)
Provides:       tex(rpxpplro.tfm)
Provides:       tex(rpxr.tfm)
Provides:       tex(rpxsc.tfm)
Provides:       tex(rpxsl.tfm)
Provides:       tex(t1pxr.fd)
Provides:       tex(t1pxss.fd)
Provides:       tex(t1pxtt.fd)
Provides:       tex(ts1pxr.fd)
Provides:       tex(ts1pxss.fd)
Provides:       tex(ts1pxtt.fd)
Provides:       tex(upxexa.fd)
Provides:       tex(upxmia.fd)
Provides:       tex(upxr.fd)
Provides:       tex(upxss.fd)
Provides:       tex(upxsya.fd)
Provides:       tex(upxsyb.fd)
Provides:       tex(upxsyc.fd)
Provides:       tex(upxtt.fd)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source110:      pxfonts.tar.xz
Source111:      pxfonts.doc.tar.xz

%description -n texlive-pxfonts
Pxfonts supplies virtual text roman fonts using Adobe Palatino
(or URWPalladioL) with some modified and additional text
symbols in the OT1, T1, and TS1 encodings; maths alphabets
using Palatino/Palladio; maths fonts providing all the symbols
of the Computer Modern and AMS fonts, including all the Greek
capital letters from CMR; and additional maths fonts of various
other symbols. The set is complemented by a sans-serif set of
text fonts, based on Helvetica/NimbusSanL, and a monospace set
derived from the parallel TX font set. All the fonts are in
Type 1 format (AFM and PFB files), and are supported by TeX
metrics (VF and TFM files) and macros for use with LaTeX.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-pxfonts-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-pxfonts
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pxfonts-doc
This package includes the documentation for texlive-pxfonts


%package -n texlive-pxfonts-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Severed fonts for texlive-pxfonts
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Fonts
Url:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-pxfonts-fonts
The  separated fonts package for texlive-pxfonts
%post -n texlive-pxfonts
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap pxfonts.map' >> /var/run/texlive/run-updmap

%postun -n texlive-pxfonts 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap pxfonts.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-pxfonts
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-pxfonts-fonts
%files -n texlive-pxfonts-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/pxfonts/00bug_fix.txt
%{_texmfdistdir}/doc/fonts/pxfonts/COPYRIGHT
%{_texmfdistdir}/doc/fonts/pxfonts/pxfontsdoc.pdf
%{_texmfdistdir}/doc/fonts/pxfonts/pxfontsdoc.tex
%{_texmfdistdir}/doc/fonts/pxfonts/pxfontsdocA4.pdf
%{_texmfdistdir}/doc/fonts/pxfonts/pxfontsdocA4.tex

%files -n texlive-pxfonts
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxbex.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxbexa.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxbmia.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxbsy.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxbsya.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxbsyb.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxbsyc.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxex.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxexa.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxmia.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxsy.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxsya.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxsyb.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/pxsyc.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpcxb.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpcxbi.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpcxi.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpcxr.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpxb.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpxbi.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpxbmi.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpxbsc.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpxi.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpxmi.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpxr.afm
%{_texmfdistdir}/fonts/afm/public/pxfonts/rpxsc.afm
%{_texmfdistdir}/fonts/map/dvips/pxfonts/pxfonts.map
%{_texmfdistdir}/fonts/map/dvips/pxfonts/pxr.map
%{_texmfdistdir}/fonts/map/dvips/pxfonts/pxr1.map
%{_texmfdistdir}/fonts/map/dvips/pxfonts/pxr2.map
%{_texmfdistdir}/fonts/map/dvips/pxfonts/pxr3.map
%{_texmfdistdir}/fonts/tfm/public/pxfonts/p1xb.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/p1xbi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/p1xbsc.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/p1xbsl.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/p1xi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/p1xr.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/p1xsc.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/p1xsl.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pcxb.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pcxbi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pcxbsl.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pcxi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pcxr.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pcxsl.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxb.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbex.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbexa.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbmi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbmi1.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbmia.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbsc.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbsl.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbsy.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbsya.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbsyb.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxbsyc.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxex.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxexa.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxmi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxmi1.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxmia.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxr.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxsc.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxsl.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxsy.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxsya.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxsyb.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/pxsyc.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpcxb.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpcxbi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpcxbsl.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpcxi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpcxr.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpcxsl.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxb.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxbi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxbmi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxbsc.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxbsl.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxmi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxpplb.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxpplbi.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxpplbo.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxpplr.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxpplri.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxpplro.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxr.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxsc.tfm
%{_texmfdistdir}/fonts/tfm/public/pxfonts/rpxsl.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/pxbex.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/pxbexa.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/pxbmia.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/pxbsy.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/pxbsya.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/pxbsyb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/pxbsyc.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/pxex.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/pxexa.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/pxmia.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/pxsy.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/pxsya.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/pxsyb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/pxsyc.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/rpcxb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/rpcxbi.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/rpcxi.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/rpcxr.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/rpxb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/rpxbi.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/rpxbmi.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/rpxbsc.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/rpxi.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/rpxmi.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/rpxr.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/pxfonts/rpxsc.pfb
%{_texmfdistdir}/fonts/vf/public/pxfonts/p1xb.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/p1xbi.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/p1xbsc.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/p1xbsl.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/p1xi.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/p1xr.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/p1xsc.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/p1xsl.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pcxb.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pcxbi.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pcxbsl.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pcxi.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pcxr.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pcxsl.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxb.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxbi.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxbmi.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxbmi1.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxbsc.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxbsl.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxi.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxmi.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxmi1.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxr.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxsc.vf
%{_texmfdistdir}/fonts/vf/public/pxfonts/pxsl.vf
%{_texmfdistdir}/tex/latex/pxfonts/omlpxmi.fd
%{_texmfdistdir}/tex/latex/pxfonts/omlpxr.fd
%{_texmfdistdir}/tex/latex/pxfonts/omspxr.fd
%{_texmfdistdir}/tex/latex/pxfonts/omspxsy.fd
%{_texmfdistdir}/tex/latex/pxfonts/omxpxex.fd
%{_texmfdistdir}/tex/latex/pxfonts/ot1pxr.fd
%{_texmfdistdir}/tex/latex/pxfonts/ot1pxss.fd
%{_texmfdistdir}/tex/latex/pxfonts/ot1pxtt.fd
%{_texmfdistdir}/tex/latex/pxfonts/pxfonts.sty
%{_texmfdistdir}/tex/latex/pxfonts/t1pxr.fd
%{_texmfdistdir}/tex/latex/pxfonts/t1pxss.fd
%{_texmfdistdir}/tex/latex/pxfonts/t1pxtt.fd
%{_texmfdistdir}/tex/latex/pxfonts/ts1pxr.fd
%{_texmfdistdir}/tex/latex/pxfonts/ts1pxss.fd
%{_texmfdistdir}/tex/latex/pxfonts/ts1pxtt.fd
%{_texmfdistdir}/tex/latex/pxfonts/upxexa.fd
%{_texmfdistdir}/tex/latex/pxfonts/upxmia.fd
%{_texmfdistdir}/tex/latex/pxfonts/upxr.fd
%{_texmfdistdir}/tex/latex/pxfonts/upxss.fd
%{_texmfdistdir}/tex/latex/pxfonts/upxsya.fd
%{_texmfdistdir}/tex/latex/pxfonts/upxsyb.fd
%{_texmfdistdir}/tex/latex/pxfonts/upxsyc.fd
%{_texmfdistdir}/tex/latex/pxfonts/upxtt.fd

%files -n texlive-pxfonts-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-pxfonts
%config %{_sysconfdir}/fonts/conf.avail/58-texlive-pxfonts.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-pxfonts/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-pxfonts/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-pxfonts/fonts.scale
%{_datadir}/fonts/texlive-pxfonts/pxbex.pfb
%{_datadir}/fonts/texlive-pxfonts/pxbexa.pfb
%{_datadir}/fonts/texlive-pxfonts/pxbmia.pfb
%{_datadir}/fonts/texlive-pxfonts/pxbsy.pfb
%{_datadir}/fonts/texlive-pxfonts/pxbsya.pfb
%{_datadir}/fonts/texlive-pxfonts/pxbsyb.pfb
%{_datadir}/fonts/texlive-pxfonts/pxbsyc.pfb
%{_datadir}/fonts/texlive-pxfonts/pxex.pfb
%{_datadir}/fonts/texlive-pxfonts/pxexa.pfb
%{_datadir}/fonts/texlive-pxfonts/pxmia.pfb
%{_datadir}/fonts/texlive-pxfonts/pxsy.pfb
%{_datadir}/fonts/texlive-pxfonts/pxsya.pfb
%{_datadir}/fonts/texlive-pxfonts/pxsyb.pfb
%{_datadir}/fonts/texlive-pxfonts/pxsyc.pfb
%{_datadir}/fonts/texlive-pxfonts/rpcxb.pfb
%{_datadir}/fonts/texlive-pxfonts/rpcxbi.pfb
%{_datadir}/fonts/texlive-pxfonts/rpcxi.pfb
%{_datadir}/fonts/texlive-pxfonts/rpcxr.pfb
%{_datadir}/fonts/texlive-pxfonts/rpxb.pfb
%{_datadir}/fonts/texlive-pxfonts/rpxbi.pfb
%{_datadir}/fonts/texlive-pxfonts/rpxbmi.pfb
%{_datadir}/fonts/texlive-pxfonts/rpxbsc.pfb
%{_datadir}/fonts/texlive-pxfonts/rpxi.pfb
%{_datadir}/fonts/texlive-pxfonts/rpxmi.pfb
%{_datadir}/fonts/texlive-pxfonts/rpxr.pfb
%{_datadir}/fonts/texlive-pxfonts/rpxsc.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pxfonts-fonts-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-pxgreeks
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn21838
Release:        0
Summary:        Shape selection for PX fonts Greek letters
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pxgreeks-doc >= %{texlive_version}
Provides:       tex(pxgreeks.sty)
Requires:       tex(pxfonts.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source112:      pxgreeks.tar.xz
Source113:      pxgreeks.doc.tar.xz

%description -n texlive-pxgreeks
The package allows LaTeX maths users of the PX fonts to select
the shapes (italic or upright) for the Greek lowercase and
uppercase letters. Once the shapes for lowercase and uppercase
have been selected via a package option, the \other prefix
(e.g., \otheralpha) allows using the alternate glyph (as in the
fourier package). The pxgreeks package does not constrain the
text font that may be used in the document.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-pxgreeks-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn21838
Release:        0
Summary:        Documentation for texlive-pxgreeks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pxgreeks-doc
This package includes the documentation for texlive-pxgreeks

%post -n texlive-pxgreeks
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pxgreeks 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pxgreeks
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pxgreeks-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pxgreeks/README
%{_texmfdistdir}/doc/latex/pxgreeks/pxgreeks.pdf

%files -n texlive-pxgreeks
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pxgreeks/pxgreeks.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pxgreeks-%{texlive_version}.%{texlive_noarch}.1.0svn21838-%{release}-zypper
%endif

%package -n texlive-pxjahyper
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3dsvn48207
Release:        0
Summary:        Hyperref support for pLaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pxjahyper-doc >= %{texlive_version}
Provides:       tex(pxjahyper.sty)
Requires:       tex(atbegshi.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source114:      pxjahyper.tar.xz
Source115:      pxjahyper.doc.tar.xz

%description -n texlive-pxjahyper
This package adjusts the behavior of hyperref on (u)pLaTeX so
that authors can properly create PDF documents that contain
document information in Japanese.

date: 2018-07-15 10:53:48 +0000


%package -n texlive-pxjahyper-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3dsvn48207
Release:        0
Summary:        Documentation for texlive-pxjahyper
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-pxjahyper-doc:ja)

%description -n texlive-pxjahyper-doc
This package includes the documentation for texlive-pxjahyper

%post -n texlive-pxjahyper
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pxjahyper 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pxjahyper
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pxjahyper-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/platex/pxjahyper/LICENSE
%{_texmfdistdir}/doc/platex/pxjahyper/README-ja.md
%{_texmfdistdir}/doc/platex/pxjahyper/README.md
%{_texmfdistdir}/doc/platex/pxjahyper/pxjahyper.pdf
%{_texmfdistdir}/doc/platex/pxjahyper/pxjahyper.tex

%files -n texlive-pxjahyper
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/platex/pxjahyper/pxjahyper.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pxjahyper-%{texlive_version}.%{texlive_noarch}.0.0.3dsvn48207-%{release}-zypper
%endif

%package -n texlive-pxjodel
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2asvn50009
Release:        0
Summary:        Help change metrics of fonts from japanese-otf
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pxjodel-doc >= %{texlive_version}
Provides:       tex(pxjodel.sty)
Requires:       tex(ifuptex.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source116:      pxjodel.tar.xz
Source117:      pxjodel.doc.tar.xz

%description -n texlive-pxjodel
This package changes the setup of the japanese-otf package so
that the TFMs for direct input are all replaced by new ones
with prefixed names; for exmaple, nmlminr-h will be replaced by
foo--nmlminr-h, where foo is a prefix specified by the user.
This function will assist users who want to use the
japanese-otf package together with tailored TFMs of Japanese
fonts. The "jodel" part of the package name stands for
"japanese-otf deluxe". Here "deluxe" is the name of
japanese-otf's option for employing multi-weight Japanese font
families. This option is probably the most likely reason for
using japanese-otf. So pxjodel is really about japanese-otf's
"deluxe" option, hence the name. It is not related to yodel
singing, although some sense of word-play is intended.

date: 2019-02-17 04:29:19 +0000


%package -n texlive-pxjodel-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2asvn50009
Release:        0
Summary:        Documentation for texlive-pxjodel
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pxjodel-doc
This package includes the documentation for texlive-pxjodel

%post -n texlive-pxjodel
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pxjodel 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pxjodel
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pxjodel-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pxjodel/LICENSE
%{_texmfdistdir}/doc/latex/pxjodel/README.md
%{_texmfdistdir}/doc/latex/pxjodel/pxjodel.pdf
%{_texmfdistdir}/doc/latex/pxjodel/pxjodel.tex
%{_texmfdistdir}/doc/latex/pxjodel/tfm/jodhgothb-hq.tfm
%{_texmfdistdir}/doc/latex/pxjodel/tfm/jodhgotheb-hq.tfm
%{_texmfdistdir}/doc/latex/pxjodel/tfm/jodhgothr-hq.tfm
%{_texmfdistdir}/doc/latex/pxjodel/tfm/jodhmgothe-hq.tfm
%{_texmfdistdir}/doc/latex/pxjodel/tfm/jodhminb-hq.tfm
%{_texmfdistdir}/doc/latex/pxjodel/tfm/jodhminl-hq.tfm
%{_texmfdistdir}/doc/latex/pxjodel/tfm/jodhminr-hq.tfm
%{_texmfdistdir}/doc/latex/pxjodel/tfm/zu-jodhgothb-hq.tfm
%{_texmfdistdir}/doc/latex/pxjodel/tfm/zu-jodhgotheb-hq.tfm
%{_texmfdistdir}/doc/latex/pxjodel/tfm/zu-jodhgothr-hq.tfm
%{_texmfdistdir}/doc/latex/pxjodel/tfm/zu-jodhmgothe-hq.tfm
%{_texmfdistdir}/doc/latex/pxjodel/tfm/zu-jodhminb-hq.tfm
%{_texmfdistdir}/doc/latex/pxjodel/tfm/zu-jodhminl-hq.tfm
%{_texmfdistdir}/doc/latex/pxjodel/tfm/zu-jodhminr-hq.tfm
%{_texmfdistdir}/doc/latex/pxjodel/vf/jodhgothb-hq.vf
%{_texmfdistdir}/doc/latex/pxjodel/vf/jodhgotheb-hq.vf
%{_texmfdistdir}/doc/latex/pxjodel/vf/jodhgothr-hq.vf
%{_texmfdistdir}/doc/latex/pxjodel/vf/jodhmgothe-hq.vf
%{_texmfdistdir}/doc/latex/pxjodel/vf/jodhminb-hq.vf
%{_texmfdistdir}/doc/latex/pxjodel/vf/jodhminl-hq.vf
%{_texmfdistdir}/doc/latex/pxjodel/vf/jodhminr-hq.vf
%{_texmfdistdir}/doc/latex/pxjodel/vf/zu-jodhgothb-hq.vf
%{_texmfdistdir}/doc/latex/pxjodel/vf/zu-jodhgotheb-hq.vf
%{_texmfdistdir}/doc/latex/pxjodel/vf/zu-jodhgothr-hq.vf
%{_texmfdistdir}/doc/latex/pxjodel/vf/zu-jodhmgothe-hq.vf
%{_texmfdistdir}/doc/latex/pxjodel/vf/zu-jodhminb-hq.vf
%{_texmfdistdir}/doc/latex/pxjodel/vf/zu-jodhminl-hq.vf
%{_texmfdistdir}/doc/latex/pxjodel/vf/zu-jodhminr-hq.vf

%files -n texlive-pxjodel
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pxjodel/pxjodel.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pxjodel-%{texlive_version}.%{texlive_noarch}.0.0.2asvn50009-%{release}-zypper
%endif

%package -n texlive-pxpgfmark
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn30212
Release:        0
Summary:        E-pTeX driver for PGF inter-picture connections
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pxpgfmark-doc >= %{texlive_version}
Provides:       tex(pxpgfmark.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source118:      pxpgfmark.tar.xz
Source119:      pxpgfmark.doc.tar.xz

%description -n texlive-pxpgfmark
The distributed drivers do not support the PGF feature of
"inter-picture connections" under e-pTeX and dvipdfmx. The
package uses existing features of dvipdfmx to fix this problem

date: 2016-12-18 07:34:28 +0000


%package -n texlive-pxpgfmark-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn30212
Release:        0
Summary:        Documentation for texlive-pxpgfmark
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pxpgfmark-doc
This package includes the documentation for texlive-pxpgfmark

%post -n texlive-pxpgfmark
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pxpgfmark 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pxpgfmark
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pxpgfmark-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pxpgfmark/LICENSE
%{_texmfdistdir}/doc/latex/pxpgfmark/README

%files -n texlive-pxpgfmark
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pxpgfmark/pxpgfmark.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pxpgfmark-%{texlive_version}.%{texlive_noarch}.0.0.2svn30212-%{release}-zypper
%endif

%package -n texlive-pxrubrica
Version:        %{texlive_version}.%{texlive_noarch}.1.3csvn48421
Release:        0
Summary:        Ruby annotations according to JIS X 4051
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pxrubrica-doc >= %{texlive_version}
Provides:       tex(pxrubrica.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source120:      pxrubrica.tar.xz
Source121:      pxrubrica.doc.tar.xz

%description -n texlive-pxrubrica
This package provides a function to add ruby annotations
(furigana) that follow the style conventional in Japanese
typography as described in the W3C technical note "Requirements
for Japanese Text Layout" ([JLREQ]) and the JIS specification
JIS X 4051. Starting with version 1.3, this package also
provides a function to add kenten (emphasis marks) to Japanese
text.

date: 2018-08-16 20:17:52 +0000


%package -n texlive-pxrubrica-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3csvn48421
Release:        0
Summary:        Documentation for texlive-pxrubrica
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-pxrubrica-doc:ja;en)

%description -n texlive-pxrubrica-doc
This package includes the documentation for texlive-pxrubrica

%post -n texlive-pxrubrica
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pxrubrica 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pxrubrica
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pxrubrica-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/platex/pxrubrica/LICENSE
%{_texmfdistdir}/doc/platex/pxrubrica/README-ja.md
%{_texmfdistdir}/doc/platex/pxrubrica/README.md
%{_texmfdistdir}/doc/platex/pxrubrica/pxrubrica-en.pdf
%{_texmfdistdir}/doc/platex/pxrubrica/pxrubrica-en.tex
%{_texmfdistdir}/doc/platex/pxrubrica/pxrubrica.pdf
%{_texmfdistdir}/doc/platex/pxrubrica/sample/test-jlreq.pdf
%{_texmfdistdir}/doc/platex/pxrubrica/sample/test-jlreq.tex
%{_texmfdistdir}/doc/platex/pxrubrica/sample/test-sample.pdf
%{_texmfdistdir}/doc/platex/pxrubrica/sample/test-sample.tex
%{_texmfdistdir}/doc/platex/pxrubrica/sample/test-sf.pdf
%{_texmfdistdir}/doc/platex/pxrubrica/sample/test-sf.tex
%{_texmfdistdir}/doc/platex/pxrubrica/sample/test-toc.pdf
%{_texmfdistdir}/doc/platex/pxrubrica/sample/test-toc.tex

%files -n texlive-pxrubrica
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/platex/pxrubrica/pxrubrica.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pxrubrica-%{texlive_version}.%{texlive_noarch}.1.3csvn48421-%{release}-zypper
%endif

%package -n texlive-pxtatescale
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn43009
Release:        0
Summary:        Patch to graphics driver for scaling in vertical direction of pTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pxtatescale-doc >= %{texlive_version}
Provides:       tex(pxtatescale.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source122:      pxtatescale.tar.xz
Source123:      pxtatescale.doc.tar.xz

%description -n texlive-pxtatescale
Patch for graphics driver 'dvipdfmx' to support correct scaling
in vertical direction of Japanese pTeX/upTeX.

date: 2017-01-24 04:45:54 +0000


%package -n texlive-pxtatescale-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn43009
Release:        0
Summary:        Documentation for texlive-pxtatescale
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pxtatescale-doc
This package includes the documentation for texlive-pxtatescale

%post -n texlive-pxtatescale
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pxtatescale 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pxtatescale
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pxtatescale-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pxtatescale/LICENSE
%{_texmfdistdir}/doc/latex/pxtatescale/README

%files -n texlive-pxtatescale
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pxtatescale/pxtatescale.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pxtatescale-%{texlive_version}.%{texlive_noarch}.0.0.4svn43009-%{release}-zypper
%endif

%package -n texlive-pxtxalfa
Version:        %{texlive_version}.%{texlive_noarch}.1svn23682
Release:        0
Summary:        Virtual maths alphabets based on pxfonts and txfonts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pxtxalfa-doc >= %{texlive_version}
Provides:       tex(px-ds.sty)
Provides:       tex(pxb-ds.tfm)
Provides:       tex(pxb-ds.vf)
Provides:       tex(pxr-ds.tfm)
Provides:       tex(pxr-ds.vf)
Provides:       tex(pxtx-cal.sty)
Provides:       tex(pxtx-frak.sty)
Provides:       tex(pxtx.map)
Provides:       tex(rtxmia.tfm)
Provides:       tex(tx-of.sty)
Provides:       tex(txb-cal.tfm)
Provides:       tex(txb-cal.vf)
Provides:       tex(txb-frak.tfm)
Provides:       tex(txb-frak.vf)
Provides:       tex(txb-of.tfm)
Provides:       tex(txb-of.vf)
Provides:       tex(txr-cal.tfm)
Provides:       tex(txr-cal.vf)
Provides:       tex(txr-ds.tfm)
Provides:       tex(txr-ds.vf)
Provides:       tex(txr-frak.tfm)
Provides:       tex(txr-frak.vf)
Provides:       tex(txr-of.tfm)
Provides:       tex(txr-of.vf)
Provides:       tex(upx-ds.fd)
Provides:       tex(utx-cal.fd)
Provides:       tex(utx-frak.fd)
Provides:       tex(utx-of.fd)
Requires:       tex(cmr10.tfm)
Requires:       tex(pxbsyb.tfm)
Requires:       tex(pxsyb.tfm)
Requires:       tex(txbmia.tfm)
Requires:       tex(txbsy.tfm)
Requires:       tex(txbsyb.tfm)
Requires:       tex(txmia.tfm)
Requires:       tex(txsy.tfm)
Requires:       tex(txsyb.tfm)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source124:      pxtxalfa.tar.xz
Source125:      pxtxalfa.doc.tar.xz

%description -n texlive-pxtxalfa
The package provides virtual math alphabets based on pxfonts
and txfonts, with LaTeX support files and adjusted metrics. The
mathalfa package offers support for this collection.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-pxtxalfa-doc
Version:        %{texlive_version}.%{texlive_noarch}.1svn23682
Release:        0
Summary:        Documentation for texlive-pxtxalfa
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pxtxalfa-doc
This package includes the documentation for texlive-pxtxalfa

%post -n texlive-pxtxalfa
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap pxtx.map' >> /var/run/texlive/run-updmap

%postun -n texlive-pxtxalfa 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap pxtx.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-pxtxalfa
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pxtxalfa-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/pxtxalfa/README
%{_texmfdistdir}/doc/fonts/pxtxalfa/pxtxalfa.pdf
%{_texmfdistdir}/doc/fonts/pxtxalfa/pxtxalfa.tex

%files -n texlive-pxtxalfa
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/pxtxalfa/pxtx.map
%{_texmfdistdir}/fonts/tfm/public/pxtxalfa/pxb-ds.tfm
%{_texmfdistdir}/fonts/tfm/public/pxtxalfa/pxr-ds.tfm
%{_texmfdistdir}/fonts/tfm/public/pxtxalfa/rtxmia.tfm
%{_texmfdistdir}/fonts/tfm/public/pxtxalfa/txb-cal.tfm
%{_texmfdistdir}/fonts/tfm/public/pxtxalfa/txb-frak.tfm
%{_texmfdistdir}/fonts/tfm/public/pxtxalfa/txb-of.tfm
%{_texmfdistdir}/fonts/tfm/public/pxtxalfa/txr-cal.tfm
%{_texmfdistdir}/fonts/tfm/public/pxtxalfa/txr-ds.tfm
%{_texmfdistdir}/fonts/tfm/public/pxtxalfa/txr-frak.tfm
%{_texmfdistdir}/fonts/tfm/public/pxtxalfa/txr-of.tfm
%{_texmfdistdir}/fonts/vf/public/pxtxalfa/pxb-ds.vf
%{_texmfdistdir}/fonts/vf/public/pxtxalfa/pxr-ds.vf
%{_texmfdistdir}/fonts/vf/public/pxtxalfa/txb-cal.vf
%{_texmfdistdir}/fonts/vf/public/pxtxalfa/txb-frak.vf
%{_texmfdistdir}/fonts/vf/public/pxtxalfa/txb-of.vf
%{_texmfdistdir}/fonts/vf/public/pxtxalfa/txr-cal.vf
%{_texmfdistdir}/fonts/vf/public/pxtxalfa/txr-ds.vf
%{_texmfdistdir}/fonts/vf/public/pxtxalfa/txr-frak.vf
%{_texmfdistdir}/fonts/vf/public/pxtxalfa/txr-of.vf
%{_texmfdistdir}/tex/latex/pxtxalfa/px-ds.sty
%{_texmfdistdir}/tex/latex/pxtxalfa/pxtx-cal.sty
%{_texmfdistdir}/tex/latex/pxtxalfa/pxtx-frak.sty
%{_texmfdistdir}/tex/latex/pxtxalfa/tx-of.sty
%{_texmfdistdir}/tex/latex/pxtxalfa/upx-ds.fd
%{_texmfdistdir}/tex/latex/pxtxalfa/utx-cal.fd
%{_texmfdistdir}/tex/latex/pxtxalfa/utx-frak.fd
%{_texmfdistdir}/tex/latex/pxtxalfa/utx-of.fd
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pxtxalfa-%{texlive_version}.%{texlive_noarch}.1svn23682-%{release}-zypper
%endif

%package -n texlive-pxufont
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn50355
Release:        0
Summary:        Emulate non-Unicode Japanese fonts using Unicode fonts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pxufont-doc >= %{texlive_version}
Provides:       tex(pxufont-ruby.sty)
Provides:       tex(pxufont.sty)
Provides:       tex(zu-brsgnmlgothb-h.tfm)
Provides:       tex(zu-brsgnmlgothb-h.vf)
Provides:       tex(zu-brsgnmlgothb-v.tfm)
Provides:       tex(zu-brsgnmlgothb-v.vf)
Provides:       tex(zu-brsgnmlgothbn-h.tfm)
Provides:       tex(zu-brsgnmlgothbn-h.vf)
Provides:       tex(zu-brsgnmlgothbn-v.tfm)
Provides:       tex(zu-brsgnmlgothbn-v.vf)
Provides:       tex(zu-brsgnmlgotheb-h.tfm)
Provides:       tex(zu-brsgnmlgotheb-h.vf)
Provides:       tex(zu-brsgnmlgotheb-v.tfm)
Provides:       tex(zu-brsgnmlgotheb-v.vf)
Provides:       tex(zu-brsgnmlgothebn-h.tfm)
Provides:       tex(zu-brsgnmlgothebn-h.vf)
Provides:       tex(zu-brsgnmlgothebn-v.tfm)
Provides:       tex(zu-brsgnmlgothebn-v.vf)
Provides:       tex(zu-brsgnmlgothr-h.tfm)
Provides:       tex(zu-brsgnmlgothr-h.vf)
Provides:       tex(zu-brsgnmlgothr-v.tfm)
Provides:       tex(zu-brsgnmlgothr-v.vf)
Provides:       tex(zu-brsgnmlgothrn-h.tfm)
Provides:       tex(zu-brsgnmlgothrn-h.vf)
Provides:       tex(zu-brsgnmlgothrn-v.tfm)
Provides:       tex(zu-brsgnmlgothrn-v.vf)
Provides:       tex(zu-brsgnmlmgothr-h.tfm)
Provides:       tex(zu-brsgnmlmgothr-h.vf)
Provides:       tex(zu-brsgnmlmgothr-v.tfm)
Provides:       tex(zu-brsgnmlmgothr-v.vf)
Provides:       tex(zu-brsgnmlmgothrn-h.tfm)
Provides:       tex(zu-brsgnmlmgothrn-h.vf)
Provides:       tex(zu-brsgnmlmgothrn-v.tfm)
Provides:       tex(zu-brsgnmlmgothrn-v.vf)
Provides:       tex(zu-brsgnmlminb-h.tfm)
Provides:       tex(zu-brsgnmlminb-h.vf)
Provides:       tex(zu-brsgnmlminb-v.tfm)
Provides:       tex(zu-brsgnmlminb-v.vf)
Provides:       tex(zu-brsgnmlminbn-h.tfm)
Provides:       tex(zu-brsgnmlminbn-h.vf)
Provides:       tex(zu-brsgnmlminbn-v.tfm)
Provides:       tex(zu-brsgnmlminbn-v.vf)
Provides:       tex(zu-brsgnmlminl-h.tfm)
Provides:       tex(zu-brsgnmlminl-h.vf)
Provides:       tex(zu-brsgnmlminl-v.tfm)
Provides:       tex(zu-brsgnmlminl-v.vf)
Provides:       tex(zu-brsgnmlminln-h.tfm)
Provides:       tex(zu-brsgnmlminln-h.vf)
Provides:       tex(zu-brsgnmlminln-v.tfm)
Provides:       tex(zu-brsgnmlminln-v.vf)
Provides:       tex(zu-brsgnmlminr-h.tfm)
Provides:       tex(zu-brsgnmlminr-h.vf)
Provides:       tex(zu-brsgnmlminr-v.tfm)
Provides:       tex(zu-brsgnmlminr-v.vf)
Provides:       tex(zu-brsgnmlminrn-h.tfm)
Provides:       tex(zu-brsgnmlminrn-h.vf)
Provides:       tex(zu-brsgnmlminrn-v.tfm)
Provides:       tex(zu-brsgnmlminrn-v.vf)
Provides:       tex(zu-cidjgb0-h.tfm)
Provides:       tex(zu-cidjgb0-h.vf)
Provides:       tex(zu-cidjgb0-v.tfm)
Provides:       tex(zu-cidjgb0-v.vf)
Provides:       tex(zu-cidjgb1-h.tfm)
Provides:       tex(zu-cidjgb1-h.vf)
Provides:       tex(zu-cidjgb1-v.tfm)
Provides:       tex(zu-cidjgb1-v.vf)
Provides:       tex(zu-cidjgb2-h.tfm)
Provides:       tex(zu-cidjgb2-h.vf)
Provides:       tex(zu-cidjgb2-v.tfm)
Provides:       tex(zu-cidjgb2-v.vf)
Provides:       tex(zu-cidjgb3-h.tfm)
Provides:       tex(zu-cidjgb3-h.vf)
Provides:       tex(zu-cidjgb3-v.tfm)
Provides:       tex(zu-cidjgb3-v.vf)
Provides:       tex(zu-cidjgb4-h.tfm)
Provides:       tex(zu-cidjgb4-h.vf)
Provides:       tex(zu-cidjgb4-v.tfm)
Provides:       tex(zu-cidjgb4-v.vf)
Provides:       tex(zu-cidjgb5-h.tfm)
Provides:       tex(zu-cidjgb5-h.vf)
Provides:       tex(zu-cidjgb5-v.tfm)
Provides:       tex(zu-cidjgb5-v.vf)
Provides:       tex(zu-cidjge0-h.tfm)
Provides:       tex(zu-cidjge0-h.vf)
Provides:       tex(zu-cidjge0-v.tfm)
Provides:       tex(zu-cidjge0-v.vf)
Provides:       tex(zu-cidjge1-h.tfm)
Provides:       tex(zu-cidjge1-h.vf)
Provides:       tex(zu-cidjge1-v.tfm)
Provides:       tex(zu-cidjge1-v.vf)
Provides:       tex(zu-cidjge2-h.tfm)
Provides:       tex(zu-cidjge2-h.vf)
Provides:       tex(zu-cidjge2-v.tfm)
Provides:       tex(zu-cidjge2-v.vf)
Provides:       tex(zu-cidjge3-h.tfm)
Provides:       tex(zu-cidjge3-h.vf)
Provides:       tex(zu-cidjge3-v.tfm)
Provides:       tex(zu-cidjge3-v.vf)
Provides:       tex(zu-cidjge4-h.tfm)
Provides:       tex(zu-cidjge4-h.vf)
Provides:       tex(zu-cidjge4-v.tfm)
Provides:       tex(zu-cidjge4-v.vf)
Provides:       tex(zu-cidjge5-h.tfm)
Provides:       tex(zu-cidjge5-h.vf)
Provides:       tex(zu-cidjge5-v.tfm)
Provides:       tex(zu-cidjge5-v.vf)
Provides:       tex(zu-cidjgr0-h.tfm)
Provides:       tex(zu-cidjgr0-h.vf)
Provides:       tex(zu-cidjgr0-v.tfm)
Provides:       tex(zu-cidjgr0-v.vf)
Provides:       tex(zu-cidjgr1-h.tfm)
Provides:       tex(zu-cidjgr1-h.vf)
Provides:       tex(zu-cidjgr1-v.tfm)
Provides:       tex(zu-cidjgr1-v.vf)
Provides:       tex(zu-cidjgr2-h.tfm)
Provides:       tex(zu-cidjgr2-h.vf)
Provides:       tex(zu-cidjgr2-v.tfm)
Provides:       tex(zu-cidjgr2-v.vf)
Provides:       tex(zu-cidjgr3-h.tfm)
Provides:       tex(zu-cidjgr3-h.vf)
Provides:       tex(zu-cidjgr3-v.tfm)
Provides:       tex(zu-cidjgr3-v.vf)
Provides:       tex(zu-cidjgr4-h.tfm)
Provides:       tex(zu-cidjgr4-h.vf)
Provides:       tex(zu-cidjgr4-v.tfm)
Provides:       tex(zu-cidjgr4-v.vf)
Provides:       tex(zu-cidjgr5-h.tfm)
Provides:       tex(zu-cidjgr5-h.vf)
Provides:       tex(zu-cidjgr5-v.tfm)
Provides:       tex(zu-cidjgr5-v.vf)
Provides:       tex(zu-cidjmb0-h.tfm)
Provides:       tex(zu-cidjmb0-h.vf)
Provides:       tex(zu-cidjmb0-v.tfm)
Provides:       tex(zu-cidjmb0-v.vf)
Provides:       tex(zu-cidjmb1-h.tfm)
Provides:       tex(zu-cidjmb1-h.vf)
Provides:       tex(zu-cidjmb1-v.tfm)
Provides:       tex(zu-cidjmb1-v.vf)
Provides:       tex(zu-cidjmb2-h.tfm)
Provides:       tex(zu-cidjmb2-h.vf)
Provides:       tex(zu-cidjmb2-v.tfm)
Provides:       tex(zu-cidjmb2-v.vf)
Provides:       tex(zu-cidjmb3-h.tfm)
Provides:       tex(zu-cidjmb3-h.vf)
Provides:       tex(zu-cidjmb3-v.tfm)
Provides:       tex(zu-cidjmb3-v.vf)
Provides:       tex(zu-cidjmb4-h.tfm)
Provides:       tex(zu-cidjmb4-h.vf)
Provides:       tex(zu-cidjmb4-v.tfm)
Provides:       tex(zu-cidjmb4-v.vf)
Provides:       tex(zu-cidjmb5-h.tfm)
Provides:       tex(zu-cidjmb5-h.vf)
Provides:       tex(zu-cidjmb5-v.tfm)
Provides:       tex(zu-cidjmb5-v.vf)
Provides:       tex(zu-cidjmgr0-h.tfm)
Provides:       tex(zu-cidjmgr0-h.vf)
Provides:       tex(zu-cidjmgr0-v.tfm)
Provides:       tex(zu-cidjmgr0-v.vf)
Provides:       tex(zu-cidjmgr1-h.tfm)
Provides:       tex(zu-cidjmgr1-h.vf)
Provides:       tex(zu-cidjmgr1-v.tfm)
Provides:       tex(zu-cidjmgr1-v.vf)
Provides:       tex(zu-cidjmgr2-h.tfm)
Provides:       tex(zu-cidjmgr2-h.vf)
Provides:       tex(zu-cidjmgr2-v.tfm)
Provides:       tex(zu-cidjmgr2-v.vf)
Provides:       tex(zu-cidjmgr3-h.tfm)
Provides:       tex(zu-cidjmgr3-h.vf)
Provides:       tex(zu-cidjmgr3-v.tfm)
Provides:       tex(zu-cidjmgr3-v.vf)
Provides:       tex(zu-cidjmgr4-h.tfm)
Provides:       tex(zu-cidjmgr4-h.vf)
Provides:       tex(zu-cidjmgr4-v.tfm)
Provides:       tex(zu-cidjmgr4-v.vf)
Provides:       tex(zu-cidjmgr5-h.tfm)
Provides:       tex(zu-cidjmgr5-h.vf)
Provides:       tex(zu-cidjmgr5-v.tfm)
Provides:       tex(zu-cidjmgr5-v.vf)
Provides:       tex(zu-cidjml0-h.tfm)
Provides:       tex(zu-cidjml0-h.vf)
Provides:       tex(zu-cidjml0-v.tfm)
Provides:       tex(zu-cidjml0-v.vf)
Provides:       tex(zu-cidjml1-h.tfm)
Provides:       tex(zu-cidjml1-h.vf)
Provides:       tex(zu-cidjml1-v.tfm)
Provides:       tex(zu-cidjml1-v.vf)
Provides:       tex(zu-cidjml2-h.tfm)
Provides:       tex(zu-cidjml2-h.vf)
Provides:       tex(zu-cidjml2-v.tfm)
Provides:       tex(zu-cidjml2-v.vf)
Provides:       tex(zu-cidjml3-h.tfm)
Provides:       tex(zu-cidjml3-h.vf)
Provides:       tex(zu-cidjml3-v.tfm)
Provides:       tex(zu-cidjml3-v.vf)
Provides:       tex(zu-cidjml4-h.tfm)
Provides:       tex(zu-cidjml4-h.vf)
Provides:       tex(zu-cidjml4-v.tfm)
Provides:       tex(zu-cidjml4-v.vf)
Provides:       tex(zu-cidjml5-h.tfm)
Provides:       tex(zu-cidjml5-h.vf)
Provides:       tex(zu-cidjml5-v.tfm)
Provides:       tex(zu-cidjml5-v.vf)
Provides:       tex(zu-cidjmr0-h.tfm)
Provides:       tex(zu-cidjmr0-h.vf)
Provides:       tex(zu-cidjmr0-v.tfm)
Provides:       tex(zu-cidjmr0-v.vf)
Provides:       tex(zu-cidjmr1-h.tfm)
Provides:       tex(zu-cidjmr1-h.vf)
Provides:       tex(zu-cidjmr1-v.tfm)
Provides:       tex(zu-cidjmr1-v.vf)
Provides:       tex(zu-cidjmr2-h.tfm)
Provides:       tex(zu-cidjmr2-h.vf)
Provides:       tex(zu-cidjmr2-v.tfm)
Provides:       tex(zu-cidjmr2-v.vf)
Provides:       tex(zu-cidjmr3-h.tfm)
Provides:       tex(zu-cidjmr3-h.vf)
Provides:       tex(zu-cidjmr3-v.tfm)
Provides:       tex(zu-cidjmr3-v.vf)
Provides:       tex(zu-cidjmr4-h.tfm)
Provides:       tex(zu-cidjmr4-h.vf)
Provides:       tex(zu-cidjmr4-v.tfm)
Provides:       tex(zu-cidjmr4-v.vf)
Provides:       tex(zu-cidjmr5-h.tfm)
Provides:       tex(zu-cidjmr5-h.vf)
Provides:       tex(zu-cidjmr5-v.tfm)
Provides:       tex(zu-cidjmr5-v.vf)
Provides:       tex(zu-goth10.tfm)
Provides:       tex(zu-goth10.vf)
Provides:       tex(zu-jis-v.tfm)
Provides:       tex(zu-jis-v.vf)
Provides:       tex(zu-jis.tfm)
Provides:       tex(zu-jis.vf)
Provides:       tex(zu-jisg-v.tfm)
Provides:       tex(zu-jisg-v.vf)
Provides:       tex(zu-jisg.tfm)
Provides:       tex(zu-jisg.vf)
Provides:       tex(zu-min10.tfm)
Provides:       tex(zu-min10.vf)
Provides:       tex(zu-nmlgothb-h.tfm)
Provides:       tex(zu-nmlgothb-h.vf)
Provides:       tex(zu-nmlgothb-v.tfm)
Provides:       tex(zu-nmlgothb-v.vf)
Provides:       tex(zu-nmlgothbn-h.tfm)
Provides:       tex(zu-nmlgothbn-h.vf)
Provides:       tex(zu-nmlgothbn-v.tfm)
Provides:       tex(zu-nmlgothbn-v.vf)
Provides:       tex(zu-nmlgotheb-h.tfm)
Provides:       tex(zu-nmlgotheb-h.vf)
Provides:       tex(zu-nmlgotheb-v.tfm)
Provides:       tex(zu-nmlgotheb-v.vf)
Provides:       tex(zu-nmlgothebn-h.tfm)
Provides:       tex(zu-nmlgothebn-h.vf)
Provides:       tex(zu-nmlgothebn-v.tfm)
Provides:       tex(zu-nmlgothebn-v.vf)
Provides:       tex(zu-nmlgothr-h.tfm)
Provides:       tex(zu-nmlgothr-h.vf)
Provides:       tex(zu-nmlgothr-v.tfm)
Provides:       tex(zu-nmlgothr-v.vf)
Provides:       tex(zu-nmlgothrn-h.tfm)
Provides:       tex(zu-nmlgothrn-h.vf)
Provides:       tex(zu-nmlgothrn-v.tfm)
Provides:       tex(zu-nmlgothrn-v.vf)
Provides:       tex(zu-nmlmgothr-h.tfm)
Provides:       tex(zu-nmlmgothr-h.vf)
Provides:       tex(zu-nmlmgothr-v.tfm)
Provides:       tex(zu-nmlmgothr-v.vf)
Provides:       tex(zu-nmlmgothrn-h.tfm)
Provides:       tex(zu-nmlmgothrn-h.vf)
Provides:       tex(zu-nmlmgothrn-v.tfm)
Provides:       tex(zu-nmlmgothrn-v.vf)
Provides:       tex(zu-nmlminb-h.tfm)
Provides:       tex(zu-nmlminb-h.vf)
Provides:       tex(zu-nmlminb-v.tfm)
Provides:       tex(zu-nmlminb-v.vf)
Provides:       tex(zu-nmlminbn-h.tfm)
Provides:       tex(zu-nmlminbn-h.vf)
Provides:       tex(zu-nmlminbn-v.tfm)
Provides:       tex(zu-nmlminbn-v.vf)
Provides:       tex(zu-nmlminl-h.tfm)
Provides:       tex(zu-nmlminl-h.vf)
Provides:       tex(zu-nmlminl-v.tfm)
Provides:       tex(zu-nmlminl-v.vf)
Provides:       tex(zu-nmlminln-h.tfm)
Provides:       tex(zu-nmlminln-h.vf)
Provides:       tex(zu-nmlminln-v.tfm)
Provides:       tex(zu-nmlminln-v.vf)
Provides:       tex(zu-nmlminr-h.tfm)
Provides:       tex(zu-nmlminr-h.vf)
Provides:       tex(zu-nmlminr-v.tfm)
Provides:       tex(zu-nmlminr-v.vf)
Provides:       tex(zu-nmlminrn-h.tfm)
Provides:       tex(zu-nmlminrn-h.vf)
Provides:       tex(zu-nmlminrn-v.tfm)
Provides:       tex(zu-nmlminrn-v.vf)
Provides:       tex(zu-rubygothb-h.tfm)
Provides:       tex(zu-rubygothb-h.vf)
Provides:       tex(zu-rubygothb-v.tfm)
Provides:       tex(zu-rubygothb-v.vf)
Provides:       tex(zu-rubygotheb-h.tfm)
Provides:       tex(zu-rubygotheb-h.vf)
Provides:       tex(zu-rubygotheb-v.tfm)
Provides:       tex(zu-rubygotheb-v.vf)
Provides:       tex(zu-rubygothr-h.tfm)
Provides:       tex(zu-rubygothr-h.vf)
Provides:       tex(zu-rubygothr-v.tfm)
Provides:       tex(zu-rubygothr-v.vf)
Provides:       tex(zu-rubymgothr-h.tfm)
Provides:       tex(zu-rubymgothr-h.vf)
Provides:       tex(zu-rubymgothr-v.tfm)
Provides:       tex(zu-rubymgothr-v.vf)
Provides:       tex(zu-rubyminb-h.tfm)
Provides:       tex(zu-rubyminb-h.vf)
Provides:       tex(zu-rubyminb-v.tfm)
Provides:       tex(zu-rubyminb-v.vf)
Provides:       tex(zu-rubyminl-h.tfm)
Provides:       tex(zu-rubyminl-h.vf)
Provides:       tex(zu-rubyminl-v.tfm)
Provides:       tex(zu-rubyminl-v.vf)
Provides:       tex(zu-rubyminr-h.tfm)
Provides:       tex(zu-rubyminr-h.vf)
Provides:       tex(zu-rubyminr-v.tfm)
Provides:       tex(zu-rubyminr-v.vf)
Provides:       tex(zu-tgoth10.tfm)
Provides:       tex(zu-tgoth10.vf)
Provides:       tex(zu-tmin10.tfm)
Provides:       tex(zu-tmin10.vf)
Provides:       tex(zu-upbrsgnmlgothb-h.tfm)
Provides:       tex(zu-upbrsgnmlgothb-h.vf)
Provides:       tex(zu-upbrsgnmlgothb-v.tfm)
Provides:       tex(zu-upbrsgnmlgothb-v.vf)
Provides:       tex(zu-upbrsgnmlgothbn-h.tfm)
Provides:       tex(zu-upbrsgnmlgothbn-h.vf)
Provides:       tex(zu-upbrsgnmlgothbn-v.tfm)
Provides:       tex(zu-upbrsgnmlgothbn-v.vf)
Provides:       tex(zu-upbrsgnmlgotheb-h.tfm)
Provides:       tex(zu-upbrsgnmlgotheb-h.vf)
Provides:       tex(zu-upbrsgnmlgotheb-v.tfm)
Provides:       tex(zu-upbrsgnmlgotheb-v.vf)
Provides:       tex(zu-upbrsgnmlgothebn-h.tfm)
Provides:       tex(zu-upbrsgnmlgothebn-h.vf)
Provides:       tex(zu-upbrsgnmlgothebn-v.tfm)
Provides:       tex(zu-upbrsgnmlgothebn-v.vf)
Provides:       tex(zu-upbrsgnmlgothr-h.tfm)
Provides:       tex(zu-upbrsgnmlgothr-h.vf)
Provides:       tex(zu-upbrsgnmlgothr-v.tfm)
Provides:       tex(zu-upbrsgnmlgothr-v.vf)
Provides:       tex(zu-upbrsgnmlgothrn-h.tfm)
Provides:       tex(zu-upbrsgnmlgothrn-h.vf)
Provides:       tex(zu-upbrsgnmlgothrn-v.tfm)
Provides:       tex(zu-upbrsgnmlgothrn-v.vf)
Provides:       tex(zu-upbrsgnmlmgothr-h.tfm)
Provides:       tex(zu-upbrsgnmlmgothr-h.vf)
Provides:       tex(zu-upbrsgnmlmgothr-v.tfm)
Provides:       tex(zu-upbrsgnmlmgothr-v.vf)
Provides:       tex(zu-upbrsgnmlmgothrn-h.tfm)
Provides:       tex(zu-upbrsgnmlmgothrn-h.vf)
Provides:       tex(zu-upbrsgnmlmgothrn-v.tfm)
Provides:       tex(zu-upbrsgnmlmgothrn-v.vf)
Provides:       tex(zu-upbrsgnmlminb-h.tfm)
Provides:       tex(zu-upbrsgnmlminb-h.vf)
Provides:       tex(zu-upbrsgnmlminb-v.tfm)
Provides:       tex(zu-upbrsgnmlminb-v.vf)
Provides:       tex(zu-upbrsgnmlminbn-h.tfm)
Provides:       tex(zu-upbrsgnmlminbn-h.vf)
Provides:       tex(zu-upbrsgnmlminbn-v.tfm)
Provides:       tex(zu-upbrsgnmlminbn-v.vf)
Provides:       tex(zu-upbrsgnmlminl-h.tfm)
Provides:       tex(zu-upbrsgnmlminl-h.vf)
Provides:       tex(zu-upbrsgnmlminl-v.tfm)
Provides:       tex(zu-upbrsgnmlminl-v.vf)
Provides:       tex(zu-upbrsgnmlminln-h.tfm)
Provides:       tex(zu-upbrsgnmlminln-h.vf)
Provides:       tex(zu-upbrsgnmlminln-v.tfm)
Provides:       tex(zu-upbrsgnmlminln-v.vf)
Provides:       tex(zu-upbrsgnmlminr-h.tfm)
Provides:       tex(zu-upbrsgnmlminr-h.vf)
Provides:       tex(zu-upbrsgnmlminr-v.tfm)
Provides:       tex(zu-upbrsgnmlminr-v.vf)
Provides:       tex(zu-upbrsgnmlminrn-h.tfm)
Provides:       tex(zu-upbrsgnmlminrn-h.vf)
Provides:       tex(zu-upbrsgnmlminrn-v.tfm)
Provides:       tex(zu-upbrsgnmlminrn-v.vf)
Provides:       tex(zu-upnmlgothb-h.tfm)
Provides:       tex(zu-upnmlgothb-h.vf)
Provides:       tex(zu-upnmlgothb-v.tfm)
Provides:       tex(zu-upnmlgothb-v.vf)
Provides:       tex(zu-upnmlgothbn-h.tfm)
Provides:       tex(zu-upnmlgothbn-h.vf)
Provides:       tex(zu-upnmlgothbn-v.tfm)
Provides:       tex(zu-upnmlgothbn-v.vf)
Provides:       tex(zu-upnmlgotheb-h.tfm)
Provides:       tex(zu-upnmlgotheb-h.vf)
Provides:       tex(zu-upnmlgotheb-v.tfm)
Provides:       tex(zu-upnmlgotheb-v.vf)
Provides:       tex(zu-upnmlgothebn-h.tfm)
Provides:       tex(zu-upnmlgothebn-h.vf)
Provides:       tex(zu-upnmlgothebn-v.tfm)
Provides:       tex(zu-upnmlgothebn-v.vf)
Provides:       tex(zu-upnmlgothr-h.tfm)
Provides:       tex(zu-upnmlgothr-h.vf)
Provides:       tex(zu-upnmlgothr-v.tfm)
Provides:       tex(zu-upnmlgothr-v.vf)
Provides:       tex(zu-upnmlgothrn-h.tfm)
Provides:       tex(zu-upnmlgothrn-h.vf)
Provides:       tex(zu-upnmlgothrn-v.tfm)
Provides:       tex(zu-upnmlgothrn-v.vf)
Provides:       tex(zu-upnmlmgothr-h.tfm)
Provides:       tex(zu-upnmlmgothr-h.vf)
Provides:       tex(zu-upnmlmgothr-v.tfm)
Provides:       tex(zu-upnmlmgothr-v.vf)
Provides:       tex(zu-upnmlmgothrn-h.tfm)
Provides:       tex(zu-upnmlmgothrn-h.vf)
Provides:       tex(zu-upnmlmgothrn-v.tfm)
Provides:       tex(zu-upnmlmgothrn-v.vf)
Provides:       tex(zu-upnmlminb-h.tfm)
Provides:       tex(zu-upnmlminb-h.vf)
Provides:       tex(zu-upnmlminb-v.tfm)
Provides:       tex(zu-upnmlminb-v.vf)
Provides:       tex(zu-upnmlminbn-h.tfm)
Provides:       tex(zu-upnmlminbn-h.vf)
Provides:       tex(zu-upnmlminbn-v.tfm)
Provides:       tex(zu-upnmlminbn-v.vf)
Provides:       tex(zu-upnmlminl-h.tfm)
Provides:       tex(zu-upnmlminl-h.vf)
Provides:       tex(zu-upnmlminl-v.tfm)
Provides:       tex(zu-upnmlminl-v.vf)
Provides:       tex(zu-upnmlminln-h.tfm)
Provides:       tex(zu-upnmlminln-h.vf)
Provides:       tex(zu-upnmlminln-v.tfm)
Provides:       tex(zu-upnmlminln-v.vf)
Provides:       tex(zu-upnmlminr-h.tfm)
Provides:       tex(zu-upnmlminr-h.vf)
Provides:       tex(zu-upnmlminr-v.tfm)
Provides:       tex(zu-upnmlminr-v.vf)
Provides:       tex(zu-upnmlminrn-h.tfm)
Provides:       tex(zu-upnmlminrn-h.vf)
Provides:       tex(zu-upnmlminrn-v.tfm)
Provides:       tex(zu-upnmlminrn-v.vf)
Provides:       tex(zu-uprubygothb-h.tfm)
Provides:       tex(zu-uprubygothb-h.vf)
Provides:       tex(zu-uprubygothb-v.tfm)
Provides:       tex(zu-uprubygothb-v.vf)
Provides:       tex(zu-uprubygotheb-h.tfm)
Provides:       tex(zu-uprubygotheb-h.vf)
Provides:       tex(zu-uprubygotheb-v.tfm)
Provides:       tex(zu-uprubygotheb-v.vf)
Provides:       tex(zu-uprubygothr-h.tfm)
Provides:       tex(zu-uprubygothr-h.vf)
Provides:       tex(zu-uprubygothr-v.tfm)
Provides:       tex(zu-uprubygothr-v.vf)
Provides:       tex(zu-uprubymgothr-h.tfm)
Provides:       tex(zu-uprubymgothr-h.vf)
Provides:       tex(zu-uprubymgothr-v.tfm)
Provides:       tex(zu-uprubymgothr-v.vf)
Provides:       tex(zu-uprubyminb-h.tfm)
Provides:       tex(zu-uprubyminb-h.vf)
Provides:       tex(zu-uprubyminb-v.tfm)
Provides:       tex(zu-uprubyminb-v.vf)
Provides:       tex(zu-uprubyminl-h.tfm)
Provides:       tex(zu-uprubyminl-h.vf)
Provides:       tex(zu-uprubyminl-v.tfm)
Provides:       tex(zu-uprubyminl-v.vf)
Provides:       tex(zu-uprubyminr-h.tfm)
Provides:       tex(zu-uprubyminr-h.vf)
Provides:       tex(zu-uprubyminr-v.tfm)
Provides:       tex(zu-uprubyminr-v.vf)
Provides:       tex(zur-gjgb-h.tfm)
Provides:       tex(zur-gjgb-v.tfm)
Provides:       tex(zur-gjge-h.tfm)
Provides:       tex(zur-gjge-v.tfm)
Provides:       tex(zur-gjgr-h.tfm)
Provides:       tex(zur-gjgr-v.tfm)
Provides:       tex(zur-gjmb-h.tfm)
Provides:       tex(zur-gjmb-v.tfm)
Provides:       tex(zur-gjmgr-h.tfm)
Provides:       tex(zur-gjmgr-v.tfm)
Provides:       tex(zur-gjml-h.tfm)
Provides:       tex(zur-gjml-v.tfm)
Provides:       tex(zur-gjmr-h.tfm)
Provides:       tex(zur-gjmr-v.tfm)
Provides:       tex(zur-rjgb-h.tfm)
Provides:       tex(zur-rjgb-v.tfm)
Provides:       tex(zur-rjge-h.tfm)
Provides:       tex(zur-rjge-v.tfm)
Provides:       tex(zur-rjgr-h.tfm)
Provides:       tex(zur-rjgr-v.tfm)
Provides:       tex(zur-rjmb-h.tfm)
Provides:       tex(zur-rjmb-v.tfm)
Provides:       tex(zur-rjmgr-h.tfm)
Provides:       tex(zur-rjmgr-v.tfm)
Provides:       tex(zur-rjml-h.tfm)
Provides:       tex(zur-rjml-v.tfm)
Provides:       tex(zur-rjmr-h.tfm)
Provides:       tex(zur-rjmr-v.tfm)
Requires:       tex(ifuptex.sty)
Requires:       tex(otf-ujgb-h.tfm)
Requires:       tex(otf-ujgb-v.tfm)
Requires:       tex(otf-ujgbn-h.tfm)
Requires:       tex(otf-ujgbn-v.tfm)
Requires:       tex(otf-ujge-h.tfm)
Requires:       tex(otf-ujge-v.tfm)
Requires:       tex(otf-ujgen-h.tfm)
Requires:       tex(otf-ujgen-v.tfm)
Requires:       tex(otf-ujgr-h.tfm)
Requires:       tex(otf-ujgr-v.tfm)
Requires:       tex(otf-ujgrn-h.tfm)
Requires:       tex(otf-ujgrn-v.tfm)
Requires:       tex(otf-ujmb-h.tfm)
Requires:       tex(otf-ujmb-v.tfm)
Requires:       tex(otf-ujmbn-h.tfm)
Requires:       tex(otf-ujmbn-v.tfm)
Requires:       tex(otf-ujmgr-h.tfm)
Requires:       tex(otf-ujmgr-v.tfm)
Requires:       tex(otf-ujmgrn-h.tfm)
Requires:       tex(otf-ujmgrn-v.tfm)
Requires:       tex(otf-ujml-h.tfm)
Requires:       tex(otf-ujml-v.tfm)
Requires:       tex(otf-ujmln-h.tfm)
Requires:       tex(otf-ujmln-v.tfm)
Requires:       tex(otf-ujmr-h.tfm)
Requires:       tex(otf-ujmr-v.tfm)
Requires:       tex(otf-ujmrn-h.tfm)
Requires:       tex(otf-ujmrn-v.tfm)
Requires:       tex(upgbm-h.tfm)
Requires:       tex(upgbm-hq.tfm)
Requires:       tex(upgbm-v.tfm)
Requires:       tex(uphgothb-h.tfm)
Requires:       tex(uphgothb-v.tfm)
Requires:       tex(uphgothbn-h.tfm)
Requires:       tex(uphgothbn-v.tfm)
Requires:       tex(uphgotheb-h.tfm)
Requires:       tex(uphgotheb-v.tfm)
Requires:       tex(uphgothebn-h.tfm)
Requires:       tex(uphgothebn-v.tfm)
Requires:       tex(uphgothr-h.tfm)
Requires:       tex(uphgothr-v.tfm)
Requires:       tex(uphgothrn-h.tfm)
Requires:       tex(uphgothrn-v.tfm)
Requires:       tex(uphmgothr-h.tfm)
Requires:       tex(uphmgothr-v.tfm)
Requires:       tex(uphmgothrn-h.tfm)
Requires:       tex(uphmgothrn-v.tfm)
Requires:       tex(uphminb-h.tfm)
Requires:       tex(uphminb-v.tfm)
Requires:       tex(uphminbn-h.tfm)
Requires:       tex(uphminbn-v.tfm)
Requires:       tex(uphminl-h.tfm)
Requires:       tex(uphminl-v.tfm)
Requires:       tex(uphminln-h.tfm)
Requires:       tex(uphminln-v.tfm)
Requires:       tex(uphminr-h.tfm)
Requires:       tex(uphminr-v.tfm)
Requires:       tex(uphminrn-h.tfm)
Requires:       tex(uphminrn-v.tfm)
Requires:       tex(uprml-h.tfm)
Requires:       tex(uprml-hq.tfm)
Requires:       tex(uprml-v.tfm)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source126:      pxufont.tar.xz
Source127:      pxufont.doc.tar.xz

%description -n texlive-pxufont
The set of the Japanese logical fonts (JFMs) that are used as
standard fonts in pTeX and upTeX contains both Unicode JFMs and
non-Unicode JFMs. This bundle provides an alternative set of
non-Unicode JFMs that are tied to the virtual fonts (VFs) that
refer to the glyphs in the Unicode JFMs. Moreover it provides a
LaTeX package that redefines the NFSS settings of the Japanese
fonts of (u)pLaTeX so that the new set of non-Unicode JFMs will
be employed. As a whole, this bundle allows users to dispense
with the mapping setup on non-Unicode JFMs. Such a setup is
useful in particular when users want to use OpenType fonts
(such as Source Han Serif) that have a glyph encoding different
from Adobe-Japan1, because mapping setups from non-Unicode JFMs
to such physical fonts are difficult to prepare.

date: 2019-03-12 07:30:26 +0000


%package -n texlive-pxufont-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn50355
Release:        0
Summary:        Documentation for texlive-pxufont
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pxufont-doc
This package includes the documentation for texlive-pxufont

%post -n texlive-pxufont
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pxufont 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pxufont
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pxufont-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pxufont/LICENSE
%{_texmfdistdir}/doc/latex/pxufont/README.md

%files -n texlive-pxufont
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlgothb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlgothb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlgothbn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlgothbn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlgotheb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlgotheb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlgothebn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlgothebn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlgothr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlgothr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlgothrn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlgothrn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlmgothr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlmgothr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlmgothrn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlmgothrn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlminb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlminb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlminbn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlminbn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlminl-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlminl-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlminln-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlminln-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlminr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlminr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlminrn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-brsgnmlminrn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgb0-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgb0-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgb1-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgb1-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgb2-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgb2-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgb3-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgb3-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgb4-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgb4-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgb5-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgb5-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjge0-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjge0-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjge1-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjge1-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjge2-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjge2-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjge3-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjge3-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjge4-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjge4-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjge5-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjge5-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgr0-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgr0-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgr1-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgr1-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgr2-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgr2-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgr3-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgr3-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgr4-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgr4-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgr5-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjgr5-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmb0-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmb0-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmb1-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmb1-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmb2-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmb2-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmb3-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmb3-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmb4-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmb4-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmb5-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmb5-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmgr0-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmgr0-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmgr1-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmgr1-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmgr2-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmgr2-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmgr3-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmgr3-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmgr4-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmgr4-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmgr5-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmgr5-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjml0-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjml0-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjml1-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjml1-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjml2-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjml2-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjml3-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjml3-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjml4-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjml4-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjml5-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjml5-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmr0-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmr0-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmr1-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmr1-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmr2-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmr2-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmr3-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmr3-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmr4-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmr4-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmr5-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-cidjmr5-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-goth10.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-jis-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-jis.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-jisg-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-jisg.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-min10.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlgothb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlgothb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlgothbn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlgothbn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlgotheb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlgotheb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlgothebn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlgothebn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlgothr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlgothr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlgothrn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlgothrn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlmgothr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlmgothr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlmgothrn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlmgothrn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlminb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlminb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlminbn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlminbn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlminl-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlminl-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlminln-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlminln-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlminr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlminr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlminrn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-nmlminrn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-rubygothb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-rubygothb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-rubygotheb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-rubygotheb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-rubygothr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-rubygothr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-rubymgothr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-rubymgothr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-rubyminb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-rubyminb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-rubyminl-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-rubyminl-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-rubyminr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-rubyminr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-tgoth10.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-tmin10.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlgothb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlgothb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlgothbn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlgothbn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlgotheb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlgotheb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlgothebn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlgothebn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlgothr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlgothr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlgothrn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlgothrn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlmgothr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlmgothr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlmgothrn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlmgothrn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlminb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlminb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlminbn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlminbn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlminl-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlminl-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlminln-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlminln-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlminr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlminr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlminrn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upbrsgnmlminrn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlgothb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlgothb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlgothbn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlgothbn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlgotheb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlgotheb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlgothebn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlgothebn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlgothr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlgothr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlgothrn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlgothrn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlmgothr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlmgothr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlmgothrn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlmgothrn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlminb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlminb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlminbn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlminbn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlminl-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlminl-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlminln-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlminln-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlminr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlminr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlminrn-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-upnmlminrn-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-uprubygothb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-uprubygothb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-uprubygotheb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-uprubygotheb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-uprubygothr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-uprubygothr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-uprubymgothr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-uprubymgothr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-uprubyminb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-uprubyminb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-uprubyminl-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-uprubyminl-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-uprubyminr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zu-uprubyminr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-gjgb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-gjgb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-gjge-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-gjge-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-gjgr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-gjgr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-gjmb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-gjmb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-gjmgr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-gjmgr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-gjml-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-gjml-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-gjmr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-gjmr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-rjgb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-rjgb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-rjge-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-rjge-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-rjgr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-rjgr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-rjmb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-rjmb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-rjmgr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-rjmgr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-rjml-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-rjml-v.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-rjmr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/pxufont/zur-rjmr-v.tfm
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlgothb-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlgothb-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlgothbn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlgothbn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlgotheb-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlgotheb-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlgothebn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlgothebn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlgothr-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlgothr-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlgothrn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlgothrn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlmgothr-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlmgothr-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlmgothrn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlmgothrn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlminb-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlminb-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlminbn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlminbn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlminl-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlminl-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlminln-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlminln-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlminr-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlminr-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlminrn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-brsgnmlminrn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgb0-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgb0-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgb1-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgb1-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgb2-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgb2-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgb3-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgb3-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgb4-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgb4-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgb5-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgb5-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjge0-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjge0-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjge1-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjge1-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjge2-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjge2-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjge3-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjge3-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjge4-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjge4-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjge5-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjge5-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgr0-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgr0-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgr1-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgr1-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgr2-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgr2-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgr3-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgr3-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgr4-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgr4-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgr5-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjgr5-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmb0-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmb0-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmb1-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmb1-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmb2-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmb2-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmb3-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmb3-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmb4-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmb4-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmb5-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmb5-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmgr0-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmgr0-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmgr1-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmgr1-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmgr2-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmgr2-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmgr3-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmgr3-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmgr4-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmgr4-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmgr5-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmgr5-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjml0-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjml0-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjml1-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjml1-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjml2-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjml2-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjml3-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjml3-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjml4-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjml4-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjml5-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjml5-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmr0-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmr0-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmr1-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmr1-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmr2-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmr2-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmr3-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmr3-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmr4-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmr4-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmr5-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-cidjmr5-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-goth10.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-jis-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-jis.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-jisg-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-jisg.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-min10.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlgothb-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlgothb-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlgothbn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlgothbn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlgotheb-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlgotheb-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlgothebn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlgothebn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlgothr-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlgothr-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlgothrn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlgothrn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlmgothr-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlmgothr-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlmgothrn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlmgothrn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlminb-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlminb-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlminbn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlminbn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlminl-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlminl-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlminln-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlminln-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlminr-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlminr-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlminrn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-nmlminrn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-rubygothb-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-rubygothb-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-rubygotheb-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-rubygotheb-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-rubygothr-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-rubygothr-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-rubymgothr-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-rubymgothr-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-rubyminb-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-rubyminb-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-rubyminl-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-rubyminl-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-rubyminr-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-rubyminr-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-tgoth10.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-tmin10.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlgothb-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlgothb-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlgothbn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlgothbn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlgotheb-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlgotheb-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlgothebn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlgothebn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlgothr-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlgothr-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlgothrn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlgothrn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlmgothr-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlmgothr-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlmgothrn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlmgothrn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlminb-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlminb-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlminbn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlminbn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlminl-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlminl-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlminln-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlminln-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlminr-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlminr-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlminrn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upbrsgnmlminrn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlgothb-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlgothb-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlgothbn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlgothbn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlgotheb-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlgotheb-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlgothebn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlgothebn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlgothr-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlgothr-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlgothrn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlgothrn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlmgothr-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlmgothr-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlmgothrn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlmgothrn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlminb-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlminb-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlminbn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlminbn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlminl-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlminl-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlminln-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlminln-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlminr-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlminr-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlminrn-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-upnmlminrn-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-uprubygothb-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-uprubygothb-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-uprubygotheb-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-uprubygotheb-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-uprubygothr-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-uprubygothr-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-uprubymgothr-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-uprubymgothr-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-uprubyminb-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-uprubyminb-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-uprubyminl-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-uprubyminl-v.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-uprubyminr-h.vf
%{_texmfdistdir}/fonts/vf/public/pxufont/zu-uprubyminr-v.vf
%{_texmfdistdir}/tex/latex/pxufont/pxufont-ruby.sty
%{_texmfdistdir}/tex/latex/pxufont/pxufont.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pxufont-%{texlive_version}.%{texlive_noarch}.0.0.5svn50355-%{release}-zypper
%endif

%package -n texlive-pygmentex
Version:        %{texlive_version}.%{texlive_noarch}.0.0.8svn34996
Release:        0
Summary:        Use Pygments to format code listings in documents
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive-pygmentex-bin >= %{texlive_version}
#!BuildIgnore: texlive-pygmentex-bin
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pygmentex-doc >= %{texlive_version}
Provides:       tex(pygmentex.sty)
Requires:       tex(caption.sty)
Requires:       tex(color.sty)
Requires:       tex(efbox.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mdframed.sty)
Requires:       tex(pgfkeys.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source128:      pygmentex.tar.xz
Source129:      pygmentex.doc.tar.xz

%description -n texlive-pygmentex
PygmenTeX is a Python-based LaTeX package that can be used for
typesetting code listings in a LaTeX document using Pygments.
Pygments is a generic syntax highlighter for general use in all
kinds of software such as forum systems, wikis or other
applications that need to prettify source code.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-pygmentex-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.8svn34996
Release:        0
Summary:        Documentation for texlive-pygmentex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pygmentex-doc
This package includes the documentation for texlive-pygmentex

%post -n texlive-pygmentex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pygmentex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pygmentex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pygmentex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pygmentex/Factorial.java
%{_texmfdistdir}/doc/latex/pygmentex/README
%{_texmfdistdir}/doc/latex/pygmentex/blueshade.png
%{_texmfdistdir}/doc/latex/pygmentex/demo.c
%{_texmfdistdir}/doc/latex/pygmentex/demo.delphi
%{_texmfdistdir}/doc/latex/pygmentex/demo.hs
%{_texmfdistdir}/doc/latex/pygmentex/demo.java
%{_texmfdistdir}/doc/latex/pygmentex/demo.pas
%{_texmfdistdir}/doc/latex/pygmentex/demo.pdf
%{_texmfdistdir}/doc/latex/pygmentex/demo.py
%{_texmfdistdir}/doc/latex/pygmentex/demo.tex

%files -n texlive-pygmentex
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/pygmentex/pygmentex.py
%{_texmfdistdir}/tex/latex/pygmentex/pygmentex.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pygmentex-%{texlive_version}.%{texlive_noarch}.0.0.8svn34996-%{release}-zypper
%endif

%package -n texlive-python
Version:        %{texlive_version}.%{texlive_noarch}.0.0.21svn27064
Release:        0
Summary:        Embed Python code in LaTeX
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-python-doc >= %{texlive_version}
Provides:       tex(python.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source130:      python.tar.xz
Source131:      python.doc.tar.xz

%description -n texlive-python
The package enables you to embed Python code in LaTeX, and
insert the script's output in the document.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-python-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.21svn27064
Release:        0
Summary:        Documentation for texlive-python
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-python-doc
This package includes the documentation for texlive-python

%post -n texlive-python
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-python 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-python
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-python-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/python/README

%files -n texlive-python
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/python/python.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-python-%{texlive_version}.%{texlive_noarch}.0.0.21svn27064-%{release}-zypper
%endif

%package -n texlive-pythonhighlight
Version:        %{texlive_version}.%{texlive_noarch}.svn43191
Release:        0
Summary:        Highlighting of Python code, based on the listings package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pythonhighlight-doc >= %{texlive_version}
Provides:       tex(pythonhighlight.sty)
Requires:       tex(listings.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source132:      pythonhighlight.tar.xz
Source133:      pythonhighlight.doc.tar.xz

%description -n texlive-pythonhighlight
Highlighting of Python code, based on the listings package.

date: 2017-02-11 04:22:12 +0000


%package -n texlive-pythonhighlight-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn43191
Release:        0
Summary:        Documentation for texlive-pythonhighlight
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pythonhighlight-doc
This package includes the documentation for texlive-pythonhighlight

%post -n texlive-pythonhighlight
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pythonhighlight 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pythonhighlight
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pythonhighlight-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pythonhighlight/LICENSE.rst
%{_texmfdistdir}/doc/latex/pythonhighlight/README.md

%files -n texlive-pythonhighlight
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pythonhighlight/pythonhighlight.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pythonhighlight-%{texlive_version}.%{texlive_noarch}.svn43191-%{release}-zypper
%endif

%package -n texlive-pythontex
Version:        %{texlive_version}.%{texlive_noarch}.0.0.16svn44860
Release:        0
Summary:        Run Python from within a document, typesetting the results
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive-pythontex-bin >= %{texlive_version}
#!BuildIgnore: texlive-pythontex-bin
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-pythontex-doc >= %{texlive_version}
Provides:       tex(pythontex.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fvextra.sty)
Requires:       tex(newfloat.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source134:      pythontex.tar.xz
Source135:      pythontex.doc.tar.xz

%description -n texlive-pythontex
The package allows you to enter Python code within a LaTeX
document, execute the code, and access its output in the
original document. Python code is only executed when it has
been modified, or when it meets user-specified criteria. Code
may be divided into user-defined sessions, which automatically
run in parallel. Errors and warnings are synchronized with the
LaTeX document, so that they refer to the document's line
numbers. External dependencies can be tracked, so that code is
re-executed when the data it depends on is modified. PythonTeX
also provides syntax highlighting for code in LaTeX documents
via the Pygments syntax highlighter. The package provides a
depythontex utility, that creates a copy of the document in
which all Python code has been replaced by its output. This is
useful for journal submissions, sharing documents, and
conversion to other formats.

date: 2017-07-21 06:12:38 +0000


%package -n texlive-pythontex-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.16svn44860
Release:        0
Summary:        Documentation for texlive-pythontex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-pythontex-doc
This package includes the documentation for texlive-pythontex

%post -n texlive-pythontex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pythontex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pythontex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pythontex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pythontex/NEWS.rst
%{_texmfdistdir}/doc/latex/pythontex/README
%{_texmfdistdir}/doc/latex/pythontex/pythontex.pdf
%{_texmfdistdir}/doc/latex/pythontex/pythontex_gallery.pdf
%{_texmfdistdir}/doc/latex/pythontex/pythontex_gallery.tex
%{_texmfdistdir}/doc/latex/pythontex/pythontex_quickstart.pdf
%{_texmfdistdir}/doc/latex/pythontex/pythontex_quickstart.tex
%{_texmfdistdir}/doc/latex/pythontex/syncpdb.py

%files -n texlive-pythontex
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/pythontex/depythontex.py
%{_texmfdistdir}/scripts/pythontex/depythontex2.py
%{_texmfdistdir}/scripts/pythontex/depythontex3.py
%{_texmfdistdir}/scripts/pythontex/pythontex.py
%{_texmfdistdir}/scripts/pythontex/pythontex2.py
%{_texmfdistdir}/scripts/pythontex/pythontex3.py
%{_texmfdistdir}/scripts/pythontex/pythontex_2to3.py
%{_texmfdistdir}/scripts/pythontex/pythontex_engines.py
%{_texmfdistdir}/scripts/pythontex/pythontex_install.py
%{_texmfdistdir}/scripts/pythontex/pythontex_utils.py
%{_texmfdistdir}/tex/latex/pythontex/pythontex.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pythontex-%{texlive_version}.%{texlive_noarch}.0.0.16svn44860-%{release}-zypper
%endif

%package -n texlive-qcircuit
Version:        %{texlive_version}.%{texlive_noarch}.2.6.0svn48400
Release:        0
Summary:        Macros to generate quantum ciruits
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-qcircuit-doc >= %{texlive_version}
Provides:       tex(qcircuit.sty)
Requires:       tex(xy.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source136:      qcircuit.tar.xz
Source137:      qcircuit.doc.tar.xz

%description -n texlive-qcircuit
The package supports those within the quantum information
community who typeset quantum circuits, using xy-pic package,
offering macros designed to help users generate circuits.

date: 2018-08-14 17:25:41 +0000


%package -n texlive-qcircuit-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.6.0svn48400
Release:        0
Summary:        Documentation for texlive-qcircuit
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-qcircuit-doc
This package includes the documentation for texlive-qcircuit

%post -n texlive-qcircuit
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-qcircuit 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-qcircuit
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-qcircuit-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/qcircuit/README.md
%{_texmfdistdir}/doc/latex/qcircuit/qcircuit.pdf

%files -n texlive-qcircuit
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/qcircuit/qcircuit.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-qcircuit-%{texlive_version}.%{texlive_noarch}.2.6.0svn48400-%{release}-zypper
%endif

%package -n texlive-qcm
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn15878
Release:        0
Summary:        A LaTeX2e class for making multiple choice questionnaires
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-qcm-doc >= %{texlive_version}
Provides:       tex(qcm.cls)
Provides:       tex(qcm.sty)
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(verbatim.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source138:      qcm.tar.xz
Source139:      qcm.doc.tar.xz

%description -n texlive-qcm
QCM is a package for making multiple choices questionnaires
under LaTeX2e ("QCM" is the French acronym for this style of
test). A special environment allows you to define questions and
possible answers. You can specify which answers are correct and
which are not. QCM not only formats the questions for you, but
also generates a 'form' (a grid that your students will have to
fill in), and a 'mask' (the same grid, only with correct
answers properly checked in). You can then print the mask on a
slide and correct the questionnaires more easily by
superimposing the mask on top of students' forms. QCM can also
typeset exam corrections automatically, and comes with support
for AUC-TeX.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-qcm-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn15878
Release:        0
Summary:        Documentation for texlive-qcm
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-qcm-doc
This package includes the documentation for texlive-qcm

%post -n texlive-qcm
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-qcm 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-qcm
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-qcm-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/qcm/NEWS
%{_texmfdistdir}/doc/latex/qcm/README
%{_texmfdistdir}/doc/latex/qcm/qcm.el
%{_texmfdistdir}/doc/latex/qcm/qcm.pdf

%files -n texlive-qcm
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/qcm/qcm.cls
%{_texmfdistdir}/tex/latex/qcm/qcm.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-qcm-%{texlive_version}.%{texlive_noarch}.2.1svn15878-%{release}-zypper
%endif

%package -n texlive-qobitree
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        LaTeX macros for typesetting trees
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-qobitree-doc >= %{texlive_version}
Provides:       tex(qobitree.tex)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source140:      qobitree.tar.xz
Source141:      qobitree.doc.tar.xz

%description -n texlive-qobitree
Provides commands \branch and \leaf for specifying the elements
of the tree; you build up your tree with those commands, and
then issue the \tree command to typeset the whole.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-qobitree-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-qobitree
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-qobitree-doc
This package includes the documentation for texlive-qobitree

%post -n texlive-qobitree
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-qobitree 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-qobitree
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-qobitree-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/qobitree/README
%{_texmfdistdir}/doc/latex/qobitree/example.tex

%files -n texlive-qobitree
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/qobitree/qobitree.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-qobitree-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-qpxqtx
Version:        %{texlive_version}.%{texlive_noarch}.svn45797
Release:        0
Summary:        Polish macros and fonts supporting Pagella/pxfonts and Termes/txfonts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-qpxqtx-doc >= %{texlive_version}
Provides:       tex(amspbold.tex)
Provides:       tex(amsqpx.def)
Provides:       tex(amsqpx.tex)
Provides:       tex(amsqtx.def)
Provides:       tex(amsqtx.tex)
Provides:       tex(amstbold.tex)
Provides:       tex(qpxbmi.tfm)
Provides:       tex(qpxbmi.vf)
Provides:       tex(qpxbmia.tfm)
Provides:       tex(qpxbmia.vf)
Provides:       tex(qpxmath.sty)
Provides:       tex(qpxmath.tex)
Provides:       tex(qpxmi.tfm)
Provides:       tex(qpxmi.vf)
Provides:       tex(qpxmia.tfm)
Provides:       tex(qpxmia.vf)
Provides:       tex(qtxbmi.tfm)
Provides:       tex(qtxbmi.vf)
Provides:       tex(qtxbmia.tfm)
Provides:       tex(qtxbmia.vf)
Provides:       tex(qtxmath.sty)
Provides:       tex(qtxmath.tex)
Provides:       tex(qtxmi.tfm)
Provides:       tex(qtxmi.vf)
Provides:       tex(qtxmia.tfm)
Provides:       tex(qtxmia.vf)
Requires:       tex(pxbmia.tfm)
Requires:       tex(pxbsya.tfm)
Requires:       tex(pxmia.tfm)
Requires:       tex(pxsya.tfm)
Requires:       tex(qx-qplbi.tfm)
Requires:       tex(qx-qplri.tfm)
Requires:       tex(qx-qtmbi.tfm)
Requires:       tex(qx-qtmri.tfm)
Requires:       tex(rm-qplb.tfm)
Requires:       tex(rm-qplbi.tfm)
Requires:       tex(rm-qplr.tfm)
Requires:       tex(rm-qplri.tfm)
Requires:       tex(rm-qtmb.tfm)
Requires:       tex(rm-qtmbi.tfm)
Requires:       tex(rm-qtmr.tfm)
Requires:       tex(rm-qtmri.tfm)
Requires:       tex(rpxb.tfm)
Requires:       tex(rpxbmi.tfm)
Requires:       tex(rpxmi.tfm)
Requires:       tex(rpxr.tfm)
Requires:       tex(rtxb.tfm)
Requires:       tex(rtxbmi.tfm)
Requires:       tex(rtxmi.tfm)
Requires:       tex(rtxr.tfm)
Requires:       tex(ts1-qplb.tfm)
Requires:       tex(ts1-qplr.tfm)
Requires:       tex(ts1-qtmb.tfm)
Requires:       tex(ts1-qtmr.tfm)
Requires:       tex(txbsya.tfm)
Requires:       tex(txsya.tfm)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source142:      qpxqtx.tar.xz
Source143:      qpxqtx.doc.tar.xz

%description -n texlive-qpxqtx
The qpxqtx package

%package -n texlive-qpxqtx-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn45797
Release:        0
Summary:        Documentation for texlive-qpxqtx
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-qpxqtx-doc
This package includes the documentation for texlive-qpxqtx

%post -n texlive-qpxqtx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-qpxqtx 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-qpxqtx
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-qpxqtx-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/qpxqtx/00README
%{_texmfdistdir}/doc/fonts/qpxqtx/p01tst.tex
%{_texmfdistdir}/doc/fonts/qpxqtx/p02tst.tex
%{_texmfdistdir}/doc/fonts/qpxqtx/qpxsymb.tex
%{_texmfdistdir}/doc/fonts/qpxqtx/qpxtest.tex
%{_texmfdistdir}/doc/fonts/qpxqtx/qtxsymb.tex
%{_texmfdistdir}/doc/fonts/qpxqtx/qtxtest.tex
%{_texmfdistdir}/doc/fonts/qpxqtx/t01tst.tex
%{_texmfdistdir}/doc/fonts/qpxqtx/t02tst.tex

%files -n texlive-qpxqtx
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/tfm/public/qpxqtx/qpxbmi.tfm
%{_texmfdistdir}/fonts/tfm/public/qpxqtx/qpxbmia.tfm
%{_texmfdistdir}/fonts/tfm/public/qpxqtx/qpxmi.tfm
%{_texmfdistdir}/fonts/tfm/public/qpxqtx/qpxmia.tfm
%{_texmfdistdir}/fonts/tfm/public/qpxqtx/qtxbmi.tfm
%{_texmfdistdir}/fonts/tfm/public/qpxqtx/qtxbmia.tfm
%{_texmfdistdir}/fonts/tfm/public/qpxqtx/qtxmi.tfm
%{_texmfdistdir}/fonts/tfm/public/qpxqtx/qtxmia.tfm
%{_texmfdistdir}/fonts/vf/public/qpxqtx/qpxbmi.vf
%{_texmfdistdir}/fonts/vf/public/qpxqtx/qpxbmia.vf
%{_texmfdistdir}/fonts/vf/public/qpxqtx/qpxmi.vf
%{_texmfdistdir}/fonts/vf/public/qpxqtx/qpxmia.vf
%{_texmfdistdir}/fonts/vf/public/qpxqtx/qtxbmi.vf
%{_texmfdistdir}/fonts/vf/public/qpxqtx/qtxbmia.vf
%{_texmfdistdir}/fonts/vf/public/qpxqtx/qtxmi.vf
%{_texmfdistdir}/fonts/vf/public/qpxqtx/qtxmia.vf
%{_texmfdistdir}/tex/generic/qpxqtx/amspbold.tex
%{_texmfdistdir}/tex/generic/qpxqtx/amsqpx.def
%{_texmfdistdir}/tex/generic/qpxqtx/amsqpx.tex
%{_texmfdistdir}/tex/generic/qpxqtx/amsqtx.def
%{_texmfdistdir}/tex/generic/qpxqtx/amsqtx.tex
%{_texmfdistdir}/tex/generic/qpxqtx/amstbold.tex
%{_texmfdistdir}/tex/generic/qpxqtx/qpxmath.sty
%{_texmfdistdir}/tex/generic/qpxqtx/qpxmath.tex
%{_texmfdistdir}/tex/generic/qpxqtx/qtxmath.sty
%{_texmfdistdir}/tex/generic/qpxqtx/qtxmath.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-qpxqtx-%{texlive_version}.%{texlive_noarch}.svn45797-%{release}-zypper
%endif

%package -n texlive-qrcode
Version:        %{texlive_version}.%{texlive_noarch}.1.51svn36065
Release:        0
Summary:        Generate QR codes in LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-qrcode-doc >= %{texlive_version}
Provides:       tex(qrcode.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source144:      qrcode.tar.xz
Source145:      qrcode.doc.tar.xz

%description -n texlive-qrcode
The package generates QR (Quick Response) codes in LaTeX,
without the need for PSTricks or any other graphical package.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-qrcode-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.51svn36065
Release:        0
Summary:        Documentation for texlive-qrcode
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-qrcode-doc
This package includes the documentation for texlive-qrcode

%post -n texlive-qrcode
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-qrcode 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-qrcode
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-qrcode-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/qrcode/README
%{_texmfdistdir}/doc/latex/qrcode/qrcode.pdf

%files -n texlive-qrcode
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/qrcode/qrcode.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-qrcode-%{texlive_version}.%{texlive_noarch}.1.51svn36065-%{release}-zypper
%endif

%package -n texlive-qsharp
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3.1901.1401svn49722
Release:        0
Summary:        Syntax highlighting for the Q# language
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-qsharp-doc >= %{texlive_version}
Provides:       tex(qsharp.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source146:      qsharp.tar.xz
Source147:      qsharp.doc.tar.xz

%description -n texlive-qsharp
The package provides syntax highlighting for the Q# language, a
domain-specific language for quantum programming.

date: 2019-01-20 04:31:27 +0000


%package -n texlive-qsharp-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3.1901.1401svn49722
Release:        0
Summary:        Documentation for texlive-qsharp
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-qsharp-doc
This package includes the documentation for texlive-qsharp

%post -n texlive-qsharp
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-qsharp 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-qsharp
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-qsharp-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/qsharp/Install.ps1
%{_texmfdistdir}/doc/latex/qsharp/LICENSE
%{_texmfdistdir}/doc/latex/qsharp/README.md

%files -n texlive-qsharp
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/qsharp/qsharp.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-qsharp-%{texlive_version}.%{texlive_noarch}.0.0.3.1901.1401svn49722-%{release}-zypper
%endif

%package -n texlive-qstest
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Bundle for unit tests and pattern matching
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-qstest-doc >= %{texlive_version}
Provides:       tex(makematch.sty)
Provides:       tex(qstest.sty)
Requires:       tex(verbatim.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source148:      qstest.tar.xz
Source149:      qstest.doc.tar.xz

%description -n texlive-qstest
This is the public release of the qstest bundle (written for
DocScape Publisher) (C) 2006, 2007 QuinScape GmbH. The bundle
contains the packages 'makematch' for matching patterns to
targets (with a generalization in the form of pattern lists and
keyword lists), and 'qstest' for performing unit tests,
allowing the user to run a number of logged tests ensuring the
consistency of values, properties and call sequences during
execution of test code. Both packages make extensive use of in
their package documentation, providing illustrated examples
that are automatically verified to work as expected. Check the
README file for details.

date: 2018-01-06 11:14:59 +0000


%package -n texlive-qstest-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-qstest
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-qstest-doc
This package includes the documentation for texlive-qstest

%post -n texlive-qstest
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-qstest 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-qstest
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-qstest-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/qstest/README
%{_texmfdistdir}/doc/latex/qstest/makematch-qs.tex
%{_texmfdistdir}/doc/latex/qstest/makematch.pdf
%{_texmfdistdir}/doc/latex/qstest/qstest-qs.tex
%{_texmfdistdir}/doc/latex/qstest/qstest.pdf

%files -n texlive-qstest
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/qstest/makematch.sty
%{_texmfdistdir}/tex/latex/qstest/qstest.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-qstest-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-qsymbols
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Maths symbol abbreviations
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-qsymbols-doc >= %{texlive_version}
Provides:       tex(qsymbols.sty)
Requires:       tex(amsbsy.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(stmaryrd.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source150:      qsymbols.tar.xz
Source151:      qsymbols.doc.tar.xz

%description -n texlive-qsymbols
Provides macros for defining systematic mnemonic abbreviations,
starting with ` for math symbols and \" for arrows, using
standard symbols as well as those from the amsfonts bundle and
the stmaryrd package.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-qsymbols-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-qsymbols
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-qsymbols-doc
This package includes the documentation for texlive-qsymbols

%post -n texlive-qsymbols
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-qsymbols 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-qsymbols
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-qsymbols-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/qsymbols/CATALOG
%{_texmfdistdir}/doc/latex/qsymbols/COPYING
%{_texmfdistdir}/doc/latex/qsymbols/MANIFEST
%{_texmfdistdir}/doc/latex/qsymbols/README
%{_texmfdistdir}/doc/latex/qsymbols/qsymbols.pdf
%{_texmfdistdir}/doc/latex/qsymbols/qsymbols.tex

%files -n texlive-qsymbols
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/qsymbols/qsymbols.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-qsymbols-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-qtree
Version:        %{texlive_version}.%{texlive_noarch}.3.1bsvn15878
Release:        0
Summary:        Draw tree structures
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-qtree-doc >= %{texlive_version}
Provides:       tex(qtree.sty)
Requires:       tex(pict2e.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source152:      qtree.tar.xz
Source153:      qtree.doc.tar.xz

%description -n texlive-qtree
The package offers support for drawing tree diagrams, and is
especially suitable for linguistics use. It allows trees to be
specified in a simple bracket notation, automatically
calculates branch sizes, and supports both DVI/PostScript and
PDF output by use of pict2e facilities. The package is a
development of the existing qobitree package, offering a new
front end.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-qtree-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.1bsvn15878
Release:        0
Summary:        Documentation for texlive-qtree
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-qtree-doc:en)

%description -n texlive-qtree-doc
This package includes the documentation for texlive-qtree

%post -n texlive-qtree
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-qtree 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-qtree
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-qtree-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/qtree/README
%{_texmfdistdir}/doc/latex/qtree/qarrows.pdf
%{_texmfdistdir}/doc/latex/qtree/qarrows.tex
%{_texmfdistdir}/doc/latex/qtree/qtreenotes.pdf
%{_texmfdistdir}/doc/latex/qtree/qtreenotes.tex

%files -n texlive-qtree
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/qtree/qtree.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-qtree-%{texlive_version}.%{texlive_noarch}.3.1bsvn15878-%{release}-zypper
%endif

%package -n texlive-quantikz
Version:        %{texlive_version}.%{texlive_noarch}.0.0.9.4svn50869
Release:        0
Summary:        Draw quantum circuit diagrams
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-quantikz-doc >= %{texlive_version}
Provides:       tex(tikzlibraryquantikz.code.tex)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source154:      quantikz.tar.xz
Source155:      quantikz.doc.tar.xz

%description -n texlive-quantikz
The purpose of this package is to extend TikZ with the
functionality for drawing quantum circuit diagrams.

date: 2019-04-08 16:50:41 +0000


%package -n texlive-quantikz-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.9.4svn50869
Release:        0
Summary:        Documentation for texlive-quantikz
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-quantikz-doc
This package includes the documentation for texlive-quantikz

%post -n texlive-quantikz
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-quantikz 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-quantikz
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-quantikz-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/quantikz/README.md
%{_texmfdistdir}/doc/latex/quantikz/quantikz.pdf
%{_texmfdistdir}/doc/latex/quantikz/quantikz.tex

%files -n texlive-quantikz
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/quantikz/tikzlibraryquantikz.code.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-quantikz-%{texlive_version}.%{texlive_noarch}.0.0.9.4svn50869-%{release}-zypper
%endif

%package -n texlive-quattrocento
Version:        %{texlive_version}.%{texlive_noarch}.svn50729
Release:        0
Summary:        LaTeX support for Quattrocento and Quattrocento Sans fonts
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires:       texlive-quattrocento-fonts >= %{texlive_version}
Recommends:     texlive-quattrocento-doc >= %{texlive_version}
Provides:       tex(LY1Quattrocento-Sup.fd)
Provides:       tex(LY1Quattrocento-TLF.fd)
Provides:       tex(LY1QuattrocentoSans-Sup.fd)
Provides:       tex(LY1QuattrocentoSans-TLF.fd)
Provides:       tex(OT1Quattrocento-Sup.fd)
Provides:       tex(OT1Quattrocento-TLF.fd)
Provides:       tex(OT1QuattrocentoSans-Sup.fd)
Provides:       tex(OT1QuattrocentoSans-TLF.fd)
Provides:       tex(Quattrocento-Bold-sup-ly1--base.tfm)
Provides:       tex(Quattrocento-Bold-sup-ly1.tfm)
Provides:       tex(Quattrocento-Bold-sup-ly1.vf)
Provides:       tex(Quattrocento-Bold-sup-ot1.tfm)
Provides:       tex(Quattrocento-Bold-sup-t1--base.tfm)
Provides:       tex(Quattrocento-Bold-sup-t1.tfm)
Provides:       tex(Quattrocento-Bold-sup-t1.vf)
Provides:       tex(Quattrocento-Bold-tlf-ly1--base.tfm)
Provides:       tex(Quattrocento-Bold-tlf-ly1.tfm)
Provides:       tex(Quattrocento-Bold-tlf-ly1.vf)
Provides:       tex(Quattrocento-Bold-tlf-ot1.tfm)
Provides:       tex(Quattrocento-Bold-tlf-t1--base.tfm)
Provides:       tex(Quattrocento-Bold-tlf-t1.tfm)
Provides:       tex(Quattrocento-Bold-tlf-t1.vf)
Provides:       tex(Quattrocento-Bold-tlf-ts1--base.tfm)
Provides:       tex(Quattrocento-Bold-tlf-ts1.tfm)
Provides:       tex(Quattrocento-Bold-tlf-ts1.vf)
Provides:       tex(Quattrocento-BoldItalic-sup-ly1--base.tfm)
Provides:       tex(Quattrocento-BoldItalic-sup-ly1.tfm)
Provides:       tex(Quattrocento-BoldItalic-sup-ly1.vf)
Provides:       tex(Quattrocento-BoldItalic-sup-ot1.tfm)
Provides:       tex(Quattrocento-BoldItalic-sup-t1--base.tfm)
Provides:       tex(Quattrocento-BoldItalic-sup-t1.tfm)
Provides:       tex(Quattrocento-BoldItalic-sup-t1.vf)
Provides:       tex(Quattrocento-BoldItalic-tlf-ly1--base.tfm)
Provides:       tex(Quattrocento-BoldItalic-tlf-ly1.tfm)
Provides:       tex(Quattrocento-BoldItalic-tlf-ly1.vf)
Provides:       tex(Quattrocento-BoldItalic-tlf-ot1.tfm)
Provides:       tex(Quattrocento-BoldItalic-tlf-t1--base.tfm)
Provides:       tex(Quattrocento-BoldItalic-tlf-t1.tfm)
Provides:       tex(Quattrocento-BoldItalic-tlf-t1.vf)
Provides:       tex(Quattrocento-BoldItalic-tlf-ts1--base.tfm)
Provides:       tex(Quattrocento-BoldItalic-tlf-ts1.tfm)
Provides:       tex(Quattrocento-BoldItalic-tlf-ts1.vf)
Provides:       tex(Quattrocento-Italic-sup-ly1--base.tfm)
Provides:       tex(Quattrocento-Italic-sup-ly1.tfm)
Provides:       tex(Quattrocento-Italic-sup-ly1.vf)
Provides:       tex(Quattrocento-Italic-sup-ot1.tfm)
Provides:       tex(Quattrocento-Italic-sup-t1--base.tfm)
Provides:       tex(Quattrocento-Italic-sup-t1.tfm)
Provides:       tex(Quattrocento-Italic-sup-t1.vf)
Provides:       tex(Quattrocento-Italic-tlf-ly1--base.tfm)
Provides:       tex(Quattrocento-Italic-tlf-ly1.tfm)
Provides:       tex(Quattrocento-Italic-tlf-ly1.vf)
Provides:       tex(Quattrocento-Italic-tlf-ot1.tfm)
Provides:       tex(Quattrocento-Italic-tlf-t1--base.tfm)
Provides:       tex(Quattrocento-Italic-tlf-t1.tfm)
Provides:       tex(Quattrocento-Italic-tlf-t1.vf)
Provides:       tex(Quattrocento-Italic-tlf-ts1--base.tfm)
Provides:       tex(Quattrocento-Italic-tlf-ts1.tfm)
Provides:       tex(Quattrocento-Italic-tlf-ts1.vf)
Provides:       tex(Quattrocento-sup-ly1--base.tfm)
Provides:       tex(Quattrocento-sup-ly1.tfm)
Provides:       tex(Quattrocento-sup-ly1.vf)
Provides:       tex(Quattrocento-sup-ot1.tfm)
Provides:       tex(Quattrocento-sup-t1--base.tfm)
Provides:       tex(Quattrocento-sup-t1.tfm)
Provides:       tex(Quattrocento-sup-t1.vf)
Provides:       tex(Quattrocento-tlf-ly1--base.tfm)
Provides:       tex(Quattrocento-tlf-ly1.tfm)
Provides:       tex(Quattrocento-tlf-ly1.vf)
Provides:       tex(Quattrocento-tlf-ot1.tfm)
Provides:       tex(Quattrocento-tlf-t1--base.tfm)
Provides:       tex(Quattrocento-tlf-t1.tfm)
Provides:       tex(Quattrocento-tlf-t1.vf)
Provides:       tex(Quattrocento-tlf-ts1--base.tfm)
Provides:       tex(Quattrocento-tlf-ts1.tfm)
Provides:       tex(Quattrocento-tlf-ts1.vf)
Provides:       tex(QuattrocentoSans-Bold-sup-ly1--base.tfm)
Provides:       tex(QuattrocentoSans-Bold-sup-ly1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-Bold-sup-ly1.tfm)
Provides:       tex(QuattrocentoSans-Bold-sup-ly1.vf)
Provides:       tex(QuattrocentoSans-Bold-sup-ot1--base.tfm)
Provides:       tex(QuattrocentoSans-Bold-sup-ot1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-Bold-sup-ot1.tfm)
Provides:       tex(QuattrocentoSans-Bold-sup-ot1.vf)
Provides:       tex(QuattrocentoSans-Bold-sup-t1--base.tfm)
Provides:       tex(QuattrocentoSans-Bold-sup-t1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-Bold-sup-t1.tfm)
Provides:       tex(QuattrocentoSans-Bold-sup-t1.vf)
Provides:       tex(QuattrocentoSans-Bold-tlf-ly1--base.tfm)
Provides:       tex(QuattrocentoSans-Bold-tlf-ly1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-Bold-tlf-ly1.tfm)
Provides:       tex(QuattrocentoSans-Bold-tlf-ly1.vf)
Provides:       tex(QuattrocentoSans-Bold-tlf-ot1--base.tfm)
Provides:       tex(QuattrocentoSans-Bold-tlf-ot1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-Bold-tlf-ot1.tfm)
Provides:       tex(QuattrocentoSans-Bold-tlf-ot1.vf)
Provides:       tex(QuattrocentoSans-Bold-tlf-t1--base.tfm)
Provides:       tex(QuattrocentoSans-Bold-tlf-t1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-Bold-tlf-t1.tfm)
Provides:       tex(QuattrocentoSans-Bold-tlf-t1.vf)
Provides:       tex(QuattrocentoSans-Bold-tlf-ts1--base.tfm)
Provides:       tex(QuattrocentoSans-Bold-tlf-ts1.tfm)
Provides:       tex(QuattrocentoSans-Bold-tlf-ts1.vf)
Provides:       tex(QuattrocentoSans-BoldItalic-sup-ly1--base.tfm)
Provides:       tex(QuattrocentoSans-BoldItalic-sup-ly1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-BoldItalic-sup-ly1.tfm)
Provides:       tex(QuattrocentoSans-BoldItalic-sup-ly1.vf)
Provides:       tex(QuattrocentoSans-BoldItalic-sup-ot1--base.tfm)
Provides:       tex(QuattrocentoSans-BoldItalic-sup-ot1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-BoldItalic-sup-ot1.tfm)
Provides:       tex(QuattrocentoSans-BoldItalic-sup-ot1.vf)
Provides:       tex(QuattrocentoSans-BoldItalic-sup-t1--base.tfm)
Provides:       tex(QuattrocentoSans-BoldItalic-sup-t1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-BoldItalic-sup-t1.tfm)
Provides:       tex(QuattrocentoSans-BoldItalic-sup-t1.vf)
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-ly1--base.tfm)
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-ly1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-ly1.tfm)
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-ly1.vf)
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-ot1--base.tfm)
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-ot1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-ot1.tfm)
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-ot1.vf)
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-t1--base.tfm)
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-t1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-t1.tfm)
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-t1.vf)
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-ts1--base.tfm)
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-ts1.tfm)
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-ts1.vf)
Provides:       tex(QuattrocentoSans-Italic-sup-ly1--base.tfm)
Provides:       tex(QuattrocentoSans-Italic-sup-ly1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-Italic-sup-ly1.tfm)
Provides:       tex(QuattrocentoSans-Italic-sup-ly1.vf)
Provides:       tex(QuattrocentoSans-Italic-sup-ot1--base.tfm)
Provides:       tex(QuattrocentoSans-Italic-sup-ot1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-Italic-sup-ot1.tfm)
Provides:       tex(QuattrocentoSans-Italic-sup-ot1.vf)
Provides:       tex(QuattrocentoSans-Italic-sup-t1--base.tfm)
Provides:       tex(QuattrocentoSans-Italic-sup-t1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-Italic-sup-t1.tfm)
Provides:       tex(QuattrocentoSans-Italic-sup-t1.vf)
Provides:       tex(QuattrocentoSans-Italic-tlf-ly1--base.tfm)
Provides:       tex(QuattrocentoSans-Italic-tlf-ly1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-Italic-tlf-ly1.tfm)
Provides:       tex(QuattrocentoSans-Italic-tlf-ly1.vf)
Provides:       tex(QuattrocentoSans-Italic-tlf-ot1--base.tfm)
Provides:       tex(QuattrocentoSans-Italic-tlf-ot1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-Italic-tlf-ot1.tfm)
Provides:       tex(QuattrocentoSans-Italic-tlf-ot1.vf)
Provides:       tex(QuattrocentoSans-Italic-tlf-t1--base.tfm)
Provides:       tex(QuattrocentoSans-Italic-tlf-t1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-Italic-tlf-t1.tfm)
Provides:       tex(QuattrocentoSans-Italic-tlf-t1.vf)
Provides:       tex(QuattrocentoSans-Italic-tlf-ts1--base.tfm)
Provides:       tex(QuattrocentoSans-Italic-tlf-ts1.tfm)
Provides:       tex(QuattrocentoSans-Italic-tlf-ts1.vf)
Provides:       tex(QuattrocentoSans-sup-ly1--base.tfm)
Provides:       tex(QuattrocentoSans-sup-ly1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-sup-ly1.tfm)
Provides:       tex(QuattrocentoSans-sup-ly1.vf)
Provides:       tex(QuattrocentoSans-sup-ot1--base.tfm)
Provides:       tex(QuattrocentoSans-sup-ot1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-sup-ot1.tfm)
Provides:       tex(QuattrocentoSans-sup-ot1.vf)
Provides:       tex(QuattrocentoSans-sup-t1--base.tfm)
Provides:       tex(QuattrocentoSans-sup-t1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-sup-t1.tfm)
Provides:       tex(QuattrocentoSans-sup-t1.vf)
Provides:       tex(QuattrocentoSans-tlf-ly1--base.tfm)
Provides:       tex(QuattrocentoSans-tlf-ly1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-tlf-ly1.tfm)
Provides:       tex(QuattrocentoSans-tlf-ly1.vf)
Provides:       tex(QuattrocentoSans-tlf-ot1--base.tfm)
Provides:       tex(QuattrocentoSans-tlf-ot1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-tlf-ot1.tfm)
Provides:       tex(QuattrocentoSans-tlf-ot1.vf)
Provides:       tex(QuattrocentoSans-tlf-t1--base.tfm)
Provides:       tex(QuattrocentoSans-tlf-t1--lcdfj.tfm)
Provides:       tex(QuattrocentoSans-tlf-t1.tfm)
Provides:       tex(QuattrocentoSans-tlf-t1.vf)
Provides:       tex(QuattrocentoSans-tlf-ts1--base.tfm)
Provides:       tex(QuattrocentoSans-tlf-ts1.tfm)
Provides:       tex(QuattrocentoSans-tlf-ts1.vf)
Provides:       tex(T1Quattrocento-Sup.fd)
Provides:       tex(T1Quattrocento-TLF.fd)
Provides:       tex(T1QuattrocentoSans-Sup.fd)
Provides:       tex(T1QuattrocentoSans-TLF.fd)
Provides:       tex(TS1Quattrocento-TLF.fd)
Provides:       tex(TS1QuattrocentoSans-TLF.fd)
Provides:       tex(qtrcnt_3fwis5.enc)
Provides:       tex(qtrcnt_464xel.enc)
Provides:       tex(qtrcnt_5tsqgq.enc)
Provides:       tex(qtrcnt_6abmaa.enc)
Provides:       tex(qtrcnt_765rgb.enc)
Provides:       tex(qtrcnt_biaxdc.enc)
Provides:       tex(qtrcnt_cpzb4n.enc)
Provides:       tex(qtrcnt_dn5k7b.enc)
Provides:       tex(qtrcnt_dw2g3h.enc)
Provides:       tex(qtrcnt_ezrk6a.enc)
Provides:       tex(qtrcnt_h2bn35.enc)
Provides:       tex(qtrcnt_iyhp72.enc)
Provides:       tex(qtrcnt_jqoy2i.enc)
Provides:       tex(qtrcnt_lk3wmz.enc)
Provides:       tex(qtrcnt_mamppr.enc)
Provides:       tex(qtrcnt_n36lnh.enc)
Provides:       tex(qtrcnt_nfidqf.enc)
Provides:       tex(qtrcnt_slhr5d.enc)
Provides:       tex(qtrcnt_szwdgc.enc)
Provides:       tex(qtrcnt_tixcdz.enc)
Provides:       tex(qtrcnt_vzn2dc.enc)
Provides:       tex(qtrcnt_wczi5x.enc)
Provides:       tex(qtrcnt_wpi2yi.enc)
Provides:       tex(qtrcnt_xvywtm.enc)
Provides:       tex(qtrcnt_xzkr3s.enc)
Provides:       tex(qtrcnt_y54nu7.enc)
Provides:       tex(quattrocento.map)
Provides:       tex(quattrocento.sty)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source156:      quattrocento.tar.xz
Source157:      quattrocento.doc.tar.xz

%description -n texlive-quattrocento
The package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Quattrocento and Quattrocento Sans families of
fonts, designed by Pablo Impallari; the fonts themselves are
also provided, in both Type 1 and OpenType format. Quattrocento
is a classic typeface with wide and open letterforms, and great
x-height, which makes it very legible for body text at small
sizes. Tiny details that only show up at bigger sizes make it
also great for display use. Quattrocento Sans is the perfect
sans-serif companion for Quattrocento.

date: 2019-04-03 16:45:52 +0000


%package -n texlive-quattrocento-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn50729
Release:        0
Summary:        Documentation for texlive-quattrocento
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-quattrocento-doc
This package includes the documentation for texlive-quattrocento


%package -n texlive-quattrocento-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn50729
Release:        0
Summary:        Severed fonts for texlive-quattrocento
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
Url:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-quattrocento-fonts
The  separated fonts package for texlive-quattrocento
%post -n texlive-quattrocento
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap quattrocento.map' >> /var/run/texlive/run-updmap

%postun -n texlive-quattrocento 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap quattrocento.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-quattrocento
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-quattrocento-fonts
%files -n texlive-quattrocento-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/quattrocento/OFL.txt
%{_texmfdistdir}/doc/fonts/quattrocento/README
%{_texmfdistdir}/doc/fonts/quattrocento/quattrocento-samples.pdf
%{_texmfdistdir}/doc/fonts/quattrocento/quattrocento-samples.tex

%files -n texlive-quattrocento
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_3fwis5.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_464xel.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_5tsqgq.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_6abmaa.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_765rgb.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_biaxdc.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_cpzb4n.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_dn5k7b.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_dw2g3h.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_ezrk6a.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_h2bn35.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_iyhp72.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_jqoy2i.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_lk3wmz.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_mamppr.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_n36lnh.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_nfidqf.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_slhr5d.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_szwdgc.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_tixcdz.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_vzn2dc.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_wczi5x.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_wpi2yi.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_xvywtm.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_xzkr3s.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_y54nu7.enc
%{_texmfdistdir}/fonts/map/dvips/quattrocento/quattrocento.map
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/quattrocento/Quattrocento-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/quattrocento/Quattrocento-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/quattrocento/Quattrocento-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/quattrocento/Quattrocento.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/quattrocento/QuattrocentoSans-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/quattrocento/QuattrocentoSans-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/quattrocento/QuattrocentoSans-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/quattrocento/QuattrocentoSans.otf
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Italic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Italic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Italic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Italic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Italic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-sup-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-sup-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-sup-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-sup-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-tlf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-tlf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-tlf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-tlf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-sup-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-sup-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-sup-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-sup-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-tlf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-tlf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-tlf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-tlf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-sup-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-sup-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-sup-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-sup-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-tlf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-tlf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-tlf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-tlf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-tlf-ts1.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/quattrocento/Quattrocento-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/quattrocento/Quattrocento-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/quattrocento/Quattrocento-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/quattrocento/Quattrocento.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/quattrocento/QuattrocentoSans-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/quattrocento/QuattrocentoSans-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/quattrocento/QuattrocentoSans-BoldItalicLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/quattrocento/QuattrocentoSans-BoldLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/quattrocento/QuattrocentoSans-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/quattrocento/QuattrocentoSans-ItalicLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/quattrocento/QuattrocentoSans.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/quattrocento/QuattrocentoSansLCDFJ.pfb
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-Bold-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-Bold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-BoldItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-BoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-Italic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-Italic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Bold-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Bold-sup-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Bold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Bold-tlf-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Italic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Italic-sup-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Italic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Italic-tlf-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-sup-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-tlf-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-tlf-ts1.vf
%{_texmfdistdir}/tex/latex/quattrocento/LY1Quattrocento-Sup.fd
%{_texmfdistdir}/tex/latex/quattrocento/LY1Quattrocento-TLF.fd
%{_texmfdistdir}/tex/latex/quattrocento/LY1QuattrocentoSans-Sup.fd
%{_texmfdistdir}/tex/latex/quattrocento/LY1QuattrocentoSans-TLF.fd
%{_texmfdistdir}/tex/latex/quattrocento/OT1Quattrocento-Sup.fd
%{_texmfdistdir}/tex/latex/quattrocento/OT1Quattrocento-TLF.fd
%{_texmfdistdir}/tex/latex/quattrocento/OT1QuattrocentoSans-Sup.fd
%{_texmfdistdir}/tex/latex/quattrocento/OT1QuattrocentoSans-TLF.fd
%{_texmfdistdir}/tex/latex/quattrocento/T1Quattrocento-Sup.fd
%{_texmfdistdir}/tex/latex/quattrocento/T1Quattrocento-TLF.fd
%{_texmfdistdir}/tex/latex/quattrocento/T1QuattrocentoSans-Sup.fd
%{_texmfdistdir}/tex/latex/quattrocento/T1QuattrocentoSans-TLF.fd
%{_texmfdistdir}/tex/latex/quattrocento/TS1Quattrocento-TLF.fd
%{_texmfdistdir}/tex/latex/quattrocento/TS1QuattrocentoSans-TLF.fd
%{_texmfdistdir}/tex/latex/quattrocento/quattrocento.sty

%files -n texlive-quattrocento-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-quattrocento
%config %{_sysconfdir}/fonts/conf.avail/58-texlive-quattrocento.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-quattrocento.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-quattrocento/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-quattrocento/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-quattrocento/fonts.scale
%{_datadir}/fonts/texlive-quattrocento/Quattrocento-Bold.otf
%{_datadir}/fonts/texlive-quattrocento/Quattrocento-BoldItalic.otf
%{_datadir}/fonts/texlive-quattrocento/Quattrocento-Italic.otf
%{_datadir}/fonts/texlive-quattrocento/Quattrocento.otf
%{_datadir}/fonts/texlive-quattrocento/QuattrocentoSans-Bold.otf
%{_datadir}/fonts/texlive-quattrocento/QuattrocentoSans-BoldItalic.otf
%{_datadir}/fonts/texlive-quattrocento/QuattrocentoSans-Italic.otf
%{_datadir}/fonts/texlive-quattrocento/QuattrocentoSans.otf
%{_datadir}/fonts/texlive-quattrocento/Quattrocento-Bold.pfb
%{_datadir}/fonts/texlive-quattrocento/Quattrocento-BoldItalic.pfb
%{_datadir}/fonts/texlive-quattrocento/Quattrocento-Italic.pfb
%{_datadir}/fonts/texlive-quattrocento/Quattrocento.pfb
%{_datadir}/fonts/texlive-quattrocento/QuattrocentoSans-Bold.pfb
%{_datadir}/fonts/texlive-quattrocento/QuattrocentoSans-BoldItalic.pfb
%{_datadir}/fonts/texlive-quattrocento/QuattrocentoSans-BoldItalicLCDFJ.pfb
%{_datadir}/fonts/texlive-quattrocento/QuattrocentoSans-BoldLCDFJ.pfb
%{_datadir}/fonts/texlive-quattrocento/QuattrocentoSans-Italic.pfb
%{_datadir}/fonts/texlive-quattrocento/QuattrocentoSans-ItalicLCDFJ.pfb
%{_datadir}/fonts/texlive-quattrocento/QuattrocentoSans.pfb
%{_datadir}/fonts/texlive-quattrocento/QuattrocentoSansLCDFJ.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-quattrocento-fonts-%{texlive_version}.%{texlive_noarch}.svn50729-%{release}-zypper
%endif

%package -n texlive-quicktype
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn42183
Release:        0
Summary:        LaTeX package for quick typesetting
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-quicktype-doc >= %{texlive_version}
Provides:       tex(quicktype.sty)
Requires:       tex(graphicx.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source158:      quicktype.tar.xz
Source159:      quicktype.doc.tar.xz

%description -n texlive-quicktype
Intended for the quick typesetting of basic documents using
LaTeX using shortcuts to existing commands and specific
commands for quick formatting and creation of tables and title
pages with a graphic image.

date: 2016-10-08 04:05:32 +0000


%package -n texlive-quicktype-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn42183
Release:        0
Summary:        Documentation for texlive-quicktype
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-quicktype-doc
This package includes the documentation for texlive-quicktype

%post -n texlive-quicktype
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-quicktype 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-quicktype
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-quicktype-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/quicktype/QT.png
%{_texmfdistdir}/doc/latex/quicktype/Quicktype.pdf
%{_texmfdistdir}/doc/latex/quicktype/QuicktypeSample.pdf
%{_texmfdistdir}/doc/latex/quicktype/README.txt

%files -n texlive-quicktype
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/quicktype/quicktype.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-quicktype-%{texlive_version}.%{texlive_noarch}.0.0.1svn42183-%{release}-zypper
%endif

%package -n texlive-quotchap
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn28046
Release:        0
Summary:        Decorative chapter headings
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-quotchap-doc >= %{texlive_version}
Provides:       tex(quotchap.sty)
Requires:       tex(color.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source160:      quotchap.tar.xz
Source161:      quotchap.doc.tar.xz

%description -n texlive-quotchap
A package for creating decorative chapter headings with
quotations. Uses graphical and coloured output and by default
needs the "Adobe standard font set" (as supported by psnfss).

date: 2016-06-24 17:18:15 +0000


%package -n texlive-quotchap-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn28046
Release:        0
Summary:        Documentation for texlive-quotchap
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-quotchap-doc
This package includes the documentation for texlive-quotchap

%post -n texlive-quotchap
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-quotchap 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-quotchap
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-quotchap-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/quotchap/README
%{_texmfdistdir}/doc/latex/quotchap/document.pdf
%{_texmfdistdir}/doc/latex/quotchap/document.tex
%{_texmfdistdir}/doc/latex/quotchap/quotchap.pdf

%files -n texlive-quotchap
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/quotchap/quotchap.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-quotchap-%{texlive_version}.%{texlive_noarch}.1.1svn28046-%{release}-zypper
%endif

%package -n texlive-quoting
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1csvn32818
Release:        0
Summary:        Consolidated environment for displayed text
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-quoting-doc >= %{texlive_version}
Provides:       tex(quoting.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(kvoptions.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source162:      quoting.tar.xz
Source163:      quoting.doc.tar.xz

%description -n texlive-quoting
As an alternative to the LaTeX standard environments quotation
and quote, the package provides a consolidated environment for
displayed text. First-line indentation may be activated by
adding a blank line before the quoting environment. A key-value
interface (using kvoptions) allows the user to configure font
properties and spacing and to control orphans within and after
the environment.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-quoting-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1csvn32818
Release:        0
Summary:        Documentation for texlive-quoting
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-quoting-doc
This package includes the documentation for texlive-quoting

%post -n texlive-quoting
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-quoting 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-quoting
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-quoting-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/quoting/README
%{_texmfdistdir}/doc/latex/quoting/quoting.pdf

%files -n texlive-quoting
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/quoting/quoting.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-quoting-%{texlive_version}.%{texlive_noarch}.0.0.1csvn32818-%{release}-zypper
%endif

%package -n texlive-quotmark
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Consistent quote marks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-quotmark-doc >= %{texlive_version}
Provides:       tex(quotmark-UKenglish.def)
Provides:       tex(quotmark-USenglish.def)
Provides:       tex(quotmark-afrikaans.def)
Provides:       tex(quotmark-brazil.def)
Provides:       tex(quotmark-bulgarian.def)
Provides:       tex(quotmark-catalan.def)
Provides:       tex(quotmark-croatian.def)
Provides:       tex(quotmark-czech.def)
Provides:       tex(quotmark-danish.def)
Provides:       tex(quotmark-dutch.def)
Provides:       tex(quotmark-estonian.def)
Provides:       tex(quotmark-finnish.def)
Provides:       tex(quotmark-frenchb.def)
Provides:       tex(quotmark-germanb.def)
Provides:       tex(quotmark-greek.def)
Provides:       tex(quotmark-hebrew.def)
Provides:       tex(quotmark-icelandic.def)
Provides:       tex(quotmark-irish.def)
Provides:       tex(quotmark-italian.def)
Provides:       tex(quotmark-magyar.def)
Provides:       tex(quotmark-ngermanb.def)
Provides:       tex(quotmark-norsk.def)
Provides:       tex(quotmark-polish.def)
Provides:       tex(quotmark-portuges.def)
Provides:       tex(quotmark-romanian.def)
Provides:       tex(quotmark-russianb.def)
Provides:       tex(quotmark-serbian.def)
Provides:       tex(quotmark-slovak.def)
Provides:       tex(quotmark-slovene.def)
Provides:       tex(quotmark-sorbian.def)
Provides:       tex(quotmark-spanish.def)
Provides:       tex(quotmark-swedish.def)
Provides:       tex(quotmark-swiss.def)
Provides:       tex(quotmark-turkish.def)
Provides:       tex(quotmark-ukraineb.def)
Provides:       tex(quotmark-welsh.def)
Provides:       tex(quotmark.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source164:      quotmark.tar.xz
Source165:      quotmark.doc.tar.xz

%description -n texlive-quotmark
The package provides a means of ensuring consistent quote marks
throughout your document. The style can be changed either via
package option or command, and the package detects language
selections (from the babel or ngerman packages), and uses the
punctuation marks appropriate for the current language. The
author now considers the package obsolete, and recommends use
of csquotes in its place.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-quotmark-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-quotmark
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-quotmark-doc
This package includes the documentation for texlive-quotmark

%post -n texlive-quotmark
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-quotmark 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-quotmark
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-quotmark-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/quotmark/CHANGES
%{_texmfdistdir}/doc/latex/quotmark/README
%{_texmfdistdir}/doc/latex/quotmark/quotmark.pdf
%{_texmfdistdir}/doc/latex/quotmark/sample.tex

%files -n texlive-quotmark
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/quotmark/quotmark-UKenglish.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-USenglish.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-afrikaans.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-brazil.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-bulgarian.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-catalan.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-croatian.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-czech.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-danish.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-dutch.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-estonian.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-finnish.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-frenchb.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-germanb.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-greek.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-hebrew.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-icelandic.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-irish.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-italian.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-magyar.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-ngermanb.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-norsk.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-polish.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-portuges.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-romanian.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-russianb.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-serbian.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-slovak.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-slovene.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-sorbian.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-spanish.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-swedish.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-swiss.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-turkish.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-ukraineb.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-welsh.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-quotmark-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif

%package -n texlive-quran
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn49563
Release:        0
Summary:        An easy way to typeset any part of The Holy Quran
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-quran-doc >= %{texlive_version}
Provides:       tex(quran-transde.def)
Provides:       tex(quran-transen.def)
Provides:       tex(quran-transfa.def)
Provides:       tex(quran-translt.def)
Provides:       tex(quran.sty)
Provides:       tex(qurantext-de.translation.def)
Provides:       tex(qurantext-en.translation.def)
Provides:       tex(qurantext-en.transliteration.def)
Provides:       tex(qurantext-fa.translation.def)
Provides:       tex(qurantext-simple.def)
Provides:       tex(qurantext-uthmani.def)
Requires:       tex(biditools.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source166:      quran.tar.xz
Source167:      quran.doc.tar.xz

%description -n texlive-quran
This package offers the user an easy way to typeset The Holy
Quran. It has been inspired by the lipsum and ptext packages
and provides several macros for typesetting the whole or any
part of Quran based on its popular division, including surah,
ayah, juz, hizb, quarter, and page. Besides the Arabic
original, translations to English, German, and Persian are
provided, as well as an English transliteration.

date: 2018-12-31 09:29:21 +0000


%package -n texlive-quran-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn49563
Release:        0
Summary:        Documentation for texlive-quran
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-quran-doc
This package includes the documentation for texlive-quran

%post -n texlive-quran
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-quran 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-quran
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-quran-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/xelatex/quran/README
%{_texmfdistdir}/doc/xelatex/quran/defaulttext.pdf
%{_texmfdistdir}/doc/xelatex/quran/defaulttext.tex
%{_texmfdistdir}/doc/xelatex/quran/quran-doc.pdf
%{_texmfdistdir}/doc/xelatex/quran/quran-doc.tex
%{_texmfdistdir}/doc/xelatex/quran/quran-test.pdf
%{_texmfdistdir}/doc/xelatex/quran/quran-test.tex
%{_texmfdistdir}/doc/xelatex/quran/quran-test1.pdf
%{_texmfdistdir}/doc/xelatex/quran/quran-test1.tex
%{_texmfdistdir}/doc/xelatex/quran/quran-test2.pdf
%{_texmfdistdir}/doc/xelatex/quran/quran-test2.tex
%{_texmfdistdir}/doc/xelatex/quran/quran.png
%{_texmfdistdir}/doc/xelatex/quran/uthmanitext.pdf
%{_texmfdistdir}/doc/xelatex/quran/uthmanitext.tex

%files -n texlive-quran
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/xelatex/quran/quran-transde.def
%{_texmfdistdir}/tex/xelatex/quran/quran-transen.def
%{_texmfdistdir}/tex/xelatex/quran/quran-transfa.def
%{_texmfdistdir}/tex/xelatex/quran/quran-translt.def
%{_texmfdistdir}/tex/xelatex/quran/quran.sty
%{_texmfdistdir}/tex/xelatex/quran/qurantext-de.translation.def
%{_texmfdistdir}/tex/xelatex/quran/qurantext-en.translation.def
%{_texmfdistdir}/tex/xelatex/quran/qurantext-en.transliteration.def
%{_texmfdistdir}/tex/xelatex/quran/qurantext-fa.translation.def
%{_texmfdistdir}/tex/xelatex/quran/qurantext-simple.def
%{_texmfdistdir}/tex/xelatex/quran/qurantext-uthmani.def
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-quran-%{texlive_version}.%{texlive_noarch}.1.5svn49563-%{release}-zypper
%endif

%package -n texlive-quran-de
Version:        %{texlive_version}.%{texlive_noarch}.0.0.14svn49562
Release:        0
Summary:        German translations to the quran package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-quran-de-doc >= %{texlive_version}
Provides:       tex(quran-de.sty)
Provides:       tex(qurantext-deii.translation.def)
Provides:       tex(qurantext-deiii.translation.def)
Provides:       tex(qurantext-deiv.translation.def)
Requires:       tex(quran.sty)
Requires:       tex(qurantext-de.translation.def)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source168:      quran-de.tar.xz
Source169:      quran-de.doc.tar.xz

%description -n texlive-quran-de
The package is prepared for typesetting some of German
translations of the Holy Quran. It adds three more German
translations to the quran package

date: 2019-01-01 08:59:14 +0000


%package -n texlive-quran-de-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.14svn49562
Release:        0
Summary:        Documentation for texlive-quran-de
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-quran-de-doc
This package includes the documentation for texlive-quran-de

%post -n texlive-quran-de
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-quran-de 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-quran-de
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-quran-de-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/xelatex/quran-de/README
%{_texmfdistdir}/doc/xelatex/quran-de/quran-de-doc.pdf
%{_texmfdistdir}/doc/xelatex/quran-de/quran-de-doc.tex
%{_texmfdistdir}/doc/xelatex/quran-de/quran-de-test.pdf
%{_texmfdistdir}/doc/xelatex/quran-de/quran-de-test.tex
%{_texmfdistdir}/doc/xelatex/quran-de/quran.png

%files -n texlive-quran-de
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/xelatex/quran-de/quran-de.sty
%{_texmfdistdir}/tex/xelatex/quran-de/qurantext-deii.translation.def
%{_texmfdistdir}/tex/xelatex/quran-de/qurantext-deiii.translation.def
%{_texmfdistdir}/tex/xelatex/quran-de/qurantext-deiv.translation.def
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-quran-de-%{texlive_version}.%{texlive_noarch}.0.0.14svn49562-%{release}-zypper
%endif

%package -n texlive-r_und_s
Version:        %{texlive_version}.%{texlive_noarch}.1.3isvn15878
Release:        0
Summary:        Chemical hazard codes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-r_und_s-doc >= %{texlive_version}
Provides:       tex(eng_rs.sty)
Provides:       tex(eng_rs.tex)
Provides:       tex(fr_rs.sty)
Provides:       tex(fr_rs.tex)
Provides:       tex(nl_rs.sty)
Provides:       tex(nl_rs.tex)
Provides:       tex(r_und_s.sty)
Provides:       tex(r_und_s.tex)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source170:      r_und_s.tar.xz
Source171:      r_und_s.doc.tar.xz

%description -n texlive-r_und_s
The r_und_s package decodes the german 'R- und S-Satze', which
are numerically coded security advice for chemical substances
into plain text. This is, e.g., used to compose security sheets
or lab protocols and especially useful for students of
chemistry. There are four packages, giving texts in German,
English, French and Dutch.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-r_und_s-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3isvn15878
Release:        0
Summary:        Documentation for texlive-r_und_s
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-r_und_s-doc
This package includes the documentation for texlive-r_und_s

%post -n texlive-r_und_s
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-r_und_s 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-r_und_s
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-r_und_s-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/r_und_s/README

%files -n texlive-r_und_s
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/r_und_s/eng_rs.sty
%{_texmfdistdir}/tex/latex/r_und_s/eng_rs.tex
%{_texmfdistdir}/tex/latex/r_und_s/fr_rs.sty
%{_texmfdistdir}/tex/latex/r_und_s/fr_rs.tex
%{_texmfdistdir}/tex/latex/r_und_s/nl_rs.sty
%{_texmfdistdir}/tex/latex/r_und_s/nl_rs.tex
%{_texmfdistdir}/tex/latex/r_und_s/r_und_s.sty
%{_texmfdistdir}/tex/latex/r_und_s/r_und_s.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-r_und_s-%{texlive_version}.%{texlive_noarch}.1.3isvn15878-%{release}-zypper
%endif

%package -n texlive-raleway
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn42629
Release:        0
Summary:        Use Raleway with TeX(-alike) systems
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires:       texlive-raleway-fonts >= %{texlive_version}
Recommends:     texlive-raleway-doc >= %{texlive_version}
Provides:       tex(LY1Raleway-TLF.fd)
Provides:       tex(LY1Raleway-TOsF.fd)
Provides:       tex(OT1Raleway-TLF.fd)
Provides:       tex(OT1Raleway-TOsF.fd)
Provides:       tex(Raleway-Black-tlf-ly1--base.tfm)
Provides:       tex(Raleway-Black-tlf-ly1.tfm)
Provides:       tex(Raleway-Black-tlf-ly1.vf)
Provides:       tex(Raleway-Black-tlf-ot1.tfm)
Provides:       tex(Raleway-Black-tlf-sc-ly1--base.tfm)
Provides:       tex(Raleway-Black-tlf-sc-ly1.tfm)
Provides:       tex(Raleway-Black-tlf-sc-ly1.vf)
Provides:       tex(Raleway-Black-tlf-sc-ot1--base.tfm)
Provides:       tex(Raleway-Black-tlf-sc-ot1.tfm)
Provides:       tex(Raleway-Black-tlf-sc-ot1.vf)
Provides:       tex(Raleway-Black-tlf-sc-t1--base.tfm)
Provides:       tex(Raleway-Black-tlf-sc-t1.tfm)
Provides:       tex(Raleway-Black-tlf-sc-t1.vf)
Provides:       tex(Raleway-Black-tlf-t1--base.tfm)
Provides:       tex(Raleway-Black-tlf-t1.tfm)
Provides:       tex(Raleway-Black-tlf-t1.vf)
Provides:       tex(Raleway-Black-tlf-ts1--base.tfm)
Provides:       tex(Raleway-Black-tlf-ts1.tfm)
Provides:       tex(Raleway-Black-tlf-ts1.vf)
Provides:       tex(Raleway-Black-tosf-ly1--base.tfm)
Provides:       tex(Raleway-Black-tosf-ly1.tfm)
Provides:       tex(Raleway-Black-tosf-ly1.vf)
Provides:       tex(Raleway-Black-tosf-ot1.tfm)
Provides:       tex(Raleway-Black-tosf-sc-ly1--base.tfm)
Provides:       tex(Raleway-Black-tosf-sc-ly1.tfm)
Provides:       tex(Raleway-Black-tosf-sc-ly1.vf)
Provides:       tex(Raleway-Black-tosf-sc-ot1--base.tfm)
Provides:       tex(Raleway-Black-tosf-sc-ot1.tfm)
Provides:       tex(Raleway-Black-tosf-sc-ot1.vf)
Provides:       tex(Raleway-Black-tosf-sc-t1--base.tfm)
Provides:       tex(Raleway-Black-tosf-sc-t1.tfm)
Provides:       tex(Raleway-Black-tosf-sc-t1.vf)
Provides:       tex(Raleway-Black-tosf-t1--base.tfm)
Provides:       tex(Raleway-Black-tosf-t1.tfm)
Provides:       tex(Raleway-Black-tosf-t1.vf)
Provides:       tex(Raleway-Black-tosf-ts1--base.tfm)
Provides:       tex(Raleway-Black-tosf-ts1.tfm)
Provides:       tex(Raleway-Black-tosf-ts1.vf)
Provides:       tex(Raleway-BlackItalic-tlf-ly1--base.tfm)
Provides:       tex(Raleway-BlackItalic-tlf-ly1.tfm)
Provides:       tex(Raleway-BlackItalic-tlf-ly1.vf)
Provides:       tex(Raleway-BlackItalic-tlf-ot1.tfm)
Provides:       tex(Raleway-BlackItalic-tlf-sc-ly1--base.tfm)
Provides:       tex(Raleway-BlackItalic-tlf-sc-ly1.tfm)
Provides:       tex(Raleway-BlackItalic-tlf-sc-ly1.vf)
Provides:       tex(Raleway-BlackItalic-tlf-sc-ot1--base.tfm)
Provides:       tex(Raleway-BlackItalic-tlf-sc-ot1.tfm)
Provides:       tex(Raleway-BlackItalic-tlf-sc-ot1.vf)
Provides:       tex(Raleway-BlackItalic-tlf-sc-t1--base.tfm)
Provides:       tex(Raleway-BlackItalic-tlf-sc-t1.tfm)
Provides:       tex(Raleway-BlackItalic-tlf-sc-t1.vf)
Provides:       tex(Raleway-BlackItalic-tlf-t1--base.tfm)
Provides:       tex(Raleway-BlackItalic-tlf-t1.tfm)
Provides:       tex(Raleway-BlackItalic-tlf-t1.vf)
Provides:       tex(Raleway-BlackItalic-tlf-ts1--base.tfm)
Provides:       tex(Raleway-BlackItalic-tlf-ts1.tfm)
Provides:       tex(Raleway-BlackItalic-tlf-ts1.vf)
Provides:       tex(Raleway-BlackItalic-tosf-ly1--base.tfm)
Provides:       tex(Raleway-BlackItalic-tosf-ly1.tfm)
Provides:       tex(Raleway-BlackItalic-tosf-ly1.vf)
Provides:       tex(Raleway-BlackItalic-tosf-ot1.tfm)
Provides:       tex(Raleway-BlackItalic-tosf-sc-ly1--base.tfm)
Provides:       tex(Raleway-BlackItalic-tosf-sc-ly1.tfm)
Provides:       tex(Raleway-BlackItalic-tosf-sc-ly1.vf)
Provides:       tex(Raleway-BlackItalic-tosf-sc-ot1--base.tfm)
Provides:       tex(Raleway-BlackItalic-tosf-sc-ot1.tfm)
Provides:       tex(Raleway-BlackItalic-tosf-sc-ot1.vf)
Provides:       tex(Raleway-BlackItalic-tosf-sc-t1--base.tfm)
Provides:       tex(Raleway-BlackItalic-tosf-sc-t1.tfm)
Provides:       tex(Raleway-BlackItalic-tosf-sc-t1.vf)
Provides:       tex(Raleway-BlackItalic-tosf-t1--base.tfm)
Provides:       tex(Raleway-BlackItalic-tosf-t1.tfm)
Provides:       tex(Raleway-BlackItalic-tosf-t1.vf)
Provides:       tex(Raleway-BlackItalic-tosf-ts1--base.tfm)
Provides:       tex(Raleway-BlackItalic-tosf-ts1.tfm)
Provides:       tex(Raleway-BlackItalic-tosf-ts1.vf)
Provides:       tex(Raleway-Bold-tlf-ly1--base.tfm)
Provides:       tex(Raleway-Bold-tlf-ly1.tfm)
Provides:       tex(Raleway-Bold-tlf-ly1.vf)
Provides:       tex(Raleway-Bold-tlf-ot1.tfm)
Provides:       tex(Raleway-Bold-tlf-sc-ly1--base.tfm)
Provides:       tex(Raleway-Bold-tlf-sc-ly1.tfm)
Provides:       tex(Raleway-Bold-tlf-sc-ly1.vf)
Provides:       tex(Raleway-Bold-tlf-sc-ot1--base.tfm)
Provides:       tex(Raleway-Bold-tlf-sc-ot1.tfm)
Provides:       tex(Raleway-Bold-tlf-sc-ot1.vf)
Provides:       tex(Raleway-Bold-tlf-sc-t1--base.tfm)
Provides:       tex(Raleway-Bold-tlf-sc-t1.tfm)
Provides:       tex(Raleway-Bold-tlf-sc-t1.vf)
Provides:       tex(Raleway-Bold-tlf-t1--base.tfm)
Provides:       tex(Raleway-Bold-tlf-t1.tfm)
Provides:       tex(Raleway-Bold-tlf-t1.vf)
Provides:       tex(Raleway-Bold-tlf-ts1--base.tfm)
Provides:       tex(Raleway-Bold-tlf-ts1.tfm)
Provides:       tex(Raleway-Bold-tlf-ts1.vf)
Provides:       tex(Raleway-Bold-tosf-ly1--base.tfm)
Provides:       tex(Raleway-Bold-tosf-ly1.tfm)
Provides:       tex(Raleway-Bold-tosf-ly1.vf)
Provides:       tex(Raleway-Bold-tosf-ot1.tfm)
Provides:       tex(Raleway-Bold-tosf-sc-ly1--base.tfm)
Provides:       tex(Raleway-Bold-tosf-sc-ly1.tfm)
Provides:       tex(Raleway-Bold-tosf-sc-ly1.vf)
Provides:       tex(Raleway-Bold-tosf-sc-ot1--base.tfm)
Provides:       tex(Raleway-Bold-tosf-sc-ot1.tfm)
Provides:       tex(Raleway-Bold-tosf-sc-ot1.vf)
Provides:       tex(Raleway-Bold-tosf-sc-t1--base.tfm)
Provides:       tex(Raleway-Bold-tosf-sc-t1.tfm)
Provides:       tex(Raleway-Bold-tosf-sc-t1.vf)
Provides:       tex(Raleway-Bold-tosf-t1--base.tfm)
Provides:       tex(Raleway-Bold-tosf-t1.tfm)
Provides:       tex(Raleway-Bold-tosf-t1.vf)
Provides:       tex(Raleway-Bold-tosf-ts1--base.tfm)
Provides:       tex(Raleway-Bold-tosf-ts1.tfm)
Provides:       tex(Raleway-Bold-tosf-ts1.vf)
Provides:       tex(Raleway-BoldItalic-tlf-ly1--base.tfm)
Provides:       tex(Raleway-BoldItalic-tlf-ly1.tfm)
Provides:       tex(Raleway-BoldItalic-tlf-ly1.vf)
Provides:       tex(Raleway-BoldItalic-tlf-ot1.tfm)
Provides:       tex(Raleway-BoldItalic-tlf-sc-ly1--base.tfm)
Provides:       tex(Raleway-BoldItalic-tlf-sc-ly1.tfm)
Provides:       tex(Raleway-BoldItalic-tlf-sc-ly1.vf)
Provides:       tex(Raleway-BoldItalic-tlf-sc-ot1--base.tfm)
Provides:       tex(Raleway-BoldItalic-tlf-sc-ot1.tfm)
Provides:       tex(Raleway-BoldItalic-tlf-sc-ot1.vf)
Provides:       tex(Raleway-BoldItalic-tlf-sc-t1--base.tfm)
Provides:       tex(Raleway-BoldItalic-tlf-sc-t1.tfm)
Provides:       tex(Raleway-BoldItalic-tlf-sc-t1.vf)
Provides:       tex(Raleway-BoldItalic-tlf-t1--base.tfm)
Provides:       tex(Raleway-BoldItalic-tlf-t1.tfm)
Provides:       tex(Raleway-BoldItalic-tlf-t1.vf)
Provides:       tex(Raleway-BoldItalic-tlf-ts1--base.tfm)
Provides:       tex(Raleway-BoldItalic-tlf-ts1.tfm)
Provides:       tex(Raleway-BoldItalic-tlf-ts1.vf)
Provides:       tex(Raleway-BoldItalic-tosf-ly1--base.tfm)
Provides:       tex(Raleway-BoldItalic-tosf-ly1.tfm)
Provides:       tex(Raleway-BoldItalic-tosf-ly1.vf)
Provides:       tex(Raleway-BoldItalic-tosf-ot1.tfm)
Provides:       tex(Raleway-BoldItalic-tosf-sc-ly1--base.tfm)
Provides:       tex(Raleway-BoldItalic-tosf-sc-ly1.tfm)
Provides:       tex(Raleway-BoldItalic-tosf-sc-ly1.vf)
Provides:       tex(Raleway-BoldItalic-tosf-sc-ot1--base.tfm)
Provides:       tex(Raleway-BoldItalic-tosf-sc-ot1.tfm)
Provides:       tex(Raleway-BoldItalic-tosf-sc-ot1.vf)
Provides:       tex(Raleway-BoldItalic-tosf-sc-t1--base.tfm)
Provides:       tex(Raleway-BoldItalic-tosf-sc-t1.tfm)
Provides:       tex(Raleway-BoldItalic-tosf-sc-t1.vf)
Provides:       tex(Raleway-BoldItalic-tosf-t1--base.tfm)
Provides:       tex(Raleway-BoldItalic-tosf-t1.tfm)
Provides:       tex(Raleway-BoldItalic-tosf-t1.vf)
Provides:       tex(Raleway-BoldItalic-tosf-ts1--base.tfm)
Provides:       tex(Raleway-BoldItalic-tosf-ts1.tfm)
Provides:       tex(Raleway-BoldItalic-tosf-ts1.vf)
Provides:       tex(Raleway-ExtraBold-tlf-ly1--base.tfm)
Provides:       tex(Raleway-ExtraBold-tlf-ly1.tfm)
Provides:       tex(Raleway-ExtraBold-tlf-ly1.vf)
Provides:       tex(Raleway-ExtraBold-tlf-ot1.tfm)
Provides:       tex(Raleway-ExtraBold-tlf-sc-ly1--base.tfm)
Provides:       tex(Raleway-ExtraBold-tlf-sc-ly1.tfm)
Provides:       tex(Raleway-ExtraBold-tlf-sc-ly1.vf)
Provides:       tex(Raleway-ExtraBold-tlf-sc-ot1--base.tfm)
Provides:       tex(Raleway-ExtraBold-tlf-sc-ot1.tfm)
Provides:       tex(Raleway-ExtraBold-tlf-sc-ot1.vf)
Provides:       tex(Raleway-ExtraBold-tlf-sc-t1--base.tfm)
Provides:       tex(Raleway-ExtraBold-tlf-sc-t1.tfm)
Provides:       tex(Raleway-ExtraBold-tlf-sc-t1.vf)
Provides:       tex(Raleway-ExtraBold-tlf-t1--base.tfm)
Provides:       tex(Raleway-ExtraBold-tlf-t1.tfm)
Provides:       tex(Raleway-ExtraBold-tlf-t1.vf)
Provides:       tex(Raleway-ExtraBold-tlf-ts1--base.tfm)
Provides:       tex(Raleway-ExtraBold-tlf-ts1.tfm)
Provides:       tex(Raleway-ExtraBold-tlf-ts1.vf)
Provides:       tex(Raleway-ExtraBold-tosf-ly1--base.tfm)
Provides:       tex(Raleway-ExtraBold-tosf-ly1.tfm)
Provides:       tex(Raleway-ExtraBold-tosf-ly1.vf)
Provides:       tex(Raleway-ExtraBold-tosf-ot1.tfm)
Provides:       tex(Raleway-ExtraBold-tosf-sc-ly1--base.tfm)
Provides:       tex(Raleway-ExtraBold-tosf-sc-ly1.tfm)
Provides:       tex(Raleway-ExtraBold-tosf-sc-ly1.vf)
Provides:       tex(Raleway-ExtraBold-tosf-sc-ot1--base.tfm)
Provides:       tex(Raleway-ExtraBold-tosf-sc-ot1.tfm)
Provides:       tex(Raleway-ExtraBold-tosf-sc-ot1.vf)
Provides:       tex(Raleway-ExtraBold-tosf-sc-t1--base.tfm)
Provides:       tex(Raleway-ExtraBold-tosf-sc-t1.tfm)
Provides:       tex(Raleway-ExtraBold-tosf-sc-t1.vf)
Provides:       tex(Raleway-ExtraBold-tosf-t1--base.tfm)
Provides:       tex(Raleway-ExtraBold-tosf-t1.tfm)
Provides:       tex(Raleway-ExtraBold-tosf-t1.vf)
Provides:       tex(Raleway-ExtraBold-tosf-ts1--base.tfm)
Provides:       tex(Raleway-ExtraBold-tosf-ts1.tfm)
Provides:       tex(Raleway-ExtraBold-tosf-ts1.vf)
Provides:       tex(Raleway-ExtraBoldItalic-tlf-ly1--base.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tlf-ly1.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tlf-ly1.vf)
Provides:       tex(Raleway-ExtraBoldItalic-tlf-ot1.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tlf-sc-ly1--base.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tlf-sc-ly1.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tlf-sc-ly1.vf)
Provides:       tex(Raleway-ExtraBoldItalic-tlf-sc-ot1--base.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tlf-sc-ot1.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tlf-sc-ot1.vf)
Provides:       tex(Raleway-ExtraBoldItalic-tlf-sc-t1--base.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tlf-sc-t1.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tlf-sc-t1.vf)
Provides:       tex(Raleway-ExtraBoldItalic-tlf-t1--base.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tlf-t1.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tlf-t1.vf)
Provides:       tex(Raleway-ExtraBoldItalic-tlf-ts1--base.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tlf-ts1.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tlf-ts1.vf)
Provides:       tex(Raleway-ExtraBoldItalic-tosf-ly1--base.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tosf-ly1.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tosf-ly1.vf)
Provides:       tex(Raleway-ExtraBoldItalic-tosf-ot1.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tosf-sc-ly1--base.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tosf-sc-ly1.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tosf-sc-ly1.vf)
Provides:       tex(Raleway-ExtraBoldItalic-tosf-sc-ot1--base.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tosf-sc-ot1.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tosf-sc-ot1.vf)
Provides:       tex(Raleway-ExtraBoldItalic-tosf-sc-t1--base.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tosf-sc-t1.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tosf-sc-t1.vf)
Provides:       tex(Raleway-ExtraBoldItalic-tosf-t1--base.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tosf-t1.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tosf-t1.vf)
Provides:       tex(Raleway-ExtraBoldItalic-tosf-ts1--base.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tosf-ts1.tfm)
Provides:       tex(Raleway-ExtraBoldItalic-tosf-ts1.vf)
Provides:       tex(Raleway-ExtraLight-tlf-ly1--base.tfm)
Provides:       tex(Raleway-ExtraLight-tlf-ly1.tfm)
Provides:       tex(Raleway-ExtraLight-tlf-ly1.vf)
Provides:       tex(Raleway-ExtraLight-tlf-ot1.tfm)
Provides:       tex(Raleway-ExtraLight-tlf-sc-ly1--base.tfm)
Provides:       tex(Raleway-ExtraLight-tlf-sc-ly1.tfm)
Provides:       tex(Raleway-ExtraLight-tlf-sc-ly1.vf)
Provides:       tex(Raleway-ExtraLight-tlf-sc-ot1--base.tfm)
Provides:       tex(Raleway-ExtraLight-tlf-sc-ot1.tfm)
Provides:       tex(Raleway-ExtraLight-tlf-sc-ot1.vf)
Provides:       tex(Raleway-ExtraLight-tlf-sc-t1--base.tfm)
Provides:       tex(Raleway-ExtraLight-tlf-sc-t1.tfm)
Provides:       tex(Raleway-ExtraLight-tlf-sc-t1.vf)
Provides:       tex(Raleway-ExtraLight-tlf-t1--base.tfm)
Provides:       tex(Raleway-ExtraLight-tlf-t1.tfm)
Provides:       tex(Raleway-ExtraLight-tlf-t1.vf)
Provides:       tex(Raleway-ExtraLight-tlf-ts1--base.tfm)
Provides:       tex(Raleway-ExtraLight-tlf-ts1.tfm)
Provides:       tex(Raleway-ExtraLight-tlf-ts1.vf)
Provides:       tex(Raleway-ExtraLight-tosf-ly1--base.tfm)
Provides:       tex(Raleway-ExtraLight-tosf-ly1.tfm)
Provides:       tex(Raleway-ExtraLight-tosf-ly1.vf)
Provides:       tex(Raleway-ExtraLight-tosf-ot1.tfm)
Provides:       tex(Raleway-ExtraLight-tosf-sc-ly1--base.tfm)
Provides:       tex(Raleway-ExtraLight-tosf-sc-ly1.tfm)
Provides:       tex(Raleway-ExtraLight-tosf-sc-ly1.vf)
Provides:       tex(Raleway-ExtraLight-tosf-sc-ot1--base.tfm)
Provides:       tex(Raleway-ExtraLight-tosf-sc-ot1.tfm)
Provides:       tex(Raleway-ExtraLight-tosf-sc-ot1.vf)
Provides:       tex(Raleway-ExtraLight-tosf-sc-t1--base.tfm)
Provides:       tex(Raleway-ExtraLight-tosf-sc-t1.tfm)
Provides:       tex(Raleway-ExtraLight-tosf-sc-t1.vf)
Provides:       tex(Raleway-ExtraLight-tosf-t1--base.tfm)
Provides:       tex(Raleway-ExtraLight-tosf-t1.tfm)
Provides:       tex(Raleway-ExtraLight-tosf-t1.vf)
Provides:       tex(Raleway-ExtraLight-tosf-ts1--base.tfm)
Provides:       tex(Raleway-ExtraLight-tosf-ts1.tfm)
Provides:       tex(Raleway-ExtraLight-tosf-ts1.vf)
Provides:       tex(Raleway-ExtraLightItalic-tlf-ly1--base.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tlf-ly1.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tlf-ly1.vf)
Provides:       tex(Raleway-ExtraLightItalic-tlf-ot1.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tlf-sc-ly1--base.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tlf-sc-ly1.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tlf-sc-ly1.vf)
Provides:       tex(Raleway-ExtraLightItalic-tlf-sc-ot1--base.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tlf-sc-ot1.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tlf-sc-ot1.vf)
Provides:       tex(Raleway-ExtraLightItalic-tlf-sc-t1--base.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tlf-sc-t1.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tlf-sc-t1.vf)
Provides:       tex(Raleway-ExtraLightItalic-tlf-t1--base.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tlf-t1.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tlf-t1.vf)
Provides:       tex(Raleway-ExtraLightItalic-tlf-ts1--base.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tlf-ts1.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tlf-ts1.vf)
Provides:       tex(Raleway-ExtraLightItalic-tosf-ly1--base.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tosf-ly1.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tosf-ly1.vf)
Provides:       tex(Raleway-ExtraLightItalic-tosf-ot1.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tosf-sc-ly1--base.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tosf-sc-ly1.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tosf-sc-ly1.vf)
Provides:       tex(Raleway-ExtraLightItalic-tosf-sc-ot1--base.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tosf-sc-ot1.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tosf-sc-ot1.vf)
Provides:       tex(Raleway-ExtraLightItalic-tosf-sc-t1--base.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tosf-sc-t1.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tosf-sc-t1.vf)
Provides:       tex(Raleway-ExtraLightItalic-tosf-t1--base.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tosf-t1.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tosf-t1.vf)
Provides:       tex(Raleway-ExtraLightItalic-tosf-ts1--base.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tosf-ts1.tfm)
Provides:       tex(Raleway-ExtraLightItalic-tosf-ts1.vf)
Provides:       tex(Raleway-Italic-tlf-ly1--base.tfm)
Provides:       tex(Raleway-Italic-tlf-ly1.tfm)
Provides:       tex(Raleway-Italic-tlf-ly1.vf)
Provides:       tex(Raleway-Italic-tlf-ot1.tfm)
Provides:       tex(Raleway-Italic-tlf-sc-ly1--base.tfm)
Provides:       tex(Raleway-Italic-tlf-sc-ly1.tfm)
Provides:       tex(Raleway-Italic-tlf-sc-ly1.vf)
Provides:       tex(Raleway-Italic-tlf-sc-ot1--base.tfm)
Provides:       tex(Raleway-Italic-tlf-sc-ot1.tfm)
Provides:       tex(Raleway-Italic-tlf-sc-ot1.vf)
Provides:       tex(Raleway-Italic-tlf-sc-t1--base.tfm)
Provides:       tex(Raleway-Italic-tlf-sc-t1.tfm)
Provides:       tex(Raleway-Italic-tlf-sc-t1.vf)
Provides:       tex(Raleway-Italic-tlf-t1--base.tfm)
Provides:       tex(Raleway-Italic-tlf-t1.tfm)
Provides:       tex(Raleway-Italic-tlf-t1.vf)
Provides:       tex(Raleway-Italic-tlf-ts1--base.tfm)
Provides:       tex(Raleway-Italic-tlf-ts1.tfm)
Provides:       tex(Raleway-Italic-tlf-ts1.vf)
Provides:       tex(Raleway-Italic-tosf-ly1--base.tfm)
Provides:       tex(Raleway-Italic-tosf-ly1.tfm)
Provides:       tex(Raleway-Italic-tosf-ly1.vf)
Provides:       tex(Raleway-Italic-tosf-ot1.tfm)
Provides:       tex(Raleway-Italic-tosf-sc-ly1--base.tfm)
Provides:       tex(Raleway-Italic-tosf-sc-ly1.tfm)
Provides:       tex(Raleway-Italic-tosf-sc-ly1.vf)
Provides:       tex(Raleway-Italic-tosf-sc-ot1--base.tfm)
Provides:       tex(Raleway-Italic-tosf-sc-ot1.tfm)
Provides:       tex(Raleway-Italic-tosf-sc-ot1.vf)
Provides:       tex(Raleway-Italic-tosf-sc-t1--base.tfm)
Provides:       tex(Raleway-Italic-tosf-sc-t1.tfm)
Provides:       tex(Raleway-Italic-tosf-sc-t1.vf)
Provides:       tex(Raleway-Italic-tosf-t1--base.tfm)
Provides:       tex(Raleway-Italic-tosf-t1.tfm)
Provides:       tex(Raleway-Italic-tosf-t1.vf)
Provides:       tex(Raleway-Italic-tosf-ts1--base.tfm)
Provides:       tex(Raleway-Italic-tosf-ts1.tfm)
Provides:       tex(Raleway-Italic-tosf-ts1.vf)
Provides:       tex(Raleway-Light-tlf-ly1--base.tfm)
Provides:       tex(Raleway-Light-tlf-ly1.tfm)
Provides:       tex(Raleway-Light-tlf-ly1.vf)
Provides:       tex(Raleway-Light-tlf-ot1.tfm)
Provides:       tex(Raleway-Light-tlf-sc-ly1--base.tfm)
Provides:       tex(Raleway-Light-tlf-sc-ly1.tfm)
Provides:       tex(Raleway-Light-tlf-sc-ly1.vf)
Provides:       tex(Raleway-Light-tlf-sc-ot1--base.tfm)
Provides:       tex(Raleway-Light-tlf-sc-ot1.tfm)
Provides:       tex(Raleway-Light-tlf-sc-ot1.vf)
Provides:       tex(Raleway-Light-tlf-sc-t1--base.tfm)
Provides:       tex(Raleway-Light-tlf-sc-t1.tfm)
Provides:       tex(Raleway-Light-tlf-sc-t1.vf)
Provides:       tex(Raleway-Light-tlf-t1--base.tfm)
Provides:       tex(Raleway-Light-tlf-t1.tfm)
Provides:       tex(Raleway-Light-tlf-t1.vf)
Provides:       tex(Raleway-Light-tlf-ts1--base.tfm)
Provides:       tex(Raleway-Light-tlf-ts1.tfm)
Provides:       tex(Raleway-Light-tlf-ts1.vf)
Provides:       tex(Raleway-Light-tosf-ly1--base.tfm)
Provides:       tex(Raleway-Light-tosf-ly1.tfm)
Provides:       tex(Raleway-Light-tosf-ly1.vf)
Provides:       tex(Raleway-Light-tosf-ot1.tfm)
Provides:       tex(Raleway-Light-tosf-sc-ly1--base.tfm)
Provides:       tex(Raleway-Light-tosf-sc-ly1.tfm)
Provides:       tex(Raleway-Light-tosf-sc-ly1.vf)
Provides:       tex(Raleway-Light-tosf-sc-ot1--base.tfm)
Provides:       tex(Raleway-Light-tosf-sc-ot1.tfm)
Provides:       tex(Raleway-Light-tosf-sc-ot1.vf)
Provides:       tex(Raleway-Light-tosf-sc-t1--base.tfm)
Provides:       tex(Raleway-Light-tosf-sc-t1.tfm)
Provides:       tex(Raleway-Light-tosf-sc-t1.vf)
Provides:       tex(Raleway-Light-tosf-t1--base.tfm)
Provides:       tex(Raleway-Light-tosf-t1.tfm)
Provides:       tex(Raleway-Light-tosf-t1.vf)
Provides:       tex(Raleway-Light-tosf-ts1--base.tfm)
Provides:       tex(Raleway-Light-tosf-ts1.tfm)
Provides:       tex(Raleway-Light-tosf-ts1.vf)
Provides:       tex(Raleway-LightItalic-tlf-ly1--base.tfm)
Provides:       tex(Raleway-LightItalic-tlf-ly1.tfm)
Provides:       tex(Raleway-LightItalic-tlf-ly1.vf)
Provides:       tex(Raleway-LightItalic-tlf-ot1.tfm)
Provides:       tex(Raleway-LightItalic-tlf-sc-ly1--base.tfm)
Provides:       tex(Raleway-LightItalic-tlf-sc-ly1.tfm)
Provides:       tex(Raleway-LightItalic-tlf-sc-ly1.vf)
Provides:       tex(Raleway-LightItalic-tlf-sc-ot1--base.tfm)
Provides:       tex(Raleway-LightItalic-tlf-sc-ot1.tfm)
Provides:       tex(Raleway-LightItalic-tlf-sc-ot1.vf)
Provides:       tex(Raleway-LightItalic-tlf-sc-t1--base.tfm)
Provides:       tex(Raleway-LightItalic-tlf-sc-t1.tfm)
Provides:       tex(Raleway-LightItalic-tlf-sc-t1.vf)
Provides:       tex(Raleway-LightItalic-tlf-t1--base.tfm)
Provides:       tex(Raleway-LightItalic-tlf-t1.tfm)
Provides:       tex(Raleway-LightItalic-tlf-t1.vf)
Provides:       tex(Raleway-LightItalic-tlf-ts1--base.tfm)
Provides:       tex(Raleway-LightItalic-tlf-ts1.tfm)
Provides:       tex(Raleway-LightItalic-tlf-ts1.vf)
Provides:       tex(Raleway-LightItalic-tosf-ly1--base.tfm)
Provides:       tex(Raleway-LightItalic-tosf-ly1.tfm)
Provides:       tex(Raleway-LightItalic-tosf-ly1.vf)
Provides:       tex(Raleway-LightItalic-tosf-ot1.tfm)
Provides:       tex(Raleway-LightItalic-tosf-sc-ly1--base.tfm)
Provides:       tex(Raleway-LightItalic-tosf-sc-ly1.tfm)
Provides:       tex(Raleway-LightItalic-tosf-sc-ly1.vf)
Provides:       tex(Raleway-LightItalic-tosf-sc-ot1--base.tfm)
Provides:       tex(Raleway-LightItalic-tosf-sc-ot1.tfm)
Provides:       tex(Raleway-LightItalic-tosf-sc-ot1.vf)
Provides:       tex(Raleway-LightItalic-tosf-sc-t1--base.tfm)
Provides:       tex(Raleway-LightItalic-tosf-sc-t1.tfm)
Provides:       tex(Raleway-LightItalic-tosf-sc-t1.vf)
Provides:       tex(Raleway-LightItalic-tosf-t1--base.tfm)
Provides:       tex(Raleway-LightItalic-tosf-t1.tfm)
Provides:       tex(Raleway-LightItalic-tosf-t1.vf)
Provides:       tex(Raleway-LightItalic-tosf-ts1--base.tfm)
Provides:       tex(Raleway-LightItalic-tosf-ts1.tfm)
Provides:       tex(Raleway-LightItalic-tosf-ts1.vf)
Provides:       tex(Raleway-Medium-tlf-ly1--base.tfm)
Provides:       tex(Raleway-Medium-tlf-ly1.tfm)
Provides:       tex(Raleway-Medium-tlf-ly1.vf)
Provides:       tex(Raleway-Medium-tlf-ot1.tfm)
Provides:       tex(Raleway-Medium-tlf-sc-ly1--base.tfm)
Provides:       tex(Raleway-Medium-tlf-sc-ly1.tfm)
Provides:       tex(Raleway-Medium-tlf-sc-ly1.vf)
Provides:       tex(Raleway-Medium-tlf-sc-ot1--base.tfm)
Provides:       tex(Raleway-Medium-tlf-sc-ot1.tfm)
Provides:       tex(Raleway-Medium-tlf-sc-ot1.vf)
Provides:       tex(Raleway-Medium-tlf-sc-t1--base.tfm)
Provides:       tex(Raleway-Medium-tlf-sc-t1.tfm)
Provides:       tex(Raleway-Medium-tlf-sc-t1.vf)
Provides:       tex(Raleway-Medium-tlf-t1--base.tfm)
Provides:       tex(Raleway-Medium-tlf-t1.tfm)
Provides:       tex(Raleway-Medium-tlf-t1.vf)
Provides:       tex(Raleway-Medium-tlf-ts1--base.tfm)
Provides:       tex(Raleway-Medium-tlf-ts1.tfm)
Provides:       tex(Raleway-Medium-tlf-ts1.vf)
Provides:       tex(Raleway-Medium-tosf-ly1--base.tfm)
Provides:       tex(Raleway-Medium-tosf-ly1.tfm)
Provides:       tex(Raleway-Medium-tosf-ly1.vf)
Provides:       tex(Raleway-Medium-tosf-ot1.tfm)
Provides:       tex(Raleway-Medium-tosf-sc-ly1--base.tfm)
Provides:       tex(Raleway-Medium-tosf-sc-ly1.tfm)
Provides:       tex(Raleway-Medium-tosf-sc-ly1.vf)
Provides:       tex(Raleway-Medium-tosf-sc-ot1--base.tfm)
Provides:       tex(Raleway-Medium-tosf-sc-ot1.tfm)
Provides:       tex(Raleway-Medium-tosf-sc-ot1.vf)
Provides:       tex(Raleway-Medium-tosf-sc-t1--base.tfm)
Provides:       tex(Raleway-Medium-tosf-sc-t1.tfm)
Provides:       tex(Raleway-Medium-tosf-sc-t1.vf)
Provides:       tex(Raleway-Medium-tosf-t1--base.tfm)
Provides:       tex(Raleway-Medium-tosf-t1.tfm)
Provides:       tex(Raleway-Medium-tosf-t1.vf)
Provides:       tex(Raleway-Medium-tosf-ts1--base.tfm)
Provides:       tex(Raleway-Medium-tosf-ts1.tfm)
Provides:       tex(Raleway-Medium-tosf-ts1.vf)
Provides:       tex(Raleway-MediumItalic-tlf-ly1--base.tfm)
Provides:       tex(Raleway-MediumItalic-tlf-ly1.tfm)
Provides:       tex(Raleway-MediumItalic-tlf-ly1.vf)
Provides:       tex(Raleway-MediumItalic-tlf-ot1.tfm)
Provides:       tex(Raleway-MediumItalic-tlf-sc-ly1--base.tfm)
Provides:       tex(Raleway-MediumItalic-tlf-sc-ly1.tfm)
Provides:       tex(Raleway-MediumItalic-tlf-sc-ly1.vf)
Provides:       tex(Raleway-MediumItalic-tlf-sc-ot1--base.tfm)
Provides:       tex(Raleway-MediumItalic-tlf-sc-ot1.tfm)
Provides:       tex(Raleway-MediumItalic-tlf-sc-ot1.vf)
Provides:       tex(Raleway-MediumItalic-tlf-sc-t1--base.tfm)
Provides:       tex(Raleway-MediumItalic-tlf-sc-t1.tfm)
Provides:       tex(Raleway-MediumItalic-tlf-sc-t1.vf)
Provides:       tex(Raleway-MediumItalic-tlf-t1--base.tfm)
Provides:       tex(Raleway-MediumItalic-tlf-t1.tfm)
Provides:       tex(Raleway-MediumItalic-tlf-t1.vf)
Provides:       tex(Raleway-MediumItalic-tlf-ts1--base.tfm)
Provides:       tex(Raleway-MediumItalic-tlf-ts1.tfm)
Provides:       tex(Raleway-MediumItalic-tlf-ts1.vf)
Provides:       tex(Raleway-MediumItalic-tosf-ly1--base.tfm)
Provides:       tex(Raleway-MediumItalic-tosf-ly1.tfm)
Provides:       tex(Raleway-MediumItalic-tosf-ly1.vf)
Provides:       tex(Raleway-MediumItalic-tosf-ot1.tfm)
Provides:       tex(Raleway-MediumItalic-tosf-sc-ly1--base.tfm)
Provides:       tex(Raleway-MediumItalic-tosf-sc-ly1.tfm)
Provides:       tex(Raleway-MediumItalic-tosf-sc-ly1.vf)
Provides:       tex(Raleway-MediumItalic-tosf-sc-ot1--base.tfm)
Provides:       tex(Raleway-MediumItalic-tosf-sc-ot1.tfm)
Provides:       tex(Raleway-MediumItalic-tosf-sc-ot1.vf)
Provides:       tex(Raleway-MediumItalic-tosf-sc-t1--base.tfm)
Provides:       tex(Raleway-MediumItalic-tosf-sc-t1.tfm)
Provides:       tex(Raleway-MediumItalic-tosf-sc-t1.vf)
Provides:       tex(Raleway-MediumItalic-tosf-t1--base.tfm)
Provides:       tex(Raleway-MediumItalic-tosf-t1.tfm)
Provides:       tex(Raleway-MediumItalic-tosf-t1.vf)
Provides:       tex(Raleway-MediumItalic-tosf-ts1--base.tfm)
Provides:       tex(Raleway-MediumItalic-tosf-ts1.tfm)
Provides:       tex(Raleway-MediumItalic-tosf-ts1.vf)
Provides:       tex(Raleway-Regular-tlf-ly1--base.tfm)
Provides:       tex(Raleway-Regular-tlf-ly1.tfm)
Provides:       tex(Raleway-Regular-tlf-ly1.vf)
Provides:       tex(Raleway-Regular-tlf-ot1.tfm)
Provides:       tex(Raleway-Regular-tlf-sc-ly1--base.tfm)
Provides:       tex(Raleway-Regular-tlf-sc-ly1.tfm)
Provides:       tex(Raleway-Regular-tlf-sc-ly1.vf)
Provides:       tex(Raleway-Regular-tlf-sc-ot1--base.tfm)
Provides:       tex(Raleway-Regular-tlf-sc-ot1.tfm)
Provides:       tex(Raleway-Regular-tlf-sc-ot1.vf)
Provides:       tex(Raleway-Regular-tlf-sc-t1--base.tfm)
Provides:       tex(Raleway-Regular-tlf-sc-t1.tfm)
Provides:       tex(Raleway-Regular-tlf-sc-t1.vf)
Provides:       tex(Raleway-Regular-tlf-t1--base.tfm)
Provides:       tex(Raleway-Regular-tlf-t1.tfm)
Provides:       tex(Raleway-Regular-tlf-t1.vf)
Provides:       tex(Raleway-Regular-tlf-ts1--base.tfm)
Provides:       tex(Raleway-Regular-tlf-ts1.tfm)
Provides:       tex(Raleway-Regular-tlf-ts1.vf)
Provides:       tex(Raleway-Regular-tosf-ly1--base.tfm)
Provides:       tex(Raleway-Regular-tosf-ly1.tfm)
Provides:       tex(Raleway-Regular-tosf-ly1.vf)
Provides:       tex(Raleway-Regular-tosf-ot1.tfm)
Provides:       tex(Raleway-Regular-tosf-sc-ly1--base.tfm)
Provides:       tex(Raleway-Regular-tosf-sc-ly1.tfm)
Provides:       tex(Raleway-Regular-tosf-sc-ly1.vf)
Provides:       tex(Raleway-Regular-tosf-sc-ot1--base.tfm)
Provides:       tex(Raleway-Regular-tosf-sc-ot1.tfm)
Provides:       tex(Raleway-Regular-tosf-sc-ot1.vf)
Provides:       tex(Raleway-Regular-tosf-sc-t1--base.tfm)
Provides:       tex(Raleway-Regular-tosf-sc-t1.tfm)
Provides:       tex(Raleway-Regular-tosf-sc-t1.vf)
Provides:       tex(Raleway-Regular-tosf-t1--base.tfm)
Provides:       tex(Raleway-Regular-tosf-t1.tfm)
Provides:       tex(Raleway-Regular-tosf-t1.vf)
Provides:       tex(Raleway-Regular-tosf-ts1--base.tfm)
Provides:       tex(Raleway-Regular-tosf-ts1.tfm)
Provides:       tex(Raleway-Regular-tosf-ts1.vf)
Provides:       tex(Raleway-SemiBold-tlf-ly1--base.tfm)
Provides:       tex(Raleway-SemiBold-tlf-ly1.tfm)
Provides:       tex(Raleway-SemiBold-tlf-ly1.vf)
Provides:       tex(Raleway-SemiBold-tlf-ot1.tfm)
Provides:       tex(Raleway-SemiBold-tlf-sc-ly1--base.tfm)
Provides:       tex(Raleway-SemiBold-tlf-sc-ly1.tfm)
Provides:       tex(Raleway-SemiBold-tlf-sc-ly1.vf)
Provides:       tex(Raleway-SemiBold-tlf-sc-ot1--base.tfm)
Provides:       tex(Raleway-SemiBold-tlf-sc-ot1.tfm)
Provides:       tex(Raleway-SemiBold-tlf-sc-ot1.vf)
Provides:       tex(Raleway-SemiBold-tlf-sc-t1--base.tfm)
Provides:       tex(Raleway-SemiBold-tlf-sc-t1.tfm)
Provides:       tex(Raleway-SemiBold-tlf-sc-t1.vf)
Provides:       tex(Raleway-SemiBold-tlf-t1--base.tfm)
Provides:       tex(Raleway-SemiBold-tlf-t1.tfm)
Provides:       tex(Raleway-SemiBold-tlf-t1.vf)
Provides:       tex(Raleway-SemiBold-tlf-ts1--base.tfm)
Provides:       tex(Raleway-SemiBold-tlf-ts1.tfm)
Provides:       tex(Raleway-SemiBold-tlf-ts1.vf)
Provides:       tex(Raleway-SemiBold-tosf-ly1--base.tfm)
Provides:       tex(Raleway-SemiBold-tosf-ly1.tfm)
Provides:       tex(Raleway-SemiBold-tosf-ly1.vf)
Provides:       tex(Raleway-SemiBold-tosf-ot1.tfm)
Provides:       tex(Raleway-SemiBold-tosf-sc-ly1--base.tfm)
Provides:       tex(Raleway-SemiBold-tosf-sc-ly1.tfm)
Provides:       tex(Raleway-SemiBold-tosf-sc-ly1.vf)
Provides:       tex(Raleway-SemiBold-tosf-sc-ot1--base.tfm)
Provides:       tex(Raleway-SemiBold-tosf-sc-ot1.tfm)
Provides:       tex(Raleway-SemiBold-tosf-sc-ot1.vf)
Provides:       tex(Raleway-SemiBold-tosf-sc-t1--base.tfm)
Provides:       tex(Raleway-SemiBold-tosf-sc-t1.tfm)
Provides:       tex(Raleway-SemiBold-tosf-sc-t1.vf)
Provides:       tex(Raleway-SemiBold-tosf-t1--base.tfm)
Provides:       tex(Raleway-SemiBold-tosf-t1.tfm)
Provides:       tex(Raleway-SemiBold-tosf-t1.vf)
Provides:       tex(Raleway-SemiBold-tosf-ts1--base.tfm)
Provides:       tex(Raleway-SemiBold-tosf-ts1.tfm)
Provides:       tex(Raleway-SemiBold-tosf-ts1.vf)
Provides:       tex(Raleway-SemiBoldItalic-tlf-ly1--base.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tlf-ly1.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tlf-ly1.vf)
Provides:       tex(Raleway-SemiBoldItalic-tlf-ot1.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tlf-sc-ly1--base.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tlf-sc-ly1.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tlf-sc-ly1.vf)
Provides:       tex(Raleway-SemiBoldItalic-tlf-sc-ot1--base.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tlf-sc-ot1.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tlf-sc-ot1.vf)
Provides:       tex(Raleway-SemiBoldItalic-tlf-sc-t1--base.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tlf-sc-t1.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tlf-sc-t1.vf)
Provides:       tex(Raleway-SemiBoldItalic-tlf-t1--base.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tlf-t1.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tlf-t1.vf)
Provides:       tex(Raleway-SemiBoldItalic-tlf-ts1--base.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tlf-ts1.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tlf-ts1.vf)
Provides:       tex(Raleway-SemiBoldItalic-tosf-ly1--base.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tosf-ly1.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tosf-ly1.vf)
Provides:       tex(Raleway-SemiBoldItalic-tosf-ot1.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tosf-sc-ly1--base.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tosf-sc-ly1.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tosf-sc-ly1.vf)
Provides:       tex(Raleway-SemiBoldItalic-tosf-sc-ot1--base.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tosf-sc-ot1.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tosf-sc-ot1.vf)
Provides:       tex(Raleway-SemiBoldItalic-tosf-sc-t1--base.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tosf-sc-t1.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tosf-sc-t1.vf)
Provides:       tex(Raleway-SemiBoldItalic-tosf-t1--base.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tosf-t1.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tosf-t1.vf)
Provides:       tex(Raleway-SemiBoldItalic-tosf-ts1--base.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tosf-ts1.tfm)
Provides:       tex(Raleway-SemiBoldItalic-tosf-ts1.vf)
Provides:       tex(Raleway-Thin-tlf-ly1--base.tfm)
Provides:       tex(Raleway-Thin-tlf-ly1.tfm)
Provides:       tex(Raleway-Thin-tlf-ly1.vf)
Provides:       tex(Raleway-Thin-tlf-ot1.tfm)
Provides:       tex(Raleway-Thin-tlf-sc-ly1--base.tfm)
Provides:       tex(Raleway-Thin-tlf-sc-ly1.tfm)
Provides:       tex(Raleway-Thin-tlf-sc-ly1.vf)
Provides:       tex(Raleway-Thin-tlf-sc-ot1--base.tfm)
Provides:       tex(Raleway-Thin-tlf-sc-ot1.tfm)
Provides:       tex(Raleway-Thin-tlf-sc-ot1.vf)
Provides:       tex(Raleway-Thin-tlf-sc-t1--base.tfm)
Provides:       tex(Raleway-Thin-tlf-sc-t1.tfm)
Provides:       tex(Raleway-Thin-tlf-sc-t1.vf)
Provides:       tex(Raleway-Thin-tlf-t1--base.tfm)
Provides:       tex(Raleway-Thin-tlf-t1.tfm)
Provides:       tex(Raleway-Thin-tlf-t1.vf)
Provides:       tex(Raleway-Thin-tlf-ts1--base.tfm)
Provides:       tex(Raleway-Thin-tlf-ts1.tfm)
Provides:       tex(Raleway-Thin-tlf-ts1.vf)
Provides:       tex(Raleway-Thin-tosf-ly1--base.tfm)
Provides:       tex(Raleway-Thin-tosf-ly1.tfm)
Provides:       tex(Raleway-Thin-tosf-ly1.vf)
Provides:       tex(Raleway-Thin-tosf-ot1.tfm)
Provides:       tex(Raleway-Thin-tosf-sc-ly1--base.tfm)
Provides:       tex(Raleway-Thin-tosf-sc-ly1.tfm)
Provides:       tex(Raleway-Thin-tosf-sc-ly1.vf)
Provides:       tex(Raleway-Thin-tosf-sc-ot1--base.tfm)
Provides:       tex(Raleway-Thin-tosf-sc-ot1.tfm)
Provides:       tex(Raleway-Thin-tosf-sc-ot1.vf)
Provides:       tex(Raleway-Thin-tosf-sc-t1--base.tfm)
Provides:       tex(Raleway-Thin-tosf-sc-t1.tfm)
Provides:       tex(Raleway-Thin-tosf-sc-t1.vf)
Provides:       tex(Raleway-Thin-tosf-t1--base.tfm)
Provides:       tex(Raleway-Thin-tosf-t1.tfm)
Provides:       tex(Raleway-Thin-tosf-t1.vf)
Provides:       tex(Raleway-Thin-tosf-ts1--base.tfm)
Provides:       tex(Raleway-Thin-tosf-ts1.tfm)
Provides:       tex(Raleway-Thin-tosf-ts1.vf)
Provides:       tex(Raleway-ThinItalic-tlf-ly1--base.tfm)
Provides:       tex(Raleway-ThinItalic-tlf-ly1.tfm)
Provides:       tex(Raleway-ThinItalic-tlf-ly1.vf)
Provides:       tex(Raleway-ThinItalic-tlf-ot1.tfm)
Provides:       tex(Raleway-ThinItalic-tlf-sc-ly1--base.tfm)
Provides:       tex(Raleway-ThinItalic-tlf-sc-ly1.tfm)
Provides:       tex(Raleway-ThinItalic-tlf-sc-ly1.vf)
Provides:       tex(Raleway-ThinItalic-tlf-sc-ot1--base.tfm)
Provides:       tex(Raleway-ThinItalic-tlf-sc-ot1.tfm)
Provides:       tex(Raleway-ThinItalic-tlf-sc-ot1.vf)
Provides:       tex(Raleway-ThinItalic-tlf-sc-t1--base.tfm)
Provides:       tex(Raleway-ThinItalic-tlf-sc-t1.tfm)
Provides:       tex(Raleway-ThinItalic-tlf-sc-t1.vf)
Provides:       tex(Raleway-ThinItalic-tlf-t1--base.tfm)
Provides:       tex(Raleway-ThinItalic-tlf-t1.tfm)
Provides:       tex(Raleway-ThinItalic-tlf-t1.vf)
Provides:       tex(Raleway-ThinItalic-tlf-ts1--base.tfm)
Provides:       tex(Raleway-ThinItalic-tlf-ts1.tfm)
Provides:       tex(Raleway-ThinItalic-tlf-ts1.vf)
Provides:       tex(Raleway-ThinItalic-tosf-ly1--base.tfm)
Provides:       tex(Raleway-ThinItalic-tosf-ly1.tfm)
Provides:       tex(Raleway-ThinItalic-tosf-ly1.vf)
Provides:       tex(Raleway-ThinItalic-tosf-ot1.tfm)
Provides:       tex(Raleway-ThinItalic-tosf-sc-ly1--base.tfm)
Provides:       tex(Raleway-ThinItalic-tosf-sc-ly1.tfm)
Provides:       tex(Raleway-ThinItalic-tosf-sc-ly1.vf)
Provides:       tex(Raleway-ThinItalic-tosf-sc-ot1--base.tfm)
Provides:       tex(Raleway-ThinItalic-tosf-sc-ot1.tfm)
Provides:       tex(Raleway-ThinItalic-tosf-sc-ot1.vf)
Provides:       tex(Raleway-ThinItalic-tosf-sc-t1--base.tfm)
Provides:       tex(Raleway-ThinItalic-tosf-sc-t1.tfm)
Provides:       tex(Raleway-ThinItalic-tosf-sc-t1.vf)
Provides:       tex(Raleway-ThinItalic-tosf-t1--base.tfm)
Provides:       tex(Raleway-ThinItalic-tosf-t1.tfm)
Provides:       tex(Raleway-ThinItalic-tosf-t1.vf)
Provides:       tex(Raleway-ThinItalic-tosf-ts1--base.tfm)
Provides:       tex(Raleway-ThinItalic-tosf-ts1.tfm)
Provides:       tex(Raleway-ThinItalic-tosf-ts1.vf)
Provides:       tex(Raleway.map)
Provides:       tex(T1Raleway-TLF.fd)
Provides:       tex(T1Raleway-TOsF.fd)
Provides:       tex(TS1Raleway-TLF.fd)
Provides:       tex(TS1Raleway-TOsF.fd)
Provides:       tex(a_2bcjq6.enc)
Provides:       tex(a_biciir.enc)
Provides:       tex(a_bzmckq.enc)
Provides:       tex(a_f3uqdf.enc)
Provides:       tex(a_gvxmk7.enc)
Provides:       tex(a_ioname.enc)
Provides:       tex(a_k2dfwc.enc)
Provides:       tex(a_mgzrni.enc)
Provides:       tex(a_mzuigi.enc)
Provides:       tex(a_oaf34p.enc)
Provides:       tex(a_pcwse4.enc)
Provides:       tex(a_sor5xn.enc)
Provides:       tex(a_u6n666.enc)
Provides:       tex(a_yqxcf3.enc)
Provides:       tex(raleway-type1-autoinst.sty)
Provides:       tex(raleway.sty)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source172:      raleway.tar.xz
Source173:      raleway.doc.tar.xz

%description -n texlive-raleway
The package provides the Raleway family in an easy to use way.
For XeLaTeX and LuaLaTeX users the original OpenType fonts are
used. The entire font family is included.

date: 2016-12-03 17:07:41 +0000


%package -n texlive-raleway-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn42629
Release:        0
Summary:        Documentation for texlive-raleway
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-raleway-doc
This package includes the documentation for texlive-raleway


%package -n texlive-raleway-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn42629
Release:        0
Summary:        Severed fonts for texlive-raleway
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
Url:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-raleway-fonts
The  separated fonts package for texlive-raleway
%post -n texlive-raleway
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap Raleway.map' >> /var/run/texlive/run-updmap

%postun -n texlive-raleway 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap Raleway.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-raleway
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-raleway-fonts
%files -n texlive-raleway-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/raleway/LPPL.txt
%{_texmfdistdir}/doc/latex/raleway/OFL.txt
%{_texmfdistdir}/doc/latex/raleway/raleway-otf-specimen.pdf
%{_texmfdistdir}/doc/latex/raleway/raleway-otf-specimen.tex
%{_texmfdistdir}/doc/latex/raleway/raleway-type1-specimen.pdf
%{_texmfdistdir}/doc/latex/raleway/raleway-type1-specimen.tex
%{_texmfdistdir}/doc/latex/raleway/raleway.pdf
%{_texmfdistdir}/doc/latex/raleway/raleway.tex

%files -n texlive-raleway
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/raleway/a_2bcjq6.enc
%{_texmfdistdir}/fonts/enc/dvips/raleway/a_biciir.enc
%{_texmfdistdir}/fonts/enc/dvips/raleway/a_bzmckq.enc
%{_texmfdistdir}/fonts/enc/dvips/raleway/a_f3uqdf.enc
%{_texmfdistdir}/fonts/enc/dvips/raleway/a_gvxmk7.enc
%{_texmfdistdir}/fonts/enc/dvips/raleway/a_ioname.enc
%{_texmfdistdir}/fonts/enc/dvips/raleway/a_k2dfwc.enc
%{_texmfdistdir}/fonts/enc/dvips/raleway/a_mgzrni.enc
%{_texmfdistdir}/fonts/enc/dvips/raleway/a_mzuigi.enc
%{_texmfdistdir}/fonts/enc/dvips/raleway/a_oaf34p.enc
%{_texmfdistdir}/fonts/enc/dvips/raleway/a_pcwse4.enc
%{_texmfdistdir}/fonts/enc/dvips/raleway/a_sor5xn.enc
%{_texmfdistdir}/fonts/enc/dvips/raleway/a_u6n666.enc
%{_texmfdistdir}/fonts/enc/dvips/raleway/a_yqxcf3.enc
%{_texmfdistdir}/fonts/map/dvips/raleway/Raleway.map
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/raleway/Raleway-Black-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/raleway/Raleway-Black.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/raleway/Raleway-Bold-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/raleway/Raleway-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/raleway/Raleway-ExtraBold-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/raleway/Raleway-ExtraBold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/raleway/Raleway-ExtraLight-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/raleway/Raleway-ExtraLight.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/raleway/Raleway-Light-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/raleway/Raleway-Light.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/raleway/Raleway-Medium-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/raleway/Raleway-Medium.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/raleway/Raleway-Regular-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/raleway/Raleway-Regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/raleway/Raleway-SemiBold-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/raleway/Raleway-SemiBold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/raleway/Raleway-Thin-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/impallari/raleway/Raleway-Thin.otf
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Black-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BlackItalic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Bold-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-BoldItalic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBold-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraBoldItalic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLight-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ExtraLightItalic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Italic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Light-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-LightItalic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Medium-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-MediumItalic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Regular-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBold-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-SemiBoldItalic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-Thin-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/raleway/Raleway-ThinItalic-tosf-ts1.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/raleway/Raleway-Black.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/raleway/Raleway-BlackItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/raleway/Raleway-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/raleway/Raleway-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/raleway/Raleway-ExtraBold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/raleway/Raleway-ExtraBoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/raleway/Raleway-ExtraLight.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/raleway/Raleway-ExtraLightItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/raleway/Raleway-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/raleway/Raleway-Light.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/raleway/Raleway-LightItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/raleway/Raleway-Medium.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/raleway/Raleway-MediumItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/raleway/Raleway-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/raleway/Raleway-SemiBold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/raleway/Raleway-SemiBoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/raleway/Raleway-Thin.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/impallari/raleway/Raleway-ThinItalic.pfb
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Black-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Black-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Black-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Black-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Black-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Black-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Black-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Black-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Black-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Black-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Black-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Black-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BlackItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BlackItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BlackItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BlackItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BlackItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BlackItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BlackItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BlackItalic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BlackItalic-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BlackItalic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BlackItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BlackItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Bold-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Bold-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Bold-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Bold-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Bold-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Bold-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Bold-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Bold-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Bold-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BoldItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BoldItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BoldItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BoldItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BoldItalic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BoldItalic-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BoldItalic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BoldItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-BoldItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBold-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBold-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBold-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBold-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBold-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBold-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBold-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBold-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBold-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBoldItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBoldItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBoldItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBoldItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBoldItalic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBoldItalic-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBoldItalic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBoldItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraBoldItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLight-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLight-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLight-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLight-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLight-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLight-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLight-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLight-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLight-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLight-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLight-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLight-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLightItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLightItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLightItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLightItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLightItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLightItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLightItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLightItalic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLightItalic-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLightItalic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLightItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ExtraLightItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Italic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Italic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Italic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Italic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Italic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Italic-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Italic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Italic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Italic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Light-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Light-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Light-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Light-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Light-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Light-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Light-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Light-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Light-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Light-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Light-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Light-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-LightItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-LightItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-LightItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-LightItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-LightItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-LightItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-LightItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-LightItalic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-LightItalic-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-LightItalic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-LightItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-LightItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Medium-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Medium-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Medium-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Medium-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Medium-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Medium-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Medium-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Medium-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Medium-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Medium-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Medium-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Medium-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-MediumItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-MediumItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-MediumItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-MediumItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-MediumItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-MediumItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-MediumItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-MediumItalic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-MediumItalic-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-MediumItalic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-MediumItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-MediumItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Regular-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Regular-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Regular-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Regular-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Regular-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Regular-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Regular-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Regular-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Regular-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Regular-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Regular-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBold-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBold-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBold-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBold-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBold-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBold-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBold-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBold-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBold-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBoldItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBoldItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBoldItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBoldItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBoldItalic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBoldItalic-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBoldItalic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBoldItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-SemiBoldItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Thin-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Thin-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Thin-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Thin-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Thin-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Thin-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Thin-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Thin-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Thin-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Thin-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Thin-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-Thin-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ThinItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ThinItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ThinItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ThinItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ThinItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ThinItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ThinItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ThinItalic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ThinItalic-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ThinItalic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ThinItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/raleway/Raleway-ThinItalic-tosf-ts1.vf
%{_texmfdistdir}/tex/latex/raleway/LY1Raleway-TLF.fd
%{_texmfdistdir}/tex/latex/raleway/LY1Raleway-TOsF.fd
%{_texmfdistdir}/tex/latex/raleway/OT1Raleway-TLF.fd
%{_texmfdistdir}/tex/latex/raleway/OT1Raleway-TOsF.fd
%{_texmfdistdir}/tex/latex/raleway/T1Raleway-TLF.fd
%{_texmfdistdir}/tex/latex/raleway/T1Raleway-TOsF.fd
%{_texmfdistdir}/tex/latex/raleway/TS1Raleway-TLF.fd
%{_texmfdistdir}/tex/latex/raleway/TS1Raleway-TOsF.fd
%{_texmfdistdir}/tex/latex/raleway/raleway-type1-autoinst.sty
%{_texmfdistdir}/tex/latex/raleway/raleway.sty

%files -n texlive-raleway-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-raleway
%config %{_sysconfdir}/fonts/conf.avail/58-texlive-raleway.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-raleway.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-raleway/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-raleway/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-raleway/fonts.scale
%{_datadir}/fonts/texlive-raleway/Raleway-Black-Italic.otf
%{_datadir}/fonts/texlive-raleway/Raleway-Black.otf
%{_datadir}/fonts/texlive-raleway/Raleway-Bold-Italic.otf
%{_datadir}/fonts/texlive-raleway/Raleway-Bold.otf
%{_datadir}/fonts/texlive-raleway/Raleway-ExtraBold-Italic.otf
%{_datadir}/fonts/texlive-raleway/Raleway-ExtraBold.otf
%{_datadir}/fonts/texlive-raleway/Raleway-ExtraLight-Italic.otf
%{_datadir}/fonts/texlive-raleway/Raleway-ExtraLight.otf
%{_datadir}/fonts/texlive-raleway/Raleway-Light-Italic.otf
%{_datadir}/fonts/texlive-raleway/Raleway-Light.otf
%{_datadir}/fonts/texlive-raleway/Raleway-Medium-Italic.otf
%{_datadir}/fonts/texlive-raleway/Raleway-Medium.otf
%{_datadir}/fonts/texlive-raleway/Raleway-Regular-Italic.otf
%{_datadir}/fonts/texlive-raleway/Raleway-Regular.otf
%{_datadir}/fonts/texlive-raleway/Raleway-SemiBold-Italic.otf
%{_datadir}/fonts/texlive-raleway/Raleway-SemiBold.otf
%{_datadir}/fonts/texlive-raleway/Raleway-Thin-Italic.otf
%{_datadir}/fonts/texlive-raleway/Raleway-Thin.otf
%{_datadir}/fonts/texlive-raleway/Raleway-Black.pfb
%{_datadir}/fonts/texlive-raleway/Raleway-BlackItalic.pfb
%{_datadir}/fonts/texlive-raleway/Raleway-Bold.pfb
%{_datadir}/fonts/texlive-raleway/Raleway-BoldItalic.pfb
%{_datadir}/fonts/texlive-raleway/Raleway-ExtraBold.pfb
%{_datadir}/fonts/texlive-raleway/Raleway-ExtraBoldItalic.pfb
%{_datadir}/fonts/texlive-raleway/Raleway-ExtraLight.pfb
%{_datadir}/fonts/texlive-raleway/Raleway-ExtraLightItalic.pfb
%{_datadir}/fonts/texlive-raleway/Raleway-Italic.pfb
%{_datadir}/fonts/texlive-raleway/Raleway-Light.pfb
%{_datadir}/fonts/texlive-raleway/Raleway-LightItalic.pfb
%{_datadir}/fonts/texlive-raleway/Raleway-Medium.pfb
%{_datadir}/fonts/texlive-raleway/Raleway-MediumItalic.pfb
%{_datadir}/fonts/texlive-raleway/Raleway-Regular.pfb
%{_datadir}/fonts/texlive-raleway/Raleway-SemiBold.pfb
%{_datadir}/fonts/texlive-raleway/Raleway-SemiBoldItalic.pfb
%{_datadir}/fonts/texlive-raleway/Raleway-Thin.pfb
%{_datadir}/fonts/texlive-raleway/Raleway-ThinItalic.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-raleway-fonts-%{texlive_version}.%{texlive_noarch}.1.4svn42629-%{release}-zypper
%endif

%package -n texlive-ran_toks
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn44429
Release:        0
Summary:        Randomise token strings
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-ran_toks-doc >= %{texlive_version}
Provides:       tex(ran_toks.sty)
Requires:       tex(verbatim.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source174:      ran_toks.tar.xz
Source175:      ran_toks.doc.tar.xz

%description -n texlive-ran_toks
The package provides means of randomising lists of tokens, or
lists of chunks of tokens. Two mechanisms for defining chunks
are provided: the macro \ranToks command accepts an argument
containing tokens to be randomised; and the \bRTVToks/\eRTVToks
commands delimit a collection of tokens for randomising; each
group inside a rtVw constitutes one of these (typically larger)
token sets.

date: 2017-05-18 20:38:32 +0000


%package -n texlive-ran_toks-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn44429
Release:        0
Summary:        Documentation for texlive-ran_toks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-ran_toks-doc
This package includes the documentation for texlive-ran_toks

%post -n texlive-ran_toks
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ran_toks 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ran_toks
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ran_toks-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ran_toks/README.md
%{_texmfdistdir}/doc/latex/ran_toks/doc/rantoks_man.pdf
%{_texmfdistdir}/doc/latex/ran_toks/doc/rantoks_man.tex
%{_texmfdistdir}/doc/latex/ran_toks/examples/db1.tex
%{_texmfdistdir}/doc/latex/ran_toks/examples/db2.tex
%{_texmfdistdir}/doc/latex/ran_toks/examples/db3.tex
%{_texmfdistdir}/doc/latex/ran_toks/examples/db4.tex
%{_texmfdistdir}/doc/latex/ran_toks/examples/mc-db.tex
%{_texmfdistdir}/doc/latex/ran_toks/examples/mytext.verb
%{_texmfdistdir}/doc/latex/ran_toks/examples/ran_toks.tex
%{_texmfdistdir}/doc/latex/ran_toks/examples/random_tst.tex
%{_texmfdistdir}/doc/latex/ran_toks/examples/random_tst_qz.tex

%files -n texlive-ran_toks
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ran_toks/ran_toks.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ran_toks-%{texlive_version}.%{texlive_noarch}.1.1svn44429-%{release}-zypper
%endif

%package -n texlive-randbild
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn15878
Release:        0
Summary:        Marginal pictures
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-randbild-doc >= %{texlive_version}
Provides:       tex(randbild.sty)
Requires:       tex(pst-plot.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source176:      randbild.tar.xz
Source177:      randbild.doc.tar.xz

%description -n texlive-randbild
Provides environments randbild to draw small marginal plots
(using the packages pstricks and pst-plot), and randbildbasis
(the same, only without the automatically drawn coordinate
system).

date: 2018-09-15 11:56:20 +0000


%package -n texlive-randbild-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn15878
Release:        0
Summary:        Documentation for texlive-randbild
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-randbild-doc:de)

%description -n texlive-randbild-doc
This package includes the documentation for texlive-randbild

%post -n texlive-randbild
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-randbild 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-randbild
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-randbild-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/randbild/README
%{_texmfdistdir}/doc/latex/randbild/randbild.pdf

%files -n texlive-randbild
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/randbild/randbild.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-randbild-%{texlive_version}.%{texlive_noarch}.0.0.2svn15878-%{release}-zypper
%endif

%package -n texlive-randomlist
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn45281
Release:        0
Summary:        Deal with database, loop, and random in order to build personalized exercises
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-randomlist-doc >= %{texlive_version}
Provides:       tex(randomlist.sty)
Provides:       tex(randomlist.tex)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source178:      randomlist.tar.xz
Source179:      randomlist.doc.tar.xz

%description -n texlive-randomlist
The main aim of this package is to work on lists, especially
with random operations. The hidden aim is to build a personnal
collection of exercises with different data for each pupil.

date: 2018-01-07 13:49:11 +0000


%package -n texlive-randomlist-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn45281
Release:        0
Summary:        Documentation for texlive-randomlist
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-randomlist-doc
This package includes the documentation for texlive-randomlist

%post -n texlive-randomlist
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-randomlist 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-randomlist
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-randomlist-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/randomlist/Makefile
%{_texmfdistdir}/doc/generic/randomlist/README.txt
%{_texmfdistdir}/doc/generic/randomlist/comets.dat
%{_texmfdistdir}/doc/generic/randomlist/pupils.dat
%{_texmfdistdir}/doc/generic/randomlist/pythagoras.dat
%{_texmfdistdir}/doc/generic/randomlist/randomlist.pdf
%{_texmfdistdir}/doc/generic/randomlist/test-fr.pdf
%{_texmfdistdir}/doc/generic/randomlist/test-fr.tex
%{_texmfdistdir}/doc/generic/randomlist/test.pdf
%{_texmfdistdir}/doc/generic/randomlist/test.tex
%{_texmfdistdir}/doc/generic/randomlist/testtex.pdf
%{_texmfdistdir}/doc/generic/randomlist/testtex.tex

%files -n texlive-randomlist
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/randomlist/randomlist.sty
%{_texmfdistdir}/tex/generic/randomlist/randomlist.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-randomlist-%{texlive_version}.%{texlive_noarch}.1.3svn45281-%{release}-zypper
%endif

%package -n texlive-randomwalk
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn49513
Release:        0
Summary:        Random walks using TikZ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-randomwalk-doc >= %{texlive_version}
Provides:       tex(randomwalk.sty)
Requires:       tex(expl3.sty)
Requires:       tex(pgfcore.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source180:      randomwalk.tar.xz
Source181:      randomwalk.doc.tar.xz

%description -n texlive-randomwalk
The randomwalk package provides a user command, \RandomWalk, to
draw random walks with a given number of steps. Lengths and
angles of the steps can be customized in various ways. The
package uses lcg for its 'random' numbers and PGF/TikZ for its
graphical output.

date: 2018-12-28 14:55:21 +0000


%package -n texlive-randomwalk-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn49513
Release:        0
Summary:        Documentation for texlive-randomwalk
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-randomwalk-doc
This package includes the documentation for texlive-randomwalk

%post -n texlive-randomwalk
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-randomwalk 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-randomwalk
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-randomwalk-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/randomwalk/README.md
%{_texmfdistdir}/doc/latex/randomwalk/randomwalk.pdf

%files -n texlive-randomwalk
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/randomwalk/randomwalk.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-randomwalk-%{texlive_version}.%{texlive_noarch}.0.0.6svn49513-%{release}-zypper
%endif

%package -n texlive-randtext
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Randomise the order of characters in strings
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-randtext-doc >= %{texlive_version}
Provides:       tex(randtext.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source182:      randtext.tar.xz
Source183:      randtext.doc.tar.xz

%description -n texlive-randtext
The package provides a single macro \randomize{TEXT} that
typesets the characters of TEXT in random order, such that the
resulting output appears correct, but most automated attempts
to read the file will misunderstand it. This function allows
one to include an email address in a TeX document and publish
it online without fear of email address harvesters or spammers
easily picking up the address.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-randtext-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-randtext
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-randtext-doc
This package includes the documentation for texlive-randtext

%post -n texlive-randtext
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-randtext 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-randtext
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-randtext-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/randtext/README

%files -n texlive-randtext
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/randtext/randtext.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-randtext-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-rank-2-roots
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn48515
Release:        0
Summary:        Draw (mathematical) rank 2 root systems
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rank-2-roots-doc >= %{texlive_version}
Provides:       tex(rank-2-roots.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(expl3.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source184:      rank-2-roots.tar.xz
Source185:      rank-2-roots.doc.tar.xz

%description -n texlive-rank-2-roots
This package concerns mathematical drawings arising in
representation theory. The purpose of this package is to ease
drawing of rank 2 root systems, with Weyl chambers, weight
lattices, and parabolic subgroups. Required packages are tikz,
etoolbox, expl3, pgfkeys, pgfopts, xparse, and xstring.

date: 2018-09-01 04:52:31 +0000


%package -n texlive-rank-2-roots-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn48515
Release:        0
Summary:        Documentation for texlive-rank-2-roots
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rank-2-roots-doc
This package includes the documentation for texlive-rank-2-roots

%post -n texlive-rank-2-roots
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rank-2-roots 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rank-2-roots
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rank-2-roots-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/rank-2-roots/README
%{_texmfdistdir}/doc/latex/rank-2-roots/rank-2-roots.bib
%{_texmfdistdir}/doc/latex/rank-2-roots/rank-2-roots.pdf
%{_texmfdistdir}/doc/latex/rank-2-roots/rank-2-roots.tex

%files -n texlive-rank-2-roots
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/rank-2-roots/rank-2-roots.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rank-2-roots-%{texlive_version}.%{texlive_noarch}.1.0svn48515-%{release}-zypper
%endif

%package -n texlive-rccol
Version:        %{texlive_version}.%{texlive_noarch}.1.2csvn15878
Release:        0
Summary:        Decimal-centered optionally rounded numbers in tabular
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rccol-doc >= %{texlive_version}
Provides:       tex(rccol.sty)
Requires:       tex(array.sty)
Requires:       tex(fltpoint.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source186:      rccol.tar.xz
Source187:      rccol.doc.tar.xz

%description -n texlive-rccol
The rccol package provides decimal-centered numbers:
corresponding digits and decimal separators aligned.
Furthermore, rounding to the desired precision is possible. The
package makes use of the fltpoint package (as well as the LaTeX
required array package).

date: 2016-06-24 17:18:15 +0000


%package -n texlive-rccol-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2csvn15878
Release:        0
Summary:        Documentation for texlive-rccol
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rccol-doc
This package includes the documentation for texlive-rccol

%post -n texlive-rccol
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rccol 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rccol
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rccol-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/rccol/README
%{_texmfdistdir}/doc/latex/rccol/rccol.pdf

%files -n texlive-rccol
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/rccol/rccol.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rccol-%{texlive_version}.%{texlive_noarch}.1.2csvn15878-%{release}-zypper
%endif

%package -n texlive-rcs
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Use RCS (revision control system) tags in LaTeX documents
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rcs-doc >= %{texlive_version}
Provides:       tex(rcs.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source188:      rcs.tar.xz
Source189:      rcs.doc.tar.xz

%description -n texlive-rcs
The rcs package utilizes the inclusion of RCS supplied data in
LaTeX documents. It's upward compatible to *all* rcs styles I
know of. In particular, you can easily access values of every
RCS field in your document put the checkin date on the
titlepage put RCS fields in a footline You can typeset revision
logs. Not in verbatim -- real LaTeX text! But you need a
configurable RCS for that. Refer to the user manual for more
detailed information. You can also configure the rcs package
easily to do special things for any keyword. This bundle comes
with a user manual, an internal interface description, full
documentation of the implementation, style information for
AUC-TeX, and test cases.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-rcs-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-rcs
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rcs-doc
This package includes the documentation for texlive-rcs

%post -n texlive-rcs
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rcs 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rcs
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rcs-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/rcs/CATALOG
%{_texmfdistdir}/doc/latex/rcs/History
%{_texmfdistdir}/doc/latex/rcs/INSTALL
%{_texmfdistdir}/doc/latex/rcs/License
%{_texmfdistdir}/doc/latex/rcs/MANIFEST
%{_texmfdistdir}/doc/latex/rcs/README
%{_texmfdistdir}/doc/latex/rcs/rcs-conf.pdf
%{_texmfdistdir}/doc/latex/rcs/rcs-user.pdf

%files -n texlive-rcs
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/rcs/rcs.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rcs-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-rcs-multi
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1asvn21939
Release:        0
Summary:        Typeset RCS version control in multiple-file documents
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rcs-multi-doc >= %{texlive_version}
Provides:       tex(rcs-multi.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source190:      rcs-multi.tar.xz
Source191:      rcs-multi.doc.tar.xz

%description -n texlive-rcs-multi
The package enables the user to typeset version control
information provided by RCS keywords (e.g., $ID: ... $) in
LaTeX documents that contain multiple TeX files. The package is
based on the author's svn-multi package.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-rcs-multi-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1asvn21939
Release:        0
Summary:        Documentation for texlive-rcs-multi
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rcs-multi-doc
This package includes the documentation for texlive-rcs-multi

%post -n texlive-rcs-multi
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rcs-multi 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rcs-multi
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rcs-multi-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/rcs-multi/example.pdf
%{_texmfdistdir}/doc/latex/rcs-multi/rcs-multi.pdf

%files -n texlive-rcs-multi
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/rcs-multi/rcs-multi.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rcs-multi-%{texlive_version}.%{texlive_noarch}.0.0.1asvn21939-%{release}-zypper
%endif

%package -n texlive-rcsinfo
Version:        %{texlive_version}.%{texlive_noarch}.1.11svn15878
Release:        0
Summary:        Support for the revision control system
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rcsinfo-doc >= %{texlive_version}
Provides:       tex(rcsinfo.cfg)
Provides:       tex(rcsinfo.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fancyheadings.sty)
Requires:       tex(scrpage2.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source192:      rcsinfo.tar.xz
Source193:      rcsinfo.doc.tar.xz

%description -n texlive-rcsinfo
A package to extract RCS (Revision Control System) information
and use it in a LaTeX document. For users of LaTeX2HTML
rcsinfo.perl is included.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-rcsinfo-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.11svn15878
Release:        0
Summary:        Documentation for texlive-rcsinfo
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rcsinfo-doc
This package includes the documentation for texlive-rcsinfo

%post -n texlive-rcsinfo
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rcsinfo 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rcsinfo
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rcsinfo-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/rcsinfo/README
%{_texmfdistdir}/doc/latex/rcsinfo/README-1.9
%{_texmfdistdir}/doc/latex/rcsinfo/rcsinfo.init
%{_texmfdistdir}/doc/latex/rcsinfo/rcsinfo.pdf
%{_texmfdistdir}/doc/latex/rcsinfo/rcsinfo.perl
%{_texmfdistdir}/doc/latex/rcsinfo/rcsinfo2html.tex

%files -n texlive-rcsinfo
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/rcsinfo/rcsinfo.cfg
%{_texmfdistdir}/tex/latex/rcsinfo/rcsinfo.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rcsinfo-%{texlive_version}.%{texlive_noarch}.1.11svn15878-%{release}-zypper
%endif

%package -n texlive-readarray
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn42467
Release:        0
Summary:        Read, store and recall array-formatted data
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-readarray-doc >= %{texlive_version}
Provides:       tex(readarray.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source194:      readarray.tar.xz
Source195:      readarray.doc.tar.xz

%description -n texlive-readarray
The package allows the user to input formatted data into
elements of a 2-D or 3-D array and to recall that data at will
by individual cell number. The data can be but need not be
numerical in nature. It can be, for example, formatted text.
While the package can be used for any application where indexed
data is called for, the package proves particularly useful when
elements of multiple arrays must be recallable and dynamically
combined at time of compilation, rather than in advance.

date: 2016-11-15 22:30:18 +0000


%package -n texlive-readarray-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn42467
Release:        0
Summary:        Documentation for texlive-readarray
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-readarray-doc
This package includes the documentation for texlive-readarray

%post -n texlive-readarray
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-readarray 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-readarray
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-readarray-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/readarray/README
%{_texmfdistdir}/doc/latex/readarray/readarray.pdf
%{_texmfdistdir}/doc/latex/readarray/readarray.tex

%files -n texlive-readarray
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/readarray/readarray.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-readarray-%{texlive_version}.%{texlive_noarch}.2.0svn42467-%{release}-zypper
%endif

%package -n texlive-realboxes
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn23581
Release:        0
Summary:        Variants of common box-commands that read their content as real box and not as macro argument
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-realboxes-doc >= %{texlive_version}
Provides:       tex(realboxes.sty)
Requires:       tex(adjcalc.sty)
Requires:       tex(calc.sty)
Requires:       tex(collectbox.sty)
Requires:       tex(color.sty)
Requires:       tex(dashbox.sty)
Requires:       tex(fancybox.sty)
Requires:       tex(graphics.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source196:      realboxes.tar.xz
Source197:      realboxes.doc.tar.xz

%description -n texlive-realboxes
The package uses the author's package collectbox to define
variants of common box related macros which read the content as
real box and not as macro argument. This enables the use of
verbatim or other special material as part of this content. The
provided macros have the same names as the original versions
but start with an upper-case letter instead. The "long-form"
macros, like \Makebox, can also be used as environments, but
not the "short-form" macros, like \Mbox. However, normally the
long form uses the short form anyway when no optional arguments
are used.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-realboxes-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn23581
Release:        0
Summary:        Documentation for texlive-realboxes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-realboxes-doc
This package includes the documentation for texlive-realboxes

%post -n texlive-realboxes
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-realboxes 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-realboxes
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-realboxes-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/realboxes/README
%{_texmfdistdir}/doc/latex/realboxes/realboxes.pdf

%files -n texlive-realboxes
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/realboxes/realboxes.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-realboxes-%{texlive_version}.%{texlive_noarch}.0.0.2svn23581-%{release}-zypper
%endif

%package -n texlive-realhats
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn50134
Release:        0
Summary:        Put real hats on symbols instead of ^
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-realhats-doc >= %{texlive_version}
Provides:       tex(realhats.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(calc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(lcg.sty)
Requires:       tex(stackengine.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source198:      realhats.tar.xz
Source199:      realhats.doc.tar.xz

%description -n texlive-realhats
This package makes \hat put real hats on symbols.

date: 2019-02-27 04:05:57 +0000


%package -n texlive-realhats-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn50134
Release:        0
Summary:        Documentation for texlive-realhats
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-realhats-doc
This package includes the documentation for texlive-realhats

%post -n texlive-realhats
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-realhats 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-realhats
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-realhats-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/realhats/README.md
%{_texmfdistdir}/doc/latex/realhats/readme_images/hats.png
%{_texmfdistdir}/doc/latex/realhats/realhats.pdf

%files -n texlive-realhats
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/realhats/hats/realhats-beret.png
%{_texmfdistdir}/tex/latex/realhats/hats/realhats-cowboy.png
%{_texmfdistdir}/tex/latex/realhats/hats/realhats-fez.png
%{_texmfdistdir}/tex/latex/realhats/hats/realhats-makelatexgreatagain.png
%{_texmfdistdir}/tex/latex/realhats/hats/realhats-santa.png
%{_texmfdistdir}/tex/latex/realhats/hats/realhats-scottish.png
%{_texmfdistdir}/tex/latex/realhats/hats/realhats-sombrero.png
%{_texmfdistdir}/tex/latex/realhats/hats/realhats-tophat.png
%{_texmfdistdir}/tex/latex/realhats/hats/realhats-witch.png
%{_texmfdistdir}/tex/latex/realhats/realhats.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-realhats-%{texlive_version}.%{texlive_noarch}.2.0svn50134-%{release}-zypper
%endif

%package -n texlive-realscripts
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3dsvn39706
Release:        0
Summary:        Access OpenType subscript and superscript glyphs
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-realscripts-doc >= %{texlive_version}
Provides:       tex(realscripts.sty)
Requires:       tex(fontspec.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source200:      realscripts.tar.xz
Source201:      realscripts.doc.tar.xz

%description -n texlive-realscripts
This small package replaces \textsuperscript and \textsubscript
commands by equivalent commands that use OpenType font features
to access appropriate glyphs if possible. The package also
patches LaTeX's default footnote command to use this new
\textsuperscript for footnote symbols. The package requires
fontspec running on either XeLaTeX or LuaLaTeX. The package
holds functions that were once parts of the xltxtra package,
which now loads realscripts by default.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-realscripts-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3dsvn39706
Release:        0
Summary:        Documentation for texlive-realscripts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-realscripts-doc
This package includes the documentation for texlive-realscripts

%post -n texlive-realscripts
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-realscripts 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-realscripts
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-realscripts-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/realscripts/README.md
%{_texmfdistdir}/doc/latex/realscripts/realscripts.pdf

%files -n texlive-realscripts
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/realscripts/realscripts.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-realscripts-%{texlive_version}.%{texlive_noarch}.0.0.3dsvn39706-%{release}-zypper
%endif

%package -n texlive-rec-thy
Version:        %{texlive_version}.%{texlive_noarch}.3.01svn50047
Release:        0
Summary:        Commands to typeset recursion theory papers
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rec-thy-doc >= %{texlive_version}
Provides:       tex(rec-thy.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifmtarg.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(suffix.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source202:      rec-thy.tar.xz
Source203:      rec-thy.doc.tar.xz

%description -n texlive-rec-thy
The package provides many macros to express standard notation
in recursion theory (otherwise known as computability theory).

date: 2019-02-17 08:19:28 +0000


%package -n texlive-rec-thy-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.01svn50047
Release:        0
Summary:        Documentation for texlive-rec-thy
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rec-thy-doc
This package includes the documentation for texlive-rec-thy

%post -n texlive-rec-thy
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rec-thy 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rec-thy
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rec-thy-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/rec-thy/README
%{_texmfdistdir}/doc/latex/rec-thy/rec-thy.pdf
%{_texmfdistdir}/doc/latex/rec-thy/rec-thy.tex

%files -n texlive-rec-thy
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/rec-thy/rec-thy.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rec-thy-%{texlive_version}.%{texlive_noarch}.3.01svn50047-%{release}-zypper
%endif

%package -n texlive-recipe
Version:        %{texlive_version}.%{texlive_noarch}.0.0.9svn15878
Release:        0
Summary:        A LaTeX class to typeset recipes
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-recipe-doc >= %{texlive_version}
Provides:       tex(recipe.cls)
Requires:       tex(book.cls)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source204:      recipe.tar.xz
Source205:      recipe.doc.tar.xz

%description -n texlive-recipe
The layout design is relative straightforward (and traditional:
see 'sample output' under 'documentation'); the class needs
uses the Bookman and BrushScript-Italic fonts.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-recipe-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.9svn15878
Release:        0
Summary:        Documentation for texlive-recipe
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-recipe-doc:it)

%description -n texlive-recipe-doc
This package includes the documentation for texlive-recipe

%post -n texlive-recipe
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-recipe 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-recipe
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-recipe-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/recipe/README
%{_texmfdistdir}/doc/latex/recipe/sample.pdf
%{_texmfdistdir}/doc/latex/recipe/sample.tex

%files -n texlive-recipe
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/recipe/recipe.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-recipe-%{texlive_version}.%{texlive_noarch}.0.0.9svn15878-%{release}-zypper
%endif

%package -n texlive-recipebook
Version:        %{texlive_version}.%{texlive_noarch}.svn37026
Release:        0
Summary:        Typeset 5.5" x 8" recipes for browsing or printing
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-recipebook-doc >= %{texlive_version}
Provides:       tex(RecipeBook.cls)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(anyfontsize.sty)
Requires:       tex(article.cls)
Requires:       tex(booktabs.sty)
Requires:       tex(calc.sty)
Requires:       tex(datetime.sty)
Requires:       tex(environ.sty)
Requires:       tex(eso-pic.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(gensymb.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(multicol.sty)
Requires:       tex(multirow.sty)
Requires:       tex(nicefrac.sty)
Requires:       tex(parskip.sty)
Requires:       tex(picture.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(scrextend.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(tgtermes.sty)
Requires:       tex(tikz.sty)
Requires:       tex(tocloft.sty)
Requires:       tex(wrapfig.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source206:      recipebook.tar.xz
Source207:      recipebook.doc.tar.xz

%description -n texlive-recipebook
This is a LaTeX2e class for typesetting recipes. It is designed
for typesetting one or two recipes per page, with dimensions of
5.5" x 8.5". The hyperlinked table of contents (ToC) and page
numbers make browsing recipes convenient, and the pages can be
joined together or printed two per sheet to normal letterpaper
easily. The size was chosen to work in half-page 3-ring binder
cover sheets.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-recipebook-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn37026
Release:        0
Summary:        Documentation for texlive-recipebook
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-recipebook-doc
This package includes the documentation for texlive-recipebook

%post -n texlive-recipebook
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-recipebook 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-recipebook
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-recipebook-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/recipebook/LongSample.pdf
%{_texmfdistdir}/doc/latex/recipebook/LongSample.tex
%{_texmfdistdir}/doc/latex/recipebook/README
%{_texmfdistdir}/doc/latex/recipebook/ShortSample.pdf
%{_texmfdistdir}/doc/latex/recipebook/ShortSample.tex
%{_texmfdistdir}/doc/latex/recipebook/images/Curried_butternut_squash_soup.jpg
%{_texmfdistdir}/doc/latex/recipebook/images/Curried_chicken_and_rice.jpg
%{_texmfdistdir}/doc/latex/recipebook/images/French_dip.jpg
%{_texmfdistdir}/doc/latex/recipebook/images/Grilled_chicken_with_capers.jpg
%{_texmfdistdir}/doc/latex/recipebook/images/Hawaiian_burgers.jpg
%{_texmfdistdir}/doc/latex/recipebook/images/Italian_calzones.jpg
%{_texmfdistdir}/doc/latex/recipebook/images/Pumpkin_pie_soup.jpg

%files -n texlive-recipebook
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/recipebook/RecipeBook.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-recipebook-%{texlive_version}.%{texlive_noarch}.svn37026-%{release}-zypper
%endif

%package -n texlive-recipecard
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn15878
Release:        0
Summary:        Typeset recipes in note-card-sized boxes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-recipecard-doc >= %{texlive_version}
Provides:       tex(recipecard.cls)
Requires:       tex(boxedminipage.sty)
Requires:       tex(calc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source208:      recipecard.tar.xz
Source209:      recipecard.doc.tar.xz

%description -n texlive-recipecard
The recipecard class typesets recipes into note card sized
boxes that can then be cut out and pasted on to note cards. The
recipe then looks elegant and fits in the box of recipes.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-recipecard-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn15878
Release:        0
Summary:        Documentation for texlive-recipecard
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-recipecard-doc
This package includes the documentation for texlive-recipecard

%post -n texlive-recipecard
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-recipecard 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-recipecard
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-recipecard-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/recipecard/README
%{_texmfdistdir}/doc/latex/recipecard/recipecard.pdf
%{_texmfdistdir}/doc/latex/recipecard/test2.pdf
%{_texmfdistdir}/doc/latex/recipecard/test2.tex

%files -n texlive-recipecard
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/recipecard/recipecard.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-recipecard-%{texlive_version}.%{texlive_noarch}.2.0svn15878-%{release}-zypper
%endif

%package -n texlive-rectopma
Version:        %{texlive_version}.%{texlive_noarch}.svn19980
Release:        0
Summary:        Recycle top matter
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rectopma-doc >= %{texlive_version}
Provides:       tex(rectopma.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source210:      rectopma.tar.xz
Source211:      rectopma.doc.tar.xz

%description -n texlive-rectopma
Saves the arguments of \author and \title for reference (after
\maketitle) in a document. (\maketitle simply disposes of the
information, in the standard classes and some others.)

date: 2016-06-24 17:18:15 +0000


%package -n texlive-rectopma-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn19980
Release:        0
Summary:        Documentation for texlive-rectopma
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rectopma-doc
This package includes the documentation for texlive-rectopma

%post -n texlive-rectopma
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rectopma 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rectopma
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rectopma-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/rectopma/TestTitle.pdf
%{_texmfdistdir}/doc/latex/rectopma/TestTitle.tex

%files -n texlive-rectopma
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/rectopma/rectopma.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rectopma-%{texlive_version}.%{texlive_noarch}.svn19980-%{release}-zypper
%endif

%package -n texlive-recycle
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        A font providing the "recyclable" logo
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires:       texlive-recycle-fonts >= %{texlive_version}
Recommends:     texlive-recycle-doc >= %{texlive_version}
Provides:       tex(recycle.map)
Provides:       tex(recycle.sty)
Provides:       tex(recycle.tfm)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source212:      recycle.tar.xz
Source213:      recycle.doc.tar.xz

%description -n texlive-recycle
This single-character font is provided as Metafont source, and
in Adobe Type 1 format. It is accompanied by a trivial LaTeX
package to use the logo at various sizes.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-recycle-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-recycle
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-recycle-doc
This package includes the documentation for texlive-recycle


%package -n texlive-recycle-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Severed fonts for texlive-recycle
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Fonts
Url:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-recycle-fonts
The  separated fonts package for texlive-recycle
%post -n texlive-recycle
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap recycle.map' >> /var/run/texlive/run-updmap

%postun -n texlive-recycle 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap recycle.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-recycle
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-recycle-fonts
%files -n texlive-recycle-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/recycle/README

%files -n texlive-recycle
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/recycle/recycle.map
%{_texmfdistdir}/fonts/source/public/recycle/recycle.mf
%{_texmfdistdir}/fonts/tfm/public/recycle/recycle.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/recycle/recycle.pfb
%{_texmfdistdir}/tex/latex/recycle/recycle.sty

%files -n texlive-recycle-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-recycle
%config %{_sysconfdir}/fonts/conf.avail/58-texlive-recycle.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-recycle/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-recycle/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-recycle/fonts.scale
%{_datadir}/fonts/texlive-recycle/recycle.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-recycle-fonts-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-refcheck
Version:        %{texlive_version}.%{texlive_noarch}.1.9.1svn29128
Release:        0
Summary:        Check references (in figures, table, equations, etc)
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-refcheck-doc >= %{texlive_version}
Provides:       tex(refcheck.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source214:      refcheck.tar.xz
Source215:      refcheck.doc.tar.xz

%description -n texlive-refcheck
The package checks references in a document, looking for
numbered but unlabelled equations, for labels which are not
used in the text, for unused bibliography references. It can
also display label names in text near corresponding numbers of
equations and/or bibliography references.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-refcheck-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.9.1svn29128
Release:        0
Summary:        Documentation for texlive-refcheck
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-refcheck-doc
This package includes the documentation for texlive-refcheck

%post -n texlive-refcheck
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-refcheck 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-refcheck
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-refcheck-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/refcheck/README
%{_texmfdistdir}/doc/latex/refcheck/refdemo.pdf
%{_texmfdistdir}/doc/latex/refcheck/refdemo.tex

%files -n texlive-refcheck
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/refcheck/refcheck.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-refcheck-%{texlive_version}.%{texlive_noarch}.1.9.1svn29128-%{release}-zypper
%endif

%package -n texlive-refenums
Version:        %{texlive_version}.%{texlive_noarch}.1.1.2svn44131
Release:        0
Summary:        Define named items and provide back-references with that name
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-refenums-doc >= %{texlive_version}
Provides:       tex(refenums.sty)
Requires:       tex(cleveref.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source216:      refenums.tar.xz
Source217:      refenums.doc.tar.xz

%description -n texlive-refenums
The package provides commands to define enumerable items with a
number and a long name, which can be referenced later with the
name or just the short form. For instance, "Milestone M1:
Specification created" can be defined and later on be
referenced with 'M1' or 'M1 ("Specification created")'. The
text in the references is derived from the definition and also
rendered as hyperlink to the definition.

date: 2018-03-10 13:13:43 +0000


%package -n texlive-refenums-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1.2svn44131
Release:        0
Summary:        Documentation for texlive-refenums
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-refenums-doc
This package includes the documentation for texlive-refenums

%post -n texlive-refenums
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-refenums 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-refenums
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-refenums-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/refenums/LICENSE
%{_texmfdistdir}/doc/latex/refenums/README.md
%{_texmfdistdir}/doc/latex/refenums/README.pdf
%{_texmfdistdir}/doc/latex/refenums/demo.pdf
%{_texmfdistdir}/doc/latex/refenums/demo.tex
%{_texmfdistdir}/doc/latex/refenums/test/demo-sec-param.tex

%files -n texlive-refenums
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/refenums/refenums.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-refenums-%{texlive_version}.%{texlive_noarch}.1.1.2svn44131-%{release}-zypper
%endif

%package -n texlive-reflectgraphics
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2csvn40612
Release:        0
Summary:        Techniques for reflecting graphics
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires:       tex(color.cfg)
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-reflectgraphics-doc >= %{texlive_version}
Provides:       tex(reflectgraphics.sty)
Requires:       tex(calc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(keyval.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source218:      reflectgraphics.tar.xz
Source219:      reflectgraphics.doc.tar.xz

%description -n texlive-reflectgraphics
The package provides a macro for reflecting images, in a number
of different ways, in pursuit of "more striking" graphics in a
document.

date: 2017-04-18 03:31:40 +0000


%package -n texlive-reflectgraphics-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2csvn40612
Release:        0
Summary:        Documentation for texlive-reflectgraphics
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-reflectgraphics-doc
This package includes the documentation for texlive-reflectgraphics

%post -n texlive-reflectgraphics
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-reflectgraphics 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-reflectgraphics
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-reflectgraphics-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/reflectgraphics/README
%{_texmfdistdir}/doc/latex/reflectgraphics/example.jpg
%{_texmfdistdir}/doc/latex/reflectgraphics/reflectgraphics.pdf

%files -n texlive-reflectgraphics
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/reflectgraphics/reflectgraphics.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-reflectgraphics-%{texlive_version}.%{texlive_noarch}.0.0.2csvn40612-%{release}-zypper
%endif

%package -n texlive-refman
Version:        %{texlive_version}.%{texlive_noarch}.2.0esvn15878
Release:        0
Summary:        Format technical reference manuals
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-refman-doc >= %{texlive_version}
Provides:       tex(pagepc.sty)
Provides:       tex(refart.cls)
Provides:       tex(refrep.cls)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source220:      refman.tar.xz
Source221:      refman.doc.tar.xz

%description -n texlive-refman
Document classes (report- and article-style) for writing
technical reference manuals. It offers a wide left margin for
notes to the reader, like some of the manuals distributed by
Adobe.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-refman-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0esvn15878
Release:        0
Summary:        Documentation for texlive-refman
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-refman-doc:de;en)

%description -n texlive-refman-doc
This package includes the documentation for texlive-refman

%post -n texlive-refman
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-refman 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-refman
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-refman-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/refman/00Contents
%{_texmfdistdir}/doc/latex/refman/lay_d2.tex
%{_texmfdistdir}/doc/latex/refman/lay_e2.tex
%{_texmfdistdir}/doc/latex/refman/layout_d.pdf
%{_texmfdistdir}/doc/latex/refman/layout_d.tex
%{_texmfdistdir}/doc/latex/refman/layout_e.pdf
%{_texmfdistdir}/doc/latex/refman/layout_e.tex
%{_texmfdistdir}/doc/latex/refman/refman.pdf
%{_texmfdistdir}/doc/latex/refman/refman.upl

%files -n texlive-refman
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/refman/pagepc.sty
%{_texmfdistdir}/tex/latex/refman/refart.cls
%{_texmfdistdir}/tex/latex/refman/refrep.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-refman-%{texlive_version}.%{texlive_noarch}.2.0esvn15878-%{release}-zypper
%endif

%package -n texlive-refstyle
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn20318
Release:        0
Summary:        Advanced formatting of cross references
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-refstyle-doc >= %{texlive_version}
Provides:       tex(refstyle.cfg)
Provides:       tex(refstyle.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source222:      refstyle.tar.xz
Source223:      refstyle.doc.tar.xz

%description -n texlive-refstyle
The package provides a consistent way of producing references
throughout a project. Enough flexibility is provided to make
local changes to a single reference. The user can configure
their own setup. The package offers a direct interface to
varioref (for use, for example, in large projects such as a
series of books, or a multivolume thesis written as a series of
documents), and name references from the nameref package may be
incorporated with ease. For large projects such as a series of
books or a multi volume thesis, written as freestanding
documents, a facility is provided to interface to the xr
package for external document references.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-refstyle-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn20318
Release:        0
Summary:        Documentation for texlive-refstyle
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-refstyle-doc
This package includes the documentation for texlive-refstyle

%post -n texlive-refstyle
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-refstyle 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-refstyle
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-refstyle-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/refstyle/README
%{_texmfdistdir}/doc/latex/refstyle/refconfig.pdf
%{_texmfdistdir}/doc/latex/refstyle/refstyle.pdf

%files -n texlive-refstyle
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/refstyle/refstyle.cfg
%{_texmfdistdir}/tex/latex/refstyle/refstyle.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-refstyle-%{texlive_version}.%{texlive_noarch}.0.0.5svn20318-%{release}-zypper
%endif

%package -n texlive-regcount
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn19979
Release:        0
Summary:        Display the allocation status of the TeX registers
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-regcount-doc >= %{texlive_version}
Provides:       tex(regcount.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source224:      regcount.tar.xz
Source225:      regcount.doc.tar.xz

%description -n texlive-regcount
Adds a macro \rgcounts which displays the allocation status of
the TeX registers. The display is written into the .log file as
it is a bit verbose. An automatic call to \rgcounts is done at
\begin{document} and \end{document}.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-regcount-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn19979
Release:        0
Summary:        Documentation for texlive-regcount
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-regcount-doc
This package includes the documentation for texlive-regcount

%post -n texlive-regcount
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-regcount 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-regcount
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-regcount-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/regcount/readme
%{_texmfdistdir}/doc/latex/regcount/regcount.pdf

%files -n texlive-regcount
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/regcount/regcount.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-regcount-%{texlive_version}.%{texlive_noarch}.1.0svn19979-%{release}-zypper
%endif

%package -n texlive-regexpatch
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2dsvn47601
Release:        0
Summary:        High level patching of commands
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-regexpatch-doc >= %{texlive_version}
Provides:       tex(regexpatch.sty)
Requires:       tex(expl3.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source226:      regexpatch.tar.xz
Source227:      regexpatch.doc.tar.xz

%description -n texlive-regexpatch
The package generalises the macro patching commands provided by
P. Lehmann's etoolbox. The difference between this package and
its sibling xpatch is that this package sports a very powerful
\regexpatchcmd based on the l3regex module of the LaTeX3
experimental packages.

date: 2018-05-03 06:29:38 +0000


%package -n texlive-regexpatch-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2dsvn47601
Release:        0
Summary:        Documentation for texlive-regexpatch
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-regexpatch-doc
This package includes the documentation for texlive-regexpatch

%post -n texlive-regexpatch
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-regexpatch 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-regexpatch
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-regexpatch-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/regexpatch/README
%{_texmfdistdir}/doc/latex/regexpatch/regexpatch.pdf

%files -n texlive-regexpatch
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/regexpatch/regexpatch.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-regexpatch-%{texlive_version}.%{texlive_noarch}.0.0.2dsvn47601-%{release}-zypper
%endif

%package -n texlive-register
Version:        %{texlive_version}.%{texlive_noarch}.1.9svn49581
Release:        0
Summary:        Typeset programmable elements in digital hardware (registers)
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-register-doc >= %{texlive_version}
Provides:       tex(register.sty)
Requires:       tex(calc.sty)
Requires:       tex(float.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source228:      register.tar.xz
Source229:      register.doc.tar.xz

%description -n texlive-register
This package is designed for typesetting the programmable
elements in digital hardware, i.e. registers. Such registers
typically have many fields and can be quite wide; they are thus
a challenge to typeset in a consistent manner. Register is
similar in some aspects to the bytefield package. Anyone doing
hardware documentation using LaTeX should examine both
packages. Register requires a fairly recent version of the
float package. An example Perl module and a Perl script are
provided to translate the register specifications into
programmable data structures.

date: 2019-01-01 22:34:54 +0000


%package -n texlive-register-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.9svn49581
Release:        0
Summary:        Documentation for texlive-register
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-register-doc
This package includes the documentation for texlive-register

%post -n texlive-register
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-register 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-register
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-register-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/register/README
%{_texmfdistdir}/doc/latex/register/Reg_macro.pm
%{_texmfdistdir}/doc/latex/register/reg_list.pl
%{_texmfdistdir}/doc/latex/register/register.pdf

%files -n texlive-register
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/register/register.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-register-%{texlive_version}.%{texlive_noarch}.1.9svn49581-%{release}-zypper
%endif

%package -n texlive-regstats
Version:        %{texlive_version}.%{texlive_noarch}.1.0hsvn25050
Release:        0
Summary:        Information about register use
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-regstats-doc >= %{texlive_version}
Provides:       tex(regstats.sty)
Requires:       tex(atveryend.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(intcalc.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(ltxcmds.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source230:      regstats.tar.xz
Source231:      regstats.doc.tar.xz

%description -n texlive-regstats
The package will report number of used registers (counter,
dimen, skip, muskip, box, token, input, output, math families,
languages, insertions), and will compare the number to the
maximum available number of such registers.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-regstats-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0hsvn25050
Release:        0
Summary:        Documentation for texlive-regstats
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-regstats-doc
This package includes the documentation for texlive-regstats

%post -n texlive-regstats
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-regstats 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-regstats
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-regstats-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/regstats/README
%{_texmfdistdir}/doc/latex/regstats/regstats-example.log
%{_texmfdistdir}/doc/latex/regstats/regstats-example.pdf
%{_texmfdistdir}/doc/latex/regstats/regstats-example.tex
%{_texmfdistdir}/doc/latex/regstats/regstats.pdf

%files -n texlive-regstats
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/regstats/regstats.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-regstats-%{texlive_version}.%{texlive_noarch}.1.0hsvn25050-%{release}-zypper
%endif

%package -n texlive-reledmac
Version:        %{texlive_version}.%{texlive_noarch}.2.31.2svn50740
Release:        0
Summary:        Typeset scholarly editions
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-reledmac-doc >= %{texlive_version}
Provides:       tex(reledmac.sty)
Provides:       tex(reledpar.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(suffix.sty)
Requires:       tex(xargs.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xspace.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source232:      reledmac.tar.xz
Source233:      reledmac.doc.tar.xz

%description -n texlive-reledmac
A package for typesetting scholarly critical editions,
replacing the established ledmac and eledmac packages. Ledmac
itself was a LaTeX port of the plain TeX EDMAC macros. The
package supports indexing by page and by line numbers, and
simple tabular- and array-style environments. The package is
distributed with the related reledpar package.

date: 2019-04-03 13:10:43 +0000


%package -n texlive-reledmac-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.31.2svn50740
Release:        0
Summary:        Documentation for texlive-reledmac
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-reledmac-doc
This package includes the documentation for texlive-reledmac

%post -n texlive-reledmac
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-reledmac 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-reledmac
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-reledmac-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/reledmac/README
%{_texmfdistdir}/doc/latex/reledmac/doc-include/migrate-mac.dtx
%{_texmfdistdir}/doc/latex/reledmac/doc-include/migrate-par.dtx
%{_texmfdistdir}/doc/latex/reledmac/doc-more/latexmkrc
%{_texmfdistdir}/doc/latex/reledmac/doc-more/makefile
%{_texmfdistdir}/doc/latex/reledmac/doc-more/page-typesetting-columns.pdf
%{_texmfdistdir}/doc/latex/reledmac/doc-more/page-typesetting-columns.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/1-criticalendotes.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/1-criticalendotes.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/1-criticalnotes.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/1-criticalnotes.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/1-sidenotes.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/1-sidenotes.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/1-tabular.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/1-tabular.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/1-verses-doublenumbering.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/1-verses-doublenumbering.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/1-verses.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/1-verses.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/2-cross_referencing.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/2-cross_referencing.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/2-footnote_spacing.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/2-footnote_spacing.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/2-glossaries.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/2-glossaries.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/2-indexing.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/2-indexing.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/2-lemma_disambigution.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/2-lemma_disambigution.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/2-line_numbers_in_header.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/2-line_numbers_in_header.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/2-linespacing.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/2-linespacing.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/2-manuscript-apparatus.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/2-manuscript-apparatus.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/2-notes-width.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/2-notes-width.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/2-one_series_per_pstart.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/2-one_series_per_pstart.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/2-performances.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/2-performances.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/2-reledmac-right-to-left.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/2-reledmac-right-to-left.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/2-subdivision-number-in-header.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/2-subdivision-number-in-header.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/2-titles_in_line_numbering_with_notes.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/2-titles_in_line_numbering_with_notes.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/2-titles_not_in_line_numbering.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/2-titles_not_in_line_numbering.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/3-reledpar_columns_different_languages.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/3-reledpar_columns_different_languages.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/3-reledpar_mwe.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/3-reledpar_mwe.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/3-reledpar_pages_different_languages_lualatex.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/3-reledpar_pages_different_languages_lualatex.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/3-reledpar_same_page_number_in_both_side.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/3-reledpar_same_page_number_in_both_side.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/3-reledpar_sync_setting_advancedshifted-nomax.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/3-reledpar_sync_setting_advancedshifted-nomax.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/3-reledpar_sync_setting_advancedshifted.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/3-reledpar_sync_setting_advancedshifted.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/3-reledpar_sync_setting_default.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/3-reledpar_sync_setting_default.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/3-reledpar_sync_setting_nomax-shifted.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/3-reledpar_sync_setting_nomax-shifted.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/3-reledpar_sync_setting_nomax.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/3-reledpar_sync_setting_nomax.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/3-reledpar_sync_setting_nosync.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/3-reledpar_sync_setting_nosync.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/3-reledpar_sync_setting_shifted.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/3-reledpar_sync_setting_shifted.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_column_mix_with_not_column-continuous-numbering.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_column_mix_with_not_column-continuous-numbering.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_column_mix_with_not_column.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_column_mix_with_not_column.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_columns_alignment.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_columns_alignment.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_columns_titles_in_line_numbering_with_notes.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_columns_titles_in_line_numbering_with_notes.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_inside-outside-columns.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_inside-outside-columns.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_one_series_per_pstart.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_one_series_per_pstart.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_pages_long_notes.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_pages_long_notes.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_pages_notes_leftpage.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_pages_notes_leftpage.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_pages_paragraph_separator_between.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_pages_paragraph_separator_between.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_pages_titles_in_line_numbering_with_notes.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_pages_titles_in_line_numbering_with_notes.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_titles_not_in_line_numbering.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_titles_not_in_line_numbering.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_verse_text_between.pdf
%{_texmfdistdir}/doc/latex/reledmac/examples/4-reledpar_verse_text_between.tex
%{_texmfdistdir}/doc/latex/reledmac/examples/latexmkrc
%{_texmfdistdir}/doc/latex/reledmac/examples/makefile
%{_texmfdistdir}/doc/latex/reledmac/examples/reledmac.xdy
%{_texmfdistdir}/doc/latex/reledmac/latexmkrc
%{_texmfdistdir}/doc/latex/reledmac/makefile
%{_texmfdistdir}/doc/latex/reledmac/migration.pdf
%{_texmfdistdir}/doc/latex/reledmac/reledmac.pdf
%{_texmfdistdir}/doc/latex/reledmac/reledpar.pdf

%files -n texlive-reledmac
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/reledmac/reledmac.sty
%{_texmfdistdir}/tex/latex/reledmac/reledpar.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-reledmac-%{texlive_version}.%{texlive_noarch}.2.31.2svn50740-%{release}-zypper
%endif

%package -n texlive-relenc
Version:        %{texlive_version}.%{texlive_noarch}.svn22050
Release:        0
Summary:        A "relaxed" font encoding
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-relenc-doc >= %{texlive_version}
Provides:       tex(2sidedoc.sty)
Provides:       tex(ecsubzcm.sty)
Provides:       tex(relenc.sty)
Provides:       tex(t1renc.def)
Provides:       tex(t1rzcm.fd)
Provides:       tex(zcmr8d.tfm)
Provides:       tex(zcmr8d.vf)
Provides:       tex(zcmra.tfm)
Provides:       tex(zcmra.vf)
Requires:       tex(cmmi10.tfm)
Requires:       tex(cmr10.tfm)
Requires:       tex(cmr5.tfm)
Requires:       tex(cmr6.tfm)
Requires:       tex(cmsy10.tfm)
Requires:       tex(cmtt10.tfm)
Requires:       tex(cmu10.tfm)
Requires:       tex(lasy10.tfm)
Requires:       tex(lcircle10.tfm)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source234:      relenc.tar.xz
Source235:      relenc.doc.tar.xz

%description -n texlive-relenc
LaTeX package providing a relaxed font encoding to make
available to a font designer more slots for insertion of
ligatures and accented characters.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-relenc-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn22050
Release:        0
Summary:        Documentation for texlive-relenc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-relenc-doc
This package includes the documentation for texlive-relenc

%post -n texlive-relenc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-relenc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-relenc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-relenc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/relenc/README
%{_texmfdistdir}/doc/latex/relenc/reldemo.tex
%{_texmfdistdir}/doc/latex/relenc/relenc.tex
%{_texmfdistdir}/doc/latex/relenc/zcmr8d.vf2
%{_texmfdistdir}/doc/latex/relenc/zcmr8d.vf3
%{_texmfdistdir}/doc/latex/relenc/zcmra.vf2
%{_texmfdistdir}/doc/latex/relenc/zcmra.vf3

%files -n texlive-relenc
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/tfm/public/relenc/zcmr8d.tfm
%{_texmfdistdir}/fonts/tfm/public/relenc/zcmra.tfm
%{_texmfdistdir}/fonts/vf/public/relenc/zcmr8d.vf
%{_texmfdistdir}/fonts/vf/public/relenc/zcmra.vf
%{_texmfdistdir}/tex/latex/relenc/2sidedoc.sty
%{_texmfdistdir}/tex/latex/relenc/ecsubzcm.sty
%{_texmfdistdir}/tex/latex/relenc/relenc.sty
%{_texmfdistdir}/tex/latex/relenc/t1renc.def
%{_texmfdistdir}/tex/latex/relenc/t1rzcm.fd
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-relenc-%{texlive_version}.%{texlive_noarch}.svn22050-%{release}-zypper
%endif

%package -n texlive-relsize
Version:        %{texlive_version}.%{texlive_noarch}.4.1svn30707
Release:        0
Summary:        Set the font size relative to the current font size
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-relsize-doc >= %{texlive_version}
Provides:       tex(relsize.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source236:      relsize.tar.xz
Source237:      relsize.doc.tar.xz

%description -n texlive-relsize
The basic command of the package is \relsize, whose argument is
a number of \magsteps to change size; from this are defined
commands \larger, \smaller, \textlarger, etc.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-relsize-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.1svn30707
Release:        0
Summary:        Documentation for texlive-relsize
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-relsize-doc
This package includes the documentation for texlive-relsize

%post -n texlive-relsize
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-relsize 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-relsize
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-relsize-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/relsize/README
%{_texmfdistdir}/doc/latex/relsize/relsize-doc.pdf
%{_texmfdistdir}/doc/latex/relsize/relsize-doc.tex

%files -n texlive-relsize
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/relsize/relsize.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-relsize-%{texlive_version}.%{texlive_noarch}.4.1svn30707-%{release}-zypper
%endif

%package -n texlive-reotex
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn34924
Release:        0
Summary:        Draw Reo Channels and Circuits
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-reotex-doc >= %{texlive_version}
Provides:       tex(reotex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
Requires:       tex(verbatim.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source238:      reotex.tar.xz
Source239:      reotex.doc.tar.xz

%description -n texlive-reotex
The package defines macros and other utilities to design Reo
Circuits. The package requires PGF/TikZ support.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-reotex-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn34924
Release:        0
Summary:        Documentation for texlive-reotex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-reotex-doc
This package includes the documentation for texlive-reotex

%post -n texlive-reotex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-reotex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-reotex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-reotex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/reotex/README
%{_texmfdistdir}/doc/latex/reotex/reotex.pdf
%{_texmfdistdir}/doc/latex/reotex/reotex.tex

%files -n texlive-reotex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/reotex/reotex.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-reotex-%{texlive_version}.%{texlive_noarch}.1.1svn34924-%{release}-zypper
%endif

%package -n texlive-repeatindex
Version:        %{texlive_version}.%{texlive_noarch}.0.0.01svn24305
Release:        0
Summary:        Repeat items in an index after a page or column break
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-repeatindex-doc >= %{texlive_version}
Provides:       tex(repeatindex.sty)
Requires:       tex(afterpage.sty)
Requires:       tex(makeidx.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source240:      repeatindex.tar.xz
Source241:      repeatindex.doc.tar.xz

%description -n texlive-repeatindex
This Package repeats item of an index if a page or column break
occurs within a list of subitems. This helps to find out to
which main item a subitem belongs.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-repeatindex-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.01svn24305
Release:        0
Summary:        Documentation for texlive-repeatindex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-repeatindex-doc
This package includes the documentation for texlive-repeatindex

%post -n texlive-repeatindex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-repeatindex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-repeatindex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-repeatindex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/repeatindex/README
%{_texmfdistdir}/doc/latex/repeatindex/testrepeatindex.tex

%files -n texlive-repeatindex
%defattr(-,root,root,755)
%{_texmfdistdir}/makeindex/repeatindex/repeatindex.ist
%{_texmfdistdir}/tex/latex/repeatindex/repeatindex.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-repeatindex-%{texlive_version}.%{texlive_noarch}.0.0.01svn24305-%{release}-zypper
%endif

%package -n texlive-repere
Version:        %{texlive_version}.%{texlive_noarch}.17.11.2svn45779
Release:        0
Summary:        Diagrams for school mathematics
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-repere-doc >= %{texlive_version}
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source242:      repere.tar.xz
Source243:      repere.doc.tar.xz

%description -n texlive-repere
This package provides MetaPost macros for drawing secondary
school mathematics figures in a coordinate system: axis, grids
points, vectors functions (curves, tangents, integrals,
sequences) statistic diagrams plane geometry (polygons,
circles)

date: 2017-11-12 21:58:02 +0000


%package -n texlive-repere-doc
Version:        %{texlive_version}.%{texlive_noarch}.17.11.2svn45779
Release:        0
Summary:        Documentation for texlive-repere
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-repere-doc:fr)

%description -n texlive-repere-doc
This package includes the documentation for texlive-repere

%post -n texlive-repere
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-repere 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-repere
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-repere-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/metapost/repere/README.md
%{_texmfdistdir}/doc/metapost/repere/repere-doc.pdf
%{_texmfdistdir}/doc/metapost/repere/repere-doc.tex

%files -n texlive-repere
%defattr(-,root,root,755)
%{_texmfdistdir}/metapost/repere/repere.mp
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-repere-%{texlive_version}.%{texlive_noarch}.17.11.2svn45779-%{release}-zypper
%endif

%package -n texlive-repltext
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn33442
Release:        0
Summary:        Control how text gets copied from a PDF file
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-repltext-doc >= %{texlive_version}
Provides:       tex(repltext.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source244:      repltext.tar.xz
Source245:      repltext.doc.tar.xz

%description -n texlive-repltext
The repltext package exposes to LaTeX a relatively obscure PDF
feature: replacement text. When replacement text is specified
for a piece of text, it is the replacement text, not the
typeset text that is copied and pasted.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-repltext-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn33442
Release:        0
Summary:        Documentation for texlive-repltext
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-repltext-doc
This package includes the documentation for texlive-repltext

%post -n texlive-repltext
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-repltext 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-repltext
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-repltext-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/repltext/README
%{_texmfdistdir}/doc/latex/repltext/repltext.pdf

%files -n texlive-repltext
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/repltext/repltext.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-repltext-%{texlive_version}.%{texlive_noarch}.1.0svn33442-%{release}-zypper
%endif

%package -n texlive-resphilosophica
Version:        %{texlive_version}.%{texlive_noarch}.1.34svn50402
Release:        0
Summary:        Typeset articles for the journal Res Philosophica
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-resphilosophica-doc >= %{texlive_version}
Provides:       tex(resphilosophica.cls)
Requires:       tex(amsart.cls)
Requires:       tex(collect.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(footmisc.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(lastpage.sty)
Requires:       tex(mathdesign.sty)
Requires:       tex(microtype.sty)
Requires:       tex(natbib.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source246:      resphilosophica.tar.xz
Source247:      resphilosophica.doc.tar.xz

%description -n texlive-resphilosophica
The bundle provides a class for typesetting articles for the
journal Res Philosophica. This work was commissioned by the
Saint Louis University.

date: 2019-03-15 07:43:01 +0000


%package -n texlive-resphilosophica-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.34svn50402
Release:        0
Summary:        Documentation for texlive-resphilosophica
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-resphilosophica-doc
This package includes the documentation for texlive-resphilosophica

%post -n texlive-resphilosophica
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-resphilosophica 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-resphilosophica
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-resphilosophica-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/resphilosophica/README
%{_texmfdistdir}/doc/latex/resphilosophica/resphilosophica.bib
%{_texmfdistdir}/doc/latex/resphilosophica/resphilosophica.pdf
%{_texmfdistdir}/doc/latex/resphilosophica/rpsample.bib
%{_texmfdistdir}/doc/latex/resphilosophica/rpsample.pdf
%{_texmfdistdir}/doc/latex/resphilosophica/rpsample.tex

%files -n texlive-resphilosophica
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/resphilosophica/resphilosophica.bst
%{_texmfdistdir}/tex/latex/resphilosophica/resphilosophica.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-resphilosophica-%{texlive_version}.%{texlive_noarch}.1.34svn50402-%{release}-zypper
%endif

%package -n texlive-resumecls
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3.2svn38427
Release:        0
Summary:        Typeset a resume both in English and Chinese
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-resumecls-doc >= %{texlive_version}
Provides:       tex(resumecls.cls)
Requires:       tex(article.cls)
Requires:       tex(color.sty)
Requires:       tex(ctex.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(geometry.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(natbib.sty)
Requires:       tex(tabularx.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source248:      resumecls.tar.xz
Source249:      resumecls.doc.tar.xz

%description -n texlive-resumecls
This LaTeX class makes typeseting a resume or cv both in
English and Chinese more easy.

date: 2017-04-18 03:31:40 +0000


%package -n texlive-resumecls-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3.2svn38427
Release:        0
Summary:        Documentation for texlive-resumecls
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-resumecls-doc
This package includes the documentation for texlive-resumecls

%post -n texlive-resumecls
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-resumecls 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-resumecls
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-resumecls-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/xelatex/resumecls/Makefile
%{_texmfdistdir}/doc/xelatex/resumecls/README.md
%{_texmfdistdir}/doc/xelatex/resumecls/example/Makefile
%{_texmfdistdir}/doc/xelatex/resumecls/example/README.md
%{_texmfdistdir}/doc/xelatex/resumecls/example/config-sample.mk
%{_texmfdistdir}/doc/xelatex/resumecls/example/config.mk
%{_texmfdistdir}/doc/xelatex/resumecls/example/resume-en.pdf
%{_texmfdistdir}/doc/xelatex/resumecls/example/resume-en.tex
%{_texmfdistdir}/doc/xelatex/resumecls/example/resume-zh.pdf
%{_texmfdistdir}/doc/xelatex/resumecls/example/resume-zh.tex
%{_texmfdistdir}/doc/xelatex/resumecls/example/resume.bib
%{_texmfdistdir}/doc/xelatex/resumecls/resumecls.pdf

%files -n texlive-resumecls
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/xelatex/resumecls/resumecls.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-resumecls-%{texlive_version}.%{texlive_noarch}.0.0.3.2svn38427-%{release}-zypper
%endif

%package -n texlive-resumemac
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Plain TeX macros for resumes
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-resumemac-doc >= %{texlive_version}
Provides:       tex(resumemac.tex)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source250:      resumemac.tar.xz
Source251:      resumemac.doc.tar.xz

%description -n texlive-resumemac
A set of macros is provided, together with an file that offers
an example of use.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-resumemac-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-resumemac
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-resumemac-doc
This package includes the documentation for texlive-resumemac

%post -n texlive-resumemac
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-resumemac 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-resumemac
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-resumemac-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/plain/resumemac/README
%{_texmfdistdir}/doc/plain/resumemac/sample_resume.tex

%files -n texlive-resumemac
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/plain/resumemac/resumemac.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-resumemac-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-returntogrid
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn48485
Release:        0
Summary:        Semi-automatic grid typesetting
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-returntogrid-doc >= %{texlive_version}
Provides:       tex(returntogrid.sty)
Requires:       tex(eso-pic.sty)
Requires:       tex(xparse.sty)
Requires:       tex(zref-abspage.sty)
Requires:       tex(zref-savepos.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source252:      returntogrid.tar.xz
Source253:      returntogrid.doc.tar.xz

%description -n texlive-returntogrid
returntogrid offers a few commands to get something like an
simple, semi-automatic grid typesetting. It does more or less
what the existing gridset package does. The main differences to
gridset are that returntogrid works also with LuaLaTeX and that
it has also a command to do some horizontal movements to get to
"tab" positions.

date: 2018-08-24 03:44:41 +0000


%package -n texlive-returntogrid-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn48485
Release:        0
Summary:        Documentation for texlive-returntogrid
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-returntogrid-doc
This package includes the documentation for texlive-returntogrid

%post -n texlive-returntogrid
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-returntogrid 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-returntogrid
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-returntogrid-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/returntogrid/README.md
%{_texmfdistdir}/doc/latex/returntogrid/returntogrid.pdf
%{_texmfdistdir}/doc/latex/returntogrid/returntogrid.tex

%files -n texlive-returntogrid
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/returntogrid/returntogrid.lua
%{_texmfdistdir}/tex/latex/returntogrid/returntogrid.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-returntogrid-%{texlive_version}.%{texlive_noarch}.0.0.2svn48485-%{release}-zypper
%endif

%package -n texlive-reverxii
Version:        %{texlive_version}.%{texlive_noarch}.svn24976
Release:        0
Summary:        Playing Reversi in TeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source254:      reverxii.doc.tar.xz

%description -n texlive-reverxii
Following the lead of xii.tex, this little (938 characters)
program that plays Reversi. (The program incorporates some
primitive AI.)

date: 2016-06-24 17:18:15 +0000

%post -n texlive-reverxii
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-reverxii 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-reverxii
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-reverxii
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/plain/reverxii/README
%{_texmfdistdir}/doc/plain/reverxii/reverxii.pdf
%{_texmfdistdir}/doc/plain/reverxii/reverxii.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-reverxii-%{texlive_version}.%{texlive_noarch}.svn24976-%{release}-zypper
%endif

%package -n texlive-revquantum
Version:        %{texlive_version}.%{texlive_noarch}.0.0.11svn43505
Release:        0
Summary:        Hacks to make writing quantum papers for revtex4-1 less painful
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-revquantum-doc >= %{texlive_version}
Provides:       tex(revquantum.sty)
Requires:       tex(algorithm.sty)
Requires:       tex(algpseudocode.sty)
Requires:       tex(amsbsy.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(babel.sty)
Requires:       tex(braket.sty)
Requires:       tex(color.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(letltxmacro.sty)
Requires:       tex(listings.sty)
Requires:       tex(mathpazo.sty)
Requires:       tex(sourcecodepro.sty)
Requires:       tex(stmaryrd.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source255:      revquantum.tar.xz
Source256:      revquantum.doc.tar.xz

%description -n texlive-revquantum
This package provides a number of useful hacks to solve common
annoyances with the revtex4-1 package, and to define notation
in common use within quantum information. In doing so, it
imports and configures a number of commonly-available and used
packages, and where reasonable, provides fallbacks. It also
warns when users try to load packages which are known to be
incompatible with revtex4-1.

date: 2018-01-06 11:14:59 +0000


%package -n texlive-revquantum-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.11svn43505
Release:        0
Summary:        Documentation for texlive-revquantum
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-revquantum-doc
This package includes the documentation for texlive-revquantum

%post -n texlive-revquantum
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-revquantum 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-revquantum
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-revquantum-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/revquantum/Install.ps1
%{_texmfdistdir}/doc/latex/revquantum/README.md
%{_texmfdistdir}/doc/latex/revquantum/example.pdf
%{_texmfdistdir}/doc/latex/revquantum/example.tex
%{_texmfdistdir}/doc/latex/revquantum/revquantum.pdf

%files -n texlive-revquantum
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/revquantum/revquantum.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-revquantum-%{texlive_version}.%{texlive_noarch}.0.0.11svn43505-%{release}-zypper
%endif

%package -n texlive-revtex
Version:        %{texlive_version}.%{texlive_noarch}.4.2csvn49751
Release:        0
Summary:        Styles for various Physics Journals
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-revtex-doc >= %{texlive_version}
Provides:       tex(aapm4-2.rtx)
Provides:       tex(aip4-1.rtx)
Provides:       tex(aip4-2.rtx)
Provides:       tex(aps10pt4-1.rtx)
Provides:       tex(aps10pt4-2.rtx)
Provides:       tex(aps11pt4-1.rtx)
Provides:       tex(aps11pt4-2.rtx)
Provides:       tex(aps12pt4-1.rtx)
Provides:       tex(aps12pt4-2.rtx)
Provides:       tex(aps4-1.rtx)
Provides:       tex(aps4-2.rtx)
Provides:       tex(apsrmp4-1.rtx)
Provides:       tex(apsrmp4-2.rtx)
Provides:       tex(ltxdocext.sty)
Provides:       tex(ltxfront.sty)
Provides:       tex(ltxgrid.sty)
Provides:       tex(ltxutil.sty)
Provides:       tex(reftest4-2.tex)
Provides:       tex(revsymb4-1.sty)
Provides:       tex(revsymb4-2.sty)
Provides:       tex(revtex4-1.cls)
Provides:       tex(revtex4-2.cls)
Provides:       tex(sor4-2.rtx)
Requires:       tex(fleqn.clo)
Requires:       tex(lineno.sty)
Requires:       tex(natbib.sty)
Requires:       tex(shortvrb.sty)
Requires:       tex(textcase.sty)
Requires:       tex(url.sty)
Requires:       tex(verbatim.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source257:      revtex.tar.xz
Source258:      revtex.doc.tar.xz

%description -n texlive-revtex
Includes styles for American Physical Society, American
Institute of Physics, and Optical Society of America. The
distribution consists of the RevTeX class itself, and several
support packages.

date: 2019-01-18 21:11:36 +0000


%package -n texlive-revtex-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.2csvn49751
Release:        0
Summary:        Documentation for texlive-revtex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-revtex-doc
This package includes the documentation for texlive-revtex

%post -n texlive-revtex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-revtex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-revtex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-revtex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/revtex/README
%{_texmfdistdir}/doc/latex/revtex/aip/aipguide4-2.pdf
%{_texmfdistdir}/doc/latex/revtex/aip/aipguide4-2.tex
%{_texmfdistdir}/doc/latex/revtex/aps/apsguide4-2.pdf
%{_texmfdistdir}/doc/latex/revtex/aps/apsguide4-2.tex
%{_texmfdistdir}/doc/latex/revtex/auguide/auguide4-2.pdf
%{_texmfdistdir}/doc/latex/revtex/auguide/auguide4-2.tex
%{_texmfdistdir}/doc/latex/revtex/auguide/docs.sty
%{_texmfdistdir}/doc/latex/revtex/auguide/summary4-2.pdf
%{_texmfdistdir}/doc/latex/revtex/auguide/summary4-2.tex
%{_texmfdistdir}/doc/latex/revtex/sample/aapm/aapmsamp.bib
%{_texmfdistdir}/doc/latex/revtex/sample/aapm/aapmsamp.pdf
%{_texmfdistdir}/doc/latex/revtex/sample/aapm/aapmsamp.tex
%{_texmfdistdir}/doc/latex/revtex/sample/aapm/aapmtemplate.tex
%{_texmfdistdir}/doc/latex/revtex/sample/aapm/fig_1.eps
%{_texmfdistdir}/doc/latex/revtex/sample/aapm/fig_2.eps
%{_texmfdistdir}/doc/latex/revtex/sample/aip/aipsamp.bib
%{_texmfdistdir}/doc/latex/revtex/sample/aip/aipsamp.pdf
%{_texmfdistdir}/doc/latex/revtex/sample/aip/aipsamp.tex
%{_texmfdistdir}/doc/latex/revtex/sample/aip/aiptemplate.tex
%{_texmfdistdir}/doc/latex/revtex/sample/aip/fig_1.eps
%{_texmfdistdir}/doc/latex/revtex/sample/aip/fig_2.eps
%{_texmfdistdir}/doc/latex/revtex/sample/aps/apssamp.bib
%{_texmfdistdir}/doc/latex/revtex/sample/aps/apssamp.pdf
%{_texmfdistdir}/doc/latex/revtex/sample/aps/apssamp.tex
%{_texmfdistdir}/doc/latex/revtex/sample/aps/apstemplate.tex
%{_texmfdistdir}/doc/latex/revtex/sample/aps/fig_1.eps
%{_texmfdistdir}/doc/latex/revtex/sample/aps/fig_2.eps
%{_texmfdistdir}/doc/latex/revtex/sample/aps/vid_1a.eps
%{_texmfdistdir}/doc/latex/revtex/sample/aps/vid_1b.eps
%{_texmfdistdir}/doc/latex/revtex/sample/sor/fig_1.eps
%{_texmfdistdir}/doc/latex/revtex/sample/sor/fig_2.eps
%{_texmfdistdir}/doc/latex/revtex/sample/sor/sorsamp.bib
%{_texmfdistdir}/doc/latex/revtex/sample/sor/sorsamp.pdf
%{_texmfdistdir}/doc/latex/revtex/sample/sor/sorsamp.tex
%{_texmfdistdir}/doc/latex/revtex/sample/sor/sortemplate.tex
%{_texmfdistdir}/doc/latex/revtex/source/aip4-2.pdf
%{_texmfdistdir}/doc/latex/revtex/source/ltxdocext.pdf
%{_texmfdistdir}/doc/latex/revtex/source/ltxfront.pdf
%{_texmfdistdir}/doc/latex/revtex/source/ltxgrid.pdf
%{_texmfdistdir}/doc/latex/revtex/source/ltxutil.pdf
%{_texmfdistdir}/doc/latex/revtex/source/revtex4-2.pdf

%files -n texlive-revtex
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/revtex/aapmrev4-2.bst
%{_texmfdistdir}/bibtex/bst/revtex/aipauth4-1.bst
%{_texmfdistdir}/bibtex/bst/revtex/aipauth4-2.bst
%{_texmfdistdir}/bibtex/bst/revtex/aipnum4-1.bst
%{_texmfdistdir}/bibtex/bst/revtex/aipnum4-2.bst
%{_texmfdistdir}/bibtex/bst/revtex/apsrev4-1.bst
%{_texmfdistdir}/bibtex/bst/revtex/apsrev4-2.bst
%{_texmfdistdir}/bibtex/bst/revtex/apsrmp4-1.bst
%{_texmfdistdir}/bibtex/bst/revtex/apsrmp4-2.bst
%{_texmfdistdir}/tex/latex/revtex/aapm4-2.rtx
%{_texmfdistdir}/tex/latex/revtex/aip4-1.rtx
%{_texmfdistdir}/tex/latex/revtex/aip4-2.rtx
%{_texmfdistdir}/tex/latex/revtex/aps10pt4-1.rtx
%{_texmfdistdir}/tex/latex/revtex/aps10pt4-2.rtx
%{_texmfdistdir}/tex/latex/revtex/aps11pt4-1.rtx
%{_texmfdistdir}/tex/latex/revtex/aps11pt4-2.rtx
%{_texmfdistdir}/tex/latex/revtex/aps12pt4-1.rtx
%{_texmfdistdir}/tex/latex/revtex/aps12pt4-2.rtx
%{_texmfdistdir}/tex/latex/revtex/aps4-1.rtx
%{_texmfdistdir}/tex/latex/revtex/aps4-2.rtx
%{_texmfdistdir}/tex/latex/revtex/apsrmp4-1.rtx
%{_texmfdistdir}/tex/latex/revtex/apsrmp4-2.rtx
%{_texmfdistdir}/tex/latex/revtex/ltxdocext.sty
%{_texmfdistdir}/tex/latex/revtex/ltxfront.sty
%{_texmfdistdir}/tex/latex/revtex/ltxgrid.sty
%{_texmfdistdir}/tex/latex/revtex/ltxutil.sty
%{_texmfdistdir}/tex/latex/revtex/reftest4-2.tex
%{_texmfdistdir}/tex/latex/revtex/revsymb4-1.sty
%{_texmfdistdir}/tex/latex/revtex/revsymb4-2.sty
%{_texmfdistdir}/tex/latex/revtex/revtex4-1.cls
%{_texmfdistdir}/tex/latex/revtex/revtex4-2.cls
%{_texmfdistdir}/tex/latex/revtex/sor4-2.rtx
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-revtex-%{texlive_version}.%{texlive_noarch}.4.2csvn49751-%{release}-zypper
%endif

%package -n texlive-revtex4
Version:        %{texlive_version}.%{texlive_noarch}.4.0svn45873
Release:        0
Summary:        Styles for various Physics Journals (old version)
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-revtex4-doc >= %{texlive_version}
Provides:       tex(10pt.rtx)
Provides:       tex(11pt.rtx)
Provides:       tex(12pt.rtx)
Provides:       tex(aps.rtx)
Provides:       tex(revsymb.sty)
Provides:       tex(revtex4.cls)
Provides:       tex(rmp.rtx)
Requires:       tex(natbib.sty)
Requires:       tex(url.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source259:      revtex4.tar.xz
Source260:      revtex4.doc.tar.xz

%description -n texlive-revtex4
This is an old version of revtex, and is kept as a courtesy to
users having difficulty with the incompatibility of that latest
version.

date: 2019-01-11 17:24:32 +0000


%package -n texlive-revtex4-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.0svn45873
Release:        0
Summary:        Documentation for texlive-revtex4
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-revtex4-doc
This package includes the documentation for texlive-revtex4

%post -n texlive-revtex4
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-revtex4 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-revtex4
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-revtex4-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/revtex4/DOWNLOAD
%{_texmfdistdir}/doc/latex/revtex4/README
%{_texmfdistdir}/doc/latex/revtex4/apssamp.end
%{_texmfdistdir}/doc/latex/revtex4/apssamp.tex
%{_texmfdistdir}/doc/latex/revtex4/auguide.tex
%{_texmfdistdir}/doc/latex/revtex4/differ.tex
%{_texmfdistdir}/doc/latex/revtex4/docs.sty
%{_texmfdistdir}/doc/latex/revtex4/fig_1.eps
%{_texmfdistdir}/doc/latex/revtex4/fig_2.eps
%{_texmfdistdir}/doc/latex/revtex4/ltxdocext.pdf
%{_texmfdistdir}/doc/latex/revtex4/ltxgrid.pdf
%{_texmfdistdir}/doc/latex/revtex4/ltxutil.pdf
%{_texmfdistdir}/doc/latex/revtex4/revtex4.pdf
%{_texmfdistdir}/doc/latex/revtex4/summary.tex
%{_texmfdistdir}/doc/latex/revtex4/template.aps

%files -n texlive-revtex4
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bib/revtex4/apssamp.bib
%{_texmfdistdir}/bibtex/bst/revtex4/apsrev.bst
%{_texmfdistdir}/bibtex/bst/revtex4/apsrmp.bst
%{_texmfdistdir}/tex/latex/revtex4/10pt.rtx
%{_texmfdistdir}/tex/latex/revtex4/11pt.rtx
%{_texmfdistdir}/tex/latex/revtex4/12pt.rtx
%{_texmfdistdir}/tex/latex/revtex4/aps.rtx
%{_texmfdistdir}/tex/latex/revtex4/revsymb.sty
%{_texmfdistdir}/tex/latex/revtex4/revtex4.cls
%{_texmfdistdir}/tex/latex/revtex4/rmp.rtx
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-revtex4-%{texlive_version}.%{texlive_noarch}.4.0svn45873-%{release}-zypper
%endif

%package -n texlive-rgltxdoc
Version:        %{texlive_version}.%{texlive_noarch}.1svn49684
Release:        0
Summary:        Common code for documentation of the author's packages
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rgltxdoc-doc >= %{texlive_version}
Provides:       tex(rgltxdoc.sty)
Requires:       tex(babel.sty)
Requires:       tex(cleveref.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(doc.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(hologo.sty)
Requires:       tex(hypdoc.sty)
Requires:       tex(idxlayout.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(keyvaltable.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(luainputenc.sty)
Requires:       tex(microtype.sty)
Requires:       tex(pbox.sty)
Requires:       tex(polyglossia.sty)
Requires:       tex(showexpl.sty)
Requires:       tex(typearea.sty)
Requires:       tex(varioref.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source261:      rgltxdoc.tar.xz
Source262:      rgltxdoc.doc.tar.xz

%description -n texlive-rgltxdoc
This package combines several other packages and defines
additional macros and environments for documenting LaTeX code.
The package mainly serves the purpose of combining the
preferences used in the author's own package documentations.
However, others can use the package as well. Compatibility
between versions cannot be guaranteed, however.

date: 2019-01-13 07:19:28 +0000


%package -n texlive-rgltxdoc-doc
Version:        %{texlive_version}.%{texlive_noarch}.1svn49684
Release:        0
Summary:        Documentation for texlive-rgltxdoc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rgltxdoc-doc
This package includes the documentation for texlive-rgltxdoc

%post -n texlive-rgltxdoc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rgltxdoc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rgltxdoc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rgltxdoc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/rgltxdoc/README.md
%{_texmfdistdir}/doc/latex/rgltxdoc/rgltxdoc.pdf

%files -n texlive-rgltxdoc
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/rgltxdoc/rgltxdoc.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rgltxdoc-%{texlive_version}.%{texlive_noarch}.1svn49684-%{release}-zypper
%endif

%package -n texlive-ribbonproofs
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn31137
Release:        0
Summary:        Drawing ribbon proofs
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-ribbonproofs-doc >= %{texlive_version}
Provides:       tex(ribbonproofs.sty)
Requires:       tex(etextools.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source263:      ribbonproofs.tar.xz
Source264:      ribbonproofs.doc.tar.xz

%description -n texlive-ribbonproofs
The package provides a way to draw "ribbon proofs" in LaTeX. A
ribbon proof is a diagrammatic representation of a mathematical
proof that a computer program meets its specification. These
diagrams are more human-readable, more scalable, and more
easily modified than the corresponding textual proofs.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-ribbonproofs-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn31137
Release:        0
Summary:        Documentation for texlive-ribbonproofs
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-ribbonproofs-doc
This package includes the documentation for texlive-ribbonproofs

%post -n texlive-ribbonproofs
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ribbonproofs 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ribbonproofs
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ribbonproofs-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ribbonproofs/README
%{_texmfdistdir}/doc/latex/ribbonproofs/ribbonproofsmanual.pdf
%{_texmfdistdir}/doc/latex/ribbonproofs/ribbonproofsmanual.tex

%files -n texlive-ribbonproofs
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ribbonproofs/ribbonproofs.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ribbonproofs-%{texlive_version}.%{texlive_noarch}.1.0svn31137-%{release}-zypper
%endif

%package -n texlive-rjlparshap
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Support for use of \parshape in LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rjlparshap-doc >= %{texlive_version}
Provides:       tex(rjlpshap.sty)
Requires:       tex(arrayjob.sty)
Requires:       tex(forloop.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source265:      rjlparshap.tar.xz
Source266:      rjlparshap.doc.tar.xz

%description -n texlive-rjlparshap
The package provides macros and environments that relieve the
programmer of some of the difficulties of using \parshape in
LaTeX macros. It does not actually calculate shapes in the way
that the shapepar package does.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-rjlparshap-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-rjlparshap
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rjlparshap-doc
This package includes the documentation for texlive-rjlparshap

%post -n texlive-rjlparshap
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rjlparshap 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rjlparshap
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rjlparshap-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/rjlparshap/README
%{_texmfdistdir}/doc/latex/rjlparshap/rjlpshap.pdf

%files -n texlive-rjlparshap
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/rjlparshap/rjlpshap.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rjlparshap-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif

%package -n texlive-rlepsf
Version:        %{texlive_version}.%{texlive_noarch}.svn19082
Release:        0
Summary:        Rewrite labels in EPS graphics
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rlepsf-doc >= %{texlive_version}
Provides:       tex(rlepsf.tex)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source267:      rlepsf.tar.xz
Source268:      rlepsf.doc.tar.xz

%description -n texlive-rlepsf
A macro package for use with epsf.tex which allows PostScript
labels in an Encapsulated PostScript file to be replaced by TeX
labels. The package provides commands \relabel (simply replace
a PostScript string), \adjustrelabel (replace a PostScript
string, with position adjustment), and \extralabel (add a label
at given coordinates). You can, if you so choose, use the
facilities of the labelfig package in place of using
\extralabel.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-rlepsf-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn19082
Release:        0
Summary:        Documentation for texlive-rlepsf
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rlepsf-doc
This package includes the documentation for texlive-rlepsf

%post -n texlive-rlepsf
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rlepsf 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rlepsf
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rlepsf-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/rlepsf/read.me
%{_texmfdistdir}/doc/generic/rlepsf/rlepsdoc.ps

%files -n texlive-rlepsf
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/rlepsf/rlepsf.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rlepsf-%{texlive_version}.%{texlive_noarch}.svn19082-%{release}-zypper
%endif

%package -n texlive-rmathbr
Version:        %{texlive_version}.%{texlive_noarch}.1.0.3svn40415
Release:        0
Summary:        Repeating of math operator at the broken line and the new line in inline equations
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rmathbr-doc >= %{texlive_version}
Provides:       tex(rmathbr.sty)
Requires:       tex(ifetex.sty)
Requires:       tex(mathstyle.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source269:      rmathbr.tar.xz
Source270:      rmathbr.doc.tar.xz

%description -n texlive-rmathbr
Repeating of math operators at the broken line and the new line
in inline equations is used in Cyrillic mathematical typography
(Russian for example), but unfortunately LaTeX does not provide
such an option. This package solves the problem by extending
ideas described in M. I. Grinchuk "TeX and Russian Traditions
of Typesetting", TUGboat 17(4) (1996) 385 and supports most of
LaTeX mathematical packages. See the documentation for details.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-rmathbr-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.3svn40415
Release:        0
Summary:        Documentation for texlive-rmathbr
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rmathbr-doc
This package includes the documentation for texlive-rmathbr

%post -n texlive-rmathbr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rmathbr 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rmathbr
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rmathbr-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/rmathbr/README
%{_texmfdistdir}/doc/latex/rmathbr/rmathbr.pdf

%files -n texlive-rmathbr
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/rmathbr/rmathbr.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rmathbr-%{texlive_version}.%{texlive_noarch}.1.0.3svn40415-%{release}-zypper
%endif

%package -n texlive-rmpage
Version:        %{texlive_version}.%{texlive_noarch}.0.0.92svn20002
Release:        0
Summary:        A package to help change page layout parameters in LaTeX
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-rmpage-doc >= %{texlive_version}
Provides:       tex(rmpage.sty)
Provides:       tex(rmpgen.cfg)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source271:      rmpage.tar.xz
Source272:      rmpage.doc.tar.xz

%description -n texlive-rmpage
The package lets you change page layout parameters in small
steps over a range of values using options. It can set
\textwidth appropriately for the main fount, and ensure that
the text fits inside the printable area of a printer. An
rmpage-formatted document can be typeset identically without
rmpage after a single cut and paste operation. Local
configuration can set defaults: for all documents; and by
class, by printer, and by paper size. The geometry package is
better if you want to set page layout parameters to particular
measurements.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-rmpage-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.92svn20002
Release:        0
Summary:        Documentation for texlive-rmpage
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-rmpage-doc
This package includes the documentation for texlive-rmpage

%post -n texlive-rmpage
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-rmpage 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-rmpage
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-rmpage-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/rmpage/readme
%{_texmfdistdir}/doc/latex/rmpage/rmpage-doc.pdf
%{_texmfdistdir}/doc/latex/rmpage/rmpage-doc.tex
%{_texmfdistdir}/doc/latex/rmpage/rmpage.tex
%{_texmfdistdir}/doc/latex/rmpage/rmplocal.gfc

%files -n texlive-rmpage
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/rmpage/rmpage.sty
%{_texmfdistdir}/tex/latex/rmpage/rmpgen.cfg
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-rmpage-%{texlive_version}.%{texlive_noarch}.0.0.92svn20002-%{release}-zypper
%endif

%package -n texlive-roboto
Version:        %{texlive_version}.%{texlive_noarch}.svn50809
Release:        0
Summary:        Support for the Roboto family of fonts
License:        Apache-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires:       texlive-roboto-fonts >= %{texlive_version}
Recommends:     texlive-roboto-doc >= %{texlive_version}
Provides:       tex(LY1Roboto-LF.fd)
Provides:       tex(LY1Roboto-OsF.fd)
Provides:       tex(LY1Roboto-TLF.fd)
Provides:       tex(LY1Roboto-TOsF.fd)
Provides:       tex(LY1RobotoCondensed-LF.fd)
Provides:       tex(LY1RobotoCondensed-OsF.fd)
Provides:       tex(LY1RobotoCondensed-TLF.fd)
Provides:       tex(LY1RobotoCondensed-TOsF.fd)
Provides:       tex(LY1RobotoMono-TLF.fd)
Provides:       tex(LY1RobotoSlab-TLF.fd)
Provides:       tex(OT1Roboto-LF.fd)
Provides:       tex(OT1Roboto-OsF.fd)
Provides:       tex(OT1Roboto-TLF.fd)
Provides:       tex(OT1Roboto-TOsF.fd)
Provides:       tex(OT1RobotoCondensed-LF.fd)
Provides:       tex(OT1RobotoCondensed-OsF.fd)
Provides:       tex(OT1RobotoCondensed-TLF.fd)
Provides:       tex(OT1RobotoCondensed-TOsF.fd)
Provides:       tex(OT1RobotoMono-TLF.fd)
Provides:       tex(OT1RobotoSlab-TLF.fd)
Provides:       tex(Roboto-Black-lf-ly1--base.tfm)
Provides:       tex(Roboto-Black-lf-ly1.tfm)
Provides:       tex(Roboto-Black-lf-ly1.vf)
Provides:       tex(Roboto-Black-lf-ot1.tfm)
Provides:       tex(Roboto-Black-lf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Black-lf-sc-ly1.tfm)
Provides:       tex(Roboto-Black-lf-sc-ly1.vf)
Provides:       tex(Roboto-Black-lf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Black-lf-sc-ot1.tfm)
Provides:       tex(Roboto-Black-lf-sc-ot1.vf)
Provides:       tex(Roboto-Black-lf-sc-t1--base.tfm)
Provides:       tex(Roboto-Black-lf-sc-t1.tfm)
Provides:       tex(Roboto-Black-lf-sc-t1.vf)
Provides:       tex(Roboto-Black-lf-t1--base.tfm)
Provides:       tex(Roboto-Black-lf-t1.tfm)
Provides:       tex(Roboto-Black-lf-t1.vf)
Provides:       tex(Roboto-Black-lf-ts1--base.tfm)
Provides:       tex(Roboto-Black-lf-ts1.tfm)
Provides:       tex(Roboto-Black-lf-ts1.vf)
Provides:       tex(Roboto-Black-osf-ly1--base.tfm)
Provides:       tex(Roboto-Black-osf-ly1.tfm)
Provides:       tex(Roboto-Black-osf-ly1.vf)
Provides:       tex(Roboto-Black-osf-ot1.tfm)
Provides:       tex(Roboto-Black-osf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Black-osf-sc-ly1.tfm)
Provides:       tex(Roboto-Black-osf-sc-ly1.vf)
Provides:       tex(Roboto-Black-osf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Black-osf-sc-ot1.tfm)
Provides:       tex(Roboto-Black-osf-sc-ot1.vf)
Provides:       tex(Roboto-Black-osf-sc-t1--base.tfm)
Provides:       tex(Roboto-Black-osf-sc-t1.tfm)
Provides:       tex(Roboto-Black-osf-sc-t1.vf)
Provides:       tex(Roboto-Black-osf-t1--base.tfm)
Provides:       tex(Roboto-Black-osf-t1.tfm)
Provides:       tex(Roboto-Black-osf-t1.vf)
Provides:       tex(Roboto-Black-osf-ts1--base.tfm)
Provides:       tex(Roboto-Black-osf-ts1.tfm)
Provides:       tex(Roboto-Black-osf-ts1.vf)
Provides:       tex(Roboto-Black-tlf-ly1--base.tfm)
Provides:       tex(Roboto-Black-tlf-ly1.tfm)
Provides:       tex(Roboto-Black-tlf-ly1.vf)
Provides:       tex(Roboto-Black-tlf-ot1.tfm)
Provides:       tex(Roboto-Black-tlf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Black-tlf-sc-ly1.tfm)
Provides:       tex(Roboto-Black-tlf-sc-ly1.vf)
Provides:       tex(Roboto-Black-tlf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Black-tlf-sc-ot1.tfm)
Provides:       tex(Roboto-Black-tlf-sc-ot1.vf)
Provides:       tex(Roboto-Black-tlf-sc-t1--base.tfm)
Provides:       tex(Roboto-Black-tlf-sc-t1.tfm)
Provides:       tex(Roboto-Black-tlf-sc-t1.vf)
Provides:       tex(Roboto-Black-tlf-t1--base.tfm)
Provides:       tex(Roboto-Black-tlf-t1.tfm)
Provides:       tex(Roboto-Black-tlf-t1.vf)
Provides:       tex(Roboto-Black-tlf-ts1--base.tfm)
Provides:       tex(Roboto-Black-tlf-ts1.tfm)
Provides:       tex(Roboto-Black-tlf-ts1.vf)
Provides:       tex(Roboto-Black-tosf-ly1--base.tfm)
Provides:       tex(Roboto-Black-tosf-ly1.tfm)
Provides:       tex(Roboto-Black-tosf-ly1.vf)
Provides:       tex(Roboto-Black-tosf-ot1.tfm)
Provides:       tex(Roboto-Black-tosf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Black-tosf-sc-ly1.tfm)
Provides:       tex(Roboto-Black-tosf-sc-ly1.vf)
Provides:       tex(Roboto-Black-tosf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Black-tosf-sc-ot1.tfm)
Provides:       tex(Roboto-Black-tosf-sc-ot1.vf)
Provides:       tex(Roboto-Black-tosf-sc-t1--base.tfm)
Provides:       tex(Roboto-Black-tosf-sc-t1.tfm)
Provides:       tex(Roboto-Black-tosf-sc-t1.vf)
Provides:       tex(Roboto-Black-tosf-t1--base.tfm)
Provides:       tex(Roboto-Black-tosf-t1.tfm)
Provides:       tex(Roboto-Black-tosf-t1.vf)
Provides:       tex(Roboto-Black-tosf-ts1--base.tfm)
Provides:       tex(Roboto-Black-tosf-ts1.tfm)
Provides:       tex(Roboto-Black-tosf-ts1.vf)
Provides:       tex(Roboto-BlackItalic-lf-ly1--base.tfm)
Provides:       tex(Roboto-BlackItalic-lf-ly1.tfm)
Provides:       tex(Roboto-BlackItalic-lf-ly1.vf)
Provides:       tex(Roboto-BlackItalic-lf-ot1.tfm)
Provides:       tex(Roboto-BlackItalic-lf-sc-ly1--base.tfm)
Provides:       tex(Roboto-BlackItalic-lf-sc-ly1.tfm)
Provides:       tex(Roboto-BlackItalic-lf-sc-ly1.vf)
Provides:       tex(Roboto-BlackItalic-lf-sc-ot1--base.tfm)
Provides:       tex(Roboto-BlackItalic-lf-sc-ot1.tfm)
Provides:       tex(Roboto-BlackItalic-lf-sc-ot1.vf)
Provides:       tex(Roboto-BlackItalic-lf-sc-t1--base.tfm)
Provides:       tex(Roboto-BlackItalic-lf-sc-t1.tfm)
Provides:       tex(Roboto-BlackItalic-lf-sc-t1.vf)
Provides:       tex(Roboto-BlackItalic-lf-t1--base.tfm)
Provides:       tex(Roboto-BlackItalic-lf-t1.tfm)
Provides:       tex(Roboto-BlackItalic-lf-t1.vf)
Provides:       tex(Roboto-BlackItalic-lf-ts1--base.tfm)
Provides:       tex(Roboto-BlackItalic-lf-ts1.tfm)
Provides:       tex(Roboto-BlackItalic-lf-ts1.vf)
Provides:       tex(Roboto-BlackItalic-osf-ly1--base.tfm)
Provides:       tex(Roboto-BlackItalic-osf-ly1.tfm)
Provides:       tex(Roboto-BlackItalic-osf-ly1.vf)
Provides:       tex(Roboto-BlackItalic-osf-ot1.tfm)
Provides:       tex(Roboto-BlackItalic-osf-sc-ly1--base.tfm)
Provides:       tex(Roboto-BlackItalic-osf-sc-ly1.tfm)
Provides:       tex(Roboto-BlackItalic-osf-sc-ly1.vf)
Provides:       tex(Roboto-BlackItalic-osf-sc-ot1--base.tfm)
Provides:       tex(Roboto-BlackItalic-osf-sc-ot1.tfm)
Provides:       tex(Roboto-BlackItalic-osf-sc-ot1.vf)
Provides:       tex(Roboto-BlackItalic-osf-sc-t1--base.tfm)
Provides:       tex(Roboto-BlackItalic-osf-sc-t1.tfm)
Provides:       tex(Roboto-BlackItalic-osf-sc-t1.vf)
Provides:       tex(Roboto-BlackItalic-osf-t1--base.tfm)
Provides:       tex(Roboto-BlackItalic-osf-t1.tfm)
Provides:       tex(Roboto-BlackItalic-osf-t1.vf)
Provides:       tex(Roboto-BlackItalic-osf-ts1--base.tfm)
Provides:       tex(Roboto-BlackItalic-osf-ts1.tfm)
Provides:       tex(Roboto-BlackItalic-osf-ts1.vf)
Provides:       tex(Roboto-BlackItalic-tlf-ly1--base.tfm)
Provides:       tex(Roboto-BlackItalic-tlf-ly1.tfm)
Provides:       tex(Roboto-BlackItalic-tlf-ly1.vf)
Provides:       tex(Roboto-BlackItalic-tlf-ot1.tfm)
Provides:       tex(Roboto-BlackItalic-tlf-sc-ly1--base.tfm)
Provides:       tex(Roboto-BlackItalic-tlf-sc-ly1.tfm)
Provides:       tex(Roboto-BlackItalic-tlf-sc-ly1.vf)
Provides:       tex(Roboto-BlackItalic-tlf-sc-ot1--base.tfm)
Provides:       tex(Roboto-BlackItalic-tlf-sc-ot1.tfm)
Provides:       tex(Roboto-BlackItalic-tlf-sc-ot1.vf)
Provides:       tex(Roboto-BlackItalic-tlf-sc-t1--base.tfm)
Provides:       tex(Roboto-BlackItalic-tlf-sc-t1.tfm)
Provides:       tex(Roboto-BlackItalic-tlf-sc-t1.vf)
Provides:       tex(Roboto-BlackItalic-tlf-t1--base.tfm)
Provides:       tex(Roboto-BlackItalic-tlf-t1.tfm)
Provides:       tex(Roboto-BlackItalic-tlf-t1.vf)
Provides:       tex(Roboto-BlackItalic-tlf-ts1--base.tfm)
Provides:       tex(Roboto-BlackItalic-tlf-ts1.tfm)
Provides:       tex(Roboto-BlackItalic-tlf-ts1.vf)
Provides:       tex(Roboto-BlackItalic-tosf-ly1--base.tfm)
Provides:       tex(Roboto-BlackItalic-tosf-ly1.tfm)
Provides:       tex(Roboto-BlackItalic-tosf-ly1.vf)
Provides:       tex(Roboto-BlackItalic-tosf-ot1.tfm)
Provides:       tex(Roboto-BlackItalic-tosf-sc-ly1--base.tfm)
Provides:       tex(Roboto-BlackItalic-tosf-sc-ly1.tfm)
Provides:       tex(Roboto-BlackItalic-tosf-sc-ly1.vf)
Provides:       tex(Roboto-BlackItalic-tosf-sc-ot1--base.tfm)
Provides:       tex(Roboto-BlackItalic-tosf-sc-ot1.tfm)
Provides:       tex(Roboto-BlackItalic-tosf-sc-ot1.vf)
Provides:       tex(Roboto-BlackItalic-tosf-sc-t1--base.tfm)
Provides:       tex(Roboto-BlackItalic-tosf-sc-t1.tfm)
Provides:       tex(Roboto-BlackItalic-tosf-sc-t1.vf)
Provides:       tex(Roboto-BlackItalic-tosf-t1--base.tfm)
Provides:       tex(Roboto-BlackItalic-tosf-t1.tfm)
Provides:       tex(Roboto-BlackItalic-tosf-t1.vf)
Provides:       tex(Roboto-BlackItalic-tosf-ts1--base.tfm)
Provides:       tex(Roboto-BlackItalic-tosf-ts1.tfm)
Provides:       tex(Roboto-BlackItalic-tosf-ts1.vf)
Provides:       tex(Roboto-Bold-lf-ly1--base.tfm)
Provides:       tex(Roboto-Bold-lf-ly1.tfm)
Provides:       tex(Roboto-Bold-lf-ly1.vf)
Provides:       tex(Roboto-Bold-lf-ot1.tfm)
Provides:       tex(Roboto-Bold-lf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Bold-lf-sc-ly1.tfm)
Provides:       tex(Roboto-Bold-lf-sc-ly1.vf)
Provides:       tex(Roboto-Bold-lf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Bold-lf-sc-ot1.tfm)
Provides:       tex(Roboto-Bold-lf-sc-ot1.vf)
Provides:       tex(Roboto-Bold-lf-sc-t1--base.tfm)
Provides:       tex(Roboto-Bold-lf-sc-t1.tfm)
Provides:       tex(Roboto-Bold-lf-sc-t1.vf)
Provides:       tex(Roboto-Bold-lf-t1--base.tfm)
Provides:       tex(Roboto-Bold-lf-t1.tfm)
Provides:       tex(Roboto-Bold-lf-t1.vf)
Provides:       tex(Roboto-Bold-lf-ts1--base.tfm)
Provides:       tex(Roboto-Bold-lf-ts1.tfm)
Provides:       tex(Roboto-Bold-lf-ts1.vf)
Provides:       tex(Roboto-Bold-osf-ly1--base.tfm)
Provides:       tex(Roboto-Bold-osf-ly1.tfm)
Provides:       tex(Roboto-Bold-osf-ly1.vf)
Provides:       tex(Roboto-Bold-osf-ot1.tfm)
Provides:       tex(Roboto-Bold-osf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Bold-osf-sc-ly1.tfm)
Provides:       tex(Roboto-Bold-osf-sc-ly1.vf)
Provides:       tex(Roboto-Bold-osf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Bold-osf-sc-ot1.tfm)
Provides:       tex(Roboto-Bold-osf-sc-ot1.vf)
Provides:       tex(Roboto-Bold-osf-sc-t1--base.tfm)
Provides:       tex(Roboto-Bold-osf-sc-t1.tfm)
Provides:       tex(Roboto-Bold-osf-sc-t1.vf)
Provides:       tex(Roboto-Bold-osf-t1--base.tfm)
Provides:       tex(Roboto-Bold-osf-t1.tfm)
Provides:       tex(Roboto-Bold-osf-t1.vf)
Provides:       tex(Roboto-Bold-osf-ts1--base.tfm)
Provides:       tex(Roboto-Bold-osf-ts1.tfm)
Provides:       tex(Roboto-Bold-osf-ts1.vf)
Provides:       tex(Roboto-Bold-tlf-ly1--base.tfm)
Provides:       tex(Roboto-Bold-tlf-ly1.tfm)
Provides:       tex(Roboto-Bold-tlf-ly1.vf)
Provides:       tex(Roboto-Bold-tlf-ot1.tfm)
Provides:       tex(Roboto-Bold-tlf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Bold-tlf-sc-ly1.tfm)
Provides:       tex(Roboto-Bold-tlf-sc-ly1.vf)
Provides:       tex(Roboto-Bold-tlf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Bold-tlf-sc-ot1.tfm)
Provides:       tex(Roboto-Bold-tlf-sc-ot1.vf)
Provides:       tex(Roboto-Bold-tlf-sc-t1--base.tfm)
Provides:       tex(Roboto-Bold-tlf-sc-t1.tfm)
Provides:       tex(Roboto-Bold-tlf-sc-t1.vf)
Provides:       tex(Roboto-Bold-tlf-t1--base.tfm)
Provides:       tex(Roboto-Bold-tlf-t1.tfm)
Provides:       tex(Roboto-Bold-tlf-t1.vf)
Provides:       tex(Roboto-Bold-tlf-ts1--base.tfm)
Provides:       tex(Roboto-Bold-tlf-ts1.tfm)
Provides:       tex(Roboto-Bold-tlf-ts1.vf)
Provides:       tex(Roboto-Bold-tosf-ly1--base.tfm)
Provides:       tex(Roboto-Bold-tosf-ly1.tfm)
Provides:       tex(Roboto-Bold-tosf-ly1.vf)
Provides:       tex(Roboto-Bold-tosf-ot1.tfm)
Provides:       tex(Roboto-Bold-tosf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Bold-tosf-sc-ly1.tfm)
Provides:       tex(Roboto-Bold-tosf-sc-ly1.vf)
Provides:       tex(Roboto-Bold-tosf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Bold-tosf-sc-ot1.tfm)
Provides:       tex(Roboto-Bold-tosf-sc-ot1.vf)
Provides:       tex(Roboto-Bold-tosf-sc-t1--base.tfm)
Provides:       tex(Roboto-Bold-tosf-sc-t1.tfm)
Provides:       tex(Roboto-Bold-tosf-sc-t1.vf)
Provides:       tex(Roboto-Bold-tosf-t1--base.tfm)
Provides:       tex(Roboto-Bold-tosf-t1.tfm)
Provides:       tex(Roboto-Bold-tosf-t1.vf)
Provides:       tex(Roboto-Bold-tosf-ts1--base.tfm)
Provides:       tex(Roboto-Bold-tosf-ts1.tfm)
Provides:       tex(Roboto-Bold-tosf-ts1.vf)
Provides:       tex(Roboto-BoldItalic-lf-ly1--base.tfm)
Provides:       tex(Roboto-BoldItalic-lf-ly1.tfm)
Provides:       tex(Roboto-BoldItalic-lf-ly1.vf)
Provides:       tex(Roboto-BoldItalic-lf-ot1.tfm)
Provides:       tex(Roboto-BoldItalic-lf-sc-ly1--base.tfm)
Provides:       tex(Roboto-BoldItalic-lf-sc-ly1.tfm)
Provides:       tex(Roboto-BoldItalic-lf-sc-ly1.vf)
Provides:       tex(Roboto-BoldItalic-lf-sc-ot1--base.tfm)
Provides:       tex(Roboto-BoldItalic-lf-sc-ot1.tfm)
Provides:       tex(Roboto-BoldItalic-lf-sc-ot1.vf)
Provides:       tex(Roboto-BoldItalic-lf-sc-t1--base.tfm)
Provides:       tex(Roboto-BoldItalic-lf-sc-t1.tfm)
Provides:       tex(Roboto-BoldItalic-lf-sc-t1.vf)
Provides:       tex(Roboto-BoldItalic-lf-t1--base.tfm)
Provides:       tex(Roboto-BoldItalic-lf-t1.tfm)
Provides:       tex(Roboto-BoldItalic-lf-t1.vf)
Provides:       tex(Roboto-BoldItalic-lf-ts1--base.tfm)
Provides:       tex(Roboto-BoldItalic-lf-ts1.tfm)
Provides:       tex(Roboto-BoldItalic-lf-ts1.vf)
Provides:       tex(Roboto-BoldItalic-osf-ly1--base.tfm)
Provides:       tex(Roboto-BoldItalic-osf-ly1.tfm)
Provides:       tex(Roboto-BoldItalic-osf-ly1.vf)
Provides:       tex(Roboto-BoldItalic-osf-ot1.tfm)
Provides:       tex(Roboto-BoldItalic-osf-sc-ly1--base.tfm)
Provides:       tex(Roboto-BoldItalic-osf-sc-ly1.tfm)
Provides:       tex(Roboto-BoldItalic-osf-sc-ly1.vf)
Provides:       tex(Roboto-BoldItalic-osf-sc-ot1--base.tfm)
Provides:       tex(Roboto-BoldItalic-osf-sc-ot1.tfm)
Provides:       tex(Roboto-BoldItalic-osf-sc-ot1.vf)
Provides:       tex(Roboto-BoldItalic-osf-sc-t1--base.tfm)
Provides:       tex(Roboto-BoldItalic-osf-sc-t1.tfm)
Provides:       tex(Roboto-BoldItalic-osf-sc-t1.vf)
Provides:       tex(Roboto-BoldItalic-osf-t1--base.tfm)
Provides:       tex(Roboto-BoldItalic-osf-t1.tfm)
Provides:       tex(Roboto-BoldItalic-osf-t1.vf)
Provides:       tex(Roboto-BoldItalic-osf-ts1--base.tfm)
Provides:       tex(Roboto-BoldItalic-osf-ts1.tfm)
Provides:       tex(Roboto-BoldItalic-osf-ts1.vf)
Provides:       tex(Roboto-BoldItalic-tlf-ly1--base.tfm)
Provides:       tex(Roboto-BoldItalic-tlf-ly1.tfm)
Provides:       tex(Roboto-BoldItalic-tlf-ly1.vf)
Provides:       tex(Roboto-BoldItalic-tlf-ot1.tfm)
Provides:       tex(Roboto-BoldItalic-tlf-sc-ly1--base.tfm)
Provides:       tex(Roboto-BoldItalic-tlf-sc-ly1.tfm)
Provides:       tex(Roboto-BoldItalic-tlf-sc-ly1.vf)
Provides:       tex(Roboto-BoldItalic-tlf-sc-ot1--base.tfm)
Provides:       tex(Roboto-BoldItalic-tlf-sc-ot1.tfm)
Provides:       tex(Roboto-BoldItalic-tlf-sc-ot1.vf)
Provides:       tex(Roboto-BoldItalic-tlf-sc-t1--base.tfm)
Provides:       tex(Roboto-BoldItalic-tlf-sc-t1.tfm)
Provides:       tex(Roboto-BoldItalic-tlf-sc-t1.vf)
Provides:       tex(Roboto-BoldItalic-tlf-t1--base.tfm)
Provides:       tex(Roboto-BoldItalic-tlf-t1.tfm)
Provides:       tex(Roboto-BoldItalic-tlf-t1.vf)
Provides:       tex(Roboto-BoldItalic-tlf-ts1--base.tfm)
Provides:       tex(Roboto-BoldItalic-tlf-ts1.tfm)
Provides:       tex(Roboto-BoldItalic-tlf-ts1.vf)
Provides:       tex(Roboto-BoldItalic-tosf-ly1--base.tfm)
Provides:       tex(Roboto-BoldItalic-tosf-ly1.tfm)
Provides:       tex(Roboto-BoldItalic-tosf-ly1.vf)
Provides:       tex(Roboto-BoldItalic-tosf-ot1.tfm)
Provides:       tex(Roboto-BoldItalic-tosf-sc-ly1--base.tfm)
Provides:       tex(Roboto-BoldItalic-tosf-sc-ly1.tfm)
Provides:       tex(Roboto-BoldItalic-tosf-sc-ly1.vf)
Provides:       tex(Roboto-BoldItalic-tosf-sc-ot1--base.tfm)
Provides:       tex(Roboto-BoldItalic-tosf-sc-ot1.tfm)
Provides:       tex(Roboto-BoldItalic-tosf-sc-ot1.vf)
Provides:       tex(Roboto-BoldItalic-tosf-sc-t1--base.tfm)
Provides:       tex(Roboto-BoldItalic-tosf-sc-t1.tfm)
Provides:       tex(Roboto-BoldItalic-tosf-sc-t1.vf)
Provides:       tex(Roboto-BoldItalic-tosf-t1--base.tfm)
Provides:       tex(Roboto-BoldItalic-tosf-t1.tfm)
Provides:       tex(Roboto-BoldItalic-tosf-t1.vf)
Provides:       tex(Roboto-BoldItalic-tosf-ts1--base.tfm)
Provides:       tex(Roboto-BoldItalic-tosf-ts1.tfm)
Provides:       tex(Roboto-BoldItalic-tosf-ts1.vf)
Provides:       tex(Roboto-Italic-lf-ly1--base.tfm)
Provides:       tex(Roboto-Italic-lf-ly1.tfm)
Provides:       tex(Roboto-Italic-lf-ly1.vf)
Provides:       tex(Roboto-Italic-lf-ot1.tfm)
Provides:       tex(Roboto-Italic-lf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Italic-lf-sc-ly1.tfm)
Provides:       tex(Roboto-Italic-lf-sc-ly1.vf)
Provides:       tex(Roboto-Italic-lf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Italic-lf-sc-ot1.tfm)
Provides:       tex(Roboto-Italic-lf-sc-ot1.vf)
Provides:       tex(Roboto-Italic-lf-sc-t1--base.tfm)
Provides:       tex(Roboto-Italic-lf-sc-t1.tfm)
Provides:       tex(Roboto-Italic-lf-sc-t1.vf)
Provides:       tex(Roboto-Italic-lf-t1--base.tfm)
Provides:       tex(Roboto-Italic-lf-t1.tfm)
Provides:       tex(Roboto-Italic-lf-t1.vf)
Provides:       tex(Roboto-Italic-lf-ts1--base.tfm)
Provides:       tex(Roboto-Italic-lf-ts1.tfm)
Provides:       tex(Roboto-Italic-lf-ts1.vf)
Provides:       tex(Roboto-Italic-osf-ly1--base.tfm)
Provides:       tex(Roboto-Italic-osf-ly1.tfm)
Provides:       tex(Roboto-Italic-osf-ly1.vf)
Provides:       tex(Roboto-Italic-osf-ot1.tfm)
Provides:       tex(Roboto-Italic-osf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Italic-osf-sc-ly1.tfm)
Provides:       tex(Roboto-Italic-osf-sc-ly1.vf)
Provides:       tex(Roboto-Italic-osf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Italic-osf-sc-ot1.tfm)
Provides:       tex(Roboto-Italic-osf-sc-ot1.vf)
Provides:       tex(Roboto-Italic-osf-sc-t1--base.tfm)
Provides:       tex(Roboto-Italic-osf-sc-t1.tfm)
Provides:       tex(Roboto-Italic-osf-sc-t1.vf)
Provides:       tex(Roboto-Italic-osf-t1--base.tfm)
Provides:       tex(Roboto-Italic-osf-t1.tfm)
Provides:       tex(Roboto-Italic-osf-t1.vf)
Provides:       tex(Roboto-Italic-osf-ts1--base.tfm)
Provides:       tex(Roboto-Italic-osf-ts1.tfm)
Provides:       tex(Roboto-Italic-osf-ts1.vf)
Provides:       tex(Roboto-Italic-tlf-ly1--base.tfm)
Provides:       tex(Roboto-Italic-tlf-ly1.tfm)
Provides:       tex(Roboto-Italic-tlf-ly1.vf)
Provides:       tex(Roboto-Italic-tlf-ot1.tfm)
Provides:       tex(Roboto-Italic-tlf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Italic-tlf-sc-ly1.tfm)
Provides:       tex(Roboto-Italic-tlf-sc-ly1.vf)
Provides:       tex(Roboto-Italic-tlf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Italic-tlf-sc-ot1.tfm)
Provides:       tex(Roboto-Italic-tlf-sc-ot1.vf)
Provides:       tex(Roboto-Italic-tlf-sc-t1--base.tfm)
Provides:       tex(Roboto-Italic-tlf-sc-t1.tfm)
Provides:       tex(Roboto-Italic-tlf-sc-t1.vf)
Provides:       tex(Roboto-Italic-tlf-t1--base.tfm)
Provides:       tex(Roboto-Italic-tlf-t1.tfm)
Provides:       tex(Roboto-Italic-tlf-t1.vf)
Provides:       tex(Roboto-Italic-tlf-ts1--base.tfm)
Provides:       tex(Roboto-Italic-tlf-ts1.tfm)
Provides:       tex(Roboto-Italic-tlf-ts1.vf)
Provides:       tex(Roboto-Italic-tosf-ly1--base.tfm)
Provides:       tex(Roboto-Italic-tosf-ly1.tfm)
Provides:       tex(Roboto-Italic-tosf-ly1.vf)
Provides:       tex(Roboto-Italic-tosf-ot1.tfm)
Provides:       tex(Roboto-Italic-tosf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Italic-tosf-sc-ly1.tfm)
Provides:       tex(Roboto-Italic-tosf-sc-ly1.vf)
Provides:       tex(Roboto-Italic-tosf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Italic-tosf-sc-ot1.tfm)
Provides:       tex(Roboto-Italic-tosf-sc-ot1.vf)
Provides:       tex(Roboto-Italic-tosf-sc-t1--base.tfm)
Provides:       tex(Roboto-Italic-tosf-sc-t1.tfm)
Provides:       tex(Roboto-Italic-tosf-sc-t1.vf)
Provides:       tex(Roboto-Italic-tosf-t1--base.tfm)
Provides:       tex(Roboto-Italic-tosf-t1.tfm)
Provides:       tex(Roboto-Italic-tosf-t1.vf)
Provides:       tex(Roboto-Italic-tosf-ts1--base.tfm)
Provides:       tex(Roboto-Italic-tosf-ts1.tfm)
Provides:       tex(Roboto-Italic-tosf-ts1.vf)
Provides:       tex(Roboto-Light-lf-ly1--base.tfm)
Provides:       tex(Roboto-Light-lf-ly1.tfm)
Provides:       tex(Roboto-Light-lf-ly1.vf)
Provides:       tex(Roboto-Light-lf-ot1.tfm)
Provides:       tex(Roboto-Light-lf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Light-lf-sc-ly1.tfm)
Provides:       tex(Roboto-Light-lf-sc-ly1.vf)
Provides:       tex(Roboto-Light-lf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Light-lf-sc-ot1.tfm)
Provides:       tex(Roboto-Light-lf-sc-ot1.vf)
Provides:       tex(Roboto-Light-lf-sc-t1--base.tfm)
Provides:       tex(Roboto-Light-lf-sc-t1.tfm)
Provides:       tex(Roboto-Light-lf-sc-t1.vf)
Provides:       tex(Roboto-Light-lf-t1--base.tfm)
Provides:       tex(Roboto-Light-lf-t1.tfm)
Provides:       tex(Roboto-Light-lf-t1.vf)
Provides:       tex(Roboto-Light-lf-ts1--base.tfm)
Provides:       tex(Roboto-Light-lf-ts1.tfm)
Provides:       tex(Roboto-Light-lf-ts1.vf)
Provides:       tex(Roboto-Light-osf-ly1--base.tfm)
Provides:       tex(Roboto-Light-osf-ly1.tfm)
Provides:       tex(Roboto-Light-osf-ly1.vf)
Provides:       tex(Roboto-Light-osf-ot1.tfm)
Provides:       tex(Roboto-Light-osf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Light-osf-sc-ly1.tfm)
Provides:       tex(Roboto-Light-osf-sc-ly1.vf)
Provides:       tex(Roboto-Light-osf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Light-osf-sc-ot1.tfm)
Provides:       tex(Roboto-Light-osf-sc-ot1.vf)
Provides:       tex(Roboto-Light-osf-sc-t1--base.tfm)
Provides:       tex(Roboto-Light-osf-sc-t1.tfm)
Provides:       tex(Roboto-Light-osf-sc-t1.vf)
Provides:       tex(Roboto-Light-osf-t1--base.tfm)
Provides:       tex(Roboto-Light-osf-t1.tfm)
Provides:       tex(Roboto-Light-osf-t1.vf)
Provides:       tex(Roboto-Light-osf-ts1--base.tfm)
Provides:       tex(Roboto-Light-osf-ts1.tfm)
Provides:       tex(Roboto-Light-osf-ts1.vf)
Provides:       tex(Roboto-Light-tlf-ly1--base.tfm)
Provides:       tex(Roboto-Light-tlf-ly1.tfm)
Provides:       tex(Roboto-Light-tlf-ly1.vf)
Provides:       tex(Roboto-Light-tlf-ot1.tfm)
Provides:       tex(Roboto-Light-tlf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Light-tlf-sc-ly1.tfm)
Provides:       tex(Roboto-Light-tlf-sc-ly1.vf)
Provides:       tex(Roboto-Light-tlf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Light-tlf-sc-ot1.tfm)
Provides:       tex(Roboto-Light-tlf-sc-ot1.vf)
Provides:       tex(Roboto-Light-tlf-sc-t1--base.tfm)
Provides:       tex(Roboto-Light-tlf-sc-t1.tfm)
Provides:       tex(Roboto-Light-tlf-sc-t1.vf)
Provides:       tex(Roboto-Light-tlf-t1--base.tfm)
Provides:       tex(Roboto-Light-tlf-t1.tfm)
Provides:       tex(Roboto-Light-tlf-t1.vf)
Provides:       tex(Roboto-Light-tlf-ts1--base.tfm)
Provides:       tex(Roboto-Light-tlf-ts1.tfm)
Provides:       tex(Roboto-Light-tlf-ts1.vf)
Provides:       tex(Roboto-Light-tosf-ly1--base.tfm)
Provides:       tex(Roboto-Light-tosf-ly1.tfm)
Provides:       tex(Roboto-Light-tosf-ly1.vf)
Provides:       tex(Roboto-Light-tosf-ot1.tfm)
Provides:       tex(Roboto-Light-tosf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Light-tosf-sc-ly1.tfm)
Provides:       tex(Roboto-Light-tosf-sc-ly1.vf)
Provides:       tex(Roboto-Light-tosf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Light-tosf-sc-ot1.tfm)
Provides:       tex(Roboto-Light-tosf-sc-ot1.vf)
Provides:       tex(Roboto-Light-tosf-sc-t1--base.tfm)
Provides:       tex(Roboto-Light-tosf-sc-t1.tfm)
Provides:       tex(Roboto-Light-tosf-sc-t1.vf)
Provides:       tex(Roboto-Light-tosf-t1--base.tfm)
Provides:       tex(Roboto-Light-tosf-t1.tfm)
Provides:       tex(Roboto-Light-tosf-t1.vf)
Provides:       tex(Roboto-Light-tosf-ts1--base.tfm)
Provides:       tex(Roboto-Light-tosf-ts1.tfm)
Provides:       tex(Roboto-Light-tosf-ts1.vf)
Provides:       tex(Roboto-LightItalic-lf-ly1--base.tfm)
Provides:       tex(Roboto-LightItalic-lf-ly1.tfm)
Provides:       tex(Roboto-LightItalic-lf-ly1.vf)
Provides:       tex(Roboto-LightItalic-lf-ot1.tfm)
Provides:       tex(Roboto-LightItalic-lf-sc-ly1--base.tfm)
Provides:       tex(Roboto-LightItalic-lf-sc-ly1.tfm)
Provides:       tex(Roboto-LightItalic-lf-sc-ly1.vf)
Provides:       tex(Roboto-LightItalic-lf-sc-ot1--base.tfm)
Provides:       tex(Roboto-LightItalic-lf-sc-ot1.tfm)
Provides:       tex(Roboto-LightItalic-lf-sc-ot1.vf)
Provides:       tex(Roboto-LightItalic-lf-sc-t1--base.tfm)
Provides:       tex(Roboto-LightItalic-lf-sc-t1.tfm)
Provides:       tex(Roboto-LightItalic-lf-sc-t1.vf)
Provides:       tex(Roboto-LightItalic-lf-t1--base.tfm)
Provides:       tex(Roboto-LightItalic-lf-t1.tfm)
Provides:       tex(Roboto-LightItalic-lf-t1.vf)
Provides:       tex(Roboto-LightItalic-lf-ts1--base.tfm)
Provides:       tex(Roboto-LightItalic-lf-ts1.tfm)
Provides:       tex(Roboto-LightItalic-lf-ts1.vf)
Provides:       tex(Roboto-LightItalic-osf-ly1--base.tfm)
Provides:       tex(Roboto-LightItalic-osf-ly1.tfm)
Provides:       tex(Roboto-LightItalic-osf-ly1.vf)
Provides:       tex(Roboto-LightItalic-osf-ot1.tfm)
Provides:       tex(Roboto-LightItalic-osf-sc-ly1--base.tfm)
Provides:       tex(Roboto-LightItalic-osf-sc-ly1.tfm)
Provides:       tex(Roboto-LightItalic-osf-sc-ly1.vf)
Provides:       tex(Roboto-LightItalic-osf-sc-ot1--base.tfm)
Provides:       tex(Roboto-LightItalic-osf-sc-ot1.tfm)
Provides:       tex(Roboto-LightItalic-osf-sc-ot1.vf)
Provides:       tex(Roboto-LightItalic-osf-sc-t1--base.tfm)
Provides:       tex(Roboto-LightItalic-osf-sc-t1.tfm)
Provides:       tex(Roboto-LightItalic-osf-sc-t1.vf)
Provides:       tex(Roboto-LightItalic-osf-t1--base.tfm)
Provides:       tex(Roboto-LightItalic-osf-t1.tfm)
Provides:       tex(Roboto-LightItalic-osf-t1.vf)
Provides:       tex(Roboto-LightItalic-osf-ts1--base.tfm)
Provides:       tex(Roboto-LightItalic-osf-ts1.tfm)
Provides:       tex(Roboto-LightItalic-osf-ts1.vf)
Provides:       tex(Roboto-LightItalic-tlf-ly1--base.tfm)
Provides:       tex(Roboto-LightItalic-tlf-ly1.tfm)
Provides:       tex(Roboto-LightItalic-tlf-ly1.vf)
Provides:       tex(Roboto-LightItalic-tlf-ot1.tfm)
Provides:       tex(Roboto-LightItalic-tlf-sc-ly1--base.tfm)
Provides:       tex(Roboto-LightItalic-tlf-sc-ly1.tfm)
Provides:       tex(Roboto-LightItalic-tlf-sc-ly1.vf)
Provides:       tex(Roboto-LightItalic-tlf-sc-ot1--base.tfm)
Provides:       tex(Roboto-LightItalic-tlf-sc-ot1.tfm)
Provides:       tex(Roboto-LightItalic-tlf-sc-ot1.vf)
Provides:       tex(Roboto-LightItalic-tlf-sc-t1--base.tfm)
Provides:       tex(Roboto-LightItalic-tlf-sc-t1.tfm)
Provides:       tex(Roboto-LightItalic-tlf-sc-t1.vf)
Provides:       tex(Roboto-LightItalic-tlf-t1--base.tfm)
Provides:       tex(Roboto-LightItalic-tlf-t1.tfm)
Provides:       tex(Roboto-LightItalic-tlf-t1.vf)
Provides:       tex(Roboto-LightItalic-tlf-ts1--base.tfm)
Provides:       tex(Roboto-LightItalic-tlf-ts1.tfm)
Provides:       tex(Roboto-LightItalic-tlf-ts1.vf)
Provides:       tex(Roboto-LightItalic-tosf-ly1--base.tfm)
Provides:       tex(Roboto-LightItalic-tosf-ly1.tfm)
Provides:       tex(Roboto-LightItalic-tosf-ly1.vf)
Provides:       tex(Roboto-LightItalic-tosf-ot1.tfm)
Provides:       tex(Roboto-LightItalic-tosf-sc-ly1--base.tfm)
Provides:       tex(Roboto-LightItalic-tosf-sc-ly1.tfm)
Provides:       tex(Roboto-LightItalic-tosf-sc-ly1.vf)
Provides:       tex(Roboto-LightItalic-tosf-sc-ot1--base.tfm)
Provides:       tex(Roboto-LightItalic-tosf-sc-ot1.tfm)
Provides:       tex(Roboto-LightItalic-tosf-sc-ot1.vf)
Provides:       tex(Roboto-LightItalic-tosf-sc-t1--base.tfm)
Provides:       tex(Roboto-LightItalic-tosf-sc-t1.tfm)
Provides:       tex(Roboto-LightItalic-tosf-sc-t1.vf)
Provides:       tex(Roboto-LightItalic-tosf-t1--base.tfm)
Provides:       tex(Roboto-LightItalic-tosf-t1.tfm)
Provides:       tex(Roboto-LightItalic-tosf-t1.vf)
Provides:       tex(Roboto-LightItalic-tosf-ts1--base.tfm)
Provides:       tex(Roboto-LightItalic-tosf-ts1.tfm)
Provides:       tex(Roboto-LightItalic-tosf-ts1.vf)
Provides:       tex(Roboto-Medium-lf-ly1--base.tfm)
Provides:       tex(Roboto-Medium-lf-ly1.tfm)
Provides:       tex(Roboto-Medium-lf-ly1.vf)
Provides:       tex(Roboto-Medium-lf-ot1.tfm)
Provides:       tex(Roboto-Medium-lf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Medium-lf-sc-ly1.tfm)
Provides:       tex(Roboto-Medium-lf-sc-ly1.vf)
Provides:       tex(Roboto-Medium-lf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Medium-lf-sc-ot1.tfm)
Provides:       tex(Roboto-Medium-lf-sc-ot1.vf)
Provides:       tex(Roboto-Medium-lf-sc-t1--base.tfm)
Provides:       tex(Roboto-Medium-lf-sc-t1.tfm)
Provides:       tex(Roboto-Medium-lf-sc-t1.vf)
Provides:       tex(Roboto-Medium-lf-t1--base.tfm)
Provides:       tex(Roboto-Medium-lf-t1.tfm)
Provides:       tex(Roboto-Medium-lf-t1.vf)
Provides:       tex(Roboto-Medium-lf-ts1--base.tfm)
Provides:       tex(Roboto-Medium-lf-ts1.tfm)
Provides:       tex(Roboto-Medium-lf-ts1.vf)
Provides:       tex(Roboto-Medium-osf-ly1--base.tfm)
Provides:       tex(Roboto-Medium-osf-ly1.tfm)
Provides:       tex(Roboto-Medium-osf-ly1.vf)
Provides:       tex(Roboto-Medium-osf-ot1.tfm)
Provides:       tex(Roboto-Medium-osf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Medium-osf-sc-ly1.tfm)
Provides:       tex(Roboto-Medium-osf-sc-ly1.vf)
Provides:       tex(Roboto-Medium-osf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Medium-osf-sc-ot1.tfm)
Provides:       tex(Roboto-Medium-osf-sc-ot1.vf)
Provides:       tex(Roboto-Medium-osf-sc-t1--base.tfm)
Provides:       tex(Roboto-Medium-osf-sc-t1.tfm)
Provides:       tex(Roboto-Medium-osf-sc-t1.vf)
Provides:       tex(Roboto-Medium-osf-t1--base.tfm)
Provides:       tex(Roboto-Medium-osf-t1.tfm)
Provides:       tex(Roboto-Medium-osf-t1.vf)
Provides:       tex(Roboto-Medium-osf-ts1--base.tfm)
Provides:       tex(Roboto-Medium-osf-ts1.tfm)
Provides:       tex(Roboto-Medium-osf-ts1.vf)
Provides:       tex(Roboto-Medium-tlf-ly1--base.tfm)
Provides:       tex(Roboto-Medium-tlf-ly1.tfm)
Provides:       tex(Roboto-Medium-tlf-ly1.vf)
Provides:       tex(Roboto-Medium-tlf-ot1.tfm)
Provides:       tex(Roboto-Medium-tlf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Medium-tlf-sc-ly1.tfm)
Provides:       tex(Roboto-Medium-tlf-sc-ly1.vf)
Provides:       tex(Roboto-Medium-tlf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Medium-tlf-sc-ot1.tfm)
Provides:       tex(Roboto-Medium-tlf-sc-ot1.vf)
Provides:       tex(Roboto-Medium-tlf-sc-t1--base.tfm)
Provides:       tex(Roboto-Medium-tlf-sc-t1.tfm)
Provides:       tex(Roboto-Medium-tlf-sc-t1.vf)
Provides:       tex(Roboto-Medium-tlf-t1--base.tfm)
Provides:       tex(Roboto-Medium-tlf-t1.tfm)
Provides:       tex(Roboto-Medium-tlf-t1.vf)
Provides:       tex(Roboto-Medium-tlf-ts1--base.tfm)
Provides:       tex(Roboto-Medium-tlf-ts1.tfm)
Provides:       tex(Roboto-Medium-tlf-ts1.vf)
Provides:       tex(Roboto-Medium-tosf-ly1--base.tfm)
Provides:       tex(Roboto-Medium-tosf-ly1.tfm)
Provides:       tex(Roboto-Medium-tosf-ly1.vf)
Provides:       tex(Roboto-Medium-tosf-ot1.tfm)
Provides:       tex(Roboto-Medium-tosf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Medium-tosf-sc-ly1.tfm)
Provides:       tex(Roboto-Medium-tosf-sc-ly1.vf)
Provides:       tex(Roboto-Medium-tosf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Medium-tosf-sc-ot1.tfm)
Provides:       tex(Roboto-Medium-tosf-sc-ot1.vf)
Provides:       tex(Roboto-Medium-tosf-sc-t1--base.tfm)
Provides:       tex(Roboto-Medium-tosf-sc-t1.tfm)
Provides:       tex(Roboto-Medium-tosf-sc-t1.vf)
Provides:       tex(Roboto-Medium-tosf-t1--base.tfm)
Provides:       tex(Roboto-Medium-tosf-t1.tfm)
Provides:       tex(Roboto-Medium-tosf-t1.vf)
Provides:       tex(Roboto-Medium-tosf-ts1--base.tfm)
Provides:       tex(Roboto-Medium-tosf-ts1.tfm)
Provides:       tex(Roboto-Medium-tosf-ts1.vf)
Provides:       tex(Roboto-MediumItalic-lf-ly1--base.tfm)
Provides:       tex(Roboto-MediumItalic-lf-ly1.tfm)
Provides:       tex(Roboto-MediumItalic-lf-ly1.vf)
Provides:       tex(Roboto-MediumItalic-lf-ot1.tfm)
Provides:       tex(Roboto-MediumItalic-lf-sc-ly1--base.tfm)
Provides:       tex(Roboto-MediumItalic-lf-sc-ly1.tfm)
Provides:       tex(Roboto-MediumItalic-lf-sc-ly1.vf)
Provides:       tex(Roboto-MediumItalic-lf-sc-ot1--base.tfm)
Provides:       tex(Roboto-MediumItalic-lf-sc-ot1.tfm)
Provides:       tex(Roboto-MediumItalic-lf-sc-ot1.vf)
Provides:       tex(Roboto-MediumItalic-lf-sc-t1--base.tfm)
Provides:       tex(Roboto-MediumItalic-lf-sc-t1.tfm)
Provides:       tex(Roboto-MediumItalic-lf-sc-t1.vf)
Provides:       tex(Roboto-MediumItalic-lf-t1--base.tfm)
Provides:       tex(Roboto-MediumItalic-lf-t1.tfm)
Provides:       tex(Roboto-MediumItalic-lf-t1.vf)
Provides:       tex(Roboto-MediumItalic-lf-ts1--base.tfm)
Provides:       tex(Roboto-MediumItalic-lf-ts1.tfm)
Provides:       tex(Roboto-MediumItalic-lf-ts1.vf)
Provides:       tex(Roboto-MediumItalic-osf-ly1--base.tfm)
Provides:       tex(Roboto-MediumItalic-osf-ly1.tfm)
Provides:       tex(Roboto-MediumItalic-osf-ly1.vf)
Provides:       tex(Roboto-MediumItalic-osf-ot1.tfm)
Provides:       tex(Roboto-MediumItalic-osf-sc-ly1--base.tfm)
Provides:       tex(Roboto-MediumItalic-osf-sc-ly1.tfm)
Provides:       tex(Roboto-MediumItalic-osf-sc-ly1.vf)
Provides:       tex(Roboto-MediumItalic-osf-sc-ot1--base.tfm)
Provides:       tex(Roboto-MediumItalic-osf-sc-ot1.tfm)
Provides:       tex(Roboto-MediumItalic-osf-sc-ot1.vf)
Provides:       tex(Roboto-MediumItalic-osf-sc-t1--base.tfm)
Provides:       tex(Roboto-MediumItalic-osf-sc-t1.tfm)
Provides:       tex(Roboto-MediumItalic-osf-sc-t1.vf)
Provides:       tex(Roboto-MediumItalic-osf-t1--base.tfm)
Provides:       tex(Roboto-MediumItalic-osf-t1.tfm)
Provides:       tex(Roboto-MediumItalic-osf-t1.vf)
Provides:       tex(Roboto-MediumItalic-osf-ts1--base.tfm)
Provides:       tex(Roboto-MediumItalic-osf-ts1.tfm)
Provides:       tex(Roboto-MediumItalic-osf-ts1.vf)
Provides:       tex(Roboto-MediumItalic-tlf-ly1--base.tfm)
Provides:       tex(Roboto-MediumItalic-tlf-ly1.tfm)
Provides:       tex(Roboto-MediumItalic-tlf-ly1.vf)
Provides:       tex(Roboto-MediumItalic-tlf-ot1.tfm)
Provides:       tex(Roboto-MediumItalic-tlf-sc-ly1--base.tfm)
Provides:       tex(Roboto-MediumItalic-tlf-sc-ly1.tfm)
Provides:       tex(Roboto-MediumItalic-tlf-sc-ly1.vf)
Provides:       tex(Roboto-MediumItalic-tlf-sc-ot1--base.tfm)
Provides:       tex(Roboto-MediumItalic-tlf-sc-ot1.tfm)
Provides:       tex(Roboto-MediumItalic-tlf-sc-ot1.vf)
Provides:       tex(Roboto-MediumItalic-tlf-sc-t1--base.tfm)
Provides:       tex(Roboto-MediumItalic-tlf-sc-t1.tfm)
Provides:       tex(Roboto-MediumItalic-tlf-sc-t1.vf)
Provides:       tex(Roboto-MediumItalic-tlf-t1--base.tfm)
Provides:       tex(Roboto-MediumItalic-tlf-t1.tfm)
Provides:       tex(Roboto-MediumItalic-tlf-t1.vf)
Provides:       tex(Roboto-MediumItalic-tlf-ts1--base.tfm)
Provides:       tex(Roboto-MediumItalic-tlf-ts1.tfm)
Provides:       tex(Roboto-MediumItalic-tlf-ts1.vf)
Provides:       tex(Roboto-MediumItalic-tosf-ly1--base.tfm)
Provides:       tex(Roboto-MediumItalic-tosf-ly1.tfm)
Provides:       tex(Roboto-MediumItalic-tosf-ly1.vf)
Provides:       tex(Roboto-MediumItalic-tosf-ot1.tfm)
Provides:       tex(Roboto-MediumItalic-tosf-sc-ly1--base.tfm)
Provides:       tex(Roboto-MediumItalic-tosf-sc-ly1.tfm)
Provides:       tex(Roboto-MediumItalic-tosf-sc-ly1.vf)
Provides:       tex(Roboto-MediumItalic-tosf-sc-ot1--base.tfm)
Provides:       tex(Roboto-MediumItalic-tosf-sc-ot1.tfm)
Provides:       tex(Roboto-MediumItalic-tosf-sc-ot1.vf)
Provides:       tex(Roboto-MediumItalic-tosf-sc-t1--base.tfm)
Provides:       tex(Roboto-MediumItalic-tosf-sc-t1.tfm)
Provides:       tex(Roboto-MediumItalic-tosf-sc-t1.vf)
Provides:       tex(Roboto-MediumItalic-tosf-t1--base.tfm)
Provides:       tex(Roboto-MediumItalic-tosf-t1.tfm)
Provides:       tex(Roboto-MediumItalic-tosf-t1.vf)
Provides:       tex(Roboto-MediumItalic-tosf-ts1--base.tfm)
Provides:       tex(Roboto-MediumItalic-tosf-ts1.tfm)
Provides:       tex(Roboto-MediumItalic-tosf-ts1.vf)
Provides:       tex(Roboto-Regular-lf-ly1--base.tfm)
Provides:       tex(Roboto-Regular-lf-ly1.tfm)
Provides:       tex(Roboto-Regular-lf-ly1.vf)
Provides:       tex(Roboto-Regular-lf-ot1.tfm)
Provides:       tex(Roboto-Regular-lf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Regular-lf-sc-ly1.tfm)
Provides:       tex(Roboto-Regular-lf-sc-ly1.vf)
Provides:       tex(Roboto-Regular-lf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Regular-lf-sc-ot1.tfm)
Provides:       tex(Roboto-Regular-lf-sc-ot1.vf)
Provides:       tex(Roboto-Regular-lf-sc-t1--base.tfm)
Provides:       tex(Roboto-Regular-lf-sc-t1.tfm)
Provides:       tex(Roboto-Regular-lf-sc-t1.vf)
Provides:       tex(Roboto-Regular-lf-t1--base.tfm)
Provides:       tex(Roboto-Regular-lf-t1.tfm)
Provides:       tex(Roboto-Regular-lf-t1.vf)
Provides:       tex(Roboto-Regular-lf-ts1--base.tfm)
Provides:       tex(Roboto-Regular-lf-ts1.tfm)
Provides:       tex(Roboto-Regular-lf-ts1.vf)
Provides:       tex(Roboto-Regular-osf-ly1--base.tfm)
Provides:       tex(Roboto-Regular-osf-ly1.tfm)
Provides:       tex(Roboto-Regular-osf-ly1.vf)
Provides:       tex(Roboto-Regular-osf-ot1.tfm)
Provides:       tex(Roboto-Regular-osf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Regular-osf-sc-ly1.tfm)
Provides:       tex(Roboto-Regular-osf-sc-ly1.vf)
Provides:       tex(Roboto-Regular-osf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Regular-osf-sc-ot1.tfm)
Provides:       tex(Roboto-Regular-osf-sc-ot1.vf)
Provides:       tex(Roboto-Regular-osf-sc-t1--base.tfm)
Provides:       tex(Roboto-Regular-osf-sc-t1.tfm)
Provides:       tex(Roboto-Regular-osf-sc-t1.vf)
Provides:       tex(Roboto-Regular-osf-t1--base.tfm)
Provides:       tex(Roboto-Regular-osf-t1.tfm)
Provides:       tex(Roboto-Regular-osf-t1.vf)
Provides:       tex(Roboto-Regular-osf-ts1--base.tfm)
Provides:       tex(Roboto-Regular-osf-ts1.tfm)
Provides:       tex(Roboto-Regular-osf-ts1.vf)
Provides:       tex(Roboto-Regular-tlf-ly1--base.tfm)
Provides:       tex(Roboto-Regular-tlf-ly1.tfm)
Provides:       tex(Roboto-Regular-tlf-ly1.vf)
Provides:       tex(Roboto-Regular-tlf-ot1.tfm)
Provides:       tex(Roboto-Regular-tlf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Regular-tlf-sc-ly1.tfm)
Provides:       tex(Roboto-Regular-tlf-sc-ly1.vf)
Provides:       tex(Roboto-Regular-tlf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Regular-tlf-sc-ot1.tfm)
Provides:       tex(Roboto-Regular-tlf-sc-ot1.vf)
Provides:       tex(Roboto-Regular-tlf-sc-t1--base.tfm)
Provides:       tex(Roboto-Regular-tlf-sc-t1.tfm)
Provides:       tex(Roboto-Regular-tlf-sc-t1.vf)
Provides:       tex(Roboto-Regular-tlf-t1--base.tfm)
Provides:       tex(Roboto-Regular-tlf-t1.tfm)
Provides:       tex(Roboto-Regular-tlf-t1.vf)
Provides:       tex(Roboto-Regular-tlf-ts1--base.tfm)
Provides:       tex(Roboto-Regular-tlf-ts1.tfm)
Provides:       tex(Roboto-Regular-tlf-ts1.vf)
Provides:       tex(Roboto-Regular-tosf-ly1--base.tfm)
Provides:       tex(Roboto-Regular-tosf-ly1.tfm)
Provides:       tex(Roboto-Regular-tosf-ly1.vf)
Provides:       tex(Roboto-Regular-tosf-ot1.tfm)
Provides:       tex(Roboto-Regular-tosf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Regular-tosf-sc-ly1.tfm)
Provides:       tex(Roboto-Regular-tosf-sc-ly1.vf)
Provides:       tex(Roboto-Regular-tosf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Regular-tosf-sc-ot1.tfm)
Provides:       tex(Roboto-Regular-tosf-sc-ot1.vf)
Provides:       tex(Roboto-Regular-tosf-sc-t1--base.tfm)
Provides:       tex(Roboto-Regular-tosf-sc-t1.tfm)
Provides:       tex(Roboto-Regular-tosf-sc-t1.vf)
Provides:       tex(Roboto-Regular-tosf-t1--base.tfm)
Provides:       tex(Roboto-Regular-tosf-t1.tfm)
Provides:       tex(Roboto-Regular-tosf-t1.vf)
Provides:       tex(Roboto-Regular-tosf-ts1--base.tfm)
Provides:       tex(Roboto-Regular-tosf-ts1.tfm)
Provides:       tex(Roboto-Regular-tosf-ts1.vf)
Provides:       tex(Roboto-Thin-lf-ly1--base.tfm)
Provides:       tex(Roboto-Thin-lf-ly1.tfm)
Provides:       tex(Roboto-Thin-lf-ly1.vf)
Provides:       tex(Roboto-Thin-lf-ot1.tfm)
Provides:       tex(Roboto-Thin-lf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Thin-lf-sc-ly1.tfm)
Provides:       tex(Roboto-Thin-lf-sc-ly1.vf)
Provides:       tex(Roboto-Thin-lf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Thin-lf-sc-ot1.tfm)
Provides:       tex(Roboto-Thin-lf-sc-ot1.vf)
Provides:       tex(Roboto-Thin-lf-sc-t1--base.tfm)
Provides:       tex(Roboto-Thin-lf-sc-t1.tfm)
Provides:       tex(Roboto-Thin-lf-sc-t1.vf)
Provides:       tex(Roboto-Thin-lf-t1--base.tfm)
Provides:       tex(Roboto-Thin-lf-t1.tfm)
Provides:       tex(Roboto-Thin-lf-t1.vf)
Provides:       tex(Roboto-Thin-lf-ts1--base.tfm)
Provides:       tex(Roboto-Thin-lf-ts1.tfm)
Provides:       tex(Roboto-Thin-lf-ts1.vf)
Provides:       tex(Roboto-Thin-osf-ly1--base.tfm)
Provides:       tex(Roboto-Thin-osf-ly1.tfm)
Provides:       tex(Roboto-Thin-osf-ly1.vf)
Provides:       tex(Roboto-Thin-osf-ot1.tfm)
Provides:       tex(Roboto-Thin-osf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Thin-osf-sc-ly1.tfm)
Provides:       tex(Roboto-Thin-osf-sc-ly1.vf)
Provides:       tex(Roboto-Thin-osf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Thin-osf-sc-ot1.tfm)
Provides:       tex(Roboto-Thin-osf-sc-ot1.vf)
Provides:       tex(Roboto-Thin-osf-sc-t1--base.tfm)
Provides:       tex(Roboto-Thin-osf-sc-t1.tfm)
Provides:       tex(Roboto-Thin-osf-sc-t1.vf)
Provides:       tex(Roboto-Thin-osf-t1--base.tfm)
Provides:       tex(Roboto-Thin-osf-t1.tfm)
Provides:       tex(Roboto-Thin-osf-t1.vf)
Provides:       tex(Roboto-Thin-osf-ts1--base.tfm)
Provides:       tex(Roboto-Thin-osf-ts1.tfm)
Provides:       tex(Roboto-Thin-osf-ts1.vf)
Provides:       tex(Roboto-Thin-tlf-ly1--base.tfm)
Provides:       tex(Roboto-Thin-tlf-ly1.tfm)
Provides:       tex(Roboto-Thin-tlf-ly1.vf)
Provides:       tex(Roboto-Thin-tlf-ot1.tfm)
Provides:       tex(Roboto-Thin-tlf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Thin-tlf-sc-ly1.tfm)
Provides:       tex(Roboto-Thin-tlf-sc-ly1.vf)
Provides:       tex(Roboto-Thin-tlf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Thin-tlf-sc-ot1.tfm)
Provides:       tex(Roboto-Thin-tlf-sc-ot1.vf)
Provides:       tex(Roboto-Thin-tlf-sc-t1--base.tfm)
Provides:       tex(Roboto-Thin-tlf-sc-t1.tfm)
Provides:       tex(Roboto-Thin-tlf-sc-t1.vf)
Provides:       tex(Roboto-Thin-tlf-t1--base.tfm)
Provides:       tex(Roboto-Thin-tlf-t1.tfm)
Provides:       tex(Roboto-Thin-tlf-t1.vf)
Provides:       tex(Roboto-Thin-tlf-ts1--base.tfm)
Provides:       tex(Roboto-Thin-tlf-ts1.tfm)
Provides:       tex(Roboto-Thin-tlf-ts1.vf)
Provides:       tex(Roboto-Thin-tosf-ly1--base.tfm)
Provides:       tex(Roboto-Thin-tosf-ly1.tfm)
Provides:       tex(Roboto-Thin-tosf-ly1.vf)
Provides:       tex(Roboto-Thin-tosf-ot1.tfm)
Provides:       tex(Roboto-Thin-tosf-sc-ly1--base.tfm)
Provides:       tex(Roboto-Thin-tosf-sc-ly1.tfm)
Provides:       tex(Roboto-Thin-tosf-sc-ly1.vf)
Provides:       tex(Roboto-Thin-tosf-sc-ot1--base.tfm)
Provides:       tex(Roboto-Thin-tosf-sc-ot1.tfm)
Provides:       tex(Roboto-Thin-tosf-sc-ot1.vf)
Provides:       tex(Roboto-Thin-tosf-sc-t1--base.tfm)
Provides:       tex(Roboto-Thin-tosf-sc-t1.tfm)
Provides:       tex(Roboto-Thin-tosf-sc-t1.vf)
Provides:       tex(Roboto-Thin-tosf-t1--base.tfm)
Provides:       tex(Roboto-Thin-tosf-t1.tfm)
Provides:       tex(Roboto-Thin-tosf-t1.vf)
Provides:       tex(Roboto-Thin-tosf-ts1--base.tfm)
Provides:       tex(Roboto-Thin-tosf-ts1.tfm)
Provides:       tex(Roboto-Thin-tosf-ts1.vf)
Provides:       tex(Roboto-ThinItalic-lf-ly1--base.tfm)
Provides:       tex(Roboto-ThinItalic-lf-ly1.tfm)
Provides:       tex(Roboto-ThinItalic-lf-ly1.vf)
Provides:       tex(Roboto-ThinItalic-lf-ot1.tfm)
Provides:       tex(Roboto-ThinItalic-lf-sc-ly1--base.tfm)
Provides:       tex(Roboto-ThinItalic-lf-sc-ly1.tfm)
Provides:       tex(Roboto-ThinItalic-lf-sc-ly1.vf)
Provides:       tex(Roboto-ThinItalic-lf-sc-ot1--base.tfm)
Provides:       tex(Roboto-ThinItalic-lf-sc-ot1.tfm)
Provides:       tex(Roboto-ThinItalic-lf-sc-ot1.vf)
Provides:       tex(Roboto-ThinItalic-lf-sc-t1--base.tfm)
Provides:       tex(Roboto-ThinItalic-lf-sc-t1.tfm)
Provides:       tex(Roboto-ThinItalic-lf-sc-t1.vf)
Provides:       tex(Roboto-ThinItalic-lf-t1--base.tfm)
Provides:       tex(Roboto-ThinItalic-lf-t1.tfm)
Provides:       tex(Roboto-ThinItalic-lf-t1.vf)
Provides:       tex(Roboto-ThinItalic-lf-ts1--base.tfm)
Provides:       tex(Roboto-ThinItalic-lf-ts1.tfm)
Provides:       tex(Roboto-ThinItalic-lf-ts1.vf)
Provides:       tex(Roboto-ThinItalic-osf-ly1--base.tfm)
Provides:       tex(Roboto-ThinItalic-osf-ly1.tfm)
Provides:       tex(Roboto-ThinItalic-osf-ly1.vf)
Provides:       tex(Roboto-ThinItalic-osf-ot1.tfm)
Provides:       tex(Roboto-ThinItalic-osf-sc-ly1--base.tfm)
Provides:       tex(Roboto-ThinItalic-osf-sc-ly1.tfm)
Provides:       tex(Roboto-ThinItalic-osf-sc-ly1.vf)
Provides:       tex(Roboto-ThinItalic-osf-sc-ot1--base.tfm)
Provides:       tex(Roboto-ThinItalic-osf-sc-ot1.tfm)
Provides:       tex(Roboto-ThinItalic-osf-sc-ot1.vf)
Provides:       tex(Roboto-ThinItalic-osf-sc-t1--base.tfm)
Provides:       tex(Roboto-ThinItalic-osf-sc-t1.tfm)
Provides:       tex(Roboto-ThinItalic-osf-sc-t1.vf)
Provides:       tex(Roboto-ThinItalic-osf-t1--base.tfm)
Provides:       tex(Roboto-ThinItalic-osf-t1.tfm)
Provides:       tex(Roboto-ThinItalic-osf-t1.vf)
Provides:       tex(Roboto-ThinItalic-osf-ts1--base.tfm)
Provides:       tex(Roboto-ThinItalic-osf-ts1.tfm)
Provides:       tex(Roboto-ThinItalic-osf-ts1.vf)
Provides:       tex(Roboto-ThinItalic-tlf-ly1--base.tfm)
Provides:       tex(Roboto-ThinItalic-tlf-ly1.tfm)
Provides:       tex(Roboto-ThinItalic-tlf-ly1.vf)
Provides:       tex(Roboto-ThinItalic-tlf-ot1.tfm)
Provides:       tex(Roboto-ThinItalic-tlf-sc-ly1--base.tfm)
Provides:       tex(Roboto-ThinItalic-tlf-sc-ly1.tfm)
Provides:       tex(Roboto-ThinItalic-tlf-sc-ly1.vf)
Provides:       tex(Roboto-ThinItalic-tlf-sc-ot1--base.tfm)
Provides:       tex(Roboto-ThinItalic-tlf-sc-ot1.tfm)
Provides:       tex(Roboto-ThinItalic-tlf-sc-ot1.vf)
Provides:       tex(Roboto-ThinItalic-tlf-sc-t1--base.tfm)
Provides:       tex(Roboto-ThinItalic-tlf-sc-t1.tfm)
Provides:       tex(Roboto-ThinItalic-tlf-sc-t1.vf)
Provides:       tex(Roboto-ThinItalic-tlf-t1--base.tfm)
Provides:       tex(Roboto-ThinItalic-tlf-t1.tfm)
Provides:       tex(Roboto-ThinItalic-tlf-t1.vf)
Provides:       tex(Roboto-ThinItalic-tlf-ts1--base.tfm)
Provides:       tex(Roboto-ThinItalic-tlf-ts1.tfm)
Provides:       tex(Roboto-ThinItalic-tlf-ts1.vf)
Provides:       tex(Roboto-ThinItalic-tosf-ly1--base.tfm)
Provides:       tex(Roboto-ThinItalic-tosf-ly1.tfm)
Provides:       tex(Roboto-ThinItalic-tosf-ly1.vf)
Provides:       tex(Roboto-ThinItalic-tosf-ot1.tfm)
Provides:       tex(Roboto-ThinItalic-tosf-sc-ly1--base.tfm)
Provides:       tex(Roboto-ThinItalic-tosf-sc-ly1.tfm)
Provides:       tex(Roboto-ThinItalic-tosf-sc-ly1.vf)
Provides:       tex(Roboto-ThinItalic-tosf-sc-ot1--base.tfm)
Provides:       tex(Roboto-ThinItalic-tosf-sc-ot1.tfm)
Provides:       tex(Roboto-ThinItalic-tosf-sc-ot1.vf)
Provides:       tex(Roboto-ThinItalic-tosf-sc-t1--base.tfm)
Provides:       tex(Roboto-ThinItalic-tosf-sc-t1.tfm)
Provides:       tex(Roboto-ThinItalic-tosf-sc-t1.vf)
Provides:       tex(Roboto-ThinItalic-tosf-t1--base.tfm)
Provides:       tex(Roboto-ThinItalic-tosf-t1.tfm)
Provides:       tex(Roboto-ThinItalic-tosf-t1.vf)
Provides:       tex(Roboto-ThinItalic-tosf-ts1--base.tfm)
Provides:       tex(Roboto-ThinItalic-tosf-ts1.tfm)
Provides:       tex(Roboto-ThinItalic-tosf-ts1.vf)
Provides:       tex(RobotoCondensed-Bold-lf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-lf-ly1.tfm)
Provides:       tex(RobotoCondensed-Bold-lf-ly1.vf)
Provides:       tex(RobotoCondensed-Bold-lf-ot1.tfm)
Provides:       tex(RobotoCondensed-Bold-lf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-lf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-Bold-lf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-Bold-lf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-lf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-Bold-lf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-Bold-lf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-lf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-Bold-lf-sc-t1.vf)
Provides:       tex(RobotoCondensed-Bold-lf-t1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-lf-t1.tfm)
Provides:       tex(RobotoCondensed-Bold-lf-t1.vf)
Provides:       tex(RobotoCondensed-Bold-lf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-lf-ts1.tfm)
Provides:       tex(RobotoCondensed-Bold-lf-ts1.vf)
Provides:       tex(RobotoCondensed-Bold-osf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-osf-ly1.tfm)
Provides:       tex(RobotoCondensed-Bold-osf-ly1.vf)
Provides:       tex(RobotoCondensed-Bold-osf-ot1.tfm)
Provides:       tex(RobotoCondensed-Bold-osf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-osf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-Bold-osf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-Bold-osf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-osf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-Bold-osf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-Bold-osf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-osf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-Bold-osf-sc-t1.vf)
Provides:       tex(RobotoCondensed-Bold-osf-t1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-osf-t1.tfm)
Provides:       tex(RobotoCondensed-Bold-osf-t1.vf)
Provides:       tex(RobotoCondensed-Bold-osf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-osf-ts1.tfm)
Provides:       tex(RobotoCondensed-Bold-osf-ts1.vf)
Provides:       tex(RobotoCondensed-Bold-tlf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-tlf-ly1.tfm)
Provides:       tex(RobotoCondensed-Bold-tlf-ly1.vf)
Provides:       tex(RobotoCondensed-Bold-tlf-ot1.tfm)
Provides:       tex(RobotoCondensed-Bold-tlf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-tlf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-Bold-tlf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-Bold-tlf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-tlf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-Bold-tlf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-Bold-tlf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-tlf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-Bold-tlf-sc-t1.vf)
Provides:       tex(RobotoCondensed-Bold-tlf-t1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-tlf-t1.tfm)
Provides:       tex(RobotoCondensed-Bold-tlf-t1.vf)
Provides:       tex(RobotoCondensed-Bold-tlf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-tlf-ts1.tfm)
Provides:       tex(RobotoCondensed-Bold-tlf-ts1.vf)
Provides:       tex(RobotoCondensed-Bold-tosf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-tosf-ly1.tfm)
Provides:       tex(RobotoCondensed-Bold-tosf-ly1.vf)
Provides:       tex(RobotoCondensed-Bold-tosf-ot1.tfm)
Provides:       tex(RobotoCondensed-Bold-tosf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-tosf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-Bold-tosf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-Bold-tosf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-tosf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-Bold-tosf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-Bold-tosf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-tosf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-Bold-tosf-sc-t1.vf)
Provides:       tex(RobotoCondensed-Bold-tosf-t1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-tosf-t1.tfm)
Provides:       tex(RobotoCondensed-Bold-tosf-t1.vf)
Provides:       tex(RobotoCondensed-Bold-tosf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-Bold-tosf-ts1.tfm)
Provides:       tex(RobotoCondensed-Bold-tosf-ts1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-lf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-lf-ly1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-lf-ly1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-lf-ot1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-lf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-lf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-lf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-lf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-lf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-lf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-lf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-lf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-lf-sc-t1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-lf-t1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-lf-t1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-lf-t1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-lf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-lf-ts1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-lf-ts1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-osf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-osf-ly1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-osf-ly1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-osf-ot1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-osf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-osf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-osf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-osf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-osf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-osf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-osf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-osf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-osf-sc-t1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-osf-t1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-osf-t1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-osf-t1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-osf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-osf-ts1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-osf-ts1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-tlf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tlf-ly1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tlf-ly1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-tlf-ot1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tlf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tlf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tlf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-tlf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tlf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tlf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-tlf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tlf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tlf-sc-t1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-tlf-t1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tlf-t1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tlf-t1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-tlf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tlf-ts1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tlf-ts1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-tosf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tosf-ly1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tosf-ly1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-tosf-ot1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tosf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tosf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tosf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-tosf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tosf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tosf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-tosf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tosf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tosf-sc-t1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-tosf-t1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tosf-t1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tosf-t1.vf)
Provides:       tex(RobotoCondensed-BoldItalic-tosf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tosf-ts1.tfm)
Provides:       tex(RobotoCondensed-BoldItalic-tosf-ts1.vf)
Provides:       tex(RobotoCondensed-Italic-lf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-lf-ly1.tfm)
Provides:       tex(RobotoCondensed-Italic-lf-ly1.vf)
Provides:       tex(RobotoCondensed-Italic-lf-ot1.tfm)
Provides:       tex(RobotoCondensed-Italic-lf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-lf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-Italic-lf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-Italic-lf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-lf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-Italic-lf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-Italic-lf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-lf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-Italic-lf-sc-t1.vf)
Provides:       tex(RobotoCondensed-Italic-lf-t1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-lf-t1.tfm)
Provides:       tex(RobotoCondensed-Italic-lf-t1.vf)
Provides:       tex(RobotoCondensed-Italic-lf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-lf-ts1.tfm)
Provides:       tex(RobotoCondensed-Italic-lf-ts1.vf)
Provides:       tex(RobotoCondensed-Italic-osf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-osf-ly1.tfm)
Provides:       tex(RobotoCondensed-Italic-osf-ly1.vf)
Provides:       tex(RobotoCondensed-Italic-osf-ot1.tfm)
Provides:       tex(RobotoCondensed-Italic-osf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-osf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-Italic-osf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-Italic-osf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-osf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-Italic-osf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-Italic-osf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-osf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-Italic-osf-sc-t1.vf)
Provides:       tex(RobotoCondensed-Italic-osf-t1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-osf-t1.tfm)
Provides:       tex(RobotoCondensed-Italic-osf-t1.vf)
Provides:       tex(RobotoCondensed-Italic-osf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-osf-ts1.tfm)
Provides:       tex(RobotoCondensed-Italic-osf-ts1.vf)
Provides:       tex(RobotoCondensed-Italic-tlf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-tlf-ly1.tfm)
Provides:       tex(RobotoCondensed-Italic-tlf-ly1.vf)
Provides:       tex(RobotoCondensed-Italic-tlf-ot1.tfm)
Provides:       tex(RobotoCondensed-Italic-tlf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-tlf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-Italic-tlf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-Italic-tlf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-tlf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-Italic-tlf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-Italic-tlf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-tlf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-Italic-tlf-sc-t1.vf)
Provides:       tex(RobotoCondensed-Italic-tlf-t1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-tlf-t1.tfm)
Provides:       tex(RobotoCondensed-Italic-tlf-t1.vf)
Provides:       tex(RobotoCondensed-Italic-tlf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-tlf-ts1.tfm)
Provides:       tex(RobotoCondensed-Italic-tlf-ts1.vf)
Provides:       tex(RobotoCondensed-Italic-tosf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-tosf-ly1.tfm)
Provides:       tex(RobotoCondensed-Italic-tosf-ly1.vf)
Provides:       tex(RobotoCondensed-Italic-tosf-ot1.tfm)
Provides:       tex(RobotoCondensed-Italic-tosf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-tosf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-Italic-tosf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-Italic-tosf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-tosf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-Italic-tosf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-Italic-tosf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-tosf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-Italic-tosf-sc-t1.vf)
Provides:       tex(RobotoCondensed-Italic-tosf-t1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-tosf-t1.tfm)
Provides:       tex(RobotoCondensed-Italic-tosf-t1.vf)
Provides:       tex(RobotoCondensed-Italic-tosf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-Italic-tosf-ts1.tfm)
Provides:       tex(RobotoCondensed-Italic-tosf-ts1.vf)
Provides:       tex(RobotoCondensed-Light-lf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Light-lf-ly1.tfm)
Provides:       tex(RobotoCondensed-Light-lf-ly1.vf)
Provides:       tex(RobotoCondensed-Light-lf-ot1.tfm)
Provides:       tex(RobotoCondensed-Light-lf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Light-lf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-Light-lf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-Light-lf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-Light-lf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-Light-lf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-Light-lf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-Light-lf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-Light-lf-sc-t1.vf)
Provides:       tex(RobotoCondensed-Light-lf-t1--base.tfm)
Provides:       tex(RobotoCondensed-Light-lf-t1.tfm)
Provides:       tex(RobotoCondensed-Light-lf-t1.vf)
Provides:       tex(RobotoCondensed-Light-lf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-Light-lf-ts1.tfm)
Provides:       tex(RobotoCondensed-Light-lf-ts1.vf)
Provides:       tex(RobotoCondensed-Light-osf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Light-osf-ly1.tfm)
Provides:       tex(RobotoCondensed-Light-osf-ly1.vf)
Provides:       tex(RobotoCondensed-Light-osf-ot1.tfm)
Provides:       tex(RobotoCondensed-Light-osf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Light-osf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-Light-osf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-Light-osf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-Light-osf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-Light-osf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-Light-osf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-Light-osf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-Light-osf-sc-t1.vf)
Provides:       tex(RobotoCondensed-Light-osf-t1--base.tfm)
Provides:       tex(RobotoCondensed-Light-osf-t1.tfm)
Provides:       tex(RobotoCondensed-Light-osf-t1.vf)
Provides:       tex(RobotoCondensed-Light-osf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-Light-osf-ts1.tfm)
Provides:       tex(RobotoCondensed-Light-osf-ts1.vf)
Provides:       tex(RobotoCondensed-Light-tlf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Light-tlf-ly1.tfm)
Provides:       tex(RobotoCondensed-Light-tlf-ly1.vf)
Provides:       tex(RobotoCondensed-Light-tlf-ot1.tfm)
Provides:       tex(RobotoCondensed-Light-tlf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Light-tlf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-Light-tlf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-Light-tlf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-Light-tlf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-Light-tlf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-Light-tlf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-Light-tlf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-Light-tlf-sc-t1.vf)
Provides:       tex(RobotoCondensed-Light-tlf-t1--base.tfm)
Provides:       tex(RobotoCondensed-Light-tlf-t1.tfm)
Provides:       tex(RobotoCondensed-Light-tlf-t1.vf)
Provides:       tex(RobotoCondensed-Light-tlf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-Light-tlf-ts1.tfm)
Provides:       tex(RobotoCondensed-Light-tlf-ts1.vf)
Provides:       tex(RobotoCondensed-Light-tosf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Light-tosf-ly1.tfm)
Provides:       tex(RobotoCondensed-Light-tosf-ly1.vf)
Provides:       tex(RobotoCondensed-Light-tosf-ot1.tfm)
Provides:       tex(RobotoCondensed-Light-tosf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Light-tosf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-Light-tosf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-Light-tosf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-Light-tosf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-Light-tosf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-Light-tosf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-Light-tosf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-Light-tosf-sc-t1.vf)
Provides:       tex(RobotoCondensed-Light-tosf-t1--base.tfm)
Provides:       tex(RobotoCondensed-Light-tosf-t1.tfm)
Provides:       tex(RobotoCondensed-Light-tosf-t1.vf)
Provides:       tex(RobotoCondensed-Light-tosf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-Light-tosf-ts1.tfm)
Provides:       tex(RobotoCondensed-Light-tosf-ts1.vf)
Provides:       tex(RobotoCondensed-LightItalic-lf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-lf-ly1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-lf-ly1.vf)
Provides:       tex(RobotoCondensed-LightItalic-lf-ot1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-lf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-lf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-lf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-LightItalic-lf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-lf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-lf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-LightItalic-lf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-lf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-lf-sc-t1.vf)
Provides:       tex(RobotoCondensed-LightItalic-lf-t1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-lf-t1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-lf-t1.vf)
Provides:       tex(RobotoCondensed-LightItalic-lf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-lf-ts1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-lf-ts1.vf)
Provides:       tex(RobotoCondensed-LightItalic-osf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-osf-ly1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-osf-ly1.vf)
Provides:       tex(RobotoCondensed-LightItalic-osf-ot1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-osf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-osf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-osf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-LightItalic-osf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-osf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-osf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-LightItalic-osf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-osf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-osf-sc-t1.vf)
Provides:       tex(RobotoCondensed-LightItalic-osf-t1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-osf-t1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-osf-t1.vf)
Provides:       tex(RobotoCondensed-LightItalic-osf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-osf-ts1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-osf-ts1.vf)
Provides:       tex(RobotoCondensed-LightItalic-tlf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tlf-ly1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tlf-ly1.vf)
Provides:       tex(RobotoCondensed-LightItalic-tlf-ot1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tlf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tlf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tlf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-LightItalic-tlf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tlf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tlf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-LightItalic-tlf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tlf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tlf-sc-t1.vf)
Provides:       tex(RobotoCondensed-LightItalic-tlf-t1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tlf-t1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tlf-t1.vf)
Provides:       tex(RobotoCondensed-LightItalic-tlf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tlf-ts1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tlf-ts1.vf)
Provides:       tex(RobotoCondensed-LightItalic-tosf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tosf-ly1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tosf-ly1.vf)
Provides:       tex(RobotoCondensed-LightItalic-tosf-ot1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tosf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tosf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tosf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-LightItalic-tosf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tosf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tosf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-LightItalic-tosf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tosf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tosf-sc-t1.vf)
Provides:       tex(RobotoCondensed-LightItalic-tosf-t1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tosf-t1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tosf-t1.vf)
Provides:       tex(RobotoCondensed-LightItalic-tosf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tosf-ts1.tfm)
Provides:       tex(RobotoCondensed-LightItalic-tosf-ts1.vf)
Provides:       tex(RobotoCondensed-Regular-lf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-lf-ly1.tfm)
Provides:       tex(RobotoCondensed-Regular-lf-ly1.vf)
Provides:       tex(RobotoCondensed-Regular-lf-ot1.tfm)
Provides:       tex(RobotoCondensed-Regular-lf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-lf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-Regular-lf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-Regular-lf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-lf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-Regular-lf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-Regular-lf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-lf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-Regular-lf-sc-t1.vf)
Provides:       tex(RobotoCondensed-Regular-lf-t1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-lf-t1.tfm)
Provides:       tex(RobotoCondensed-Regular-lf-t1.vf)
Provides:       tex(RobotoCondensed-Regular-lf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-lf-ts1.tfm)
Provides:       tex(RobotoCondensed-Regular-lf-ts1.vf)
Provides:       tex(RobotoCondensed-Regular-osf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-osf-ly1.tfm)
Provides:       tex(RobotoCondensed-Regular-osf-ly1.vf)
Provides:       tex(RobotoCondensed-Regular-osf-ot1.tfm)
Provides:       tex(RobotoCondensed-Regular-osf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-osf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-Regular-osf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-Regular-osf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-osf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-Regular-osf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-Regular-osf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-osf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-Regular-osf-sc-t1.vf)
Provides:       tex(RobotoCondensed-Regular-osf-t1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-osf-t1.tfm)
Provides:       tex(RobotoCondensed-Regular-osf-t1.vf)
Provides:       tex(RobotoCondensed-Regular-osf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-osf-ts1.tfm)
Provides:       tex(RobotoCondensed-Regular-osf-ts1.vf)
Provides:       tex(RobotoCondensed-Regular-tlf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-tlf-ly1.tfm)
Provides:       tex(RobotoCondensed-Regular-tlf-ly1.vf)
Provides:       tex(RobotoCondensed-Regular-tlf-ot1.tfm)
Provides:       tex(RobotoCondensed-Regular-tlf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-tlf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-Regular-tlf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-Regular-tlf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-tlf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-Regular-tlf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-Regular-tlf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-tlf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-Regular-tlf-sc-t1.vf)
Provides:       tex(RobotoCondensed-Regular-tlf-t1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-tlf-t1.tfm)
Provides:       tex(RobotoCondensed-Regular-tlf-t1.vf)
Provides:       tex(RobotoCondensed-Regular-tlf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-tlf-ts1.tfm)
Provides:       tex(RobotoCondensed-Regular-tlf-ts1.vf)
Provides:       tex(RobotoCondensed-Regular-tosf-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-tosf-ly1.tfm)
Provides:       tex(RobotoCondensed-Regular-tosf-ly1.vf)
Provides:       tex(RobotoCondensed-Regular-tosf-ot1.tfm)
Provides:       tex(RobotoCondensed-Regular-tosf-sc-ly1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-tosf-sc-ly1.tfm)
Provides:       tex(RobotoCondensed-Regular-tosf-sc-ly1.vf)
Provides:       tex(RobotoCondensed-Regular-tosf-sc-ot1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-tosf-sc-ot1.tfm)
Provides:       tex(RobotoCondensed-Regular-tosf-sc-ot1.vf)
Provides:       tex(RobotoCondensed-Regular-tosf-sc-t1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-tosf-sc-t1.tfm)
Provides:       tex(RobotoCondensed-Regular-tosf-sc-t1.vf)
Provides:       tex(RobotoCondensed-Regular-tosf-t1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-tosf-t1.tfm)
Provides:       tex(RobotoCondensed-Regular-tosf-t1.vf)
Provides:       tex(RobotoCondensed-Regular-tosf-ts1--base.tfm)
Provides:       tex(RobotoCondensed-Regular-tosf-ts1.tfm)
Provides:       tex(RobotoCondensed-Regular-tosf-ts1.vf)
Provides:       tex(RobotoMono-Bold-tlf-ly1--base.tfm)
Provides:       tex(RobotoMono-Bold-tlf-ly1.tfm)
Provides:       tex(RobotoMono-Bold-tlf-ly1.vf)
Provides:       tex(RobotoMono-Bold-tlf-ot1.tfm)
Provides:       tex(RobotoMono-Bold-tlf-sc-ly1--base.tfm)
Provides:       tex(RobotoMono-Bold-tlf-sc-ly1.tfm)
Provides:       tex(RobotoMono-Bold-tlf-sc-ly1.vf)
Provides:       tex(RobotoMono-Bold-tlf-sc-ot1--base.tfm)
Provides:       tex(RobotoMono-Bold-tlf-sc-ot1.tfm)
Provides:       tex(RobotoMono-Bold-tlf-sc-ot1.vf)
Provides:       tex(RobotoMono-Bold-tlf-sc-t1--base.tfm)
Provides:       tex(RobotoMono-Bold-tlf-sc-t1.tfm)
Provides:       tex(RobotoMono-Bold-tlf-sc-t1.vf)
Provides:       tex(RobotoMono-Bold-tlf-t1--base.tfm)
Provides:       tex(RobotoMono-Bold-tlf-t1.tfm)
Provides:       tex(RobotoMono-Bold-tlf-t1.vf)
Provides:       tex(RobotoMono-Bold-tlf-ts1--base.tfm)
Provides:       tex(RobotoMono-Bold-tlf-ts1.tfm)
Provides:       tex(RobotoMono-Bold-tlf-ts1.vf)
Provides:       tex(RobotoMono-BoldItalic-tlf-ly1--base.tfm)
Provides:       tex(RobotoMono-BoldItalic-tlf-ly1.tfm)
Provides:       tex(RobotoMono-BoldItalic-tlf-ly1.vf)
Provides:       tex(RobotoMono-BoldItalic-tlf-ot1.tfm)
Provides:       tex(RobotoMono-BoldItalic-tlf-sc-ly1--base.tfm)
Provides:       tex(RobotoMono-BoldItalic-tlf-sc-ly1.tfm)
Provides:       tex(RobotoMono-BoldItalic-tlf-sc-ly1.vf)
Provides:       tex(RobotoMono-BoldItalic-tlf-sc-ot1--base.tfm)
Provides:       tex(RobotoMono-BoldItalic-tlf-sc-ot1.tfm)
Provides:       tex(RobotoMono-BoldItalic-tlf-sc-ot1.vf)
Provides:       tex(RobotoMono-BoldItalic-tlf-sc-t1--base.tfm)
Provides:       tex(RobotoMono-BoldItalic-tlf-sc-t1.tfm)
Provides:       tex(RobotoMono-BoldItalic-tlf-sc-t1.vf)
Provides:       tex(RobotoMono-BoldItalic-tlf-t1--base.tfm)
Provides:       tex(RobotoMono-BoldItalic-tlf-t1.tfm)
Provides:       tex(RobotoMono-BoldItalic-tlf-t1.vf)
Provides:       tex(RobotoMono-BoldItalic-tlf-ts1--base.tfm)
Provides:       tex(RobotoMono-BoldItalic-tlf-ts1.tfm)
Provides:       tex(RobotoMono-BoldItalic-tlf-ts1.vf)
Provides:       tex(RobotoMono-Italic-tlf-ly1--base.tfm)
Provides:       tex(RobotoMono-Italic-tlf-ly1.tfm)
Provides:       tex(RobotoMono-Italic-tlf-ly1.vf)
Provides:       tex(RobotoMono-Italic-tlf-ot1.tfm)
Provides:       tex(RobotoMono-Italic-tlf-sc-ly1--base.tfm)
Provides:       tex(RobotoMono-Italic-tlf-sc-ly1.tfm)
Provides:       tex(RobotoMono-Italic-tlf-sc-ly1.vf)
Provides:       tex(RobotoMono-Italic-tlf-sc-ot1--base.tfm)
Provides:       tex(RobotoMono-Italic-tlf-sc-ot1.tfm)
Provides:       tex(RobotoMono-Italic-tlf-sc-ot1.vf)
Provides:       tex(RobotoMono-Italic-tlf-sc-t1--base.tfm)
Provides:       tex(RobotoMono-Italic-tlf-sc-t1.tfm)
Provides:       tex(RobotoMono-Italic-tlf-sc-t1.vf)
Provides:       tex(RobotoMono-Italic-tlf-t1--base.tfm)
Provides:       tex(RobotoMono-Italic-tlf-t1.tfm)
Provides:       tex(RobotoMono-Italic-tlf-t1.vf)
Provides:       tex(RobotoMono-Italic-tlf-ts1--base.tfm)
Provides:       tex(RobotoMono-Italic-tlf-ts1.tfm)
Provides:       tex(RobotoMono-Italic-tlf-ts1.vf)
Provides:       tex(RobotoMono-Light-tlf-ly1--base.tfm)
Provides:       tex(RobotoMono-Light-tlf-ly1.tfm)
Provides:       tex(RobotoMono-Light-tlf-ly1.vf)
Provides:       tex(RobotoMono-Light-tlf-ot1.tfm)
Provides:       tex(RobotoMono-Light-tlf-sc-ly1--base.tfm)
Provides:       tex(RobotoMono-Light-tlf-sc-ly1.tfm)
Provides:       tex(RobotoMono-Light-tlf-sc-ly1.vf)
Provides:       tex(RobotoMono-Light-tlf-sc-ot1--base.tfm)
Provides:       tex(RobotoMono-Light-tlf-sc-ot1.tfm)
Provides:       tex(RobotoMono-Light-tlf-sc-ot1.vf)
Provides:       tex(RobotoMono-Light-tlf-sc-t1--base.tfm)
Provides:       tex(RobotoMono-Light-tlf-sc-t1.tfm)
Provides:       tex(RobotoMono-Light-tlf-sc-t1.vf)
Provides:       tex(RobotoMono-Light-tlf-t1--base.tfm)
Provides:       tex(RobotoMono-Light-tlf-t1.tfm)
Provides:       tex(RobotoMono-Light-tlf-t1.vf)
Provides:       tex(RobotoMono-Light-tlf-ts1--base.tfm)
Provides:       tex(RobotoMono-Light-tlf-ts1.tfm)
Provides:       tex(RobotoMono-Light-tlf-ts1.vf)
Provides:       tex(RobotoMono-LightItalic-tlf-ly1--base.tfm)
Provides:       tex(RobotoMono-LightItalic-tlf-ly1.tfm)
Provides:       tex(RobotoMono-LightItalic-tlf-ly1.vf)
Provides:       tex(RobotoMono-LightItalic-tlf-ot1.tfm)
Provides:       tex(RobotoMono-LightItalic-tlf-sc-ly1--base.tfm)
Provides:       tex(RobotoMono-LightItalic-tlf-sc-ly1.tfm)
Provides:       tex(RobotoMono-LightItalic-tlf-sc-ly1.vf)
Provides:       tex(RobotoMono-LightItalic-tlf-sc-ot1--base.tfm)
Provides:       tex(RobotoMono-LightItalic-tlf-sc-ot1.tfm)
Provides:       tex(RobotoMono-LightItalic-tlf-sc-ot1.vf)
Provides:       tex(RobotoMono-LightItalic-tlf-sc-t1--base.tfm)
Provides:       tex(RobotoMono-LightItalic-tlf-sc-t1.tfm)
Provides:       tex(RobotoMono-LightItalic-tlf-sc-t1.vf)
Provides:       tex(RobotoMono-LightItalic-tlf-t1--base.tfm)
Provides:       tex(RobotoMono-LightItalic-tlf-t1.tfm)
Provides:       tex(RobotoMono-LightItalic-tlf-t1.vf)
Provides:       tex(RobotoMono-LightItalic-tlf-ts1--base.tfm)
Provides:       tex(RobotoMono-LightItalic-tlf-ts1.tfm)
Provides:       tex(RobotoMono-LightItalic-tlf-ts1.vf)
Provides:       tex(RobotoMono-Medium-tlf-ly1--base.tfm)
Provides:       tex(RobotoMono-Medium-tlf-ly1.tfm)
Provides:       tex(RobotoMono-Medium-tlf-ly1.vf)
Provides:       tex(RobotoMono-Medium-tlf-ot1.tfm)
Provides:       tex(RobotoMono-Medium-tlf-sc-ly1--base.tfm)
Provides:       tex(RobotoMono-Medium-tlf-sc-ly1.tfm)
Provides:       tex(RobotoMono-Medium-tlf-sc-ly1.vf)
Provides:       tex(RobotoMono-Medium-tlf-sc-ot1--base.tfm)
Provides:       tex(RobotoMono-Medium-tlf-sc-ot1.tfm)
Provides:       tex(RobotoMono-Medium-tlf-sc-ot1.vf)
Provides:       tex(RobotoMono-Medium-tlf-sc-t1--base.tfm)
Provides:       tex(RobotoMono-Medium-tlf-sc-t1.tfm)
Provides:       tex(RobotoMono-Medium-tlf-sc-t1.vf)
Provides:       tex(RobotoMono-Medium-tlf-t1--base.tfm)
Provides:       tex(RobotoMono-Medium-tlf-t1.tfm)
Provides:       tex(RobotoMono-Medium-tlf-t1.vf)
Provides:       tex(RobotoMono-Medium-tlf-ts1--base.tfm)
Provides:       tex(RobotoMono-Medium-tlf-ts1.tfm)
Provides:       tex(RobotoMono-Medium-tlf-ts1.vf)
Provides:       tex(RobotoMono-MediumItalic-tlf-ly1--base.tfm)
Provides:       tex(RobotoMono-MediumItalic-tlf-ly1.tfm)
Provides:       tex(RobotoMono-MediumItalic-tlf-ly1.vf)
Provides:       tex(RobotoMono-MediumItalic-tlf-ot1.tfm)
Provides:       tex(RobotoMono-MediumItalic-tlf-sc-ly1--base.tfm)
Provides:       tex(RobotoMono-MediumItalic-tlf-sc-ly1.tfm)
Provides:       tex(RobotoMono-MediumItalic-tlf-sc-ly1.vf)
Provides:       tex(RobotoMono-MediumItalic-tlf-sc-ot1--base.tfm)
Provides:       tex(RobotoMono-MediumItalic-tlf-sc-ot1.tfm)
Provides:       tex(RobotoMono-MediumItalic-tlf-sc-ot1.vf)
Provides:       tex(RobotoMono-MediumItalic-tlf-sc-t1--base.tfm)
Provides:       tex(RobotoMono-MediumItalic-tlf-sc-t1.tfm)
Provides:       tex(RobotoMono-MediumItalic-tlf-sc-t1.vf)
Provides:       tex(RobotoMono-MediumItalic-tlf-t1--base.tfm)
Provides:       tex(RobotoMono-MediumItalic-tlf-t1.tfm)
Provides:       tex(RobotoMono-MediumItalic-tlf-t1.vf)
Provides:       tex(RobotoMono-MediumItalic-tlf-ts1--base.tfm)
Provides:       tex(RobotoMono-MediumItalic-tlf-ts1.tfm)
Provides:       tex(RobotoMono-MediumItalic-tlf-ts1.vf)
Provides:       tex(RobotoMono-Regular-tlf-ly1--base.tfm)
Provides:       tex(RobotoMono-Regular-tlf-ly1.tfm)
Provides:       tex(RobotoMono-Regular-tlf-ly1.vf)
Provides:       tex(RobotoMono-Regular-tlf-ot1.tfm)
Provides:       tex(RobotoMono-Regular-tlf-sc-ly1--base.tfm)
Provides:       tex(RobotoMono-Regular-tlf-sc-ly1.tfm)
Provides:       tex(RobotoMono-Regular-tlf-sc-ly1.vf)
Provides:       tex(RobotoMono-Regular-tlf-sc-ot1--base.tfm)
Provides:       tex(RobotoMono-Regular-tlf-sc-ot1.tfm)
Provides:       tex(RobotoMono-Regular-tlf-sc-ot1.vf)
Provides:       tex(RobotoMono-Regular-tlf-sc-t1--base.tfm)
Provides:       tex(RobotoMono-Regular-tlf-sc-t1.tfm)
Provides:       tex(RobotoMono-Regular-tlf-sc-t1.vf)
Provides:       tex(RobotoMono-Regular-tlf-t1--base.tfm)
Provides:       tex(RobotoMono-Regular-tlf-t1.tfm)
Provides:       tex(RobotoMono-Regular-tlf-t1.vf)
Provides:       tex(RobotoMono-Regular-tlf-ts1--base.tfm)
Provides:       tex(RobotoMono-Regular-tlf-ts1.tfm)
Provides:       tex(RobotoMono-Regular-tlf-ts1.vf)
Provides:       tex(RobotoMono-Thin-tlf-ly1--base.tfm)
Provides:       tex(RobotoMono-Thin-tlf-ly1.tfm)
Provides:       tex(RobotoMono-Thin-tlf-ly1.vf)
Provides:       tex(RobotoMono-Thin-tlf-ot1.tfm)
Provides:       tex(RobotoMono-Thin-tlf-sc-ly1--base.tfm)
Provides:       tex(RobotoMono-Thin-tlf-sc-ly1.tfm)
Provides:       tex(RobotoMono-Thin-tlf-sc-ly1.vf)
Provides:       tex(RobotoMono-Thin-tlf-sc-ot1--base.tfm)
Provides:       tex(RobotoMono-Thin-tlf-sc-ot1.tfm)
Provides:       tex(RobotoMono-Thin-tlf-sc-ot1.vf)
Provides:       tex(RobotoMono-Thin-tlf-sc-t1--base.tfm)
Provides:       tex(RobotoMono-Thin-tlf-sc-t1.tfm)
Provides:       tex(RobotoMono-Thin-tlf-sc-t1.vf)
Provides:       tex(RobotoMono-Thin-tlf-t1--base.tfm)
Provides:       tex(RobotoMono-Thin-tlf-t1.tfm)
Provides:       tex(RobotoMono-Thin-tlf-t1.vf)
Provides:       tex(RobotoMono-Thin-tlf-ts1--base.tfm)
Provides:       tex(RobotoMono-Thin-tlf-ts1.tfm)
Provides:       tex(RobotoMono-Thin-tlf-ts1.vf)
Provides:       tex(RobotoMono-ThinItalic-tlf-ly1--base.tfm)
Provides:       tex(RobotoMono-ThinItalic-tlf-ly1.tfm)
Provides:       tex(RobotoMono-ThinItalic-tlf-ly1.vf)
Provides:       tex(RobotoMono-ThinItalic-tlf-ot1.tfm)
Provides:       tex(RobotoMono-ThinItalic-tlf-sc-ly1--base.tfm)
Provides:       tex(RobotoMono-ThinItalic-tlf-sc-ly1.tfm)
Provides:       tex(RobotoMono-ThinItalic-tlf-sc-ly1.vf)
Provides:       tex(RobotoMono-ThinItalic-tlf-sc-ot1--base.tfm)
Provides:       tex(RobotoMono-ThinItalic-tlf-sc-ot1.tfm)
Provides:       tex(RobotoMono-ThinItalic-tlf-sc-ot1.vf)
Provides:       tex(RobotoMono-ThinItalic-tlf-sc-t1--base.tfm)
Provides:       tex(RobotoMono-ThinItalic-tlf-sc-t1.tfm)
Provides:       tex(RobotoMono-ThinItalic-tlf-sc-t1.vf)
Provides:       tex(RobotoMono-ThinItalic-tlf-t1--base.tfm)
Provides:       tex(RobotoMono-ThinItalic-tlf-t1.tfm)
Provides:       tex(RobotoMono-ThinItalic-tlf-t1.vf)
Provides:       tex(RobotoMono-ThinItalic-tlf-ts1--base.tfm)
Provides:       tex(RobotoMono-ThinItalic-tlf-ts1.tfm)
Provides:       tex(RobotoMono-ThinItalic-tlf-ts1.vf)
Provides:       tex(RobotoSlab-Bold-tlf-ly1--base.tfm)
Provides:       tex(RobotoSlab-Bold-tlf-ly1.tfm)
Provides:       tex(RobotoSlab-Bold-tlf-ly1.vf)
Provides:       tex(RobotoSlab-Bold-tlf-ot1.tfm)
Provides:       tex(RobotoSlab-Bold-tlf-sc-ly1--base.tfm)
Provides:       tex(RobotoSlab-Bold-tlf-sc-ly1.tfm)
Provides:       tex(RobotoSlab-Bold-tlf-sc-ly1.vf)
Provides:       tex(RobotoSlab-Bold-tlf-sc-ot1--base.tfm)
Provides:       tex(RobotoSlab-Bold-tlf-sc-ot1.tfm)
Provides:       tex(RobotoSlab-Bold-tlf-sc-ot1.vf)
Provides:       tex(RobotoSlab-Bold-tlf-sc-t1--base.tfm)
Provides:       tex(RobotoSlab-Bold-tlf-sc-t1.tfm)
Provides:       tex(RobotoSlab-Bold-tlf-sc-t1.vf)
Provides:       tex(RobotoSlab-Bold-tlf-t1--base.tfm)
Provides:       tex(RobotoSlab-Bold-tlf-t1.tfm)
Provides:       tex(RobotoSlab-Bold-tlf-t1.vf)
Provides:       tex(RobotoSlab-Bold-tlf-ts1--base.tfm)
Provides:       tex(RobotoSlab-Bold-tlf-ts1.tfm)
Provides:       tex(RobotoSlab-Bold-tlf-ts1.vf)
Provides:       tex(RobotoSlab-Light-tlf-ly1--base.tfm)
Provides:       tex(RobotoSlab-Light-tlf-ly1.tfm)
Provides:       tex(RobotoSlab-Light-tlf-ly1.vf)
Provides:       tex(RobotoSlab-Light-tlf-ot1.tfm)
Provides:       tex(RobotoSlab-Light-tlf-sc-ly1--base.tfm)
Provides:       tex(RobotoSlab-Light-tlf-sc-ly1.tfm)
Provides:       tex(RobotoSlab-Light-tlf-sc-ly1.vf)
Provides:       tex(RobotoSlab-Light-tlf-sc-ot1--base.tfm)
Provides:       tex(RobotoSlab-Light-tlf-sc-ot1.tfm)
Provides:       tex(RobotoSlab-Light-tlf-sc-ot1.vf)
Provides:       tex(RobotoSlab-Light-tlf-sc-t1--base.tfm)
Provides:       tex(RobotoSlab-Light-tlf-sc-t1.tfm)
Provides:       tex(RobotoSlab-Light-tlf-sc-t1.vf)
Provides:       tex(RobotoSlab-Light-tlf-t1--base.tfm)
Provides:       tex(RobotoSlab-Light-tlf-t1.tfm)
Provides:       tex(RobotoSlab-Light-tlf-t1.vf)
Provides:       tex(RobotoSlab-Light-tlf-ts1--base.tfm)
Provides:       tex(RobotoSlab-Light-tlf-ts1.tfm)
Provides:       tex(RobotoSlab-Light-tlf-ts1.vf)
Provides:       tex(RobotoSlab-Regular-tlf-ly1--base.tfm)
Provides:       tex(RobotoSlab-Regular-tlf-ly1.tfm)
Provides:       tex(RobotoSlab-Regular-tlf-ly1.vf)
Provides:       tex(RobotoSlab-Regular-tlf-ot1.tfm)
Provides:       tex(RobotoSlab-Regular-tlf-sc-ly1--base.tfm)
Provides:       tex(RobotoSlab-Regular-tlf-sc-ly1.tfm)
Provides:       tex(RobotoSlab-Regular-tlf-sc-ly1.vf)
Provides:       tex(RobotoSlab-Regular-tlf-sc-ot1--base.tfm)
Provides:       tex(RobotoSlab-Regular-tlf-sc-ot1.tfm)
Provides:       tex(RobotoSlab-Regular-tlf-sc-ot1.vf)
Provides:       tex(RobotoSlab-Regular-tlf-sc-t1--base.tfm)
Provides:       tex(RobotoSlab-Regular-tlf-sc-t1.tfm)
Provides:       tex(RobotoSlab-Regular-tlf-sc-t1.vf)
Provides:       tex(RobotoSlab-Regular-tlf-t1--base.tfm)
Provides:       tex(RobotoSlab-Regular-tlf-t1.tfm)
Provides:       tex(RobotoSlab-Regular-tlf-t1.vf)
Provides:       tex(RobotoSlab-Regular-tlf-ts1--base.tfm)
Provides:       tex(RobotoSlab-Regular-tlf-ts1.tfm)
Provides:       tex(RobotoSlab-Regular-tlf-ts1.vf)
Provides:       tex(RobotoSlab-Thin-tlf-ly1--base.tfm)
Provides:       tex(RobotoSlab-Thin-tlf-ly1.tfm)
Provides:       tex(RobotoSlab-Thin-tlf-ly1.vf)
Provides:       tex(RobotoSlab-Thin-tlf-ot1.tfm)
Provides:       tex(RobotoSlab-Thin-tlf-sc-ly1--base.tfm)
Provides:       tex(RobotoSlab-Thin-tlf-sc-ly1.tfm)
Provides:       tex(RobotoSlab-Thin-tlf-sc-ly1.vf)
Provides:       tex(RobotoSlab-Thin-tlf-sc-ot1--base.tfm)
Provides:       tex(RobotoSlab-Thin-tlf-sc-ot1.tfm)
Provides:       tex(RobotoSlab-Thin-tlf-sc-ot1.vf)
Provides:       tex(RobotoSlab-Thin-tlf-sc-t1--base.tfm)
Provides:       tex(RobotoSlab-Thin-tlf-sc-t1.tfm)
Provides:       tex(RobotoSlab-Thin-tlf-sc-t1.vf)
Provides:       tex(RobotoSlab-Thin-tlf-t1--base.tfm)
Provides:       tex(RobotoSlab-Thin-tlf-t1.tfm)
Provides:       tex(RobotoSlab-Thin-tlf-t1.vf)
Provides:       tex(RobotoSlab-Thin-tlf-ts1--base.tfm)
Provides:       tex(RobotoSlab-Thin-tlf-ts1.tfm)
Provides:       tex(RobotoSlab-Thin-tlf-ts1.vf)
Provides:       tex(T1Roboto-LF.fd)
Provides:       tex(T1Roboto-OsF.fd)
Provides:       tex(T1Roboto-TLF.fd)
Provides:       tex(T1Roboto-TOsF.fd)
Provides:       tex(T1RobotoCondensed-LF.fd)
Provides:       tex(T1RobotoCondensed-OsF.fd)
Provides:       tex(T1RobotoCondensed-TLF.fd)
Provides:       tex(T1RobotoCondensed-TOsF.fd)
Provides:       tex(T1RobotoMono-TLF.fd)
Provides:       tex(T1RobotoSlab-TLF.fd)
Provides:       tex(TS1Roboto-LF.fd)
Provides:       tex(TS1Roboto-OsF.fd)
Provides:       tex(TS1Roboto-TLF.fd)
Provides:       tex(TS1Roboto-TOsF.fd)
Provides:       tex(TS1RobotoCondensed-LF.fd)
Provides:       tex(TS1RobotoCondensed-OsF.fd)
Provides:       tex(TS1RobotoCondensed-TLF.fd)
Provides:       tex(TS1RobotoCondensed-TOsF.fd)
Provides:       tex(TS1RobotoMono-TLF.fd)
Provides:       tex(TS1RobotoSlab-TLF.fd)
Provides:       tex(rbto_35j2t6.enc)
Provides:       tex(rbto_54ufeq.enc)
Provides:       tex(rbto_5au2tj.enc)
Provides:       tex(rbto_5xgh2b.enc)
Provides:       tex(rbto_636fvq.enc)
Provides:       tex(rbto_643awl.enc)
Provides:       tex(rbto_6i2fao.enc)
Provides:       tex(rbto_7juiin.enc)
Provides:       tex(rbto_b6sxnv.enc)
Provides:       tex(rbto_bopmz4.enc)
Provides:       tex(rbto_bsqqk2.enc)
Provides:       tex(rbto_cjgvd6.enc)
Provides:       tex(rbto_ddkove.enc)
Provides:       tex(rbto_dfqeeu.enc)
Provides:       tex(rbto_e24joy.enc)
Provides:       tex(rbto_h6xohf.enc)
Provides:       tex(rbto_hlrajr.enc)
Provides:       tex(rbto_hsw3yt.enc)
Provides:       tex(rbto_ihpqsf.enc)
Provides:       tex(rbto_lhlrii.enc)
Provides:       tex(rbto_lxpby6.enc)
Provides:       tex(rbto_n6nas2.enc)
Provides:       tex(rbto_ocbbsb.enc)
Provides:       tex(rbto_ppfdyj.enc)
Provides:       tex(rbto_pxp4cf.enc)
Provides:       tex(rbto_rehtu3.enc)
Provides:       tex(rbto_s7kfgd.enc)
Provides:       tex(rbto_schjax.enc)
Provides:       tex(rbto_svcybe.enc)
Provides:       tex(rbto_swa2hd.enc)
Provides:       tex(rbto_t46jwv.enc)
Provides:       tex(rbto_tj42ls.enc)
Provides:       tex(rbto_uf77so.enc)
Provides:       tex(rbto_urgg6g.enc)
Provides:       tex(rbto_usdwn6.enc)
Provides:       tex(rbto_wkn3wn.enc)
Provides:       tex(rbto_wttfgh.enc)
Provides:       tex(rbto_xyzkxs.enc)
Provides:       tex(rbto_z4nc45.enc)
Provides:       tex(rbto_zu4wd5.enc)
Provides:       tex(roboto-mono.sty)
Provides:       tex(roboto.map)
Provides:       tex(roboto.sty)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source273:      roboto.tar.xz
Source274:      roboto.doc.tar.xz

%description -n texlive-roboto
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Roboto, RobotoCondensed, RobotoMono and
RobotoSlab families of fonts, designed by Christian Robertson
for Google.

date: 2019-04-06 03:55:05 +0000


%package -n texlive-roboto-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn50809
Release:        0
Summary:        Documentation for texlive-roboto
License:        Apache-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/

%description -n texlive-roboto-doc
This package includes the documentation for texlive-roboto


%package -n texlive-roboto-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn50809
Release:        0
Summary:        Severed fonts for texlive-roboto
License:        Apache-1.0
Group:          Productivity/Publishing/TeX/Fonts
Url:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-roboto-fonts
The  separated fonts package for texlive-roboto
%post -n texlive-roboto
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap roboto.map' >> /var/run/texlive/run-updmap

%postun -n texlive-roboto 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap roboto.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-roboto
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-roboto-fonts
%files -n texlive-roboto-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/roboto/COPYRIGHT.txt
%{_texmfdistdir}/doc/fonts/roboto/ChangeLogLaTeX.txt
%{_texmfdistdir}/doc/fonts/roboto/DESCRIPTION.en_us.html
%{_texmfdistdir}/doc/fonts/roboto/LICENSE.txt
%{_texmfdistdir}/doc/fonts/roboto/README
%{_texmfdistdir}/doc/fonts/roboto/RobotoSpecimenBook.pdf
%{_texmfdistdir}/doc/fonts/roboto/roboto-samples.pdf
%{_texmfdistdir}/doc/fonts/roboto/roboto-samples.tex

%files -n texlive-roboto
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_35j2t6.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_54ufeq.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_5au2tj.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_5xgh2b.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_636fvq.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_643awl.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_6i2fao.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_7juiin.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_b6sxnv.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_bopmz4.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_bsqqk2.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_cjgvd6.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_ddkove.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_dfqeeu.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_e24joy.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_h6xohf.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_hlrajr.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_hsw3yt.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_ihpqsf.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_lhlrii.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_lxpby6.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_n6nas2.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_ocbbsb.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_ppfdyj.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_pxp4cf.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_rehtu3.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_s7kfgd.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_schjax.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_svcybe.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_swa2hd.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_t46jwv.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_tj42ls.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_uf77so.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_urgg6g.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_usdwn6.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_wkn3wn.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_wttfgh.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_xyzkxs.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_z4nc45.enc
%{_texmfdistdir}/fonts/enc/dvips/roboto/rbto_zu4wd5.enc
%{_texmfdistdir}/fonts/map/dvips/roboto/roboto.map
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/Roboto-Black.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/Roboto-BlackItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/Roboto-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/Roboto-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/Roboto-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/Roboto-Light.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/Roboto-LightItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/Roboto-Medium.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/Roboto-MediumItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/Roboto-Regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/Roboto-Thin.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/Roboto-ThinItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/RobotoCondensed-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/RobotoCondensed-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/RobotoCondensed-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/RobotoCondensed-Light.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/RobotoCondensed-LightItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/RobotoCondensed-Regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/RobotoMono-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/RobotoMono-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/RobotoMono-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/RobotoMono-Light.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/RobotoMono-LightItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/RobotoMono-Medium.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/RobotoMono-MediumItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/RobotoMono-Regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/RobotoMono-Thin.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/RobotoMono-ThinItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/RobotoSlab-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/RobotoSlab-Light.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/RobotoSlab-Regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/google/roboto/RobotoSlab-Thin.otf
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Black-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BlackItalic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Bold-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-BoldItalic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Italic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Light-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-LightItalic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Medium-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-MediumItalic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Regular-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-Thin-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/Roboto-ThinItalic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Bold-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-BoldItalic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Italic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Light-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-LightItalic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoCondensed-Regular-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Bold-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Bold-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Bold-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Bold-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Bold-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Bold-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-BoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-BoldItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-BoldItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-BoldItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-BoldItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-BoldItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-BoldItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Italic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Italic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Italic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Italic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Italic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Italic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Light-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Light-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Light-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Light-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Light-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Light-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Light-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Light-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Light-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Light-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Light-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Light-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Light-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-LightItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-LightItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-LightItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-LightItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-LightItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-LightItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-LightItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-LightItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-LightItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-LightItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-LightItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-LightItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-LightItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Medium-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Medium-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Medium-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Medium-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Medium-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Medium-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Medium-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Medium-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Medium-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Medium-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Medium-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Medium-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Medium-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-MediumItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-MediumItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-MediumItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-MediumItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-MediumItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-MediumItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-MediumItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-MediumItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-MediumItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-MediumItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-MediumItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-MediumItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-MediumItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Regular-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Regular-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Regular-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Regular-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Regular-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Regular-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Regular-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Regular-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Regular-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Thin-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Thin-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Thin-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Thin-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Thin-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Thin-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Thin-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Thin-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Thin-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Thin-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Thin-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Thin-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-Thin-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-ThinItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-ThinItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-ThinItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-ThinItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-ThinItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-ThinItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-ThinItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-ThinItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-ThinItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-ThinItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-ThinItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-ThinItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoMono-ThinItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Bold-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Bold-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Bold-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Bold-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Bold-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Bold-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Light-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Light-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Light-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Light-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Light-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Light-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Light-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Light-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Light-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Light-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Light-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Light-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Light-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Regular-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Regular-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Regular-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Regular-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Regular-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Regular-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Regular-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Regular-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Regular-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Thin-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Thin-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Thin-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Thin-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Thin-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Thin-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Thin-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Thin-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Thin-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Thin-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Thin-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Thin-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/google/roboto/RobotoSlab-Thin-tlf-ts1.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/Roboto-Black.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/Roboto-BlackItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/Roboto-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/Roboto-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/Roboto-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/Roboto-Light.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/Roboto-LightItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/Roboto-Medium.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/Roboto-MediumItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/Roboto-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/Roboto-Thin.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/Roboto-ThinItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/RobotoCondensed-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/RobotoCondensed-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/RobotoCondensed-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/RobotoCondensed-Light.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/RobotoCondensed-LightItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/RobotoCondensed-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/RobotoMono-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/RobotoMono-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/RobotoMono-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/RobotoMono-Light.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/RobotoMono-LightItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/RobotoMono-Medium.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/RobotoMono-MediumItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/RobotoMono-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/RobotoMono-Thin.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/RobotoMono-ThinItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/RobotoSlab-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/RobotoSlab-Light.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/RobotoSlab-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/google/roboto/RobotoSlab-Thin.pfb
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-lf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-osf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Black-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BlackItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-osf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Bold-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-BoldItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Italic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-lf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-osf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Light-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-LightItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-lf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-osf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Medium-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-MediumItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-osf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Regular-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-lf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-osf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-Thin-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/Roboto-ThinItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-osf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Bold-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-BoldItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Italic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-lf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-osf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Light-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-LightItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-osf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoCondensed-Regular-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Bold-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Bold-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Bold-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-BoldItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-BoldItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-BoldItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Italic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Italic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Italic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Light-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Light-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Light-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Light-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Light-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Light-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-LightItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-LightItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-LightItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-LightItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-LightItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-LightItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Medium-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Medium-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Medium-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Medium-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Medium-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Medium-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-MediumItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-MediumItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-MediumItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-MediumItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-MediumItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-MediumItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Regular-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Regular-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Regular-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Regular-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Regular-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Thin-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Thin-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Thin-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Thin-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Thin-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-Thin-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-ThinItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-ThinItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-ThinItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-ThinItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-ThinItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoMono-ThinItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Bold-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Bold-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Bold-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Light-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Light-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Light-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Light-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Light-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Light-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Regular-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Regular-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Regular-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Regular-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Regular-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Thin-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Thin-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Thin-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Thin-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Thin-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/google/roboto/RobotoSlab-Thin-tlf-ts1.vf
%{_texmfdistdir}/tex/latex/roboto/LY1Roboto-LF.fd
%{_texmfdistdir}/tex/latex/roboto/LY1Roboto-OsF.fd
%{_texmfdistdir}/tex/latex/roboto/LY1Roboto-TLF.fd
%{_texmfdistdir}/tex/latex/roboto/LY1Roboto-TOsF.fd
%{_texmfdistdir}/tex/latex/roboto/LY1RobotoCondensed-LF.fd
%{_texmfdistdir}/tex/latex/roboto/LY1RobotoCondensed-OsF.fd
%{_texmfdistdir}/tex/latex/roboto/LY1RobotoCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/roboto/LY1RobotoCondensed-TOsF.fd
%{_texmfdistdir}/tex/latex/roboto/LY1RobotoMono-TLF.fd
%{_texmfdistdir}/tex/latex/roboto/LY1RobotoSlab-TLF.fd
%{_texmfdistdir}/tex/latex/roboto/OT1Roboto-LF.fd
%{_texmfdistdir}/tex/latex/roboto/OT1Roboto-OsF.fd
%{_texmfdistdir}/tex/latex/roboto/OT1Roboto-TLF.fd
%{_texmfdistdir}/tex/latex/roboto/OT1Roboto-TOsF.fd
%{_texmfdistdir}/tex/latex/roboto/OT1RobotoCondensed-LF.fd
%{_texmfdistdir}/tex/latex/roboto/OT1RobotoCondensed-OsF.fd
%{_texmfdistdir}/tex/latex/roboto/OT1RobotoCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/roboto/OT1RobotoCondensed-TOsF.fd
%{_texmfdistdir}/tex/latex/roboto/OT1RobotoMono-TLF.fd
%{_texmfdistdir}/tex/latex/roboto/OT1RobotoSlab-TLF.fd
%{_texmfdistdir}/tex/latex/roboto/T1Roboto-LF.fd
%{_texmfdistdir}/tex/latex/roboto/T1Roboto-OsF.fd
%{_texmfdistdir}/tex/latex/roboto/T1Roboto-TLF.fd
%{_texmfdistdir}/tex/latex/roboto/T1Roboto-TOsF.fd
%{_texmfdistdir}/tex/latex/roboto/T1RobotoCondensed-LF.fd
%{_texmfdistdir}/tex/latex/roboto/T1RobotoCondensed-OsF.fd
%{_texmfdistdir}/tex/latex/roboto/T1RobotoCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/roboto/T1RobotoCondensed-TOsF.fd
%{_texmfdistdir}/tex/latex/roboto/T1RobotoMono-TLF.fd
%{_texmfdistdir}/tex/latex/roboto/T1RobotoSlab-TLF.fd
%{_texmfdistdir}/tex/latex/roboto/TS1Roboto-LF.fd
%{_texmfdistdir}/tex/latex/roboto/TS1Roboto-OsF.fd
%{_texmfdistdir}/tex/latex/roboto/TS1Roboto-TLF.fd
%{_texmfdistdir}/tex/latex/roboto/TS1Roboto-TOsF.fd
%{_texmfdistdir}/tex/latex/roboto/TS1RobotoCondensed-LF.fd
%{_texmfdistdir}/tex/latex/roboto/TS1RobotoCondensed-OsF.fd
%{_texmfdistdir}/tex/latex/roboto/TS1RobotoCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/roboto/TS1RobotoCondensed-TOsF.fd
%{_texmfdistdir}/tex/latex/roboto/TS1RobotoMono-TLF.fd
%{_texmfdistdir}/tex/latex/roboto/TS1RobotoSlab-TLF.fd
%{_texmfdistdir}/tex/latex/roboto/roboto-mono.sty
%{_texmfdistdir}/tex/latex/roboto/roboto.sty

%files -n texlive-roboto-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-roboto
%config %{_sysconfdir}/fonts/conf.avail/58-texlive-roboto.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-roboto.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-roboto/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-roboto/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-roboto/fonts.scale
%{_datadir}/fonts/texlive-roboto/Roboto-Black.otf
%{_datadir}/fonts/texlive-roboto/Roboto-BlackItalic.otf
%{_datadir}/fonts/texlive-roboto/Roboto-Bold.otf
%{_datadir}/fonts/texlive-roboto/Roboto-BoldItalic.otf
%{_datadir}/fonts/texlive-roboto/Roboto-Italic.otf
%{_datadir}/fonts/texlive-roboto/Roboto-Light.otf
%{_datadir}/fonts/texlive-roboto/Roboto-LightItalic.otf
%{_datadir}/fonts/texlive-roboto/Roboto-Medium.otf
%{_datadir}/fonts/texlive-roboto/Roboto-MediumItalic.otf
%{_datadir}/fonts/texlive-roboto/Roboto-Regular.otf
%{_datadir}/fonts/texlive-roboto/Roboto-Thin.otf
%{_datadir}/fonts/texlive-roboto/Roboto-ThinItalic.otf
%{_datadir}/fonts/texlive-roboto/RobotoCondensed-Bold.otf
%{_datadir}/fonts/texlive-roboto/RobotoCondensed-BoldItalic.otf
%{_datadir}/fonts/texlive-roboto/RobotoCondensed-Italic.otf
%{_datadir}/fonts/texlive-roboto/RobotoCondensed-Light.otf
%{_datadir}/fonts/texlive-roboto/RobotoCondensed-LightItalic.otf
%{_datadir}/fonts/texlive-roboto/RobotoCondensed-Regular.otf
%{_datadir}/fonts/texlive-roboto/RobotoMono-Bold.otf
%{_datadir}/fonts/texlive-roboto/RobotoMono-BoldItalic.otf
%{_datadir}/fonts/texlive-roboto/RobotoMono-Italic.otf
%{_datadir}/fonts/texlive-roboto/RobotoMono-Light.otf
%{_datadir}/fonts/texlive-roboto/RobotoMono-LightItalic.otf
%{_datadir}/fonts/texlive-roboto/RobotoMono-Medium.otf
%{_datadir}/fonts/texlive-roboto/RobotoMono-MediumItalic.otf
%{_datadir}/fonts/texlive-roboto/RobotoMono-Regular.otf
%{_datadir}/fonts/texlive-roboto/RobotoMono-Thin.otf
%{_datadir}/fonts/texlive-roboto/RobotoMono-ThinItalic.otf
%{_datadir}/fonts/texlive-roboto/RobotoSlab-Bold.otf
%{_datadir}/fonts/texlive-roboto/RobotoSlab-Light.otf
%{_datadir}/fonts/texlive-roboto/RobotoSlab-Regular.otf
%{_datadir}/fonts/texlive-roboto/RobotoSlab-Thin.otf
%{_datadir}/fonts/texlive-roboto/Roboto-Black.pfb
%{_datadir}/fonts/texlive-roboto/Roboto-BlackItalic.pfb
%{_datadir}/fonts/texlive-roboto/Roboto-Bold.pfb
%{_datadir}/fonts/texlive-roboto/Roboto-BoldItalic.pfb
%{_datadir}/fonts/texlive-roboto/Roboto-Italic.pfb
%{_datadir}/fonts/texlive-roboto/Roboto-Light.pfb
%{_datadir}/fonts/texlive-roboto/Roboto-LightItalic.pfb
%{_datadir}/fonts/texlive-roboto/Roboto-Medium.pfb
%{_datadir}/fonts/texlive-roboto/Roboto-MediumItalic.pfb
%{_datadir}/fonts/texlive-roboto/Roboto-Regular.pfb
%{_datadir}/fonts/texlive-roboto/Roboto-Thin.pfb
%{_datadir}/fonts/texlive-roboto/Roboto-ThinItalic.pfb
%{_datadir}/fonts/texlive-roboto/RobotoCondensed-Bold.pfb
%{_datadir}/fonts/texlive-roboto/RobotoCondensed-BoldItalic.pfb
%{_datadir}/fonts/texlive-roboto/RobotoCondensed-Italic.pfb
%{_datadir}/fonts/texlive-roboto/RobotoCondensed-Light.pfb
%{_datadir}/fonts/texlive-roboto/RobotoCondensed-LightItalic.pfb
%{_datadir}/fonts/texlive-roboto/RobotoCondensed-Regular.pfb
%{_datadir}/fonts/texlive-roboto/RobotoMono-Bold.pfb
%{_datadir}/fonts/texlive-roboto/RobotoMono-BoldItalic.pfb
%{_datadir}/fonts/texlive-roboto/RobotoMono-Italic.pfb
%{_datadir}/fonts/texlive-roboto/RobotoMono-Light.pfb
%{_datadir}/fonts/texlive-roboto/RobotoMono-LightItalic.pfb
%{_datadir}/fonts/texlive-roboto/RobotoMono-Medium.pfb
%{_datadir}/fonts/texlive-roboto/RobotoMono-MediumItalic.pfb
%{_datadir}/fonts/texlive-roboto/RobotoMono-Regular.pfb
%{_datadir}/fonts/texlive-roboto/RobotoMono-Thin.pfb
%{_datadir}/fonts/texlive-roboto/RobotoMono-ThinItalic.pfb
%{_datadir}/fonts/texlive-roboto/RobotoSlab-Bold.pfb
%{_datadir}/fonts/texlive-roboto/RobotoSlab-Light.pfb
%{_datadir}/fonts/texlive-roboto/RobotoSlab-Regular.pfb
%{_datadir}/fonts/texlive-roboto/RobotoSlab-Thin.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-roboto-fonts-%{texlive_version}.%{texlive_noarch}.svn50809-%{release}-zypper
%endif

%package -n texlive-robustcommand
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn15878
Release:        0
Summary:        Declare robust command, with \newcommand checks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Requires(pre): texlive >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Recommends:     texlive-robustcommand-doc >= %{texlive_version}
Provides:       tex(robustcommand.sty)
# Download at ftp://ftp.ctan.org/pub/tex/systems/texlive/tlnet/archive/
# from 20190407
Source275:      robustcommand.tar.xz
Source276:      robustcommand.doc.tar.xz

%description -n texlive-robustcommand
The package merely provides a variation of
\DeclareRobustCommand, which checks for the existence of a
command before declaring it robust.

date: 2016-06-24 17:18:15 +0000


%package -n texlive-robustcommand-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn15878
Release:        0
Summary:        Documentation for texlive-robustcommand
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
Url:            http://www.tug.org/texlive/
Provides:       locale(texlive-robustcommand-doc:de)

%description -n texlive-robustcommand-doc
This package includes the documentation for texlive-robustcommand

%post -n texlive-robustcommand
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-robustcommand 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-robustcommand
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-robustcommand-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/robustcommand/README
%{_texmfdistdir}/doc/latex/robustcommand/robustcommand.pdf

%files -n texlive-robustcommand
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/robustcommand/robustcommand.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-robustcommand-%{texlive_version}.%{texlive_noarch}.0.0.1svn15878-%{release}-zypper
%endif

%prep
%setup -q -c -T

%build

%install
    rm -rf %{buildroot}
    mkdir -p %{buildroot}%{_texmfdistdir}
    mkdir -p %{buildroot}%{_texmfmaindir}/tlpkg/tlpostcode
    mkdir -p %{buildroot}%{_datadir}/texlive/tlpkg
    mkdir -p %{buildroot}/var/adm/update-scripts
    ln -sf ../../share/texmf        %{buildroot}%{_datadir}/texlive/texmf-dist
    ln -sf ../../share/texmf        %{buildroot}%{_datadir}/texlive/texmf
    ln -sf ../../../share/texmf/tlpkg/tlpostcode \
                                    %{buildroot}%{_datadir}/texlive/tlpkg/tlpostcode
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-pdf-%{texlive_version}.%{texlive_noarch}.1.2dsvn44665-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:1} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:2} -C %{buildroot}%{_datadir}/texlive
    rm -vf  %{buildroot}%{_texmfdistdir}/scripts/pst-pdf/ps4pdf.bat
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-pdgr-%{texlive_version}.%{texlive_noarch}.0.0.4svn45875-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:3} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:4} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-perspective-%{texlive_version}.%{texlive_noarch}.1.05svn39585-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:5} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:6} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-platon-%{texlive_version}.%{texlive_noarch}.0.0.01svn16538-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:7} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:8} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-plot-%{texlive_version}.%{texlive_noarch}.1.91svn48526-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:9} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:10} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-poker-%{texlive_version}.%{texlive_noarch}.0.0.03svn48347-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:11} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:12} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-poly-%{texlive_version}.%{texlive_noarch}.1.63svn35062-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:13} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:14} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-pulley-%{texlive_version}.%{texlive_noarch}.0.0.02svn45316-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:15} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:16} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-qtree-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:17} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:18} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-rputover-%{texlive_version}.%{texlive_noarch}.1.0svn44724-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:19} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:20} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-rubans-%{texlive_version}.%{texlive_noarch}.1.2svn23464-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:21} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:22} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-shell-%{texlive_version}.%{texlive_noarch}.0.0.03svn42840-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:23} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:24} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-sigsys-%{texlive_version}.%{texlive_noarch}.1.4svn21667-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:25} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:26} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-slpe-%{texlive_version}.%{texlive_noarch}.1.31svn24391-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:27} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:28} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-solarsystem-%{texlive_version}.%{texlive_noarch}.0.0.13svn45097-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:29} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:30} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-solides3d-%{texlive_version}.%{texlive_noarch}.4.34asvn49520-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:31} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:32} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-soroban-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:33} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:34} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-spectra-%{texlive_version}.%{texlive_noarch}.0.0.91svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:35} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:36} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-spinner-%{texlive_version}.%{texlive_noarch}.1.02svn44507-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:37} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:38} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-spirograph-%{texlive_version}.%{texlive_noarch}.0.0.41svn35026-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:39} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:40} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-stru-%{texlive_version}.%{texlive_noarch}.0.0.13svn38613-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:41} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:42} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-support-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:43} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-text-%{texlive_version}.%{texlive_noarch}.1.02svn49542-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:44} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:45} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-thick-%{texlive_version}.%{texlive_noarch}.1.0svn16369-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:46} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:47} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-tools-%{texlive_version}.%{texlive_noarch}.0.0.09bsvn45978-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:48} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:49} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-tree-%{texlive_version}.%{texlive_noarch}.1.13svn43272-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:50} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:51} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-tvz-%{texlive_version}.%{texlive_noarch}.1.01svn23451-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:52} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:53} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-uml-%{texlive_version}.%{texlive_noarch}.0.0.83svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:54} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:55} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-vectorian-%{texlive_version}.%{texlive_noarch}.0.0.4svn28801-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:56} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:57} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-vehicle-%{texlive_version}.%{texlive_noarch}.1.2svn45320-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:58} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:59} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-venn-%{texlive_version}.%{texlive_noarch}.0.0.01svn49316-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:60} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:61} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-vowel-%{texlive_version}.%{texlive_noarch}.1.0svn25228-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:62} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:63} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst-vue3d-%{texlive_version}.%{texlive_noarch}.1.24svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:64} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:65} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pst2pdf-%{texlive_version}.%{texlive_noarch}.0.0.18svn45476-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:66} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:67} -C %{buildroot}%{_datadir}/texlive
    # Correct wrong perl scripts if any
    for scr in %{_texmfdistdir}/scripts/pst2pdf/pst2pdf.pl
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		1,/\sif 0;$/d
		1
		i
		#! /usr/bin/perl
		.
		w
		1,3p
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pstool-%{texlive_version}.%{texlive_noarch}.1.5esvn46393-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:68} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:69} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pstools-%{texlive_version}.%{texlive_noarch}.1.68svn50602-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:70} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:71} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/ps2eps/ps2eps.pl
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pstricks-%{texlive_version}.%{texlive_noarch}.2.96svn50101-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:72} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:73} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pstricks-add-%{texlive_version}.%{texlive_noarch}.3.87svn49680-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:74} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:75} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pstricks_calcnotes-%{texlive_version}.%{texlive_noarch}.1.2svn34363-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:76} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pstring-%{texlive_version}.%{texlive_noarch}.svn42857-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:77} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:78} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ptex-%{texlive_version}.%{texlive_noarch}.svn50664-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:79} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ptex-base-%{texlive_version}.%{texlive_noarch}.svn50731-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:80} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:81} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ptex-fontmaps-%{texlive_version}.%{texlive_noarch}.20190318.0svn50446-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:82} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:83} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/ptex-fontmaps/kanji-config-updmap.pl \
	       %{_texmfdistdir}/scripts/ptex-fontmaps/kanji-fontmap-creator.pl
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ptex-fonts-%{texlive_version}.%{texlive_noarch}.svn46940-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:84} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:85} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ptex-manual-%{texlive_version}.%{texlive_noarch}.svn50733-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:86} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:87} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ptex2pdf-%{texlive_version}.%{texlive_noarch}.20181212.0svn49396-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:88} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:89} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/ptex2pdf/ptex2pdf.lua
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ptext-%{texlive_version}.%{texlive_noarch}.1.1svn30171-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:90} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:91} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ptolemaicastronomy-%{texlive_version}.%{texlive_noarch}.1.0svn50810-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:92} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:93} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ptptex-%{texlive_version}.%{texlive_noarch}.0.0.91svn19440-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:94} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:95} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-punk-%{texlive_version}.%{texlive_noarch}.svn27388-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:96} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:97} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-punk-latex-%{texlive_version}.%{texlive_noarch}.1.1svn27389-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:98} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:99} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-punknova-fonts-%{texlive_version}.%{texlive_noarch}.1.003svn24649-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:100} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:101} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/doc/fonts/punknova/tools/build.py
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-punknova
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/punknova/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-punknova
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-punknova/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-punknova/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-punknova/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-punknova/fonts.scale
    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.avail
    (cat > %{buildroot}%{_sysconfdir}/fonts/conf.avail/58-texlive-punknova.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-punknova    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-punknova/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-purifyeps-%{texlive_version}.%{texlive_noarch}.1.1svn29725-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:102} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:103} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/purifyeps/purifyeps
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pxbase-%{texlive_version}.%{texlive_noarch}.1.1bsvn44756-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:104} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:105} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pxchfon-%{texlive_version}.%{texlive_noarch}.1.4asvn50556-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:106} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:107} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pxcjkcat-%{texlive_version}.%{texlive_noarch}.1.1svn47266-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:108} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:109} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pxfonts-fonts-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:110} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:111} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-pxfonts
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/pxfonts/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-pxfonts
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-pxfonts/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-pxfonts/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-pxfonts/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-pxfonts/fonts.scale
    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.avail
    (cat > %{buildroot}%{_sysconfdir}/fonts/conf.avail/58-texlive-pxfonts.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-pxfonts    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-pxfonts/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pxgreeks-%{texlive_version}.%{texlive_noarch}.1.0svn21838-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:112} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:113} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pxjahyper-%{texlive_version}.%{texlive_noarch}.0.0.3dsvn48207-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:114} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:115} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pxjodel-%{texlive_version}.%{texlive_noarch}.0.0.2asvn50009-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:116} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:117} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pxpgfmark-%{texlive_version}.%{texlive_noarch}.0.0.2svn30212-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:118} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:119} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pxrubrica-%{texlive_version}.%{texlive_noarch}.1.3csvn48421-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:120} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:121} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pxtatescale-%{texlive_version}.%{texlive_noarch}.0.0.4svn43009-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:122} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:123} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pxtxalfa-%{texlive_version}.%{texlive_noarch}.1svn23682-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:124} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:125} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pxufont-%{texlive_version}.%{texlive_noarch}.0.0.5svn50355-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:126} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:127} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pygmentex-%{texlive_version}.%{texlive_noarch}.0.0.8svn34996-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:128} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:129} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/pygmentex/pygmentex.py
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-python-%{texlive_version}.%{texlive_noarch}.0.0.21svn27064-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:130} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:131} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pythonhighlight-%{texlive_version}.%{texlive_noarch}.svn43191-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:132} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:133} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pythontex-%{texlive_version}.%{texlive_noarch}.0.0.16svn44860-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:134} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:135} -C %{buildroot}%{_datadir}/texlive
    # Correct wrong python scripts if any
    for scr in %{_texmfdistdir}/scripts/pythontex/pythontex_engines.py \
	       %{_texmfdistdir}/scripts/pythontex/pythontex_utils.py
    do
        test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		i
		#! /usr/bin/python
		.
		w
		q
	EOF
    done
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/doc/latex/pythontex/syncpdb.py
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/pythontex/depythontex.py \
	       %{_texmfdistdir}/scripts/pythontex/depythontex2.py \
	       %{_texmfdistdir}/scripts/pythontex/depythontex3.py \
	       %{_texmfdistdir}/scripts/pythontex/pythontex.py \
	       %{_texmfdistdir}/scripts/pythontex/pythontex2.py \
	       %{_texmfdistdir}/scripts/pythontex/pythontex3.py \
	       %{_texmfdistdir}/scripts/pythontex/pythontex_2to3.py \
	       %{_texmfdistdir}/scripts/pythontex/pythontex_install.py \
	       %{_texmfdistdir}/doc/latex/pythontex/syncpdb.py
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-qcircuit-%{texlive_version}.%{texlive_noarch}.2.6.0svn48400-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:136} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:137} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-qcm-%{texlive_version}.%{texlive_noarch}.2.1svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:138} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:139} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-qobitree-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:140} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:141} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-qpxqtx-%{texlive_version}.%{texlive_noarch}.svn45797-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:142} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:143} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-qrcode-%{texlive_version}.%{texlive_noarch}.1.51svn36065-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:144} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:145} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-qsharp-%{texlive_version}.%{texlive_noarch}.0.0.3.1901.1401svn49722-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:146} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:147} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-qstest-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:148} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:149} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-qsymbols-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:150} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:151} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-qtree-%{texlive_version}.%{texlive_noarch}.3.1bsvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:152} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:153} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-quantikz-%{texlive_version}.%{texlive_noarch}.0.0.9.4svn50869-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:154} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:155} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-quattrocento-fonts-%{texlive_version}.%{texlive_noarch}.svn50729-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:156} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:157} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-quattrocento
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/impallari/quattrocento/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/impallari/quattrocento/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-quattrocento
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-quattrocento/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-quattrocento/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-quattrocento/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-quattrocento/fonts.scale
    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.avail
    (cat > %{buildroot}%{_sysconfdir}/fonts/conf.avail/58-texlive-quattrocento.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-quattrocento    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-quattrocento/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-quattrocento.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-quattrocento/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-quicktype-%{texlive_version}.%{texlive_noarch}.0.0.1svn42183-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:158} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:159} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-quotchap-%{texlive_version}.%{texlive_noarch}.1.1svn28046-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:160} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:161} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-quoting-%{texlive_version}.%{texlive_noarch}.0.0.1csvn32818-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:162} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:163} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-quotmark-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:164} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:165} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-quran-%{texlive_version}.%{texlive_noarch}.1.5svn49563-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:166} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:167} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-quran-de-%{texlive_version}.%{texlive_noarch}.0.0.14svn49562-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:168} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:169} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-r_und_s-%{texlive_version}.%{texlive_noarch}.1.3isvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:170} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:171} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-raleway-fonts-%{texlive_version}.%{texlive_noarch}.1.4svn42629-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:172} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:173} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-raleway
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/impallari/raleway/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/impallari/raleway/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-raleway
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-raleway/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-raleway/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-raleway/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-raleway/fonts.scale
    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.avail
    (cat > %{buildroot}%{_sysconfdir}/fonts/conf.avail/58-texlive-raleway.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-raleway    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-raleway/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-raleway.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-raleway/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ran_toks-%{texlive_version}.%{texlive_noarch}.1.1svn44429-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:174} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:175} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-randbild-%{texlive_version}.%{texlive_noarch}.0.0.2svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:176} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:177} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-randomlist-%{texlive_version}.%{texlive_noarch}.1.3svn45281-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:178} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:179} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-randomwalk-%{texlive_version}.%{texlive_noarch}.0.0.6svn49513-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:180} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:181} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-randtext-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:182} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:183} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rank-2-roots-%{texlive_version}.%{texlive_noarch}.1.0svn48515-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:184} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:185} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rccol-%{texlive_version}.%{texlive_noarch}.1.2csvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:186} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:187} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rcs-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:188} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:189} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rcs-multi-%{texlive_version}.%{texlive_noarch}.0.0.1asvn21939-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:190} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:191} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rcsinfo-%{texlive_version}.%{texlive_noarch}.1.11svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:192} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:193} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-readarray-%{texlive_version}.%{texlive_noarch}.2.0svn42467-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:194} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:195} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-realboxes-%{texlive_version}.%{texlive_noarch}.0.0.2svn23581-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:196} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:197} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-realhats-%{texlive_version}.%{texlive_noarch}.2.0svn50134-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:198} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:199} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-realscripts-%{texlive_version}.%{texlive_noarch}.0.0.3dsvn39706-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:200} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:201} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rec-thy-%{texlive_version}.%{texlive_noarch}.3.01svn50047-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:202} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:203} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-recipe-%{texlive_version}.%{texlive_noarch}.0.0.9svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:204} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:205} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-recipebook-%{texlive_version}.%{texlive_noarch}.svn37026-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:206} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:207} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-recipecard-%{texlive_version}.%{texlive_noarch}.2.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:208} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:209} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rectopma-%{texlive_version}.%{texlive_noarch}.svn19980-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:210} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:211} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-recycle-fonts-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:212} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:213} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-recycle
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/recycle/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-recycle
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-recycle/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-recycle/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-recycle/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-recycle/fonts.scale
    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.avail
    (cat > %{buildroot}%{_sysconfdir}/fonts/conf.avail/58-texlive-recycle.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-recycle    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-recycle/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-refcheck-%{texlive_version}.%{texlive_noarch}.1.9.1svn29128-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:214} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:215} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-refenums-%{texlive_version}.%{texlive_noarch}.1.1.2svn44131-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:216} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:217} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-reflectgraphics-%{texlive_version}.%{texlive_noarch}.0.0.2csvn40612-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:218} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:219} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-refman-%{texlive_version}.%{texlive_noarch}.2.0esvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:220} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:221} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-refstyle-%{texlive_version}.%{texlive_noarch}.0.0.5svn20318-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:222} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:223} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-regcount-%{texlive_version}.%{texlive_noarch}.1.0svn19979-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:224} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:225} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-regexpatch-%{texlive_version}.%{texlive_noarch}.0.0.2dsvn47601-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:226} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:227} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-register-%{texlive_version}.%{texlive_noarch}.1.9svn49581-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:228} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:229} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/doc/latex/register/reg_list.pl
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-regstats-%{texlive_version}.%{texlive_noarch}.1.0hsvn25050-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:230} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:231} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-reledmac-%{texlive_version}.%{texlive_noarch}.2.31.2svn50740-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:232} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:233} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-relenc-%{texlive_version}.%{texlive_noarch}.svn22050-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:234} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:235} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-relsize-%{texlive_version}.%{texlive_noarch}.4.1svn30707-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:236} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:237} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-reotex-%{texlive_version}.%{texlive_noarch}.1.1svn34924-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:238} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:239} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-repeatindex-%{texlive_version}.%{texlive_noarch}.0.0.01svn24305-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:240} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:241} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-repere-%{texlive_version}.%{texlive_noarch}.17.11.2svn45779-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:242} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:243} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-repltext-%{texlive_version}.%{texlive_noarch}.1.0svn33442-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:244} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:245} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-resphilosophica-%{texlive_version}.%{texlive_noarch}.1.34svn50402-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:246} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:247} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-resumecls-%{texlive_version}.%{texlive_noarch}.0.0.3.2svn38427-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:248} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:249} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-resumemac-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:250} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:251} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-returntogrid-%{texlive_version}.%{texlive_noarch}.0.0.2svn48485-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:252} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:253} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-reverxii-%{texlive_version}.%{texlive_noarch}.svn24976-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:254} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-revquantum-%{texlive_version}.%{texlive_noarch}.0.0.11svn43505-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:255} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:256} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-revtex-%{texlive_version}.%{texlive_noarch}.4.2csvn49751-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:257} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:258} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-revtex4-%{texlive_version}.%{texlive_noarch}.4.0svn45873-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:259} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:260} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rgltxdoc-%{texlive_version}.%{texlive_noarch}.1svn49684-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:261} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:262} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ribbonproofs-%{texlive_version}.%{texlive_noarch}.1.0svn31137-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:263} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:264} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rjlparshap-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:265} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:266} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rlepsf-%{texlive_version}.%{texlive_noarch}.svn19082-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:267} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:268} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rmathbr-%{texlive_version}.%{texlive_noarch}.1.0.3svn40415-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:269} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:270} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-rmpage-%{texlive_version}.%{texlive_noarch}.0.0.92svn20002-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:271} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:272} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-roboto-fonts-%{texlive_version}.%{texlive_noarch}.svn50809-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:273} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:274} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-roboto
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/google/roboto/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/google/roboto/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-roboto
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-roboto/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-roboto/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-roboto/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-roboto/fonts.scale
    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.avail
    (cat > %{buildroot}%{_sysconfdir}/fonts/conf.avail/58-texlive-roboto.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-roboto    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-roboto/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-roboto.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-roboto/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-robustcommand-%{texlive_version}.%{texlive_noarch}.0.0.1svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:275} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:276} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Remove this
    rm -vrf %{buildroot}%{_texmfdistdir}/tlpkg/tlpobj
    rm -vrf %{buildroot}%{_texmfmaindir}/tlpkg/tlpobj
    rm -v  %{buildroot}%{_datadir}/texlive/texmf
    rm -v  %{buildroot}%{_datadir}/texlive/texmf-dist
    rm -vr %{buildroot}%{_datadir}/texlive
    # Handle manual pages
    rm -vf %{buildroot}%{_texmfmaindir}/doc/man/Makefile
    rm -vf %{buildroot}%{_texmfmaindir}/doc/man/man*/*.pdf
    rm -vf %{buildroot}%{_texmfdistdir}/doc/man/Makefile
    rm -vf %{buildroot}%{_texmfdistdir}/doc/man/man*/*.pdf
    for path in %{buildroot}%{_texmfmaindir}/doc/man/man? \
               %{buildroot}%{_texmfdistdir}/doc/man/man?
    do
        test -d "$path" || continue
        sec=${path##*/}
        mkdir -p %{buildroot}%{_mandir}/${sec}
        for page in ${path}/*.*
        do
            test -e "$page" || continue
            mv -f $page %{buildroot}%{_mandir}/${sec}/
        done
    done
    rm -rf %{buildroot}%{_texmfmaindir}/doc/man
    rm -rf %{buildroot}%{_texmfdistdir}/doc/man
    find %{buildroot}%{_texmfmaindir}/ %{buildroot}%{_texmfdistdir}/ \
        -type f -a -perm /g+w,o+w | xargs --no-run-if-empty chmod g-w,o-w

%changelog
