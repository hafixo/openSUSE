#
# spec file for package mariadb
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


# libmysqld soname
%define soname 19
# Set this to 1 to run regression test suite (it takes a long time)
%define run_testsuite 1
# Set this to 1 for testing purposes (run all regression tests but ignore
# failures). Set this to 0 for production usage (skip tests in the
# unstable-tests list (contains also suse_skipped_tests.list) and don't
# ignore failures
%define ignore_testsuite_result 0
# OQGRAPH engine cannot be built for SLE (missing Judy dependency)
%if 0%{?is_opensuse} > 0
%define with_oqgraph 1
%else
%define with_oqgraph 0
%endif
# TokuDB engine is available only for x86_64 architecture
# see https://mariadb.com/kb/en/mariadb/tokudb/
# Temporarily stop to build it as jemalloc 5 is not backwards compatible
# and a build without jemalloc is not supported upstream (MDEV-15034)
# Also we can't use PerconaFT (AGPL licence) that is needed for tokudb
%define with_tokudb 0
# Mroonga currently only supports the x86_64 architecture
# see https://mariadb.com/kb/en/mariadb/about-mroonga/
%ifarch x86_64
%define with_mroonga 1
%else
%define with_mroonga 0
%endif
Name:           mariadb
Version:        10.2.24
Release:        0
Summary:        Server part of MariaDB
License:        SUSE-GPL-2.0-with-FLOSS-exception
Group:          Productivity/Databases/Servers
Url:            https://www.mariadb.org
Source:         https://downloads.mariadb.org/f/mariadb-%{version}/source/mariadb-%{version}.tar.gz
Source1:        %{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Source4:        README.debug
Source5:        suse-test-run
Source6:        mysql.SuSEfirewall2
Source7:        README.install
Source14:       my.ini
Source15:       mariadb.service
Source16:       mariadb.target
Source17:       mysql-systemd-helper
Source18:       mariadb@.service
Source50:       suse_skipped_tests.list
Patch0:         mysql-community-server-5.1.45-multi-configuration.patch
Patch1:         mariadb-10.2.4-logrotate.patch
Patch2:         mariadb-5.5.28-install_db-quiet.patch
Patch3:         mariadb-10.1.1-mysqld_multi-features.patch
Patch4:         mariadb-5.2.3-cnf.patch
Patch6:         mariadb-10.1.12-deharcode-libdir.patch
Patch7:         mariadb-10.0.15-logrotate-su.patch
Patch8:         mariadb-10.2.4-fortify-and-O.patch
Patch9:         mariadb-10.2.19-link-and-enable-c++11-atomics.patch
Patch11:        mariadb-10.2.9-galera_cnf.patch
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  krb5-devel
BuildRequires:  libaio-devel
BuildRequires:  libarchive-devel
BuildRequires:  libbz2-devel
BuildRequires:  libevent-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
# MariaDB requires a specific version of pcre. Provide MariaDB with
# "BuildRequires: pcre-devel" and it automatically decides if the version is
# ok or not. If not, it uses bundled pcre.
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig
BuildRequires:  procps
BuildRequires:  pwdutils
BuildRequires:  sqlite
BuildRequires:  tcpd-devel
# Tests requires time and ps and some perl modules
# Keep in sync with Requires of mysql-testsuite
BuildRequires:  time
BuildRequires:  unixODBC-devel
BuildRequires:  zlib-devel
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Env)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
# Do not ever switch away from BuildRequires: pkgconfig(libsystemd); BuildRequires systemd/systemd-devel causes build cycles
BuildRequires:  pkgconfig(libsystemd)
# Required by rcmysql
Requires:       %{name}-client
Requires:       %{name}-errormessages = %{version}
# Requires /bin/hostname because otherwise we have a conflict on Leap (bsc#1009905).
# It can be switched back to plain "hostname" when this bug is resolved
Requires:       /bin/hostname
Requires:       perl-base
Requires(pre):  pwdutils
Recommends:     logrotate
Conflicts:      otherproviders(mariadb-server)
Conflicts:      otherproviders(mysql)
Conflicts:      otherproviders(mysql-debug)
Conflicts:      otherproviders(mysql-server)
# Compatibility with Fedora/CentOS
Provides:       mariadb-server = %{version}
Provides:       mysql-server = %{version}
# Compatibility with old version
Provides:       %{name}-debug-version = %{version}
Obsoletes:      %{name}-debug-version < %{version}
Provides:       %{name}-debug = %{version}
Obsoletes:      %{name}-debug < %{version}
Provides:       mysql = %{version}
Obsoletes:      mysql < %{version}
Provides:       mysql-debug = %{version}
Obsoletes:      mysql-debug < %{version}
%if 0%{?suse_version} < 1500
# Explicit requires of systemd is not needed anymore and
# creates a problem for containers
%{?systemd_requires}
%endif
# Do not BuildRequires lzo for i586 and arm
# https://lists.launchpad.net/maria-discuss/msg04639.html
%ifnarch i586 %{arm}
BuildRequires:  lzo-devel
%endif
BuildRequires:  libedit-devel
%if 0%{with_oqgraph} > 0
BuildRequires:  judy-devel
%if 0%{?suse_version} > 1315
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
%endif
%if 0%{with_tokudb} > 0
BuildRequires:  jemalloc-devel
%endif

%description
MariaDB is an open-source, multi-threaded, relational database management
system. It's a backward compatible, drop-in replacement branch of the
MySQL Community Server.

This package only contains the server-side programs.

%package -n libmysqld%{soname}
Summary:        MariaDB embedded server library
Group:          System/Libraries
Requires:       %{name}-errormessages >= %{version}

%description -n libmysqld%{soname}
This package contains MariaDB library that allows to run an embedded
MariaDB server inside a client application.

%package -n libmysqld-devel
Summary:        MariaDB embedded server development files
Group:          Development/Libraries/C and C++
Requires:       libaio-devel
# The headers files are the shared
Requires:       libmariadb-devel >= 3.0
Requires:       libmysqld%{soname} = %{version}
Requires:       tcpd-devel

%description -n libmysqld-devel
This package contains the development header files and libraries
for developing applications that embed the MariaDB.

%package client
Summary:        Client for MariaDB
Group:          Productivity/Databases/Clients
Requires:       %{name}-errormessages = %{version}
# Explicit requires to pull in charsets for errormessages
Requires:       libmariadb3 >= 3.0
Requires(pre):  pwdutils
Conflicts:      otherproviders(mysql-client)
Provides:       mysql-client = %{version}
Obsoletes:      mysql-client < %{version}

%description client
This package contains the standard clients for MariaDB.

%package galera
Summary:        The configuration files and scripts for galera replication
Group:          Productivity/Databases/Tools
Requires:       %{name} = %{version}
# galera-3 is not in openSUSE:Factory now
#Requires:       galera-3 >= 25.3.18
Requires:       iproute2
Requires:       lsof
Requires:       rsync
Requires:       socat
Requires:       which
# We need Conflicts here as galera_new_cluster (and use_galera_new_cluster.conf)
# and galera_recovery scripts were in mariadb package but now they are in galera
# subpackage
Conflicts:      mariadb <= 10.1.25
# wsrep_* scripts were in mariadb-tools subpackage but now they are in galera subpackage
Conflicts:      mariadb-tools <= 10.1.25

%description galera
This package contains configuration files and scripts that are
needed for running MariaDB Galera Cluster.

%package errormessages
Summary:        The error messages files required by server, client and libmysqld
Group:          System/Localization
BuildArch:      noarch

%description errormessages
This package provides translated error messages for the standalone
server daemon, embedded server and client.

%package bench
Summary:        Benchmarks for MariaDB
Group:          Productivity/Databases/Tools
Requires:       %{name}-client
Requires:       perl-DBD-mysql
Conflicts:      otherproviders(mysql-bench)
Provides:       mysql-bench = %{version}
Obsoletes:      mysql-bench < %{version}

%description bench
This package contains benchmark scripts and data for MariaDB.

To run these database benchmarks, start the script "run-all-tests" in
the directory %{_datadir}/sql-bench after starting MariaDB.

%package test
Summary:        Testsuite for MariaDB
Group:          Productivity/Databases/Servers
Requires:       %{name} = %{version}
Requires:       %{name}-bench = %{version}
Requires:       %{name}-client = %{version}
Requires:       %{name}-tools = %{version}
# Requires libmariadb_plugins in order to test client plugins successfuly
Requires:       libmariadb_plugins >= 3.0
Requires:       perl-DBD-mysql
Requires:       procps
Requires:       time
# Tests requires time and ps and some perl modules
Requires:       perl(Data::Dumper)
Requires:       perl(Env)
Requires:       perl(Exporter)
Requires:       perl(Fcntl)
Requires:       perl(File::Temp)
Requires:       perl(Getopt::Long)
Requires:       perl(IPC::Open3)
Requires:       perl(Socket)
Requires:       perl(Sys::Hostname)
Requires:       perl(Test::More)
Requires:       perl(Time::HiRes)
Conflicts:      otherproviders(mysql-test)
Provides:       mysql-test = %{version}
Obsoletes:      mysql-test < %{version}

%description test
This package contains the test scripts and data for MariaDB.

To run the testsuite, run %{_datadir}/mysql-test/suse-test-run.

%package tools
Summary:        MariaDB tools
Group:          Productivity/Databases/Servers
Requires:       perl-DBD-mysql
Conflicts:      otherproviders(mysql-tools)
# make sure this package is installed when updating from 10.2 and older
Provides:       mysql-client:%{_bindir}/perror
Provides:       mysql-tools = %{version}
Provides:       mysql:%{_bindir}/mysqlhotcopy
Obsoletes:      mysql-tools < %{version}

%description tools
A set of scripts for administering a MariaDB or developing
applications with MariaDB.

%prep
%setup -q
# Remove JAR files from the tarball (used for testing from the source)
find . -name "*.jar" -type f -exec rm --verbose -f {} \;
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch6 -p0
%patch7 -p0
%patch8 -p0
%patch9 -p1
%patch11 -p1

cp %{_sourcedir}/suse-test-run .

# Remove unneeded manpages ('make install' basically installs everything under
# man/*)
rm -f man/mysqlman.1        # dummy fallback manpage
[ \! -f man/CMakeLists.txt ] || sed -i 's|mysqlman.1||'     man/CMakeLists.txt
rm -f man/mysql.server.1    # init script, not installed in our rpm
[ \! -f man/CMakeLists.txt ] || sed -i 's|mysql.server.1||' man/CMakeLists.txt
rm -f man/make_win_*.1      # windows build scripts
rm -f man/comp_err.1        # built-time utility

# Breaks VPATH builds when in sourcedir, is generated in the builddirs
rm -f sql/sql_builtin.cc

sed -i 's|@localstatedir@|%{_localstatedir}/log|' support-files/mysql-log-rotate.sh

# Broken test that needs sources
rm -f mysql-test/t/file_contents.test mysql-test/r/file_contents.result

# Specify perl path on shebangs
for i in `grep -Rl '^#!@PERL@$' .`; do
	sed -i 's|@PERL@|%{_bindir}/perl|' $i
done

# Add our list of tests that fail (correctly or temporarily) to the list of such
# tests created by upstream
cat %{SOURCE50} | tee -a mysql-test/unstable-tests

# Remove python scripts remains from tokudb upstream (those files are not used anyway)
rm -r storage/tokudb/mysql-test/tokudb/t/*.py

# Remove PerconaFT from the package because it has AGPL licence [bsc#1118754]
rm -rf storage/tokudb/PerconaFT

%build
EXTRA_FLAGS="-Wno-unused-but-set-variable -fno-strict-aliasing -Wno-unused-parameter"
# Mariadb devs seems to fall in love with -Werror option
EXTRA_FLAGS="${EXTRA_FLAGS} -Wno-error"
export CFLAGS="%{optflags} -DOPENSSL_LOAD_CONF -DPIC -fPIC -DFORCE_INIT_OF_VARS $EXTRA_FLAGS"
export CXXFLAGS="$CFLAGS -felide-constructors"
%cmake -DWITH_SSL=system                                            \
       -DWITH_LIBWRAP=ON                                            \
       -DENABLED_PROFILING=ON                                       \
       -DENABLE_DEBUG_SYNC=OFF                                      \
       -DWITH_PIC=ON                                                \
       -DWITH_ZLIB=system                                           \
       -DWITH_LIBEVENT=system                                       \
       -DWITH_JEMALLOC=no                                           \
       -DWITH_READLINE=0                                            \
       -DWITH_LIBEDIT=0                                             \
       -DWITH_EDITLINE=system                                       \
       -DINSTALL_LAYOUT=RPM                                         \
       -DWITH_LZ4=system                                            \
       -DMYSQL_UNIX_ADDR="%{_rundir}/mysql/mysql.sock"              \
       -DINSTALL_UNIX_ADDRDIR="%{_rundir}/mysql/mysql.sock"         \
       -DINSTALL_MYSQLSHAREDIR=share/%{name}                        \
       -DWITH_COMMENT="openSUSE mariadb rpm"                        \
       -DWITH_EXTRA_CHARSET=all                                     \
       -DDEFAULT_CHARSET=utf8mb4                                    \
       -DDEFAULT_COLLATION=utf8mb4_general_ci                       \
       -DWITH_INNOBASE_STORAGE_ENGINE=1                             \
       -DWITH_PERFSCHEMA_STORAGE_ENGINE=1                           \
%if 0%{with_oqgraph} < 1
       -DPLUGIN_OQGRAPH=NO                                          \
%endif
%if 0%{with_tokudb} < 1
       -DPLUGIN_TOKUDB=NO                                           \
%endif
%if 0%{with_mroonga} < 1
       -DPLUGIN_MROONGA=NO                                          \
%endif
       -DWITH_XTRADB_STORAGE_ENGINE=1                               \
       -DWITH_CSV_STORAGE_ENGINE=1                                  \
       -DWITH_HANDLERSOCKET_STORAGE_ENGINE=1                        \
       -DWITH_INNODB_MEMCACHED=ON                                   \
       -DWITH_EMBEDDED_SERVER=true                                  \
       -DWITH_WSREP=ON                                              \
       -DWITH_INNODB_DISALLOW_WRITES=1                              \
       -DWITH_LIBARCHIVE=ON                                         \
       -DWITH_MARIABACKUP=ON                                        \
       -DCOMPILATION_COMMENT="openSUSE package"                     \
       -DDENABLE_DOWNLOADS=false                                    \
       -DINSTALL_PLUGINDIR_RPM="%{_lib}/mysql/plugin"               \
       -DINSTALL_LIBDIR_RPM="%{_lib}"                               \
       -DINSTALL_SYSCONF2DIR="%{_sysconfdir}/my.cnf.d"              \
       -DCMAKE_C_FLAGS_RELWITHDEBINFO="$CFLAGS"                     \
       -DCMAKE_CXX_FLAGS_RELWITHDEBINFO="$CXXFLAGS"                 \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo                            \
       -DINSTALL_SQLBENCHDIR=share                                  \
       -DCMAKE_C_FLAGS="$CFLAGS"                                    \
       -DCMAKE_CXX_FLAGS="$CXXFLAGS"                                \
       -DCMAKE_EXE_LINKER_FLAGS="-Wl,--as-needed -pie -Wl,-z,relro,-z,now" \
       -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -pie -Wl,-z,relro,-z,now" \
       -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -pie -Wl,-z,relro,-z,now" \
       -DCMAKE_SKIP_RPATH=OFF                                       \
       -DCMAKE_SKIP_INSTALL_RPATH=ON                                \
       -Wno-dev "$@" ..
make %{?_smp_mflags}
nm --numeric-sort sql/mysqld > sql/mysqld.sym

%install
# Helper function to generate filelist for binaries and their manpages
filelist()
{
	echo '%%defattr(-, root, root)'
	pushd %{buildroot} >/dev/null
	for i; do
		if test -e usr/sbin/"$i"; then
			echo %{_sbindir}/"$i"
		fi
		if test -e usr/bin/"$i"; then
			echo %{_bindir}/"$i"
		fi
		if test -d usr/share/*/"$i"; then
			echo "/`echo usr/share/*/"$i"`"
		fi
		if test -n "`ls -1 %{buildroot}$i 2> /dev/null`"; then
			echo "$i"
		fi
		if ls usr/share/man/*/"$i".[1-9]* >/dev/null 2>&1; then
			echo "%{_mandir}/*/$i.[1-9]*"
		fi
	done
	popd >/dev/null
}

# Install the package itself
%cmake_install benchdir_root=%{_datadir}/

# Logrotate file should be named as the package
if [ ! -e %{buildroot}%{_sysconfdir}/logrotate.d/mysql ]; then
    # some versions do not install it automatically
    install -D -m 644 build/support-files/mysql-log-rotate %{buildroot}%{_sysconfdir}/logrotate.d/mysql
fi
mv %{buildroot}%{_sysconfdir}/logrotate.d/mysql %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Create log directory with the expected perms of mysql
install -d -m 700 %{buildroot}%{_localstatedir}/log/mysql/

# Symbols from build to go into libdir
install -m 644 build/sql/mysqld.sym %{buildroot}%{_libdir}/mysql/mysqld.sym

# INFO_SRC binary
install -p -m 644 build/Docs/INFO_SRC %{buildroot}%{_libdir}/mysql/

# Remove most static libs (FIXME: don't build them at all...)
[ \! -f "%{buildroot}%{_libdir}/"libmysqld.a ] || mv "%{buildroot}%{_libdir}/"libmysqld.a "%{buildroot}%{_libdir}/"libmysqld.static
rm -f %{buildroot}%{_libdir}/*.a
[ \! -f "%{buildroot}%{_libdir}/"libmysqld.static ] || mv "%{buildroot}%{_libdir}/"libmysqld.static "%{buildroot}%{_libdir}/"libmysqld.a

# Remove unused stuff
rm -f %{buildroot}%{_datadir}/mysql/{errmsg-utf8.txt,mysql-log-rotate}
rm -f %{buildroot}%{_libdir}/mysql/plugin/daemon_example.ini
# binary-configure creates the MySQL system tables and starts the server (not used)
rm -f %{buildroot}%{_datadir}/mysql/binary-configure
# FS files first-bytes recoginiton (not updated by upstream since nobody realy use that)
rm -f %{buildroot}%{_datadir}/mysql/magic
# Upstream ships them because of MDEV-10797 (we don't need them as we use our own systemd scripts)
rm -f %{buildroot}%{_datadir}/mysql/mysql.server
rm -f %{buildroot}%{_datadir}/mysql/mysqld_multi.server
# The old fork of mytop utility (we ship it as a separate package)
rm -f %{buildroot}%{_bindir}/mytop

# Remove unused upstream services
rm -f %{buildroot}'%{_unitdir}/mariadb.service'
rm -f %{buildroot}'%{_unitdir}/mariadb@.service'
rm -f %{buildroot}'%{_unitdir}/mariadb@bootstrap.service.d/use_galera_new_cluster.conf'

# Remove systemd-sysusers conf file for creating of mysql user (we do it in the specfile)
rm -f %{buildroot}%{_sysusersdir}/sysusers.conf

# Remove client libraries that are now provided in mariadb-connector-c
# Client library and links
rm %{buildroot}%{_libdir}/libmariadb*.so.*
unlink %{buildroot}%{_libdir}/libmysqlclient.so
unlink %{buildroot}%{_libdir}/libmysqlclient_r.so
unlink %{buildroot}%{_libdir}/libmariadb.so
# Client plugins
rm %{buildroot}%{_libdir}/mysql/plugin/{auth_gssapi_client.so,dialog.so,mysql_clear_password.so,sha256_password.so}
# Devel files
rm %{buildroot}%{_bindir}/mysql_config
rm %{buildroot}%{_bindir}/mariadb_config
rm %{buildroot}%{_datadir}/pkgconfig/mariadb.pc
rm -f %{buildroot}%{_prefix}/lib/pkgconfig/libmariadb.pc
rm -f %{buildroot}%{_prefix}/lib64/pkgconfig/libmariadb.pc
rm %{buildroot}%{_datadir}/aclocal/mysql.m4
rm %{buildroot}%{_mandir}/man1/mysql_config*.1*
rm -r %{buildroot}%{_includedir}/mysql

# mysql-test includes my_safe_process executable that should be moved to /usr/bin
mv %{buildroot}%{_datadir}/mysql-test/lib/My/SafeProcess/my_safe_process %{buildroot}%{_bindir}
ln -s ../../../../../bin/my_safe_process %{buildroot}%{_datadir}/mysql-test/lib/My/SafeProcess/my_safe_process

# Rename the wsrep README so it corresponds with the other README names
cp Docs/README-wsrep Docs/README.wsrep

# Generate various filelists (binaries and manpages)
# mariadb.files
filelist mariabackup mbstream innochecksum mariadb-service-convert my_print_defaults myisam_ftdump myisamchk myisamlog myisampack mysql_fix_extensions  mysql_install_db mysql_secure_installation mysql_upgrade mysqld mysqld_multi mysqld_safe mysqlbinlog mysqldumpslow resolve_stack_dump resolveip {m,}aria_chk {m,}aria_dump_log {m,}aria_ftdump {m,}aria_pack {m,}aria_read_log tokuft_logprint tokuft_logdump tokuftdump mysql_ldb sst_dump myrocks_hotbackup >mariadb.files

# mariadb-client.files
filelist mysql mysqladmin mysqlcheck mysqldump mysqlimport mysqlshow mysql_config_editor mysqld_safe_helper >mariadb-client.files

# Mysql has configuration file in _bindir
if [ -f scripts/mysqlaccess.conf ] ; then
    install -m 640 scripts/mysqlaccess.conf %{buildroot}%{_sysconfdir}/mysqlaccess.conf
    rm -f %{buildroot}%{_bindir}/mysqlaccess.conf
    echo '%config(noreplace) %attr(0640, root, mysql) %{_sysconfdir}/mysqlaccess.conf' >> mariadb-client.files
fi

# mariadb-galera.files
filelist galera_new_cluster galera_recovery wsrep_sst_common wsrep_sst_mariabackup wsrep_sst_mysqldump wsrep_sst_rsync wsrep_sst_xtrabackup-v2 wsrep_sst_xtrabackup wsrep_sst_rsync_wan >mariadb-galera.files

# mariadb-bench.files
filelist mysqlslap >mariadb-bench.files

# mariadb-test.files
filelist mysql_client_test mysql_client_test_embedded mysql_waitpid mysqltest mysqltest_embedded >mariadb-test.files

# mariadb-tools.files
filelist msql2mysql mysql_plugin mysql_convert_table_format mysql_find_rows mysql_setpermission mysql_tzinfo_to_sql mysqlaccess mysqlhotcopy perror replace mysql_embedded >mariadb-tools.files

# All configuration files
echo '%{_datadir}/mysql/*.cnf' >> mariadb.files

# Special errormessages approach
echo '%%defattr(-, root, root)' > %{_builddir}/errormessages.files
pushd %{buildroot} >/dev/null
for f in usr/share/%{name}/*; do
    if test -e $f/errmsg.sys; then
        echo "%%dir /$f" >> %{_builddir}/errormessages.files
    fi
done
echo %{_datadir}/%{name}/errmsg-utf8.txt >> %{_builddir}/errormessages.files
popd >/dev/null
mv %{_builddir}/errormessages.files mariadb-errormessages.files

# Files not installed by make install
# Some of the documentation we need to have installed
DOCS=(COPYING README.md EXCEPTIONS-CLIENT %{_sourcedir}/README.debug plugin/daemon_example/daemon_example.ini)
DOCDIR=%{buildroot}%{_defaultdocdir}/%{name}
install -d -m 755 ${DOCDIR}
for i in "${DOCS[@]}"; do
	install -m 644 "${i}" "${DOCDIR}" || true
done

# Install default configuration file
install -m 664 %{SOURCE14} %{buildroot}%{_sysconfdir}/my.cnf

# Systemd/initscript
install -D -m 755 %{_sourcedir}/mysql-systemd-helper '%{buildroot}'%{_libexecdir}/mysql/mysql-systemd-helper
sed -i 's|@MYSQLVER@|%{version}|' '%{buildroot}'%{_libexecdir}/mysql/mysql-systemd-helper
ln -sf service '%{buildroot}'%{_sbindir}/rcmysql
rm -rf '%{buildroot}'%{_sysconfdir}/init.d
install -D -m 644 %{_sourcedir}/mariadb.service '%{buildroot}'%{_unitdir}/mariadb.service
install -D -m 644 %{_sourcedir}/mariadb@.service '%{buildroot}'%{_unitdir}/mariadb@.service
install -D -m 644 %{_sourcedir}/mariadb.target '%{buildroot}'%{_unitdir}/mariadb.target
# Aliases for the backward compatibility. Create symlinks from the alias to the existing one
# We can't use 'Alias=' option only because it's effective only when the unit is enabled
ln -sf %{_unitdir}/mariadb.service %{buildroot}%{_unitdir}/mysql.service
ln -sf %{_unitdir}/mariadb@.service %{buildroot}%{_unitdir}/mysql@.service

# Rename systemd-tmpfiles conf file because each systemd-tmpfiles file shall be named in the style of package.conf or package-part.conf
mv %{buildroot}%{_tmpfilesdir}/tmpfiles.conf %{buildroot}%{_tmpfilesdir}/mariadb.conf

# Tmpfiles file to exclude mysql tempfiles that are auto-cleaned up
# bnc#852451
mkdir -p %{buildroot}%{_tmpfilesdir}
cat >> %{buildroot}%{_tmpfilesdir}/mariadb.conf <<EOF
x %{_localstatedir}/tmp/mysql.*
EOF

# SuSEfirewall service description
install -D -m 644 %{_sourcedir}/mysql.SuSEfirewall2 %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/mysql

# Testsuite
install -d -m 755 '%{buildroot}'%{_datadir}/mysql-test/
install -m 755 suse-test-run '%{buildroot}'%{_datadir}/mysql-test/
mkdir '%{buildroot}'%{_datadir}/mysql-test%{_localstatedir}

# Install the list of skipped tests to be available for user runs
install -p -m 0644 mysql-test/unstable-tests %{buildroot}%{_datadir}/mysql-test
ln -s unstable-tests %{buildroot}%{_datadir}/mysql-test/suse_skipped_tests.list

# Final fixes
find '%{buildroot}'%{_datadir}/mysql-test -name '*.orig' -delete
%fdupes -s '%{buildroot}'%{_datadir}/mysql-test
fdupes -q -n -r '%{buildroot}'%{_datadir}/mysql-test
for i in `grep -Rl '\r' '%{buildroot}'%{_datadir}/sql-bench`; do
	dos2unix "$i"
done

# Compat with old scripts
ln -s mysqlcheck '%{buildroot}'%{_bindir}/mysqlrepair
ln -s mysqlcheck '%{buildroot}'%{_bindir}/mysqlanalyze
ln -s mysqlcheck '%{buildroot}'%{_bindir}/mysqloptimize

# Use our configuration stuff instead of upstream one
rm -rf '%{buildroot}'%{_sysconfdir}/my.cnf.d
install -d -m 755 '%{buildroot}'%{_sysconfdir}/my.cnf.d

# Install galera config file and script
install -p -m 644 build/support-files/wsrep.cnf %{buildroot}%{_sysconfdir}/my.cnf.d/50-galera.cnf
install -p -m 755 build/scripts/galera_new_cluster %{buildroot}%{_bindir}/galera_new_cluster

# Documentation that was copied to wrong folder
rm -f '%{buildroot}'%{_datadir}/doc/* 2> /dev/null || true

# Unwanted packaged stuff
rm -rf '%{buildroot}'%{_datadir}/mysql/{solaris,SELinux}

# Create the directory specified in 'secure-file-priv' option
mkdir -p '%{buildroot}'%{_localstatedir}/lib/mysql-files

%check
cd build

# Run an extensive mysql test suite
# If 0%{ignore_testsuite_result} == 1 then run all tests but ignore failures
# If 0%{ignore_testsuite_result} == 0 then skip tests listed in unstable-tests
# (contains suse_skipped_tests.list) and don't ignore failures

%if 0%{run_testsuite} > 0
cd mysql-test
./mysql-test-run.pl \
    --parallel=%{?jobs:%{jobs}} \
    --force \
    --retry=0 \
    --ssl \
    --suite-timeout=720 \
    --testcase-timeout=30 \
    --mysqld=--binlog-format=mixed \
    --force-restart \
    --shutdown-timeout=60 \
    --max-test-fail=0 \
%if 0%{ignore_testsuite_result} > 0
    || :
%else
    --skip-test-list=unstable-tests
%endif
%endif

# client does not require server and needs the user too
%pre client
getent group mysql >/dev/null || groupadd -r mysql
getent passwd mysql >/dev/null || useradd -r -o -g mysql -u 60 -c "MySQL database admin" \
                  -s /bin/false -d %{_localstatedir}/lib/mysql mysql
# if mysql user is not in mysql group or if mysql user doesn't have '/bin/false' shell set, do so
id -Gn mysql | grep '\bmysql\b' &>/dev/null || usermod -g mysql mysql
getent passwd mysql | cut -d: -f7 | grep '\b/bin/false\b' &>/dev/null || usermod -s /bin/false mysql
exit 0

%pre
getent group mysql >/dev/null || groupadd -r mysql
getent passwd mysql >/dev/null || useradd -r -o -g mysql -u 60 -c "MySQL database admin" \
                  -s /bin/false -d %{_localstatedir}/lib/mysql mysql
# if mysql user is not in mysql group or if mysql user doesn't have '/bin/false' shell set, do so
id -Gn mysql | grep '\bmysql\b' &>/dev/null || usermod -g mysql mysql
getent passwd mysql | cut -d: -f7 | grep '\b/bin/false\b' &>/dev/null || usermod -s /bin/false mysql

%service_add_pre mariadb.service

%post
%service_add_post mariadb.service
%tmpfiles_create %{_tmpfilesdir}/mariadb.conf

# SLE11 Migration support
for i in protected tmp; do
    rmdir "$datadir"/.$i 2>/dev/null || :
done

# During package rename (migration maria->mysql-community-server),
# there might be config file move and we get rpmsave that we should keep
if [ -f %{_sysconfdir}/my.cnf.rpmsave ]; then
    mv %{_sysconfdir}/my.cnf{,.rpmnew}
    mv %{_sysconfdir}/my.cnf{.rpmsave,}
    cat >> %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}-something << EOF

WARNING: %{_sysconfdir}/my.cnf.rpmsave file detected!

This probably means that you are migrating from different variant of MySQL.
Your configuration was left intact and you can see the new configuration in
%{_sysconfdir}/my.cnf.rpmnew

EOF
fi

# Warn on first run
datadir="`%{_bindir}/my_print_defaults mysqld mysql_server | sed -n 's|--datadir=||p'`"
[ -n "$datadir" ] || datadir="%{_localstatedir}/lib/mysql"
if [ -d "$datadir/mysql" ]; then
    touch "$datadir/.run-mysql_upgrade"
fi
if [ \! -f "$datadir/mysql_upgrade_info" ]; then
    if [ $1 -eq 1 ]; then
        cat >> %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}-something << EOF

%(cat %{_sourcedir}/README.install)

EOF
    fi
else
    MYSQLVER="`echo %{version} | sed 's|\.[0-9]\+$||'`"
    if [ -f "$datadir/mysql_upgrade_info" ] && \
        [ -z "`grep "^$MYSQLVER" "$datadir/mysql_upgrade_info" 2> /dev/null`" ]; then
    cat >> %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}-something << EOF

WARNING: You are upgrading from different stable version of MySQL!

Your database will be migrated automatically during next restart of MySQL.
Before you do that make sure you have up to date backup of your data. It
should be mainly in $datadir directory.

EOF
    fi
fi
exit 0

%preun
%service_del_preun mariadb.service

%postun
%service_del_postun mariadb.service

%post -n libmysqld%{soname} -p /sbin/ldconfig
%postun -n libmysqld%{soname} -p /sbin/ldconfig

%files -f mariadb.files
%config(noreplace) %attr(0644, root, mysql) %{_sysconfdir}/my.cnf
%dir %attr(0755, root, mysql) %{_sysconfdir}/my.cnf.d
%config(noreplace) %attr(0644, root, mysql) %{_sysconfdir}/my.cnf.d/*
%exclude %{_sysconfdir}/my.cnf.d/50-galera.cnf
%config %{_sysconfdir}/logrotate.d/%{name}
%doc %{_defaultdocdir}/%{name}
%dir %{_libexecdir}/mysql
%dir %attr(0700, mysql, mysql) %{_localstatedir}/log/mysql
%{_libexecdir}/mysql/mysql-systemd-helper
%{_unitdir}/mariadb.service
%{_unitdir}/mariadb@.service
%{_unitdir}/mariadb.target
%{_unitdir}/mysql.service
%{_unitdir}/mysql@.service
%{_tmpfilesdir}/mariadb.conf
%{_sbindir}/rcmysql
%dir %{_datadir}/%{name}
%dir %{_datadir}/mysql
%{_datadir}/%{name}/charsets/
%{_datadir}/%{name}/*.sql
%dir %{_libdir}/mysql
%{_libdir}/mysql/mysqld.sym
%{_libdir}/mysql/INFO_SRC
%config %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/mysql
%dir %{_libdir}/mysql/plugin
%{_libdir}/mysql/plugin/*.so
%exclude %{_libdir}/mysql/plugin/dialog*.so
%ghost %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}-something
%dir %attr(0750, mysql, mysql) %{_localstatedir}/lib/mysql-files
%if 0%{with_mroonga} > 0
%{_datadir}/mariadb/mroonga/
%dir %{_datadir}/groonga/
%{_datadir}/groonga/COPYING
%{_datadir}/groonga/README.md
%dir %{_datadir}/groonga-normalizer-mysql
%{_datadir}/groonga-normalizer-mysql/README.md
%{_datadir}/groonga-normalizer-mysql/lgpl-2.0.txt
%endif
%dir %{_datadir}/mysql/policy
%dir %{_datadir}/mysql/policy/apparmor
%{_datadir}/mysql/policy/apparmor/README
%{_datadir}/mysql/policy/apparmor/usr.sbin.mysqld*
%dir %{_datadir}/mysql/policy/selinux
%{_datadir}/mysql/policy/selinux/README
%{_datadir}/mysql/policy/selinux/mariadb-server.*
%{_datadir}/mysql/policy/selinux/mariadb.te
%dir %{_datadir}/mysql/systemd
%{_datadir}/mysql/systemd/mariadb.service
%{_datadir}/mysql/systemd/mariadb@.service

%files -n libmysqld%{soname}
%{_libdir}/libmysqld.so.*

%files -n libmysqld-devel
%{_libdir}/libmysqld.a
%{_libdir}/libmysqld.so

%files client -f mariadb-client.files
%dir %{_libdir}/mysql
%dir %{_libdir}/mysql/plugin
%{_libdir}/mysql/plugin/dialog_examples.so

%files galera -f mariadb-galera.files
%doc Docs/README.wsrep
%config(noreplace) %{_sysconfdir}/my.cnf.d/50-galera.cnf
%{_datadir}/mysql/systemd/use_galera_new_cluster.conf
%{_datadir}/mysql/wsrep_notify

%files errormessages -f mariadb-errormessages.files
%{_datadir}/%{name}/*/errmsg.sys

%files bench -f mariadb-bench.files
%{_datadir}/sql-bench

%files test -f mariadb-test.files
%{_bindir}/my_safe_process
%{_mandir}/man1/my_safe_process.1*
%{_mandir}/man1/mysql-test-run.pl.1*
%{_mandir}/man1/mysql-stress-test.pl.1*
%{_datadir}/mysql-test/valgrind.supp
%dir %attr(755, mysql, mysql)%{_datadir}/mysql-test
%{_datadir}/mysql-test/[^v]*
%dir %attr(755, mysql, mysql) %{_datadir}/mysql-test%{_localstatedir}

%files tools -f mariadb-tools.files
%{_bindir}/mysqlrepair
%{_bindir}/mysqlanalyze
%{_bindir}/mysqloptimize

%changelog
