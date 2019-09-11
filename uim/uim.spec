#
# spec file for package uim
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


Name:           uim
Version:        1.8.8
Release:        0
Summary:        A multilingual input method framework
License:        BSD-3-Clause AND LGPL-2.1-or-later AND (BSD-3-Clause OR LGPL-2.0-only)
Group:          System/I18n/Japanese
Url:            https://github.com/uim/uim
Source0:        https://github.com/uim/uim/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        suse-start-uim.el
Source2:        xemacs-auto-autoloads.el
Source3:        etc-x11-xim.d-uim
Source4:        baselibs.conf
Patch2:         uim-fix-crash-in-firefox.diff
BuildRequires:  canna-devel
BuildRequires:  emacs-x11
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtbase-private-headers-devel
BuildRequires:  m17n-lib-devel
BuildRequires:  ncurses-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xemacs
%if 0%{?suse_version} <= 1500
BuildRequires:  libqt4-devel
%endif
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(anthy)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libedit)
Recommends:     %{name}-gtk3 = %{version}
Recommends:     %{name}-qt5 = %{version}
Requires(pre):  %{_bindir}/touch

%description
Uim is a multilingual input method framework.

%package devel
Summary:        Development files for the UIM input method framework
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Include Files and Libraries mandatory for Development with uim.

%package gtk2
Summary:        GTK2 IM Module for UIM
Group:          System/I18n/Japanese
Requires:       %{name} = %{version}
%gtk2_immodule_requires

%description gtk2
Contains GTK+2.0 IM module for uim

%package gtk3
Summary:        GTK3 IM Module for UIM
Group:          System/I18n/Japanese
Requires:       %{name} = %{version}
%gtk3_immodule_requires

%description gtk3
Contains GTK+3.0 IM module for uim

%if 0%{?suse_version} <= 1500
%package qt4
Summary:        Qt4 input module plugin for uim
Group:          System/I18n/Japanese
Requires:       %{name} = %{version}

%description qt4
Contains Qt4 input module plugin for uim
%endif

%package qt5
Summary:        Qt5 input module plugin for uim
Group:          System/I18n/Japanese
Requires:       %{name} = %{version}

%description qt5
Contains Qt5 input module plugin for uim

%prep
%setup -q
%patch2 -p1
cp emacs/README README.emacs
iconv -f euc-jp -t utf-8 < emacs/README.ja > README.ja.emacs

%build
%configure --disable-static \
        --libexecdir=%{_prefix}/lib/uim \
        --with-canna\
        --with-anthy-utf8 \
%if 0%{?suse_version} <= 1500
        --with-qt4 \
        --with-qt4-immodule \
%endif
        --with-qt5 \
        --with-qt5-immodule \
        --enable-kde-applet

make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}%{_includedir}/gcroots.h
rm -f %{buildroot}%{_libdir}/pkgconfig/gcroots.pc
# this file is generated by "uim-module-manager".
# touch it here to make sure that it is in the file list of the
# package, then it will be deleted when the package is uninstalled:
touch %{buildroot}%{_datadir}/uim/modules
mkdir -p %{buildroot}%{_sysconfdir}/X11/xim.d/ja
install -m 644 $RPM_SOURCE_DIR/etc-x11-xim.d-uim \
               %{buildroot}%{_sysconfdir}/X11/xim.d/uim
pushd  %{buildroot}%{_sysconfdir}/X11/xim.d/ja
    ln -s ../uim 60-uim
popd
# GNU Emacs:
install -m 644 $RPM_SOURCE_DIR/suse-start-uim.el %{buildroot}%{_datadir}/emacs/site-lisp/
pushd %{buildroot}%{_datadir}/emacs/site-lisp/uim-el
    for i in $(find . -name "*.el")
    do
        emacs -no-site-file -q -batch -eval '(setq load-path (cons "." load-path))' -f batch-byte-compile $i
    done
popd
# XEmacs
mkdir -p %{buildroot}%{_datadir}/xemacs/site-packages/lisp/uim-el
install -m 644 emacs/*.el %{buildroot}%{_datadir}/xemacs/site-packages/lisp/uim-el
pushd %{buildroot}%{_datadir}/xemacs/site-packages/lisp/uim-el
    for i in $(find . -name "*.el")
    do
        xemacs -no-site-file -q -batch -eval '(setq load-path (cons "." load-path))' -f batch-byte-compile $i
    done
popd
install -m 644 $RPM_SOURCE_DIR/xemacs-auto-autoloads.el \
    %{buildroot}%{_datadir}/xemacs/site-packages/lisp/uim-el/auto-autoloads.el
# replace buildroot in comments in .elc files by spaces with the same total length:
BUILD_ROOT_REPLACEMENT=$(echo %{buildroot} | tr [:print:] ' ')
for i in $(find %{buildroot} -name "*.elc")
do
    perl -pi -e "s|(;;; from file )%{buildroot}(%{_datadir}/xemacs/site-packages/.*)|\1BUILD_ROOT_REPLACEMENT\2|" $i
    perl -pi -e "s|(;;; from file )%{buildroot}(%{_datadir}/emacs/site-lisp/.*)|\1BUILD_ROOT_REPLACEMENT\2|" $i
done
%find_lang uim
touch uim-chardict-qt.lang
%suse_update_desktop_file uim System SystemSetup
find %{buildroot} -name "*.scm" \
    | grep -E -v "installed-modules.scm|loader.scm" \
    | sort | uniq | perl -p -e "s|%{buildroot}||" >> uim.lang
%fdupes %{buildroot}%{_prefix}/share
find %{buildroot} -type f -name "*.la" -delete -print
rm -f doc/Makefile*

%post
/sbin/ldconfig
# register uim modules to uim. This will change the files:
#     %%{_datadir}/uim/installed-modules.scm
#     %%{_datadir}/uim/loader.scm
uim-module-manager --register \
    ajax-ime anthy anthy-utf8 byeoru canna elatin  hangul  ipa-x-sampa \
    latin m17nlib pyload skk tcode trycode tutcode viqr

%postun -p /sbin/ldconfig

%post gtk2
%gtk2_immodule_post

%postun gtk2
%gtk2_immodule_postun

%post gtk3
%gtk3_immodule_post

%postun gtk3
%gtk3_immodule_postun

%files -f uim.lang
%license COPYING
%doc AUTHORS NEWS* README*
%doc doc
%dir %{_sysconfdir}/X11/xim.d/
%{_sysconfdir}/X11/xim.d/*
%{_datadir}/uim
# autogenerated by uim-module-manager:
%ghost %{_datadir}/uim/installed-modules.scm
%ghost %{_datadir}/uim/loader.scm
%ghost %{_datadir}/uim/modules
%{_bindir}/uim-sh
%{_bindir}/uim-module-manager
%{_bindir}/uim-xim
%{_bindir}/uim-fep
%{_bindir}/uim-fep-tick
%{_bindir}/uim-el-agent
%{_bindir}/uim-el-helper-agent
%{_bindir}/uim-help
%{_bindir}/uim-m17nlib-relink-icons
%{_libdir}/*.so.*
%dir %{_libdir}/uim
%if "%{_libdir}" != "%{_prefix}/lib"
%dir %{_prefix}/lib/uim
%endif
%{_prefix}/lib/uim/uim-helper-server
%dir %{_libdir}/uim/plugin/
%{_libdir}/uim/plugin/*.so
%doc %{_mandir}/man1/*.1.gz
%{_datadir}/applications/%{name}.desktop
%{_datadir}/emacs/site-lisp/*
%{_datadir}/xemacs/site-packages

%files devel
%{_libdir}/*.so
%{_includedir}/uim/
%{_libdir}/pkgconfig/uim.pc

%files gtk2
%{_bindir}/uim-*-gtk
%{_bindir}/uim-*-gtk-*
%{_bindir}/uim-input-pad-ja
%{_prefix}/lib/uim/uim-*-gtk
%{_libdir}/gtk-2*/*/immodules/*.so

%files gtk3
%{_bindir}/uim-*-gtk3
%{_bindir}/uim-*-gtk3-*
%{_prefix}/lib/uim/uim-*-gtk3
%{_libdir}/gtk-3*/*/immodules/*.so

%if 0%{?suse_version} <= 1500
%files qt4 -f uim-chardict-qt.lang
%{_bindir}/uim-*-qt4
%{_prefix}/lib/uim/uim-*-qt4
%{_libdir}/qt4/plugins/inputmethods/*.so
%endif

%files qt5 -f uim-chardict-qt.lang
%{_bindir}/uim-*-qt5
%{_prefix}/lib/uim/uim-*-qt5
%{_libdir}/qt5/plugins/platforminputcontexts/*.so

%changelog
