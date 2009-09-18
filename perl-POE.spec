#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
Summary:	POE - multitasking and networking framework for Perl
Summary(pl.UTF-8):	POE - wielozadaniowe i sieciowe środowisko dla Perla
Name:		perl-POE
Version:	1.268
Release:	1
Epoch:		2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/POE/%{pdir}-%{version}.tar.gz
# Source0-md5:	e5290beba4884064da68320dc46bf296
URL:		http://poe.perl.org/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Test-Simple >= 0.54
%if %{with tests}
BuildRequires:	perl(Filter::Util::Call) >= 1.04
BuildRequires:	perl-IO-Compress
BuildRequires:	perl-Curses
BuildRequires:	perl-Event
BuildRequires:	perl-IO-Tty >= 1.08
BuildRequires:	perl-Socket6 >= 0.14
BuildRequires:	perl-Storable >= 2.12
BuildRequires:	perl-Term-ReadKey >= 2.21
BuildRequires:	perl-Time-HiRes >= 1.59
BuildRequires:	perl-URI >= 1.30
BuildRequires:	perl-libwww
%endif
Conflicts:	perl-POE-Filter-XML < 0.29
Obsoletes:	perl-POE-Exceptions
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_noautoreq	perl(Curses) perl(HTTP::Date) perl(HTTP::Request) perl(HTTP::Response) perl(HTTP::Status) perl(URI) perl(Term::Cap) perl(Term::ReadKey) perl(Tk)

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

%description -l pl.UTF-8
POE to skrót od "Perl Object Environment" (co oznacza "środowisko
obiektowe Perla"). Jest to szkielet obsługi sieci i wielozadaniowości
(nazywanej przez niektórych "kooperatywnym wątkowaniem") dla Perla.
Jest aktywnie rozwijane od 1996 roku, a pierwsze publiczne wydanie
było w 1998 roku. Na O'Reilly's Perl Conference (teraz OSCON) w 1999
roku POE zostało nazwane "Najlepszym nowym modułem".

POE jest używane w systemach mission-critical, takich jak
międzysieciowe rynki finansowe, systemy plików, serwery aplikacji i
handlowe. Jest używane w projektach o rozmiarach od kilku linii do
dziesiątek tysięcy.

POE jest kompatybilne z Perlem od wersji 5.005_03.

POE zawiera rozwijający się szkielet komponentów. Komponenty to
wysokopoziomowe, modularne, dające się wielokrotnie wykorzystywać
kawałki programów. Część komponentów została opublikowana w CPAN,
więcej można znaleźć na stronie WWW POE.

POE zawiera komponenty i biblioteki do szybkiego tworzenia klientów,
serwerów i partnerów sieciowych. Prosta, samodzielna aplikacja WWW
zajmuje około 30 linii kodu, z których większość to właściwa logika.

%prep
%setup -q -n %{pdir}-%{version}
rm -f lib/POE/Filter/HTTPD.pm{~.orig}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	--default
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/POE/{Component/CD,Session}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -r examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES HISTORY README TODO
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/POE
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/README*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.perl
%{_mandir}/man3/*
