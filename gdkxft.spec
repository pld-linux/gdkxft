Summary:	Adapt GTK-1.2 to support xft fonts
Name:		gdkxft
Version:	1.0
Release:	1
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/Библиотеки
Group(uk):	X11/Б╕бл╕отеки
Source0:	http://philrsss.anu.edu.au/~josh/gdkxft/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
URL:		http://philrsss.anu.edu.au/~josh/gdkxft/
Requires:	gtk+
%define prefix   /usr/X11R6

%description 
A library that adds transparent support for anti-aliased fonts to the
libgdk component of gtk+-1.2.x. Gtk+ widgets will automagically use
the fonts.

%prep
%setup -q

%build
./configure --prefix=%prefix
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{prefix}/bin/gdkxft_sysinstall

%preun
%{prefix}/bin/gdkxft_sysinstall -u

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%config %{_datadir}/gdkxft.conf
%{_libdir}/libgdkxft.*
%attr(755,root,root) %{_bindir}/gdkxft_sysinstall
