#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
Summary:	POE - multitasking and networking framework for Perl
Summary(pl):	POE - wielozadaniowe i sieciowe �rodowisko dla Perla
Name:		perl-POE
Version:	0.2802
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	fd27e0e25dd77d6a19dff7cdce0160de
URL:		http://poe.perl.org/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
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

%description -l pl
POE to skr�t od "Perl Object Environment" (co oznacza "�rodowisko
obiektowe Perla"). Jest to szkielet obs�ugi sieci i wielozadaniowo�ci
(nazywanej przez niekt�rych "kooperatywnym w�tkowaniem") dla Perla.
Jest aktywnie rozwijane od 1996 roku, a pierwsze publiczne wydanie
by�o w 1998 roku. Na O'Reilly's Perl Conference (teraz OSCON) w 1999
roku POE zosta�o nazwane "Najlepszym nowym modu�em".

POE jest u�ywane w systemach mission-critical, takich jak
mi�dzysieciowe rynki finansowe, systemy plik�w, serwery aplikacji i
handlowe. Jest u�ywane w projektach o rozmiarach od kilku linii do
dziesi�tek tysi�cy.

POE jest kompatybilne z Perlem od wersji 5.005_03.

POE zawiera rozwijaj�cy si� szkielet komponent�w. Komponenty to
wysokopoziomowe, modularne, daj�ce si� wielokrotnie wykorzystywa�
kawa�ki program�w. Cz�� komponent�w zosta�a opublikowana w CPAN,
wi�cej mo�na znale�� na stronie WWW POE.

POE zawiera komponenty i biblioteki do szybkiego tworzenia klient�w,
serwer�w i partner�w sieciowych. Prosta, samodzielna aplikacja WWW
zajmuje oko�o 30 linii kodu, z kt�rych wi�kszo�� to w�a�ciwa logika.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	--default
%{__make}

%if %{with tests}
%{__chmod} 000 t/06_tk.t t/21_gtk.t
%{__make} test
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/POE/Component/CD

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -r samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES NEEDS README TODO
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/%{pdir}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
