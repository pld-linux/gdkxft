#
# Conditional build:
%bcond_without	gnome		# without capplet subpackage (which require GNOME libs to build)
#
%include	/usr/lib/rpm/macros.perl
Summary:	Adapt GTK-1.2 to support xft fonts
Summary(pl):	Wsparcie dla fontów xft dla GTK-1.2
Summary(pt_BR):	Adapta o GTK-1.2 para suportar fontes xft
Name:		gdkxft
Version:	1.5
Release:	12
License:	LGPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/gdkxft/%{name}-%{version}.tar.gz
# Source0-md5:	ed594e24cf2aefe7a71f96425c1922e8
URL:		http://gdkxft.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_gnome:BuildRequires:	control-center1-devel}
BuildRequires:	freetype-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	help2man
%{?with_gnome:BuildRequires:	libglade-gnome-devel}
BuildRequires:	libtool
BuildRequires:	rpm-perlprov
Requires(post):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library that adds transparent support for anti-aliased fonts to the
libgdk component of gtk+-1.2.x. GTK+ widgets will automagically use
the fonts.

%description -l pl
Biblioteka dodaj±ca przezroczyst± obs³ugê dla wyg³adzanych fontów w
komponencie libgdk biblioteki gtk+-1.2.x. Widgety GTK+ automatycznie
bêd± u¿ywa³y tych fontów.

%description -l pt_BR
Este pacote contém bibliotecas para adicionar suporte transparente a
fontes anti-aliased para o componente libgdk do gtk+-1.2. Os widgets
GTK+ vão automaticamente usar essas fontes.

%package devel
Summary:	Header files for developing apps
Summary(es):	Bibliotecas y archivos de inclusión para desarrollo
Summary(pl):	Pliki nag³owkowe gdkxft
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para desenvolvimento
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

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
%if %{without gnome}
cat >> acinclude.m4 <<EOF
AC_DEFUN([AM_PATH_LIBGLADE],[
AM_CONDITIONAL([HAVE_ORBIT],false)
AM_CONDITIONAL([HAVE_GNORBA],false)])
EOF
%endif
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	CFLAGS="%{rpmcflags} -I%{_includedir}/freetype2" \
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

%{__perl} -pi -e "s@\\\`gtk-config --prefix\\\` \\|\\| \"/usr\"@\"`gtk-config --prefix`\"@g" \
	$RPM_BUILD_ROOT%{_sbindir}/gdkxft_sysinstall

> $RPM_BUILD_ROOT/etc/X11/xinit/xinitrc.d/gdkxft
> $RPM_BUILD_ROOT%{_datadir}/themes/Gdkxft/gtk/gtkrc

%if %{with gnome}
install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings/GNOME
mv -f	$RPM_BUILD_ROOT%{_datadir}/gnome/apps/Settings/UIOptions \
	$RPM_BUILD_ROOT%{_applnkdir}/Settings/GNOME
%endif

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
%doc AUTHORS ChangeLog NEWS README
%dir %{_datadir}/themes/Gdkxft
%dir %{_datadir}/themes/Gdkxft/gtk
%ghost %{_datadir}/themes/Gdkxft/gtk/gtkrc
%attr(755,root,root) %ghost /etc/X11/xinit/xinitrc.d/gdkxft
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gdkxft.conf
%attr(755,root,root) %{_sbindir}/gdkxft_sysinstall
%attr(755,root,root) %{_libdir}/libgdkxft.so.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libgdkxft.la
%attr(755,root,root) %{_libdir}/libgdkxft.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libgdkxft.a

%if %{with gnome}
%files capplet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-capplet
%{_datadir}/gdkxft-capplet.glade
%{_datadir}/control-center/UIOptions/gdkxft.desktop
%{_pixmapsdir}/gdkxft.png
%{_applnkdir}/Settings/GNOME/UIOptions/gdkxft.desktop
%endif
