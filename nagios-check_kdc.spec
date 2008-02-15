%define name	nagios-check_kdc
%define version	20050715
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Nagios kdc plugin
Group:		Networking/Other
License:	BSD
URL:		http://www.loveshack.ukfsn.org/nagios/
Source0:	http://www.loveshack.ukfsn.org/nagios/check_kdc
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Check getting tickets from a kerberos KDC using a keytab. Doesn't require Perl
Kerberos stuff (unlike check_krb5), just kinit/kdestroy.

%prep

%build


%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_libdir}/nagios/plugins
install -m 755 %{SOURCE0} %{buildroot}%{_libdir}/nagios/plugins

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_kdc

