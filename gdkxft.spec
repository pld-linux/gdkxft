#
# Conditional build:
# _without_gnome	- without capplet subpackage (which require GNOME libs to build)
#
%include	/usr/lib/rpm/macros.perl
Summary:	Adapt GTK-1.2 to support xft fonts
Summary(pl):	Wsparcie dla fontów xft dla GTK-1.2
Summary(pt_BR):	Adapta o GTK-1.2 para suportar fontes xft
Name:		gdkxft
Version:	1.5
Release:	6
License:	LGPL
Group:		X11/Libraries
Source0:	http://prdownloads.sourceforge.net/gdkxft/%{name}-%{version}.tar.gz
%{!?_without_gnome:BuildRequires:	control-center-devel}
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
Biblioteka dodaj±ca prze¼roczyst± obs³ugê dla wyg³adzanych fontów w
komponencie libgdk biblioteki gtk+-1.2.x. Widgety gtk+ automatycznie
bêd± u¿ywa³y tych fontów.

%description -l pt_BR
Este pacote contém bibliotecas para adicionar suporte transparente a
fontes anti-aliased para o componente libgdk do gtk+-1.2. Os widgets
Gtk+ vão automaticamente usar essas fontes.

%package devel
Summary:	Header files for developing apps
Summary(es):	Bibliotecas y archivos de inclusión para desarrollo
Summary(pl):	Pliki nag³owkowe gdkxft
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para desenvolvimento
Group:		Development/Libraries
PreReq:		%{name} = %{version}-%{release}

%description devel
Header files for developing apps with will use libgdkxft.

%description devel -l pl
Pliki nag³ówkowe do tworzenia aplikacji u¿ywaj±cych libgdkxft.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusão necessários para desenvolvimento
baseado na libgdkxft.

%package static
Summary:	Static libraries for libgdkxft development
Summary(pl):	Statyczna biblioteka libgdkxft
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com a libgdkxft
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for libgdkxft development.

%description static -l pl
Statyczna biblioteka libgdkxft.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com a libgdkxft.

%package capplet
Summary:	Capplet to configure gdkxft in GNOME
Summary(pl):	Narzêdzie do konfiguracji gdkxft w GNOME
Group:		X11/Applications
Requires:	%{name} = %{version}

%description capplet
Capplet to configure gdkxft in GNOME.

%description capplet -l pl
Narzêdzie do konfiguracji gdkxft w GNOME.

%prep
%setup -q

%build
%configure \
	--enable-static \
	--enable-shared

sed -e s:capplet-widget.h:libcapplet1/capplet-widget.h: capplet/gdkxft-capplet.c > capplet/gdkxft-capplet.tmp
mv -f capplet/gdkxft-capplet.tmp capplet/gdkxft-capplet.c

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/X11/xinit/xinitrc.d,%{_datadir}/themes/Gdkxft/gtk}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

> $RPM_BUILD_ROOT/etc/X11/xinit/xinitrc.d/gdkxft
> $RPM_BUILD_ROOT%{_datadir}/themes/Gdkxft/gtk/gtkrc

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/gdkxft_sysinstall
/sbin/ldconfig

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/gdkxft_sysinstall -u
fi

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{_datadir}/themes/Gdkxft
%dir %{_datadir}/themes/Gdkxft/gtk
%ghost %{_datadir}/themes/Gdkxft/gtk/gtkrc
%attr(755,root,root) %ghost /etc/X11/xinit/xinitrc.d/gdkxft
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/gdkxft.conf
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
%{_datadir}/gdkxft-capplet.glade
%{_datadir}/pixmaps/gdkxft.png
%{_datadir}/control-center/UIOptions/gdkxft.desktop
%{_datadir}/gnome/apps/Settings/UIOptions/gdkxft.desktop
%endif
