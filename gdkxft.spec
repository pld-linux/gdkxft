%include	/usr/lib/rpm/macros.perl
Summary:	Adapt GTK-1.2 to support xft fonts
Summary(pl):	Wsparcie dla font�w xft dla GTK-1.2
Summary(pt_BR):	Adapta o GTK-1.2 para suportar fontes xft
Name:		gdkxft
Version:	1.5
Release:	1
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Bibliotheken
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(pt):	X11/Bibliotecas
Group(ru):	X11/����������
Group(uk):	X11/��̦�����
# Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/gdkxft/%{name}-%{version}.tar.gz
Source0:	http://prdownloads.sourceforge.net/gdkxft/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libglade-devel
BuildRequires:	libtool
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
Biblioteka dodaj�ca prze�roczyst� obs�ug� dla wyg�adzanych font�w w
komponencie libgdk biblioteki gtk+-1.2.x. Widgety gtk+ automatycznie
b�d� u�ywa�y tych font�w.

%description -l pt_BR
Este pacote cont�m bibliotecas para adicionar suporte transparente a
fontes anti-aliased para o componente libgdk do gtk+-1.2. Os widgets
Gtk+ v�o automaticamente usar essas fontes.

%package devel
Summary:	Files and libraries for developing apps
Summary(pt_BR):	Bibliotecas e arquivos de inclus�o para desenvolvimento
Summary(es):	Bibliotecas y archivos de inclusi�n para desarrollo
Group:		Development/Libraries
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
PreReq:		%{name} = %{version}-%{release}

%description devel
Header files and libraries for developing apps with will use
libgdkxft.

%description -l pt_BR devel
Bibliotecas e arquivos de inclus�o necess�rios para desenvolvimento
baseado na libgdkxft.

%package static
Summary:	Static libraries for libgdkxft development
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com a libgdkxft
Group:		Development/Libraries
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for libgdkxft development.

%description -l pt_BR static
Bibliotecas est�ticas para desenvolvimento com a libgdkxft.

%package capplet
Summary:	Capplet to configure gdkxft in GNOME
Summary(pl):	Narz�dzie do konfiguracji gdkxft w GNOME
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Group(ru):	X11/����������
Requires:	%{name} = %{version}

%description capplet
Capplet to configure gdkxft in GNOME.

%description capplet -l pl
Narz�dzie do konfiguracji gdkxft w GNOME.

%prep
%setup -q

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
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

%files capplet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-capplet
