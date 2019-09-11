#
# spec file for package php7
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


%define debug_build       0
%define asan_build        0
%global apiver            20180731
%global zendver           20180731
%global pearver           1.10.9
%define pkg_name          php7
%define extension_dir     %{_libdir}/%{pkg_name}/extensions
%define peardir           %{_datadir}/%{pkg_name}/PEAR
%define php_sysconf       %{_sysconfdir}/%{pkg_name}
%define build_firebird 0%{?is_opensuse}
%define build_sodium 0
%if %{?suse_version} > 1320
%define build_sodium 1
%endif
%define system_gd 0
# for openSUSE 42.3 is newer gd linked in devel:languages:php,
# see bsc#1074025
%if 0%{?is_opensuse} || %{?suse_version} >= 1500
%define system_gd 1
%endif
%define build_argon2 0
%if %{?suse_version} >= 1500
%define build_argon2 1
%endif
%bcond_with make_test
Name:           php7
Version:        7.3.8
Release:        0
Summary:        Interpreter for the PHP scripting language version 7
License:        PHP-3.01
Group:          Development/Languages/Other
URL:            https://secure.php.net
Source0:        https://secure.php.net/distributions/php-%{version}.tar.xz
Source1:        php-suse-addons.tar.bz2
Source5:        README.macros
Source6:        macros.php
Source8:        https://secure.php.net/distributions/php-%{version}.tar.xz.asc
Source9:        php7.keyring
Source11:       php7.rpmlintrc
Source100:      build-test.sh
## SUSE specific patches
Patch0:         php-phpize.patch
Patch2:         php-php-config.patch
Patch3:         php-ini.patch
Patch4:         php-no-build-date.patch
Patch5:         php-pts.patch
Patch6:         php-openssl.patch
Patch7:         php-systzdata-v18.patch
Patch8:         php-systemd-unit.patch
Patch10:        php-embed.patch
## Bugfix patches
# following patch is to fix configure tests for crypt; the aim is to have php
# built against glibc's crypt; problem is, that our glibc doesn't support extended
# DES, so as soon as upstream fixes this, don't forgot to remove extended DES
# from their checking as I indicated in crypt-tests.patch yet, or php will
# silently use his own implementation again
Patch12:        php-crypt-tests.patch
# https://bugs.php.net/bug.php?id=53007
Patch14:        php-odbc-cmp-int-cast.patch
# https://bugs.php.net/bug.php?id=70461
Patch15:        php-fix_net-snmp_disable_MD5.patch
# should be upstreamed, will do later
Patch17:        php-date-regenerate-lexers.patch
BuildRequires:  apache-rex
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  curl
BuildRequires:  curl-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  db-devel
BuildRequires:  freetds-devel
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gpg2
BuildRequires:  krb5-devel
BuildRequires:  libapparmor-devel
BuildRequires:  libbz2-devel
BuildRequires:  libedit-devel
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libpng-devel
BuildRequires:  libtidy-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  libxslt-devel
BuildRequires:  lmdb-devel
BuildRequires:  ncurses-devel
BuildRequires:  net-snmp-devel
BuildRequires:  openldap2-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  postfix
BuildRequires:  postgresql-devel
BuildRequires:  re2c
BuildRequires:  sqlite3-devel
BuildRequires:  tcpd-devel
BuildRequires:  unixODBC-devel
BuildRequires:  update-alternatives
BuildRequires:  xz
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(zlib)
Requires:       timezone
Recommends:     php-ctype
Recommends:     php-dom
Recommends:     php-iconv
Recommends:     php-json
Recommends:     php-sqlite
Recommends:     php-tokenizer
Recommends:     php-xmlreader
Recommends:     php-xmlwriter
# Recommends instead of Requires smtp_daemon bsc#1115213
Recommends:     smtp_daemon
# suggest php7-* instead of php-* [bsc#1022158c#4]
Suggests:       php7-gd
Suggests:       php7-gettext
Suggests:       php7-mbstring
Suggests:       php7-mysql
Suggests:       php7-pear
## Provides
Provides:       php = %{version}
Provides:       php-api = %{apiver}
Provides:       php-cli = %{version}
Provides:       php-zend-abi = %{zendver}
Provides:       php(api) = %{apiver}
Provides:       php(zend-abi) = %{zendver}
# builtin extensions
Provides:       php-date = %{version}
Provides:       php-filter = %{version}
Provides:       php-hash = %{version}
Provides:       php-pcre = %{version}
Provides:       php-reflection = %{version}
Provides:       php-session = %{version}
Provides:       php-simplexml = %{version}
Provides:       php-spl = %{version}
Provides:       php-xml = %{version}
Provides:       zend = %{zendver}
# conflicts with php5 and should replace it
Obsoletes:      php < %{version}
Obsoletes:      php5
Obsoletes:      php7-mcrypt
%if %{build_firebird}
# firebird-devel was merged into libfbclient2-devel for firebird 3
%if 0%{?suse_version} <= 1320
BuildRequires:  firebird-devel
BuildRequires:  libfbclient2-devel
%else
BuildRequires:  libfbclient-devel
%endif
%endif
%if %{system_gd}
BuildRequires:  gd-devel
%else
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(xft)
%endif
%if %{build_sodium}
BuildRequires:  libsodium-devel
%endif
%if %{build_argon2}
BuildRequires:  pkgconfig(libargon2)
%endif
%if 0%{?suse_version} >= 1315
BuildRequires:  libzip-devel
%endif
%if 0%{?suse_version} > 1320
Requires(pre):  group(www)
Requires(pre):  user(wwwrun)
%endif

%description
PHP is a server-side HTML embedded scripting language designed
primarily for web development but also used as a general-purpose
programming language.

This package contains the standard implementation of PHP, namely Zend
PHP. Included are the PHP command-line binary and the configuration
file (php.ini). This package must be installed in order to use PHP.
Additionally, extension modules and server modules (e.g. for Apache)
may be installed.

Additional documentation is available in package php-doc.

%package devel
Summary:        PHP7 development files for C/C++ extensions
# this is required by the installed  development headers
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}
# this is needed for "pecl" functionality
Requires:       autoconf
Requires:       automake
Requires:       glibc-devel
Requires:       libtool
Requires:       libxml2-devel
Requires:       pcre2-devel
Requires:       php7-pear
Provides:       pecl = %{version}
Provides:       php-devel = %{version}
Obsoletes:      php5-devel

%description devel
PHP is a server-side HTML embedded scripting language designed
primarily for web development but also used as a general-purpose
programming language.

This package contains the C headers to build PHP extensions.

%if %{with make_test}
%package testresults
Summary:        PHP7 testsuite results
Group:          Development/Languages/PHP
BuildArch:      noarch

%description testresults
PHP is a server-side HTML embedded scripting language designed
primarily for web development but also used as a general-purpose
programming language.

This package contains results from running the PHP7 testsuite.
%endif

%package pear
Summary:        PHP Extension and Application Repository
Group:          Development/Libraries/PHP
Requires:       %{name}-zlib = %{version}
Provides:       php-pear = %{pearver}
Provides:       php-pear(PEAR) = %{pearver}
%if 0%{?suse_version} <= 1330
Provides:       php7-pear-Archive_Tar
%else
Obsoletes:      php7-pear-Archive_Tar
%endif
Obsoletes:      php5-pear
BuildArch:      noarch

%description pear
PEAR is a code repository for PHP extensions and PHP library code
similar to TeX's CTAN and Perl's CPAN. This package provides an access
to the repository.

See https://pear.php.net/manual for more details.

%package -n apache2-mod_php7
Summary:        PHP7 module for the Apache 2.x webserver
Group:          Productivity/Networking/Web/Servers
Requires:       %{apache_mmn}
Requires:       %{name} = %{version}
Requires:       apache2-prefork
PreReq:         apache2
Provides:       mod_php_any = %{version}
Provides:       php-date = %{version}
Provides:       php-filter = %{version}
Provides:       php-pcre = %{version}
Provides:       php-reflection = %{version}
Provides:       php-session = %{version}
Provides:       php-simplexml = %{version}
Provides:       php-spl = %{version}
Provides:       php-xml = %{version}
Obsoletes:      apache2-mod_php5

%description -n apache2-mod_php7
PHP is a server-side, cross-platform HTML embedded scripting language.
If you are completely new to PHP and want to get some idea of how it
works, have a look at the Introductory tutorial. Once you get beyond
that, have a look at the example archive sites and some of the other
resources available in the links section.

Please refer to %{_docdir}/php7/README.SUSE for
information on how to load the module into the Apache webserver.

%package fastcgi
Summary:        FastCGI PHP7 Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-cgi = %{version}
Provides:       php-date = %{version}
Provides:       php-fastcgi = %{version}
Provides:       php-filter = %{version}
Provides:       php-pcre = %{version}
Provides:       php-reflection = %{version}
Provides:       php-session = %{version}
Provides:       php-simplexml = %{version}
Provides:       php-spl = %{version}
Provides:       php-xml = %{version}
Obsoletes:      php5-fastcgi

%description fastcgi
PHP is a server-side, cross-platform HTML embedded scripting language.
If you are completely new to PHP and want to get some idea of how it
works, have a look at the Introductory tutorial. Once you get beyond
that have a look at the example archive sites and some of the other
resources available in the links section.

Please refer to %{_docdir}/php7/README.FastCGI for
information on how to use this module.

%package fpm
Summary:        FastCGI Process Manager PHP7 Module
Group:          Development/Libraries/PHP
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsystemd)
Requires:       %{name} = %{version}
Provides:       php-date = %{version}
Provides:       php-filter = %{version}
Provides:       php-fpm = %{version}
Provides:       php-pcre = %{version}
Provides:       php-reflection = %{version}
Provides:       php-session = %{version}
Provides:       php-simplexml = %{version}
Provides:       php-spl = %{version}
Provides:       php-xml = %{version}
Obsoletes:      php5-fpm
%{systemd_requires}

%description fpm
PHP is a server-side, cross-platform HTML embedded scripting language.
If you are completely new to PHP and want to get some idea of how it
works, have a look at the Introductory tutorial. Once you get beyond
that have a look at the example archive sites and some of the other
resources available in the links section.

Please refer to %{_docdir}/php7/README.FastCGI for
information on how to use this module.

%package embed
Summary:        Embedded SAPI Library
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description embed
PHP is a server-side, cross-platform HTML embedded scripting language.
If you are completely new to PHP and want to get some idea of how it
works, have a look at the Introductory tutorial. Once you get beyond
that have a look at the example archive sites and some of the other
resources available in the links section.

%package bcmath
Summary:        "Binary Calculator" extension for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-bcmath = %{version}
Obsoletes:      php5-bcmath

%description bcmath
Binary Calculator which supports numbers of any size and precision,
represented as strings.

%package bz2
Summary:        bzip2 codec support for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-bz2 = %{version}
Obsoletes:      php5-bz2

%description bz2
PHP functions to read and write bzip2 (.bz2) compressed files.

%package calendar
Summary:        PHP7 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-calendar = %{version}
Obsoletes:      php5-calendar

%description calendar
PHP functions for converting between different calendar formats.

%package ctype
Summary:        Character class extension for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-ctype = %{version}
Obsoletes:      php5-ctype

%description ctype
PHP functions for checking whether a character or string falls into a
certain character class according to the current locale.

%package curl
Summary:        libcurl integration for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-curl = %{version}
Obsoletes:      php5-curl

%description curl
PHP interface to libcurl that allows you to connect to and communicate
with servers of many different types, using protocols of many different
types.

%package dba
Summary:        Database abstraction layer for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-dba = %{version}
Obsoletes:      php5-dba

%description dba
This is a general abstraction layer for several file-based databases.
As such, functionality is limited to a common subset of features
supported by modern databases such as Sleepycat Software's DB2. (This
is not to be confused with IBM's DB2 software, which is supported
through the ODBC functions.)

%package dom
Summary:        Document Object Model extension for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-dom = %{version}
Obsoletes:      php5-dom

%description dom
This module adds Document Object Model (DOM) support.

%package enchant
Summary:        Spell checking extension for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-enchant = %{version}
Obsoletes:      php5-enchant
# Obsolete pspell plugin as enchant is favored solution (goodbye aspell)
Obsoletes:      php5-pspell
Obsoletes:      php7-pspell

%description enchant
Enchant is the PHP binding for the Enchant library. Enchant steps in
to provide uniformity and conformity on top of all spelling
libraries, and implements certain features that may be lacking in any
individual provider library. Everything should "just work" for any
and every definition of "just working."

%package exif
Summary:        EXIF metadata extensions for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-mbstring = %{version}
Provides:       php-exif = %{version}
Obsoletes:      php5-exif

%description exif
PHP functions for extracting EXIF (Exchangable Image File Format;
metadata from images) information stored in headers of JPEG and TIFF
images.

%package fileinfo
Summary:        File identification extension for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-fileinfo = %{version}
Obsoletes:      php5-fileinfo

%description fileinfo
The functions in this module try to guess the content type and
encoding of a file by looking for certain magic byte sequences at
specific positions within the file. It uses (a bundled version of)
libmagic to heuristically determine this.

%package ftp
Summary:        FTP protocol support for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-openssl = %{version}
Provides:       php-ftp = %{version}
Obsoletes:      php5-ftp

%description ftp
PHP functions for access to file servers speaking the File Transfer
Protocol (FTP) as defined in RFC 959.

%package gd
Summary:        GD Graphics Library extension for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-gd = %{version}
Obsoletes:      php5-gd

%description gd
PHP functions to create and manipulate image files in a variety of
different image formats, including GIF, PNG, JPEG, WBMP, and XPM. Even
more convenient: PHP can output image streams directly to a browser.

%package gettext
Summary:        Native language support for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-gettext = %{version}
Obsoletes:      php5-gettext

%description gettext
PHP functions that implement a Native Language Support (NLS) API which
can be used to internationalize your PHP applications.

%package gmp
Summary:        Bignum extension for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-gmp = %{version}
Obsoletes:      php5-gmp

%description gmp
PHP functions for work with arbitrary-length integers using the GNU MP
library.

%package iconv
Summary:        Character set conversion functions for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-iconv = %{version}
Obsoletes:      php5-iconv

%description iconv
This module contains an interface to iconv character set conversion
facility. With this module, a string represented by a local character
set can be turned into another character set, which may be the
Unicode character set. Supported character sets depend on the iconv
implementation of your system.

%package intl
Summary:        ICU integration for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-intl = %{version}
Obsoletes:      php5-intl

%description intl
The internationalization (intl) extension is a wrapper for the ICU
library, enabling PHP programmers to perform UCA (Unicode Collation
Algorithm) conformant collation as well as date, time, number and
currency formatting in their scripts.

%package json
Summary:        JSON (de)serializer functions for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-json = %{version}
Obsoletes:      php5-json

%description json
This extension implements the JavaScript Object Notation (JSON)
data-interchange format.

%package ldap
Summary:        LDAP protocol support for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-openssl = %{version}
Provides:       php-ldap = %{version}
Obsoletes:      php5-ldap

%description ldap
PHP interface to the Lightweight Directory Access Protocol (LDAP).

%package mbstring
Summary:        Multibyte string functions for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-mbstring = %{version}
Obsoletes:      php5-mbstring

%description mbstring
mbstring provides multibyte specific string functions that help
dealing with multibyte encodings in PHP. mbstring handles character
encoding conversion between the possible encoding pairs. mbstring
handles Unicode-based encodings such as UTF-8 and UCS-2 and many
single-byte encodings for convenience.

%package mysql
Summary:        MySQL database client for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-pdo = %{version}
Provides:       php-mysql = %{version}
Provides:       php_any_db = %{version}
Obsoletes:      php5-mysql

%description mysql
PHP functions for access to MySQL database servers.

%if %{build_firebird}
%package firebird
Summary:        Firebird database client for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-pdo = %{version}
Provides:       php-firebird = %{version}
Provides:       php_any_db = %{version}
Obsoletes:      php5-firebird

%description firebird
PHP functions for access to firebird database servers.
%endif

%package odbc
Summary:        ODBC extension for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-pdo = %{version}
Provides:       php-odbc = %{version}
Provides:       php-pdo_odbc = %{version}
Obsoletes:      php5-odbc

%description odbc
This module adds Open Database Connectivity (ODBC) support.

%package opcache
Summary:        Opcode cache extension for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-opcache = %{version}
Obsoletes:      php5-opcache

%description opcache
OPcache improves PHP performance by storing precompiled script
bytecode in shared memory, thereby removing the need for PHP to load
and parse scripts on each request.

%package openssl
Summary:        OpenSSL integration for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-openssl = %{version}
Obsoletes:      php5-openssl

%description openssl
This extension binds functions of OpenSSL library for symmetric and
asymmetric encryption and decryption, PBKDF2, PKCS#7, PKCS#12, X.509
and other crypto operations. It also provides an implementation of
TLS streams.

%package pcntl
Summary:        Process Control extension for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-pcntl = %{version}
Obsoletes:      php5-pcntl

%description pcntl
Process Control support in PHP implements the Unix style of process
creation, program execution, signal handling and process termination
(fork, waitpid, signal, WIF flags, etc.)

%package phar
Summary:        PHP Archive extension for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-phar = %{version}
Obsoletes:      php5-phar

%description phar
The phar extension provides a way to put entire PHP applications into
a single file called a "phar" (PHP Archive) for distribution and
installation.

In addition, the phar extension also provides a file-format
abstraction method for creating and manipulating tar and zip files
through the PharData class, much as PDO provides a unified interface
for accessing different databases. Phar also can convert between tar,
zip and phar file formats.

%package pdo
Summary:        PHP Data Objects extension for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-pdo = %{version}
Obsoletes:      php5-pdo

%description pdo
The PHP Data Objects (PDO) extension defines an interface for
accessing databases in PHP. Each database driver that implements the
PDO interface can expose database-specific features as regular
extension functions. Note that you use a database-specific PDO driver
to access a database server.

PDO provides a data-access abstraction layer, which means that,
regardless of the database used, you use the same functions to issue
queries and fetch data. PDO does not provide a database abstraction;
it does not rewrite SQL or emulate missing features.

%package pgsql
Summary:        PostgreSQL database client for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-pdo = %{version}
Provides:       php-pgsql = %{version}
Provides:       php_any_db = %{version}
Obsoletes:      php5-pgsql

%description pgsql
PHP functions for access to PostgreSQL database servers. It includes
both traditional pgsql and pdo_pgsql drivers.

%package posix
Summary:        POSIX functions for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-posix = %{version}
Obsoletes:      php5-posix

%description posix
This module contains an interface to those functions defined in the
IEEE 1003.1 (POSIX.1) standards document which are not accessible
through other means.

%package readline
Summary:        PHP7 readline extension
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-readline = %{version}
Obsoletes:      php5-readline

%description readline
PHP interface to libedit, which provides editable command line as well
as PHP interactive mode (php -a).

%package shmop
Summary:        Alternate, low-level shared memory implementation for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-shmop = %{version}
Obsoletes:      php5-shmop

%description shmop
An extension created as an alternative to the sysvmsg module.

%package snmp
Summary:        SNMP extension for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-snmp = %{version}
Obsoletes:      php5-snmp

%description snmp
The SNMP extension provides a toolset for managing remote devices via
the Simple Network Management Protocol.

As it is a wrapper around the underlying Net-SNMP library, all basic
concepts are the same and the PHP functions change their behavior
depending on the Net-SNMP configuration files and environment
variables.

%package soap
Summary:        SOAP/WSDL extension module for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-soap = %{version}
Obsoletes:      php5-soap

%description soap
This module provides SOAP support.

SOAP extension can be used to write SOAP Servers and Clients. It
supports subsets of SOAP 1.1, SOAP 1.2 and WSDL 1.1 specifications.

%package sockets
Summary:        Berkeley sockets API for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-sockets = %{version}
Obsoletes:      php5-sockets

%description sockets
The socket extension implements a low-level interface to the socket
communication functions based on the BSD sockets API, providing the
possibility to act as a socket server as well as a client.

%if %{build_sodium}
%package sodium
Summary:        Cryptographic Extension Based on Libsodium
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-sodium = %{version}

%description sodium
PHP binding to libsodium software library for encryption, decryption,
signatures, password hashing and more.
%endif

%package sqlite
Summary:        SQLite database client for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-pdo = %{version}
Provides:       php-sqlite = %{version}
Obsoletes:      php5-sqlite

%description sqlite
This is an extension for the SQLite Embeddable SQL Database Engine.
https://www.sqlite.org

SQLite is a C library that implements an embeddable SQL database
engine. Programs that link with the SQLite library can have SQL
database access without running a separate RDBMS process.

SQLite is not a client library used to connect to a big database
server. SQLite is the server. The SQLite library reads and writes
directly to and from the database files on disk.

This package includes sqlite and pdo_sqlite modules for sqlite version
2 and 3 respectively.

%package sysvmsg
Summary:        SysV Message Queue support for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-sysvmsg = %{version}
Obsoletes:      php5-sysvmsg

%description sysvmsg
This module provides System V Message Queue support.

%package sysvsem
Summary:        SysV Semaphore support for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-sysvsem = %{version}
Obsoletes:      php5-sysvsem

%description sysvsem
PHP interface for System V semaphores.

%package sysvshm
Summary:        SysV Shared Memory support for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-sysvshm = %{version}
Obsoletes:      php5-sysvshm

%description sysvshm
PHP interface for System V shared memory.

%package tidy
Summary:        PHP7 binding for the Tidy HTML cleaner
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-tidy = %{version}
Obsoletes:      php5-tidy

%description tidy
Tidy is an extension based on Libtidy (http://tidy.sourceforge.net) and allows
a PHP developer to clean, repair, and traverse HTML, XHTML, and XML
documents -- including ones with embedded scripting languages such as
PHP or ASP within them using OO constructs.

%package tokenizer
Summary:        Extension module to access Zend Engine's PHP tokenizer
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-tokenizer = %{version}
Obsoletes:      php5-tokenizer

%description tokenizer
The tokenizer functions provide an interface to the PHP tokenizer
embedded in the Zend Engine. Using these functions you may write your
own PHP source analyzing or modification tools without having to deal
with the language specification at the lexical level.

%package wddx
Summary:        WDDX support for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-wddx = %{version}
Obsoletes:      php5-wddx

%description wddx
PHP functions for working with WDDX - Web Distributed Data Exchange,
a programming language-, platform- and transport-neutral data
interchange mechanism designed to pass data between different
environments and different computers.

%package xmlrpc
Summary:        XML RPC support for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-xmlrpc = %{version}
Obsoletes:      php5-xmlrpc

%description xmlrpc
This module adds XMLRPC-EPI support.

%package xsl
Summary:        PHP7 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-dom = %{version}
Provides:       php-xsl = %{version}
Obsoletes:      php5-xsl

%description xsl
PHP's XSL extension implements the XSL (Extensible Stylesheet
Language) standard, performing XSLT transformations using the libxslt
library

%package xmlreader
Summary:        Streaming XML reader extension for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-dom = %{version}
Provides:       php-xmlreader = %{version}
Obsoletes:      php5-xmlreader

%description xmlreader
The XMLReader extension is an XML Pull parser. The reader acts as a
cursor going forward on the document stream and stopping at each node
on the way.

%package xmlwriter
Summary:        Streaming-based XML writer extension for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-xmlwriter = %{version}
Obsoletes:      php5-xmlwriter

%description xmlwriter
XMLWriter wraps the libxml xmlWriter API. Represents a writer that
provides a non-cached, forward-only means of generating streams or
files containing XML data.

%package zip
Summary:        ZIP archive support for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-zip = %{version}
Obsoletes:      php5-zip

%description zip
This extension allows to transparently read or write ZIP compressed
archives and the files inside them.

%package zlib
Summary:        Zlib compression support for PHP
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-zlib = %{version}
Obsoletes:      php5-zlib

%description zlib
This module enables to transparently read and write gzip (.gz)
compressed files, through versions of most of the filesystem
functions which work with gzip-compressed files (and uncompressed
files, too, but not with sockets).

%prep
echo %{apache_mmn}
%setup -q -n php-%{version} -a 1
cp %{SOURCE5} .

%patch0
%patch2
%patch3 -p1
%patch4 -p1
%patch5
%patch6
%patch7 -p1
%patch8 -p1
%patch10 -p1
%patch12 -p1
%patch14 -p1
%patch15
%patch17 -p1

# Safety check for API version change.
vapi=`sed -n '/#define PHP_API_VERSION/{s/.* //;p}' main/php.h`
if test "x${vapi}" != "x%{apiver}"; then
    : Error: Upstream API version is now ${vapi}, expecting %{apiver}.
    : Update the apiver macro and rebuild.
    exit 1
fi
vzend=`sed -n '/#define ZEND_MODULE_API_NO/{s/^[^0-9]*//;p;}' Zend/zend_modules.h`
if test "x${vzend}" != "x%{zendver}"; then
    : Error: Upstream Zend ABI version is now ${vzend}, expecting %{zendver}.
    : Update the zendver macro and rebuild.
    exit 1
fi
vpear=`sed -n 's/.*=>.*PEAR-\(.*\)\.tar.*/\1/p' pear/install-pear-nozlib.phar`
if test "x${vpear}" != "x%{pearver}"; then
    : Error: Upstream PEAR version is now ${vpear}, expecting %{pearver}.
    : Update the pearver macro and rebuild.
    exit 1
fi
if [ %{version} != '7.3.8' ]; then
echo 'check whether pcre.jit=0 workaround is still needed'
echo 'https://bugs.php.net/bug.php?id=77260'
exit 1
fi

%build
%define _lto_cflags %{nil}
# aclocal workaround - to be improved
cat `aclocal --print-ac-dir`/{libtool,ltoptions,ltsugar,ltversion,lt~obsolete}.m4 >>aclocal.m4

# force use of system libtool:
libtoolize --force --copy
cat `aclocal --print-ac-dir`/{libtool,ltoptions,ltsugar,ltversion,lt~obsolete}.m4 >build/libtool.m4

# build directories for individual SAPIs
mkdir -p build-apache2
mkdir -p build-fpm
mkdir -p build-embed
mkdir -p build-fastcgi
mkdir -p build-cli

# get parsers regenerated
for parser in `find -type f -name "*.re"`;do
rm -v ${parser%.*}.c
done

rm -r ext/pcre/pcre2lib

# regenerate configure etc.
rm configure
./buildconf --force

# export flags
CFLAGS="%{optflags} -O3 -fPIE -fPIC -DPIC -D_GNU_SOURCE -fno-strict-aliasing"
CXXFLAGS="%{optflags} -O3 -fPIE -fPIC -DPIC -D_GNU_SOURCE -fno-strict-aliasing"
%if %{build_firebird}
CFLAGS="$CFLAGS -I/usr/include/firebird"
CXXFLAGS="$CXXFLAGS -I/usr/include/firebird"
%endif
%if %{debug_build}
CFLAGS="$CFLAGS -Og"
CXXFLAGS="$CXXFLAGS -Og"
%endif
export CFLAGS
export CXXFLAGS
export LDFLAGS="-pie"
export NO_INTERACTION=true
# where to install extensions
EXTENSION_DIR=%{extension_dir}
export EXTENSION_DIR
export PHP_MYSQLND_ENABLED=yes
export PHP_MYSQLND_COMPRESSION_SUPPORT=yes
# Fix build-cli for %arm and aarch64
export LIBS=-ltinfo

# build function
Build()
{
    sapi=$1
    pushd build-$1
    shift
    ln -sf ../configure
    %configure \
        --datadir=%{_datadir}/%{pkg_name} \
        --with-libdir=%{_lib} \
        --includedir=%{_includedir} \
        --sysconfdir=%{php_sysconf}/$sapi \
        --with-config-file-path=%{php_sysconf}/$sapi \
        --with-config-file-scan-dir=%{php_sysconf}/conf.d \
        --enable-libxml \
        --enable-session \
        --with-pcre-regex=%{_usr} \
        --enable-xml \
        --enable-simplexml \
        --enable-filter \
        --disable-debug \
        --enable-inline-optimization \
        --disable-rpath \
        --disable-static \
        --enable-shared \
        --with-pic \
        --with-gnu-ld \
        --enable-re2c-cgoto \
        --with-system-tzdata=%{_datadir}/zoneinfo \
        --enable-hash \
        --with-mhash \
        --enable-phpdbg=no \
%if %{build_sodium}
        --with-sodium=shared \
%endif
%if 0%{?suse_version} >= 1320
        --with-libzip \
%endif
%if %{build_argon2}
        --with-password-argon2=%{_usr} \
%endif
        "$@" || { cat config.log; exit 1; }
    # Some modules are builtin, reasons:
    #  - libxml can not be shared (and is needed by PEAR)
    #  - spl doesn't build shared
    #  - simplexml is needed by spl
    #  - session need to be builtin, otherwise sqlite and other session engines fail
    #  - pcre is needed for PEAR
    #  - filter is builtin due security reasons
    # We have still have harcoded RPATH in some modules
    sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
    sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=LIBTOOL_IS_BROKED|g' libtool
    # build mod_phpN.so instead of libphpN.so
    # rename does not suffice, see bsc#1089487
    if [ $sapi == apache2 ]; then
      sed -i 's/libphp/mod_php/' Makefile
    fi
%if %{asan_build}
    sed -i -e 's/\(^CFLAGS.*\)/\1 -fsanitize=address/' \
           -e 's/\(^EXTRA_LIBS =.*\)/\1 -lasan/' \
           Makefile
%endif
    make %{?_smp_mflags} PHP_PEAR_PHP_BIN=%{_bindir}/php}
    popd
}

# perform all builds
# apache2 sapi
Build apache2 \
    --with-apxs2=%{apache_apxs} \
    --disable-all \
    --disable-cli

# fast-cgi sapi
Build fastcgi \
    --enable-force-cgi-redirect \
    --disable-discard-path \
    --enable-fastcgi \
    --bindir=%{_bindir} \
    --disable-cli \
    --disable-all

Build fpm \
    --with-fpm-systemd \
    --enable-fpm \
    --bindir=%{_bindir} \
    --disable-cli \
    --disable-all \
    --localstatedir=%{_localstatedir}

Build embed \
    --enable-embed=shared \
    --disable-cli \
    --disable-all

Build cli \
    --enable-cli \
    --with-pear=%{peardir} \
    --enable-bcmath=shared \
    --enable-calendar=shared \
    --enable-ctype=shared \
    --enable-dom=shared \
    --enable-exif=shared \
    --enable-ftp=shared \
    --enable-mbstring=shared \
    --enable-mbregex \
    --enable-pcntl=shared \
    --enable-posix=shared \
    --enable-shmop=shared \
    --enable-soap=shared \
    --enable-sockets=shared \
    --enable-sysvmsg=shared \
    --enable-sysvsem=shared \
    --enable-sysvshm=shared \
    --enable-tokenizer=shared \
    --enable-wddx=shared \
    --enable-fileinfo=shared \
    --with-zlib=shared \
    --with-bz2=shared \
    --with-curl=shared \
%if %{system_gd}
    --with-gd=shared,%{_usr} \
%else
    --with-gd=shared \
%endif
    --enable-gd-native-ttf \
    --with-xpm-dir=%{_usr} \
    --with-freetype-dir=%{_usr} \
    --with-png-dir=%{_usr} \
    --with-jpeg-dir=%{_usr} \
    --with-zlib-dir=%{_usr} \
    --with-gettext=shared \
    --with-gmp=shared \
    --with-iconv=shared \
    --with-kerberos \
    --enable-json=shared \
    --with-ldap=shared \
    --with-ldap-sasl=%{_usr} \
    --with-libedit=shared,%{_usr} \
%if %{build_firebird}
    --with-interbase=shared \
%endif
    --with-mysql-sock=%{_localstatedir}/run/mysql/mysql.sock \
    --with-mysqli=shared,mysqlnd \
    --with-unixODBC=shared,%{_usr} \
    --with-openssl=shared \
    --with-pgsql=shared,%{_usr} \
    --enable-phar=shared \
    --with-enchant=shared,%{_usr} \
    --with-snmp=shared \
    --with-xmlrpc=shared \
    --enable-xmlreader=shared \
    --enable-xmlwriter=shared \
    --with-xsl=shared \
    --with-tidy=shared,%{_usr} \
    --enable-dba=shared \
    --with-db4=%{_usr} \
    --with-lmdb=%{_usr} \
    --without-gdbm \
    --with-cdb \
    --enable-pdo=shared \
    --with-pdo_sqlite=shared,%{_usr} \
    --with-sqlite3=shared,%{_usr} \
    --with-pdo-mysql=shared,mysqlnd \
%if %{build_firebird}
    --with-pdo-firebird=shared \
%endif
    --with-pdo-pgsql=shared,%{_usr} \
    --with-pdo-odbc=shared,unixODBC,%{_usr} \
    --enable-zip=shared \
    --enable-intl=shared,%{_usr} \
    --disable-cgi

%check
%if %{asan_build}
# ASAN needs /proc to be mounted
exit 0
%endif
pushd build-cli
# check if we link against system libcrypt
if [ -z "$(ldd sapi/cli/php | grep libcrypt.so)" ]; then
    echo 'php does not link against system libcrypt.'
    exit 1
fi

# check if we link against system libgd
%if %{system_gd}
if [ -z "$(ldd modules/gd.so | grep libgd.so)" ]; then
    echo 'php-gd does not link against system libgd.'
    exit 1
fi
%endif

# Run tests, using the CLI SAPI
%if %{with make_test}
export NO_INTERACTION=1 REPORT_EXIT_STATUS=1 LANG=POSIX LC_ALL=POSIX
unset TZ
# We save results for further investigation for QA
make test | tee testresults.txt || true
set +x
for f in `find .. -name "*.diff" -type f -print`; do
    echo "TEST FAILURE: $f --"
    cat "$f"
    echo "-- $f result ends."
done
set -x
unset NO_INTERACTION REPORT_EXIT_STATUS
%endif
popd
# apache module tests
%apache_rex_check -m build-apache2/libs -b build-fpm/sapi/fpm mod_php-basic mod_proxy_fcgi-php-fpm mod_proxy_fcgi-php-fpm-auth-RewriteRule mod_proxy_fcgi-php-fpm-CGIPassAuth

%install
export PHP_PEAR_METADATA_DIR=%{peardir}
export PHP_PEAR_CACHE_DIR=%{_localstatedir}/cache/pear

# install function
Install()
{
    pushd build-$1
    make install INSTALL_ROOT=%{buildroot} PHP_PEAR_PHP_BIN=%{_bindir}/php
    popd
}

# do the actual installation
Install apache2
Install fastcgi
Install cli
Install fpm
Install embed
rm %{buildroot}%{_libdir}/libphp7.la

# generate php.ini from php.ini-production:
install -dm 755 %{buildroot}/%{php_sysconf}/conf.d
install -dm 755 %{buildroot}/%{php_sysconf}/apache2
install -dm 755 %{buildroot}/%{php_sysconf}/cli
install -dm 755 %{buildroot}/%{php_sysconf}/fastcgi
install -dm 755 %{buildroot}/%{php_sysconf}/fpm
sed "s=@extdir@=%{extension_dir}=" php.ini-production > %{buildroot}/%{php_sysconf}/apache2/php.ini
sed "s=@extdir@=%{extension_dir}=" php.ini-production | sed -r 's/^(html_errors|implicit_flush|max_execution_time|register_argc_argv)/;\1/' > %{buildroot}/%{php_sysconf}/cli/php.ini
sed "s=@extdir@=%{extension_dir}=" php.ini-production > %{buildroot}/%{php_sysconf}/fastcgi/php.ini

# prepare configuration files for each extension
extern_modules=""
for f in %{buildroot}%{extension_dir}/*; do
    if test ${f##*.} = a; then
        rm $f
        continue
    fi
    if test ${f##*.} = so; then
        f=${f%.so}
    fi
    ext=${f##*/}
    extern_modules="$extern_modules $ext"
    echo "; comment out next line to disable $ext extension in php" > %{buildroot}/%{php_sysconf}/conf.d/$ext.ini
    zend_=''
    if [ $ext == "opcache" ]; then
      # https://secure.php.net/manual/en/opcache.installation.php
      zend_='zend_'
    fi
    echo "${zend_}extension=$ext.so" >> %{buildroot}/%{php_sysconf}/conf.d/$ext.ini
done
# list of builtin modules
builtin_modules=`./build-cli/sapi/cli/php -m | grep -E -v '^(\[.*)?$' | sort | tr '\n' ' '`
# update readme
sed "s=@EXTERN_MODULES@=$extern_modules=;s=@BUILTIN_MODULES@=$builtin_modules=" php-suse-addons/README.SUSE > README.SUSE
# apache configuration
mkdir -p %{buildroot}%{apache_sysconfdir}/conf.d
install -m 644 php-suse-addons/sysconfig.apache2 %{buildroot}/%{apache_sysconfdir}/conf.d/%{pkg_name}.conf
# directory for sessions
install -d %{buildroot}%{_localstatedir}/lib/%{pkg_name}
# documentation
mv sapi/cli/README README.CLI
mv sapi/cgi/README.FastCGI README.FastCGI
rm -rf %{buildroot}/{.channels,.depdb*,.filemap,.lock,usr/bin/peardev}
install -dm 0755 %{buildroot}/%{peardir}/test
# for pear cache and XML files
install -dm 0755 %{buildroot}%{_localstatedir}/{cache,lib}/pear
# provide compat symlink
mkdir -p %{buildroot}/srv/www/cgi-bin
ln -s %{_bindir}/php-cgi %{buildroot}/srv/www/cgi-bin/php
#fix symlink
sed -i -e "s@%{_builddir}/php-%{rversion}/build-cli/sapi/cli/php@php@g" %{buildroot}%{_bindir}/phar.phar
rm %{buildroot}%{_bindir}/phar
# bnc#734176
ln -s %{_bindir}/php %{buildroot}%{_bindir}/php7
ln -sf %{_bindir}/phar.phar %{buildroot}%{_bindir}/phar
# Install the macros file:
install -d %{buildroot}%{_sysconfdir}/rpm
sed -e "s/@PHP_APIVER@/%{apiver}/;s/@PHP_ZENDVER@/%{zendver}/" < $RPM_SOURCE_DIR/macros.php > macros.php
install -m 644 -c macros.php %{buildroot}%{_sysconfdir}/rpm/macros.php
#install fpm init script.
install -D -m 0644 ./build-fpm/sapi/fpm/php-fpm.service %{buildroot}%{_unitdir}/php-fpm.service
ln -s service %{buildroot}%{_sbindir}/rcphp-fpm

%post -n apache2-mod_php7
#some distro versions does not have this tool.
if [ -x %{_sbindir}/a2enmod ]; then
    if a2enmod -q php5 && ! a2enmod -q php7; then
        a2dismod php5
        a2enmod php7
    fi
fi

%preun -n apache2-mod_php7
if [ "$1" = "0" ]; then
    if [ -x %{_sbindir}/a2enmod ]; then
        if a2enmod -q php7; then
            a2dismod php7
        fi
    fi
fi

%pre fpm
%service_add_pre php-fpm.service

%postun fpm
%service_del_postun php-fpm.service

%preun fpm
%service_del_preun php-fpm.service

%post fpm
%service_add_post php-fpm.service

%post embed -p /sbin/ldconfig
%postun embed -p /sbin/ldconfig

%postun -n apache2-mod_php7
# request restart apache instanaces (which loaded php7) after apache2-mod_php7 package update
if [ $1 -eq 1 ]; then
  %apache_request_restart -m php7
fi

%posttrans -n apache2-mod_php7
# restart apache instances which have this module after zypper or rpm transaction, if not
# have restarted already in other posttrans
%apache_restart_if_needed

%files
%defattr(-, root, root)
%license LICENSE
%doc README* CODING_STANDARDS CREDITS EXTENSIONS NEWS UPGRADING
%doc php-suse-addons/test.php5
%{_mandir}/man1/*
%dir %{php_sysconf}
%dir %{php_sysconf}/conf.d
%dir %{php_sysconf}/cli
%config(noreplace) %{php_sysconf}/cli/php.ini
%{_bindir}/php
%{_bindir}/php7
%dir %{_libdir}/%{pkg_name}
%dir %{extension_dir}
%dir %{_datadir}/%{pkg_name}
%attr(0755, wwwrun, root) %dir %{_localstatedir}/lib/%{pkg_name}

%files devel
%defattr(-, root, root)
%doc README.macros
%{_includedir}/%{pkg_name}
%{_bindir}/phpize
%{_bindir}/php-config
%{_bindir}/pecl
%{_datadir}/%{pkg_name}/build
%config %{_sysconfdir}/rpm/macros.php

%if %{with make_test}
%files testresults
%defattr(-, root, root)
%doc build-cli/testresults.txt
%endif

%files pear
%defattr(-, root, root)
%{_bindir}/pear
%config(noreplace) %{php_sysconf}/cli/pear.conf
%{peardir}
%dir %{_localstatedir}/cache/pear
%dir %{_localstatedir}/lib/pear

%files fastcgi
%defattr(-, root, root)
%{_bindir}/php-cgi
/srv/www/cgi-bin/php
%dir %{php_sysconf}/fastcgi
%config(noreplace) %{php_sysconf}/fastcgi/php.ini

%files fpm
%defattr(-, root, root)
%{_sbindir}/php-fpm
%dir %{php_sysconf}/fpm
%config %{php_sysconf}/fpm/php-fpm.conf.default
%dir %{php_sysconf}/fpm/php-fpm.d
%config %{php_sysconf}/fpm/php-fpm.d/www.conf.default
%{_mandir}/man8/php-fpm.8.gz
%{_sbindir}/rcphp-fpm
%dir %{_datadir}/%{pkg_name}/fpm
%{_datadir}/%{pkg_name}/fpm/status.html
%{_unitdir}/php-fpm.service

%files embed
%defattr(-, root, root)
%{_libdir}/libphp7.so

%files -n apache2-mod_php7
%defattr(-,root,root)
%{apache_libexecdir}/mod_php7.so
%dir %{php_sysconf}/apache2
%config(noreplace) %{php_sysconf}/apache2/php.ini
%config(noreplace) %{apache_sysconfdir}/conf.d/%{pkg_name}.conf

%files bcmath
%defattr(644,root,root,755)
%{extension_dir}/bcmath.so
%config(noreplace) %{php_sysconf}/conf.d/bcmath.ini

%files bz2
%defattr(644,root,root,755)
%{extension_dir}/bz2.so
%config(noreplace) %{php_sysconf}/conf.d/bz2.ini

%files calendar
%defattr(644,root,root,755)
%{extension_dir}/calendar.so
%config(noreplace) %{php_sysconf}/conf.d/calendar.ini

%files ctype
%defattr(644,root,root,755)
%{extension_dir}/ctype.so
%config(noreplace) %{php_sysconf}/conf.d/ctype.ini

%files curl
%defattr(644,root,root,755)
%{extension_dir}/curl.so
%config(noreplace) %{php_sysconf}/conf.d/curl.ini

%files dba
%defattr(644,root,root,755)
%{extension_dir}/dba.so
%config(noreplace) %{php_sysconf}/conf.d/dba.ini

%files dom
%defattr(644,root,root,755)
%{extension_dir}/dom.so
%config(noreplace) %{php_sysconf}/conf.d/dom.ini

%files enchant
%defattr(644,root,root,755)
%{extension_dir}/enchant.so
%config(noreplace) %{php_sysconf}/conf.d/enchant.ini

%files exif
%defattr(644,root,root,755)
%{extension_dir}/exif.so
%config(noreplace) %{php_sysconf}/conf.d/exif.ini

%files fileinfo
%defattr(644,root,root,755)
%{extension_dir}/fileinfo.so
%config(noreplace) %{php_sysconf}/conf.d/fileinfo.ini

%files ftp
%defattr(644,root,root,755)
%{extension_dir}/ftp.so
%config(noreplace) %{php_sysconf}/conf.d/ftp.ini

%files gd
%defattr(644,root,root,755)
%{extension_dir}/gd.so
%config(noreplace) %{php_sysconf}/conf.d/gd.ini

%files gettext
%defattr(644,root,root,755)
%{extension_dir}/gettext.so
%config(noreplace) %{php_sysconf}/conf.d/gettext.ini

%files gmp
%defattr(644,root,root,755)
%{extension_dir}/gmp.so
%config(noreplace) %{php_sysconf}/conf.d/gmp.ini

%files iconv
%defattr(644,root,root,755)
%{extension_dir}/iconv.so
%config(noreplace) %{php_sysconf}/conf.d/iconv.ini

%files intl
%defattr(644,root,root,755)
%{extension_dir}/intl.so
%config(noreplace) %{php_sysconf}/conf.d/intl.ini

%files json
%defattr(644,root,root,755)
%{extension_dir}/json.so
%config(noreplace) %{php_sysconf}/conf.d/json.ini

%files ldap
%defattr(644,root,root,755)
%{extension_dir}/ldap.so
%config(noreplace) %{php_sysconf}/conf.d/ldap.ini

%files mbstring
%defattr(644,root,root,755)
%{extension_dir}/mbstring.so
%config(noreplace) %{php_sysconf}/conf.d/mbstring.ini

%files mysql
%defattr(644,root,root,755)
%{extension_dir}/mysqli.so
%config(noreplace) %{php_sysconf}/conf.d/mysqli.ini
%{extension_dir}/pdo_mysql.so
%config(noreplace) %{php_sysconf}/conf.d/pdo_mysql.ini

%if %{build_firebird}
%files firebird
%defattr(644,root,root,755)
%{extension_dir}/interbase.so
%config(noreplace) %{php_sysconf}/conf.d/interbase.ini
%{extension_dir}/pdo_firebird.so
%config(noreplace) %{php_sysconf}/conf.d/pdo_firebird.ini
%endif

%files odbc
%defattr(644,root,root,755)
%{extension_dir}/odbc.so
%config(noreplace) %{php_sysconf}/conf.d/odbc.ini
%{extension_dir}/pdo_odbc.so
%config(noreplace) %{php_sysconf}/conf.d/pdo_odbc.ini

%files opcache
%defattr(644,root,root,755)
%{extension_dir}/opcache.so
%config(noreplace) %{php_sysconf}/conf.d/opcache.ini

%files openssl
%defattr(644,root,root,755)
%{extension_dir}/openssl.so
%config(noreplace) %{php_sysconf}/conf.d/openssl.ini

%files phar
%defattr(644,root,root,755)
%{extension_dir}/phar.so
%config(noreplace) %{php_sysconf}/conf.d/phar.ini
%{_bindir}/phar
%{_bindir}/phar.phar

%files pcntl
%defattr(644,root,root,755)
%{extension_dir}/pcntl.so
%config(noreplace) %{php_sysconf}/conf.d/pcntl.ini

%files pdo
%defattr(644,root,root,755)
%{extension_dir}/pdo.so
%config(noreplace) %{php_sysconf}/conf.d/pdo.ini

%files pgsql
%defattr(644,root,root,755)
%{extension_dir}/pgsql.so
%config(noreplace) %{php_sysconf}/conf.d/pgsql.ini
%{extension_dir}/pdo_pgsql.so
%config(noreplace) %{php_sysconf}/conf.d/pdo_pgsql.ini

%files posix
%defattr(644,root,root,755)
%{extension_dir}/posix.so
%config(noreplace) %{php_sysconf}/conf.d/posix.ini

%files readline
%defattr(644,root,root,755)
%{extension_dir}/readline.so
%config(noreplace) %{php_sysconf}/conf.d/readline.ini

%files shmop
%defattr(644,root,root,755)
%{extension_dir}/shmop.so
%config(noreplace) %{php_sysconf}/conf.d/shmop.ini

%files snmp
%defattr(644,root,root,755)
%{extension_dir}/snmp.so
%config(noreplace) %{php_sysconf}/conf.d/snmp.ini

%files soap
%defattr(644,root,root,755)
%{extension_dir}/soap.so
%config(noreplace) %{php_sysconf}/conf.d/soap.ini

%if %{build_sodium}
%files sodium
%defattr(644,root,root,755)
%{extension_dir}/sodium.so
%config(noreplace) %{php_sysconf}/conf.d/sodium.ini
%endif

%files sockets
%defattr(644,root,root,755)
%{extension_dir}/sockets.so
%config(noreplace) %{php_sysconf}/conf.d/sockets.ini

%files sqlite
%defattr(644,root,root,755)
%{extension_dir}/pdo_sqlite.so
%config(noreplace) %{php_sysconf}/conf.d/pdo_sqlite.ini
%{extension_dir}/sqlite3.so
%config(noreplace) %{php_sysconf}/conf.d/sqlite3.ini

%files sysvmsg
%defattr(644,root,root,755)
%{extension_dir}/sysvmsg.so
%config(noreplace) %{php_sysconf}/conf.d/sysvmsg.ini

%files sysvsem
%defattr(644,root,root,755)
%{extension_dir}/sysvsem.so
%config(noreplace) %{php_sysconf}/conf.d/sysvsem.ini

%files sysvshm
%defattr(644,root,root,755)
%{extension_dir}/sysvshm.so
%config(noreplace) %{php_sysconf}/conf.d/sysvshm.ini

%files tidy
%defattr(644,root,root,755)
%{extension_dir}/tidy.so
%config(noreplace) %{php_sysconf}/conf.d/tidy.ini

%files tokenizer
%defattr(644,root,root,755)
%{extension_dir}/tokenizer.so
%config(noreplace) %{php_sysconf}/conf.d/tokenizer.ini

%files wddx
%defattr(644,root,root,755)
%{extension_dir}/wddx.so
%config(noreplace) %{php_sysconf}/conf.d/wddx.ini

%files xmlrpc
%defattr(644,root,root,755)
%{extension_dir}/xmlrpc.so
%config(noreplace) %{php_sysconf}/conf.d/xmlrpc.ini

%files xmlreader
%defattr(644,root,root,755)
%{extension_dir}/xmlreader.so
%config(noreplace) %{php_sysconf}/conf.d/xmlreader.ini

%files xmlwriter
%defattr(644,root,root,755)
%{extension_dir}/xmlwriter.so
%config(noreplace) %{php_sysconf}/conf.d/xmlwriter.ini

%files xsl
%defattr(644,root,root,755)
%{extension_dir}/xsl.so
%config(noreplace) %{php_sysconf}/conf.d/xsl.ini

%files zip
%defattr(644,root,root,755)
%{extension_dir}/zip.so
%config(noreplace) %{php_sysconf}/conf.d/zip.ini

%files zlib
%defattr(644,root,root,755)
%{extension_dir}/zlib.so
%config(noreplace) %{php_sysconf}/conf.d/zlib.ini

%changelog
