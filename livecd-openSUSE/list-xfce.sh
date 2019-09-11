install branding-openSUSE
buildignore samba-libs
install yast2-trans-stats
install patterns-xfce-xfce
installPattern xfce
install openSUSE-release-livecd-xfce
buildignore gnome-themes-accessibility
buildignore xlockmore
buildignore unzip-doc
buildignore gtk2-immodule-inuktitut
buildignore gtk2-immodule-thai
buildignore gtk2-immodule-vietnamese
buildignore gtk3-immodule-inuktitut
buildignore gtk3-immodule-thai
buildignore gtk3-immodule-vietnamese
buildignore awesfx
buildignore sbl
buildignore gnome-online-accounts

# Packages for the installer
source "$PWD/list-installer.sh"

buildignore aspell-en
install libxslt-tools

# Remove useless xfce panel plugins
buildignore xfce4-panel-plugin-xkb
buildignore xfce4-panel-plugin-notes

# Remove Libreoffice as it's too big
buildignore libreoffice

# Pulls in sane-backends
buildignore simple-scan

# Add useful extras
install gparted
install evince

# Ignore xreader for now
buildignore xreader

# From rest_cd_core
install alsa-firmware
