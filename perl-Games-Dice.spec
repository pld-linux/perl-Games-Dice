#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Games
%define		pnam	Dice
Summary:	Games::Dice Perl module - a set of dice for rolling
Summary(pl.UTF-8):	Moduł Perla Games::Dice - zbiór kości do rzucania
Name:		perl-Games-Dice
Version:	0.99_01
Release:	0.1
# "same as perl"
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Games/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	550794c12e2aaec2b2940e8c7fc331d8
URL:		http://search.cpan.org/dist/Games-Dice/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Class-Container
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Games::Dice object represents a set of dice, which are represented
by Games::Dice objects. A set of dice can be rolled, and returns a
Games::Dice::Results object. The default behavior of dice and dice
sets is simple, but can easily be augmented with subclassing.

%description -l pl.UTF-8
Obiekt Games::Dice reprezentuje zbiór kości do gry reprezentowanych
przez obiekty Games::Dice. Mogą one być rzucone, zwracają wtedy obiekt
Games::Dice::Results. Domyślne zachowanie kości jest proste, ale może
być łatwo rozszerzone przez podklasy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Games/Dice.pm
%{perl_vendorlib}/Games/Die.pm
%dir %{perl_vendorlib}/Games/Dice
%{perl_vendorlib}/Games/Dice/Result.pm
%{_mandir}/man3/*
