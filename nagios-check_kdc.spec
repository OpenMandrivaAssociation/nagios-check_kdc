%define name	nagios-check_kdc
%define version	20050715
%define release	%mkrel 10

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Nagios kdc plugin
Group:		Networking/Other
License:	BSD
URL:		http://www.loveshack.ukfsn.org/nagios/
Source0:	http://www.loveshack.ukfsn.org/nagios/check_kdc
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Check getting tickets from a kerberos KDC using a keytab. Doesn't require Perl
Kerberos stuff (unlike check_krb5), just kinit/kdestroy.

%prep
%setup -T -c
install -m 755 %{SOURCE0} check_kdc

perl -pi -e 's|/usr/kerberos/bin|%{_bindir}|' check_kdc

%build


%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/nagios/plugins
install -m 755 check_kdc %{buildroot}%{_datadir}/nagios/plugins

install -d -m 755 %{buildroot}%{_sysconfdir}/nagios/plugins.d
cat > %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_kdc.cfg <<'EOF'
define command{
	command_name	check_kdc
	command_line	%{_datadir}/nagios/plugins/check_kdc -H $HOSTADDRESS$
}
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/nagios/plugins/check_kdc
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_kdc.cfg
