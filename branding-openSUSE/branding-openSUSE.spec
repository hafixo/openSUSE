#
# spec file for package branding-openSUSE
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019 Stasiek Michalski <hellcp@opensuse.org>.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define theme_name openSUSE
%define theme_version tumbleweed
%define theme_version_clean Tumbleweed
%define date 20180403

%ifarch x86_64 %{ix86}
%define gfxboot 1
%endif

%ifarch %{arm} aarch64 %{ix86} x86_64 ppc ppc64
%define grub2 1
%endif

Name:               branding-%{theme_name}
Version:            84.87.%{date}
Release:            0
Summary:            %{theme_name} %{theme_version_clean} Brand File
License:            BSD-3-Clause AND CC-BY-SA-3.0 AND GPL-2.0-or-later
Group:              System/Fhs
URL:                https://github.com/openSUSE/branding
Source0:            branding-%{theme_version}.zip
# PATCH-FIX-UPSTREAM
Patch1:             fix-parallel-build.patch
BuildRequires:      fdupes
BuildRequires:      fribidi
BuildRequires:      suse-module-tools
BuildRequires:      update-desktop-files
BuildRequires:      rsvg-view
BuildRequires:      GraphicsMagick
BuildRequires:      unzip
BuildRequires:      optipng
Conflicts:          branding
Provides:           branding
BuildArch:          noarch
%if 0%{?suse_version} > 1320
BuildRequires:      update-bootloader-rpm-macros
%endif

%description
This package contains the file %{_sysconfdir}/SUSE-brand, and its name is used as
a trigger for installation of correct vendor brand packages.

%package -n wallpaper-branding-%{theme_name}
Summary:            %{theme_name} %{theme_version_clean} default wallpapers
License:            BSD-3-Clause
Group:              System/Fhs
Requires(post):     update-alternatives
Requires(postun):   update-alternatives
Conflicts:          wallpaper-branding
Provides:           wallpaper-branding = %{version}
BuildArch:          noarch

%description -n wallpaper-branding-%{theme_name}
%{theme_name} %{theme_version_clean} defaults wallpapers

%package -n libreoffice-branding-%{theme_name}
Summary:            %{theme_name} %{theme_version_clean} branding for LibreOffice
License:            BSD-3-Clause
Group:              Productivity/Office/Suite
Supplements:        (libreoffice and branding-%{theme_name})
Conflicts:          libreoffice-branding
Provides:           libreoffice-branding = %{version}
BuildArch:          noarch

%description -n libreoffice-branding-%{theme_name}
%{theme_name} %{theme_version_clean} branding for LibreOffice

%package -n yast2-qt-branding-%{theme_name}
Summary:            %{theme_name} %{theme_version_clean} branding for YaST2 Qt
License:            BSD-3-Clause
Group:              System/Fhs
Requires:           adobe-sourcesanspro-fonts
Requires:           google-opensans-fonts
Supplements:        (libyui-qt and branding-%{theme_name})
Conflicts:          yast2-qt-branding
Provides:           yast2-qt-branding = %{version}
BuildArch:          noarch

%description -n yast2-qt-branding-%{theme_name}
%{theme_name} %{theme_version_clean} branding for YaST2 Qt, mainly used for installation

%package -n icewm-theme-yast-installation
Summary:            %{theme_name} %{theme_version_clean} branding for IceWM during the installation
License:            BSD-3-Clause AND CC-BY-SA-3.0 AND GPL-2.0-or-later
Supplements:        ((yast-installation and icewm) and branding-%{theme_name})
Group:              System/Fhs
Conflicts:          icewm-theme-branding
BuildArch:          noarch

%description -n icewm-theme-yast-installation
This IceWM theme is specifically tailored to the %{theme_name} installation
process using YaST2

%package -n xfce4-splash-branding-%{theme_name}
Summary:            %{theme_name} %{theme_version_clean} branding for XFCE splash
License:            CC-BY-SA-3.0
Group:              System/Fhs
Supplements:        (xfce4-session and branding-%{theme_name})
Conflicts:          xfce4-splash-branding
Provides:           xfce4-splash-branding = %{version}
BuildArch:          noarch

%description -n xfce4-splash-branding-%{theme_name}
%{theme_name} %{theme_version_clean} branding for the XFCE splash

%package -n systemd-icon-branding-%{theme_name}
Summary:            %{theme_name} %{theme_version_clean} icons for systemd
License:            CC-BY-SA-3.0
Supplements:        (systemd and branding-%{theme_name})
Provides:           systemd-icon-branding = %{version}
Group:              System/Fhs
Conflicts:          systemd-icon-branding
BuildArch:          noarch

%description -n systemd-icon-branding-%{theme_name}
%{theme_name} %{theme_version_clean} icons for systemd os-release
LOGO variable

%if 0%{?grub2} > 0
%package -n grub2-branding-%{theme_name}
Summary:            %{theme_name} %{theme_version_clean} branding for GRUB2
License:            CC-BY-SA-3.0
Group:              System/Fhs
Requires:           grub2
BuildRequires:      grub2
Supplements:        (grub2 and branding-%{theme_name})
Conflicts:          grub2-branding
Provides:           grub2-branding = %{version}
BuildArch:          noarch
%if 0%{?update_bootloader_requires:1}
%{update_bootloader_requires}
%endif

%description -n grub2-branding-%{theme_name}
%{theme_name} %{theme_version_clean} branding for the GRUB2's graphical console
%endif

%if 0%{?gfxboot} > 0
%package -n gfxboot-branding-%{theme_name}
Summary:            %{theme_name} %{theme_version_clean} branding for gfxboot
License:            BSD-3-Clause
Group:              System/Boot
BuildRequires:      gfxboot-devel
PreReq:             gfxboot >= 4
Requires(post):     gfxboot >= 4
Supplements:        (gfxboot and branding-openSUSE)
Conflicts:          gfxboot-branding
Provides:           gfxboot-branding = %{version}
Provides:           gfxboot-theme = %{version}
BuildArch:          noarch

%description -n gfxboot-branding-%{theme_name}
%{theme_name} %{theme_version_clean} branding for gfxboot (graphical bootloader for grub).
%endif

%package -n plymouth-branding-%{theme_name}
Summary:            %{theme_name} %{theme_version_clean} branding for Plymouth bootsplash
License:            GPL-2.0-or-later
Group:              System/Fhs
BuildRequires:      plymouth-theme-bgrt
Requires:           plymouth-theme-bgrt
PreReq:             plymouth-theme-bgrt
PreReq:             plymouth-scripts
Requires(post):     plymouth-scripts
Requires(postun):   plymouth-scripts
Requires(post):     plymouth-theme-bgrt
Supplements:        (plymouth and branding-%{theme_name})
Conflicts:          plymouth-branding
Provides:           plymouth-branding = %{version}
BuildArch:          noarch

%description -n plymouth-branding-%{theme_name}
%{theme_name} %{theme_version_clean} branding for the plymouth bootsplash

%prep
%autosetup -p1 -n branding-%{theme_version}

%build
%make_build

%if 0%{?gfxboot} > 0
mkdir gfx
cp -a %{_datadir}/gfxboot/themes/openSUSE/ gfx
list=`cd openSUSE/gfxboot && find -type f`
for i in $list; do
  cp openSUSE/gfxboot/$i gfx/openSUSE/$i
done
pushd gfx/openSUSE
%if 0%{?sle_version}
  sed -i -e "s,product=.*,product=%{theme_name} %{theme_version_clean}," config
%else
  sed -i -e "s,product=.*,product=%{theme_name} %{theme_version_clean}," config
%endif
perl -pi -e 's/^(welcome=).*/${1}3/' src/gfxboot.cfg

export PATH=%{_prefix}/sbin:$PATH
make %{?_smp_mflags} BINDIR="/usr/sbin/"
popd
%endif

%install
%make_install

# gfxboot themes will soon get a make install - promised by snwint
# gfxboot should use a link /etc/bootsplash/theme -> /usr/share/bootsplash
# like splashy
if test -f gfx/openSUSE/bootlogo; then
    install -d -m 755 %{buildroot}%{_sysconfdir}/bootsplash/themes/openSUSE/{bootloader,cdrom}
    cp gfx/openSUSE/bootlogo %{buildroot}%{_sysconfdir}/bootsplash/themes/openSUSE/cdrom
    %{_datadir}/gfxboot/bin/unpack_bootlogo %{buildroot}%{_sysconfdir}/bootsplash/themes/openSUSE/cdrom
    install -m 644 gfx/openSUSE/{message,po/*.tr,help-boot/*.hlp} %{buildroot}%{_sysconfdir}/bootsplash/themes/openSUSE/bootloader
    %{_datadir}/gfxboot/bin/2hl --link --quiet %{buildroot}%{_sysconfdir}/bootsplash/themes/openSUSE/*
    touch %{buildroot}/boot/message
fi

for i in %{buildroot}%{_datadir}/wallpapers/*.desktop; do
    %suse_update_desktop_file "$i"
done

%fdupes -s %{buildroot}%{_datadir}/wallpapers/
%fdupes -s %{buildroot}%{_datadir}/YaST2/theme/current/wizard/

%suse_update_desktop_file %{buildroot}%{_datadir}/wallpapers/openSUSEdefault/metadata.desktop

%if 0%{?grub2} < 1
rm -rf %{buildroot}%{_datadir}/grub2
%endif

%post -n wallpaper-branding-%{theme_name}
update-alternatives --install %{_datadir}/wallpapers/openSUSE-default.xml openSUSE-default.xml %{_datadir}/wallpapers/openSUSE-default-static.xml 5

%postun -n wallpaper-branding-%{theme_name}
# Note: we don't use "$1 -eq 0", to avoid issues if the package gets renamed
if [ ! -f %{_datadir}/wallpapers/openSUSE-default-static.xml ]; then
  update-alternatives --remove openSUSE-default.xml %{_datadir}/wallpapers/openSUSE-default-static.xml
fi

%if 0%{?grub2} > 0
%post -n grub2-branding-%{theme_name}
%{_datadir}/grub2/themes/%{theme_name}/activate-theme
%if 0%{?update_bootloader_check_type_refresh_post:1}
%{update_bootloader_check_type_refresh_post grub2 grub2-efi}
%else
if test -e /boot/grub2/grub.cfg ; then
  %{_sbindir}/grub2-mkconfig -o /boot/grub2/grub.cfg || true
fi
%endif

%posttrans -n grub2-branding-%{theme_name}
%{?update_bootloader_posttrans}

%postun -n grub2-branding-%{theme_name}
if [ $1 = 0 ] ; then
  rm -rf /boot/grub2/themes/%{theme_name}
fi
%endif

%if 0%{?gfxboot} > 0
%post -n gfxboot-branding-%{theme_name}
gfxboot --update-theme %{theme_name}
%endif

%post -n plymouth-branding-%{theme_name}
OTHEME="$(%{_sbindir}/plymouth-set-default-theme)"
if [ "$OTHEME" == "text" -o "$OTHEME" == "bgrt" ]; then
   if [ ! -e /.buildenv ]; then
     %{_sbindir}/plymouth-set-default-theme bgrt
     %{?regenerate_initrd_post}
   else
     %{_sbindir}/plymouth-set-default-theme bgrt
   fi
fi

%postun -n plymouth-branding-%{theme_name}
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "bgrt" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
        %{?regenerate_initrd_post}
    fi
fi

%posttrans -n plymouth-branding-%{theme_name}
%{?regenerate_initrd_posttrans}

%files
%license LICENSE
%config %{_sysconfdir}/SUSE-brand

%files -n wallpaper-branding-%{theme_name}
%license LICENSE
%ghost %{_sysconfdir}/alternatives/openSUSE-default.xml
%{_datadir}/wallpapers/openSUSE-default.xml
%dir %{_datadir}/gnome-background-properties/
%{_datadir}/gnome-background-properties/wallpaper-branding-openSUSE.xml
%{_datadir}/wallpapers/
# File from dynamic-wallpaper-branding-openSUSE:
%exclude %{_datadir}/wallpapers/openSUSE-default-dynamic.xml

%files -n yast2-qt-branding-%{theme_name}
%dir %{_datadir}/YaST2
%dir %{_datadir}/YaST2/theme
%dir %{_datadir}/YaST2/theme/current
%{_datadir}/YaST2/theme/current/wizard

%files -n icewm-theme-yast-installation
%dir %{_sysconfdir}/icewm/
%config %{_sysconfdir}/icewm/theme
%dir %{_datadir}/icewm/
%dir %{_datadir}/icewm/themes/
%{_datadir}/icewm/themes/yast-installation/

%files -n libreoffice-branding-%{theme_name}
%dir %{_datadir}/libreoffice
%{_datadir}/libreoffice/program

%files -n xfce4-splash-branding-%{theme_name}
%license LICENSE
%{_datadir}/pixmaps/xfce4-splash-openSUSE.png

%files -n systemd-icon-branding-%{theme_name}
%{_datadir}/icons/hicolor

%if 0%{?grub2} > 0
%files -n grub2-branding-%{theme_name}
%{_datadir}/grub2
%dir /boot/grub2
%dir /boot/grub2/themes
%ghost /boot/grub2/themes/%{theme_name}
%endif

%if 0%{?gfxboot} > 0
%files -n gfxboot-branding-%{theme_name}
%{_sysconfdir}/bootsplash
%config %{_sysconfdir}/bootsplash/themes/openSUSE/bootloader/*
# Intentionally skipping over .tr files as they are hard links
%config %{_sysconfdir}/bootsplash/themes/openSUSE/cdrom/*.{hlp,jpg,mod,dat,txt,tlk,cfg,fnt}
%config %{_sysconfdir}/bootsplash/themes/openSUSE/cdrom/bootlogo
%{_sysconfdir}/bootsplash/themes/openSUSE/cdrom/*
%ghost /boot/message
%endif

%files -n plymouth-branding-%{theme_name}
%{_datadir}/plymouth/themes/spinner/watermark.png

%changelog
