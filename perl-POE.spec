#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
Summary:	POE - multitasking and networking framework for perl
#Summary(pl):	
Name:		perl-POE
Version:	0.26
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	e9affcb6facdd14a8f3c8791da9dce35
URL:		http://poe.perl.org/
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{!?_without_tests:1}0
BuildRequires:	perl(Filter::Util::Call) >= 1.04
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-Curses
BuildRequires:	perl-Event
BuildRequires:	perl-IO-Tty
BuildRequires:	perl-Storable
BuildRequires:	perl-Term-ReadKey
BuildRequires:	perl-Time-HiRes
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_noautoreq	perl(Curses) perl(HTTP::Date) perl(HTTP::Request) perl(HTTP::Response) perl(HTTP::Status) perl(URI) perl(Term::Cap) perl(Term::ReadKey)

%description
POE is an acronym of "Perl Object Environment".  It's a networking
and multitasking (some say cooperative threading) framework for Perl.
It has been in active development since 1996, with its first open
release in 1998.  O'Reilly's Perl Conference (now OSCON) named POE
"Best New Module" in 1999.

POE has been used in mission-critical systems such as internetworked
financial markets, file systems, commerce and application servers.
It has been used in projects ranging from a few lines of code to tens
of thousands.

POE is compatible with perl versions as old as 5.005_03.

POE includes an evolving component framework.  Components are high-level,
modular, reusable pieces of programs.  Several components have been
published on the CPAN, and more are listed on POE's web site.

POE includes components and libraries for making quick work of network
clients, servers, and peers.  A simple stand-alone web application takes
about 30 lines of code, most of which is your own custom logic.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	--default
%{__make}

%if %{!?_without_tests:1}0
%{__chmod} 000 t/06_tk.t t/21_gtk.t
%{__make} test
%endif

install -d $RPM_BUILD_ROOT%{perl_vendorlib}/POE/Component/CD

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -r samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES NEEDS README TODO
%{perl_vendorlib}/%{pdir}
%{_mandir}/man3/*
