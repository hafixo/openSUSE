#
# spec file for package yast2-update
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           yast2-update
Version:        4.2.4
Release:        0
Summary:        YaST2 - Update
License:        GPL-2.0-only
Group:          System/YaST
Url:            https://github.com/yast/yast-update

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-ruby-bindings >= 1.0.0
# Y2Packager::ProductUpgrade.remove_obsolete_upgrades
BuildRequires:  yast2 >= 4.2.1
# Packages#proposal_for_update
BuildRequires:  yast2-packager >= 3.2.13
# xmllint
BuildRequires:  libxml2-tools
# control.rng
BuildRequires:  yast2-installation-control
# Needed for tests
BuildRequires:  rubygem(rspec)
# Encryption.save_crypttab_names
BuildRequires:  yast2-storage-ng >= 4.1.31

# Encryption.save_crypttab_names
Requires:       yast2-storage-ng >= 4.1.31
# Y2Packager::ProductUpgrade.remove_obsolete_upgrades
Requires:       yast2 >= 4.2.1
Requires:       yast2-installation
# handle bind mount at /mnt/dev
Requires:       yast2-packager >= 4.0.61
# Pkg.TargetInitializeOptions()
Requires:       yast2-pkg-bindings >= 3.1.14
Requires:       yast2-ruby-bindings >= 1.0.0
# use parallel gzip when crating backup (much faster)
Requires:       pigz

# moved into yast2-update from yast2-installation
# to remove dependency on yast2-storage
Provides:       yast2-installation:/usr/share/YaST2/clients/vendor.ycp

# Pkg::PkgUpdateAll (map conf)
Conflicts:      yast2-pkg-bindings < 2.15.11
# Storage::DeviceMatchFstab (#244117)
Conflicts:      yast2-storage < 2.15.4

%description
Use this component if you wish to update your system.

%package FACTORY
Summary:        YaST2 - Update
Group:          System/YaST

PreReq:         %fillup_prereq

Requires:       yast2
Requires:       yast2-ruby-bindings >= 1.0.0
Requires:       yast2-update

# moved into yast2-update from yast2-installation
# to remove dependency on yast2-storage
Provides:       yast2-update:/usr/share/YaST2/clients/update.ycp

%description FACTORY
Use this component if you wish to update your system.

%prep
%setup -q

%build
%yast_build

%install
%yast_install
%yast_metainfo

%files
%{yast_moduledir}
%{yast_clientdir}/inst_rootpart.rb
%{yast_clientdir}/inst_backup.rb
%{yast_clientdir}/rootpart_proposal.rb
%{yast_clientdir}/update_proposal.rb
%{yast_clientdir}/packages_proposal.rb
%{yast_clientdir}/backup_proposal.rb
%{yast_clientdir}/inst_update_partition.rb
%{yast_clientdir}/inst_update_partition_auto.rb
%{yast_yncludedir}
%{yast_libdir}
%doc %{yast_docdir}

%files FACTORY
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_icondir}
%{yast_controldir}
%{yast_clientdir}/update.rb
%{yast_clientdir}/run_update.rb
%license COPYING

%changelog
