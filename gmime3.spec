Summary:	GMIME library
Summary(pl.UTF-8):	Biblioteka GMIME
Name:		gmime3
Version:	3.2.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gmime/3.2/gmime-%{version}.tar.xz
# Source0-md5:	1188d71c9567375b20b9632a0ed85d3f
Patch0:		%{name}-link.patch
Patch1:		%{name}-am.patch
Patch2:		%{name}-missing.patch
URL:		http://spruce.sourceforge.net/gmime/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-utils
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gobject-introspection-devel >= 1.30.0
BuildRequires:	gpgme-devel >= 1:1.6.0
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	libidn2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	glib2 >= 1:2.32.0
Requires:	gpgme >= 1:1.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library allows you to manipulate MIME messages.

%description -l pl.UTF-8
Ta biblioteka pozwala na manipulowanie wiadomościami MIME.

%package devel
Summary:	Header files to develop libgmime applications
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia programów z użyciem libgmime
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.32.0
Requires:	gpgme-devel >= 1:1.6.0
Requires:	libidn2-devel >= 2.0.0
Requires:	zlib-devel

%description devel
Header files develop libgmime applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia programów z użyciem libgmime.

%package static
Summary:	Static gmime library
Summary(pl.UTF-8):	Statyczna biblioteka gmime
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gmime library.

%description static -l pl.UTF-8
Statyczna biblioteka gmime.

%package apidocs
Summary:	gmime library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki gmime
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
gmime library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki gmime.

%package -n vala-gmime3
Summary:	Vala API for gmime library
Summary(pl.UTF-8):	API języka Vala do biblioteki gmime
Group:		Development/Languages
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n vala-gmime3
Vala API for gmime library.

%description -n vala-gmime3 -l pl.UTF-8
API języka Vala do biblioteki gmime.

%prep
%setup -q -n gmime-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-largefile \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir}

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgmime-3.0.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_libdir}/libgmime-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgmime-3.0.so.0
%{_libdir}/girepository-1.0/GMime-3.0.typelib

%files devel
%defattr(644,root,root,755)
%doc PORTING
%attr(755,root,root) %{_libdir}/libgmime-3.0.so
%{_includedir}/gmime-3.0
%{_datadir}/gir-1.0/GMime-3.0.gir
%{_pkgconfigdir}/gmime-3.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgmime-3.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gmime-3.2

%files -n vala-gmime3
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gmime-3.0.deps
%{_datadir}/vala/vapi/gmime-3.0.vapi
