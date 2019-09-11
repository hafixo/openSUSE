buildignore libreoffice-calc
buildignore libreoffice-draw
buildignore libreoffice-impress
buildignore libreoffice-icon-theme-breeze
buildignore libreoffice-icon-theme-sifr
buildignore libreoffice-icon-theme-hicontrast
buildignore colord
buildignore apparmor-utils
install branding-openSUSE

# adobe-sourcecodepro-fonts is the monospace font for openSUSE
install adobe-sourcecodepro-fonts

buildignore google-carlito-fonts
buildignore noto-sans-fonts
buildignore noto-sans-cjk-fonts
buildignore noto-sans-sc-bold-fonts
buildignore noto-sans-sc-regular-fonts
buildignore noto-sans-tc-bold-fonts
buildignore noto-sans-tc-regular-fonts
buildignore noto-sans-jp-bold-fonts
buildignore noto-sans-jp-regular-fonts
buildignore noto-sans-kr-bold-fonts
buildignore noto-sans-kr-regular-fonts

# Expected by openQA
install libreoffice-writer

# Packages for the installer
source "$PWD/list-installer.sh"

# Pulls in sane-backends
buildignore simple-scan

buildignore ghostscript
buildignore orca
buildignore myspell-en_US

# Pulls in color management tools
buildignore gnome-control-center-color

# 17 MiB, really?
buildignore libgweather-lang
buildignore gnome-user-docs
buildignore gnome-user-docs-lang
buildignore evolution-lang
buildignore zenity-lang

# Pulls in clamav
buildignore amavisd-new

# Too big
buildignore inkscape

# Pulls in various python modules and duplicity
buildignore deja-dup

buildignore gimp
buildignore noto-coloremoji-fonts
buildignore gnome-weather

install gparted

# Moved here from list-common.sh. cyrus-sasl is needed by Pidgin in Xfce Live CD
buildignore cyrus-sasl

# From rest_cd_core
install alsa-firmware

# Previously required by rest_cd_gnome
installPattern apparmor
installPattern games
installPattern gnome
installPattern gnome_basis
installPattern gnome_imaging
installPattern gnome_internet
installPattern gnome_multimedia
installPattern gnome_office
installPattern gnome_utilities
installPattern gnome_yast
installPattern imaging
installPattern multimedia
installPattern office
installPattern sw_management_gnome
installPattern yast2_basis
installPattern yast2_install_wf

# Previously recommended by rest_cd_gnome
install gnome-mines
install gnome-sudoku
install quadrapassel
install cifs-utils
