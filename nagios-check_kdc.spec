%define name	nagios-check_kdc
%define version	20050715
%define release	11

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


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 20050715-10mdv2011.0
+ Revision: 612983
- the mass rebuild of 2010.1 packages

* Fri Apr 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 20050715-9mdv2010.1
+ Revision: 535537
- fix all binary locations, using a substitution rather than a patch

* Fri Apr 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 20050715-8mdv2010.1
+ Revision: 535532
- this is a noarch package

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 20050715-7mdv2010.0
+ Revision: 430146
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 20050715-6mdv2009.0
+ Revision: 268229
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20050715-5mdv2009.0
+ Revision: 196817
- fix kinit path (bug #40307)

* Fri Feb 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20050715-4mdv2008.1
+ Revision: 168932
- fix configuration (thanks oden)

* Fri Feb 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20050715-3mdv2008.1
+ Revision: 168912
- add a configuration file

* Fri Feb 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20050715-2mdv2008.1
+ Revision: 168796
- not a noarch package, as nagios plugins installation directory is arch-dependant

* Tue Feb 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20050715-1mdv2008.1
+ Revision: 162719
- import nagios-check_kdc


* Tue Feb 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20050715-1mdv2008.1
- first mandriva package
