#
# Conditional build:
%bcond_without	dotnet	# without .net support
#
%ifarch i386 alpha sparc sparc64
%undefine	with_dotnet
%endif
%{?with_dotnet:	%include	/usr/lib/rpm/macros.mono}
Summary:	GMIME library
Summary(pl):	Biblioteka GMIME
Name:		gmime
Version:	2.1.19
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	http://spruce.sourceforge.net/gmime/sources/v2.1/gmime-%{version}.tar.gz
# Source0-md5:	81475ea1a2074a3c402e31651ea357df
Patch0:		%{name}-link.patch
URL:		http://spruce.sourceforge.net/gmime/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.11.4
# disabled by default, broken and very incomplete
#BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
%if %{with dotnet}
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.8.2
BuildRequires:	mono-csharp >= 1.1.0
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library allows you to manipulate MIME messages.

%description -l pl
Ta biblioteka pozwala na manipulowanie wiadomo�ciami MIME.

%package devel
Summary:	Header files to develop libgmime applications
Summary(pl):	Pliki nag��wkowe do tworzenia program�w z u�yciem libgmime
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.11.4
Requires:	gtk-doc-common
Requires:	zlib-devel

%description devel
Header files develop libgmime applications.

%description devel -l pl
Pliki nag��wkowe do tworzenia program�w z u�yciem libgmime.

%package static
Summary:	Static gmime library
Summary(pl):	Statyczna biblioteka gmime
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gmime library.

%description static -l pl
Statyczna biblioteka gmime.

%package -n dotnet-gmime-sharp
Summary:	.NET language bindings for gmime
Summary(pl):	Wi�zania gmime dla .NET
Group:		Development/Libraries
Requires:	dotnet-gtk-sharp2 >= 2.8.2
Requires:	mono >= 1.1.13.8
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n dotnet-gmime-sharp
.NET language bindings for gmime

%description -n dotnet-gmime-sharp -l pl
Wi�zania gmime dla .NET

%package -n dotnet-gmime-sharp-devel
Summary:	Development part of dotnet-gmime-sharp
Summary(pl):	Cz�� dla programist�w dotnet-gmime-sharp
Group:		Development/Libraries
Requires:	dotnet-%{name}-sharp = %{epoch}:%{version}-%{release}

%description -n dotnet-gmime-sharp-devel
Development part of dotnet-gmime-sharp

%description -n dotnet-gmime-sharp-devel -l pl
Cz�� dla programist�w dotnet-gmime-sharp

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-ipv6 \
	--%{?with_dotnet:enable}%{!?with_dotnet:disable}-mono \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir}

rm -f $RPM_BUILD_ROOT%{_bindir}/uu{de,en}code

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%if %{with dotnet}
%files -n dotnet-gmime-sharp
%defattr(644,root,root,755)
%dir %{_prefix}/lib/mono/gac/gmime-sharp
%{_prefix}/lib/mono/gac/gmime-sharp

%files -n dotnet-gmime-sharp-devel
%defattr(644,root,root,755)
%{_datadir}/gapi-2.0/*
%{_prefix}/lib/mono/gmime-sharp
%{_pkgconfigdir}/gmime-sharp.pc
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gmime-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_pkgconfigdir}/gmime-2.0.pc
%{_includedir}/gmime-2.0
%{_gtkdocdir}/gmime

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
