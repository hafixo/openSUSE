#
# spec file for package matrix-synapse
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


# These come from matrix-synapse's CONDITIONAL_REQUIREMENTS.
%bcond_without email_notifs
%bcond_without ldap
%bcond_without postgres
%bcond_without acme
%bcond_without saml
%bcond_without url_preview
%bcond_without jwt
# sentry-sdk isn't packaged on openSUSE.
%bcond_with    sentry

## Package updates
#
# * Update version in _service to the most recent released one
# * Call `osc service dr`
# * Update changelog manually from
#   https://github.com/matrix-org/synapse/releases or synapse/CHANGES.md
# * Commit+submit

# Synapse 1.1.0 and onwards only supports Python >= 3.5.
%define skip_python2 1

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         modname synapse
%define         pkgname matrix-synapse
Name:           %{pkgname}
Version:        1.2.0
Release:        0
Summary:        Matrix protocol reference homeserver
License:        Apache-2.0
Group:          Productivity/Networking/Instant Messenger
URL:            https://github.com/matrix-org/synapse
Source0:        %{pkgname}-%{version}.tar.xz
Source50:       %{pkgname}.service
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module psutil >= 2.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module treq >= 15.1.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  unzip
%{?systemd_requires}
Requires(pre):  shadow
%ifpython3
Requires:       %{python_flavor} >= 3.5
%endif
# NOTE: Keep this is in the same order as synapse/python_dependencie.py.
Requires:       python-Pillow >= 4.3.0
Requires:       python-PyNaCl >= 1.2.1
Requires:       python-PyYAML >= 3.11
Requires:       python-Twisted >= 18.7.0
Requires:       python-attrs >= 17.4.0
Requires:       python-bcrypt >= 3.1.0
Requires:       python-canonicaljson >= 1.1.3
Requires:       python-daemonize >= 2.3.1
Requires:       python-frozendict >= 1
Requires:       python-idna >= 2.5
Requires:       python-jsonschema >= 2.5.1
Requires:       python-msgpack >= 0.5.2
Requires:       python-netaddr >= 0.7.18
Requires:       python-phonenumbers >= 8.2.0
Requires:       python-prometheus_client >= 0.4.0
Requires:       python-psutil >= 2.0.0
Requires:       python-pyOpenSSL >= 16.0.0
Requires:       python-pyasn1 >= 0.1.9
Requires:       python-pyasn1-modules >= 0.0.7
Requires:       python-pymacaroons >= 0.13.0
Requires:       python-service_identity >= 18.1.0
Requires:       python-signedjson >= 1.0.0
Requires:       python-six >= 1.10
Requires:       python-sortedcontainers >= 1.4.4
Requires:       python-treq >= 15.1
Requires:       python-unpaddedbase64 >= 1.1.0
# Specify all CONDITIONAL_REQUIREMENTS (we Require them to avoid no-recommends
# breaking very commonly-used bits of matrix-synapse such as postgresql).
%if %{with email_notifs}
Requires:       python-Jinja2 >= 2.9
Requires:       python-bleach >= 1.4.3
%endif
%if %{with ldap}
Requires:       python-matrix-synapse-ldap3 >= 0.1
%endif
%if %{with postgres}
Requires:       python-psycopg2 >= 2.7
%endif
%if %{with acme}
Requires:       python-txacme >= 0.9.2
%endif
%if %{with saml}
Requires:       python-pysaml2 >= 4.5.0
%endif
%if %{with url_preview}
Requires:       python-lxml >= 3.5.0
%endif
%if %{with sentry}
Requires:       python-sentry-sdk >= 0.7.2
%endif
%if %{with jwt}
Requires:       python-PyJWT >= 1.6.4
%endif
BuildArch:      noarch
Provides:       matrix-synapse = %{version}
# We only provide/obsolete python2 to ensure that users upgrade.
Obsoletes:      python2-matrix-synapse < %{version}
Provides:       python2-matrix-synapse = %{version}

%python_subpackages

%description
Synapse is a Python-based reference "homeserver" implementation of
Matrix. Matrix is a system for federated Instant Messaging and VoIP.

%prep
%setup -q

# Remove all un-needed #!-lines.
find synapse/ -type f -exec sed -i '1{/^#!/d}' {} \;
# Replace all #!/usr/bin/env lines to use #!/usr/bin/$1 directly.
find ./ -type f -exec \
	sed -i '1s|^#!/usr/bin/env |#!/usr/bin/|' {} \;
# Force the usage of python_flavor.
find ./ -type f \
	-exec sed -i '1s|^#!/usr/bin/python$|#!/usr/bin/%{python_flavor}|' {} \;

# Update the python flavour in the service file.
sed -i 's|@PYTHON_FLAVOR@|%{python_flavor}|g' %{S:50}

%build
%python_build

%install
# We install scripts into /usr/lib to avoid silly conflicts with other pkgs.
install -d -m 0755 %{buildroot}%{_libexecdir}/%{pkgname}
%python_install "--install-scripts=%{_libexecdir}/%{pkgname}/"

# While we provide a systemd service, link synctl so it's simpler to use.
install -d -m 0755 %{buildroot}%{_bindir}
ln -s %{_libexecdir}/%{pkgname}/synctl %{buildroot}%{_bindir}/synctl

# Install default matrix-synapse configuration.
# TODO: Switch to the debian default config.
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{pkgname}/conf.d
install -D -m 0644 docs/sample_config.yaml %{buildroot}%{_sysconfdir}/%{pkgname}/homeserver.yaml
install -D -m 0644 contrib/systemd/log_config.yaml %{buildroot}%{_sysconfdir}/%{pkgname}/log.yaml

# Man pages.
install -D -m 0644 -t %{buildroot}%{_mandir}/man1 debian/*.1

# Runtime-dir.
mkdir -p %{buildroot}%{_rundir}/%{pkgname}

# system configuration.
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{pkgname}
install -D -m 0644 contrib/systemd/%{pkgname}.service %{buildroot}%{_unitdir}/%{pkgname}.service

# User directory.
install -d -m 0755 %{buildroot}%{_rundir}/%{pkgname}
install -d -m 0750 %{buildroot}%{_localstatedir}/lib/%{pkgname}

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%pre
getent group synapse >/dev/null || groupadd -r synapse
getent passwd synapse >/dev/null || \
    /usr/sbin/useradd -r -g synapse -s /sbin/nologin -c 'Matrix Synapse' \
        -d %{_localstatedir}/lib/synapse synapse
%service_add_pre %{pkgname}.service

%post
%service_add_post %{pkgname}.service

%preun
%service_del_preun %{pkgname}.service

%postun
%service_del_postun %{pkgname}.service

%if 0%{?suse_version} < 1500
%files -n %{pkgname}
%else
%files %{python_files}
%endif
%defattr(-,root,root,-)
%doc *.rst CHANGES.md
%license LICENSE
%dir %{_sysconfdir}/%{pkgname}
%dir %{_sysconfdir}/%{pkgname}/conf.d
%config(noreplace) %{_sysconfdir}/%{pkgname}/*.yaml
%dir %attr(0750,%{modname},%{modname}) %{_localstatedir}/lib/%{pkgname}
%{python_sitelib}
# Python helper scripts.
%{_bindir}/synctl
%{_libexecdir}/%{pkgname}
# systemd service.
%{_sbindir}/rc%{pkgname}
%{_unitdir}/%{pkgname}.service
# Man pages.
%{_mandir}/man*/*

%changelog
