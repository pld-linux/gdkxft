%include	/usr/lib/rpm/macros.perl
Summary:	Adapt GTK-1.2 to support xft fonts
Summary(pl):	Wsparcie dla fontów xft dla GTK-1.2
Name:		gdkxft
Version:	1.4
Release:	1
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/gdkxft/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
URL:		http://philrsss.anu.edu.au/~josh/gdkxft/
Prereq:		/sbin/ldconfig
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	XFree86-devel
BuildRequires:	libglade-devel
BuildRequires:	perl-devel
BuildRequires:	gtk+-devel >= 1.2.0

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description 
A library that adds transparent support for anti-aliased fonts to the
libgdk component of gtk+-1.2.x. Gtk+ widgets will automagically use
the fonts.

%description -l pl
Biblioteka dodaj±ca prze¼roczyst± obs³ugê dla wyg³adzanych fontów
w komponencie libgdk biblioteki gtk+-1.2.x. Widgety gtk+ automatycznie
bêd± u¿ywa³y tych fontów.

%prep
%setup -q

%build
rm missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure
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
%{_libdir}/libgdkxft.so*
%{_libdir}/libgdkxft.la
%attr(644,root,root) %{_libdir}/libgdkxft.a
%attr(755,root,root) %{_sbindir}/gdkxft_sysinstall
