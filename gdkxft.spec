%define ver      1.0
%define  RELEASE 1
%define  rel     %{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}
%define prefix   /usr/X11R6

Summary: Adapt GTK-1.2 to support xft fonts
Name: gdkxft
Version: %ver
Release: %rel
Copyright: LGPL
Group: X11/Libraries
Source: http://philrsss.anu.edu.au/~josh/gdkxft/gdkxft-%{ver}.tar.gz
BuildRoot: /var/tmp/gdkxft-%{PACKAGE_VERSION}-root
Packager: Josh Parsons <josh@philosophy.org.au>
URL: http://philrsss.anu.edu.au/~josh/gdkxft/
Requires: gtk+

%description 
A library that adds transparent support for anti-aliased fonts to the
libgdk component of gtk+-1.2.x.  Gtk+ widgets will automagically use
the fonts.

%prep
%setup

%build
./configure --prefix=%{prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{prefix}/bin/gdkxft_sysinstall

%preun
%{prefix}/bin/gdkxft_sysinstall -u

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%config %{prefix}/share/gdkxft.conf
%{prefix}/lib/libgdkxft.*
%{prefix}/bin/gdkxft_sysinstall
