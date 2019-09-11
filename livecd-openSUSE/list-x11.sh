buildignore PackageKit
buildignore samba-libs
buildignore release-notes-openSUSE
buildignore gnome-themes-accessibility
buildignore xlockmore
buildignore unzip-doc
buildignore gtk2-immodule-inuktitut
buildignore gtk2-immodule-thai
buildignore gtk2-immodule-vietnamese
buildignore gtk2-lang
buildignore gtk3-immodule-inuktitut
buildignore gtk3-immodule-thai
buildignore gtk3-immodule-vietnamese
buildignore gtk3-lang
buildignore evince-lang
buildignore hexchat-lang
buildignore nano-lang
buildignore zenity-lang
buildignore alsa
buildignore alsa-firmware
buildignore alsa-plugins
buildignore xscreensaver
buildignore PackageKit-gstreamer-plugin
buildignore ImageMagick
buildignore awesfx
buildignore sbl
buildignore gnome-online-accounts
buildignore xorg-x11-fonts
buildignore snapper

buildignore Mesa-libva

# No python2 necessary
buildignore python-base

buildignore aspell-en
buildignore ModemManager
buildignore yast2-printer
buildignore avahi
buildignore fprintd
buildignore accountsservice
buildignore MozillaFirefox
buildignore gcc8
buildignore vim-data

install gparted
install midori

# Moved here from list-common.sh. cyrus-sasl is needed by Pidgin in Xfce Live CD
buildignore cyrus-sasl

# Moved here from list-common.sh. Needed by createrepo_c, which is needed for libzypp-plugin-appdata
buildignore deltarpm

# Previously required by rest_cd_x11
install patterns-xfce-xfce_basis
installPattern xfce_basis
install evince
install evince-plugin-pdfdocument
install file-roller
install gparted
install hexchat
install leafpad
install lightdm
install lightdm-gtk-greeter
install photorec
install ristretto
install thunar
install thunar-volman
install xfce4-appfinder
install xfce4-mixer
install xfce4-notifyd
install xfce4-panel
install xfce4-panel-plugin-mixer
install xfce4-power-manager
install xfce4-session
install xfce4-settings
install xfconf
install xfdesktop
install xfwm4

# Previously recommended by rest_cd_x11
install dbus-1-x11
install desktop-file-utils
install libgnomesu
install libxfce4ui-tools
install libyui-qt-pkg
install pinentry-gtk2
install shared-mime-info
install xdg-user-dirs-gtk
install xdg-utils
install NetworkManager-applet
install xfce4-panel-plugin-xkb
install xfce4-terminal
install yast2-control-center-qt
