#
# Conditional build:
# _without_gnome	- without capplet subpackage (which require GNOME libs to build)
#
%include	/usr/lib/rpm/macros.perl
Summary:	Adapt GTK-1.2 to support xft fonts
Summary(pl):	Wsparcie dla fontÛw xft dla GTK-1.2
Summary(pt_BR):	Adapta o GTK-1.2 para suportar fontes xft
Name:		gdkxft
Version:	1.5
Release:	2
License:	LGPL
# Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/gdkxft/%{name}-%{version}.tar.gz
Group:		X11/Libraries
Group(cs):	X11/Knihovny
Group(da):	X11/Biblioteker
Group(de):	X11/Bibliotheken
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(it):	X11/Librerie
Group(ja):	X11/•È•§•÷•È•Í
Group(no):	X11/Biblioteker
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(pt):	X11/Bibliotecas
Group(ru):	X11/‚…¬Ã…œ‘≈À…
Group(sv):	X11/Bibliotek
Group(uk):	X11/‚¶¬Ã¶œ‘≈À…
Source0:	http://prdownloads.sourceforge.net/gdkxft/%{name}-%{version}.tar.gz
%{!?_without_gnome:BuildRequires:	libglade-devel}
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	perl-devel
Prereq:		/sbin/ldconfig
URL:		http://gdkxft.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description 
A library that adds transparent support for anti-aliased fonts to the
libgdk component of gtk+-1.2.x. Gtk+ widgets will automagically use
the fonts.

%description -l pl
Biblioteka dodaj±ca przeºroczyst± obs≥ugÍ dla wyg≥adzanych fontÛw w
komponencie libgdk biblioteki gtk+-1.2.x. Widgety gtk+ automatycznie
bÍd± uøywa≥y tych fontÛw.

%description -l pt_BR
Este pacote contÈm bibliotecas para adicionar suporte transparente a
fontes anti-aliased para o componente libgdk do gtk+-1.2. Os widgets
Gtk+ v„o automaticamente usar essas fontes.

%package devel
Summary:	Header files for developing apps
Summary(es):	Bibliotecas y archivos de inclusiÛn para desarrollo
Summary(pl):	Pliki nag≥owkowe gdkxft
Summary(pt_BR):	Bibliotecas e arquivos de inclus„o para desenvolvimento
Group:		Development/Libraries
Group(cs):	V˝vojovÈ prost¯edky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(it):	Sviluppo/Librerie
Group(ja):	≥´»Ø/•È•§•÷•È•Í
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(sv):	Utveckling/Bibliotek
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
PreReq:		%{name} = %{version}-%{release}

%description devel
Header files for developing apps with will use libgdkxft.

%description devel -l pl
Pliki nag≥Ûwkowe do tworzenia aplikacji uøywaj±cych libgdkxft.

%description devel -l pt_BR
Bibliotecas e arquivos de inclus„o necess·rios para desenvolvimento
baseado na libgdkxft.

%package static
Summary:	Static libraries for libgdkxft development
Summary(pl):	Statyczna biblioteka libgdkxft
Summary(pt_BR):	Bibliotecas est·ticas para desenvolvimento com a libgdkxft
Group:		Development/Libraries
Group(cs):	V˝vojovÈ prost¯edky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(it):	Sviluppo/Librerie
Group(ja):	≥´»Ø/•È•§•÷•È•Í
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(sv):	Utveckling/Bibliotek
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for libgdkxft development.

%description static -l pl
Statyczna biblioteka libgdkxft.

%description static -l pt_BR
Bibliotecas est·ticas para desenvolvimento com a libgdkxft.

%package capplet
Summary:	Capplet to configure gdkxft in GNOME
Summary(pl):	NarzÍdzie do konfiguracji gdkxft w GNOME
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(it):	X11/Applicazioni
Group(ja):	X11/•¢•◊•Í•±°º•∑•Á•Û
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/AplicaÁıes
Group(pt):	X11/AplicaÁıes
Group(ru):	X11/“…Ãœ÷≈Œ…—
Group(sv):	X11/Till‰mpningar
Requires:	%{name} = %{version}

%description capplet
Capplet to configure gdkxft in GNOME.

%description capplet -l pl
NarzÍdzie do konfiguracji gdkxft w GNOME.

%prep
%setup -q

%build
%configure \
	--enable-static \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
gzip -9nf AUTHORS COPYING ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/gdkxft_sysinstall
/sbin/ldconfig

%preun
%{_sbindir}/gdkxft_sysinstall -u

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%config %{_sysconfdir}/gdkxft.conf
%attr(755,root,root) %{_sbindir}/gdkxft_sysinstall
%attr(755,root,root) %{_libdir}/libgdkxft.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdkxft.la
%attr(755,root,root) %{_libdir}/libgdkxft.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libgdkxft.a

%if %{?_without_gnome:0}%{!?_without_gnome:1}
%files capplet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-capplet
%endif
