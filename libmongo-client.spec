Summary:	Alternative C driver for MongoDB
Summary(pl.UTF-8):	Alternatywny interfejs C do MongoDB
Name:		libmongo-client
Version:	0.1.8
Release:	1
License:	Apache v2.0
Group:		Libraries
Source0:	https://github.com/algernon/libmongo-client/archive/%{name}-%{version}.tar.gz
# Source0-md5:	deef5bdfd48f2542461dd0a0aa34add6
URL:		https://github.com/algernon/libmongo-client
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	libtool >= 2:2.0
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.16.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautocompressdoc	*.h

%description
This is an alternative C driver for MongoDB, with slightly different
goals than the official one: libmongo-client is meant to be a stable
(API, ABI and quality alike), clean, well documented and well tested
shared library, that strives to make the most common use cases as
convenient as possible.

%description -l pl.UTF-8
libmongo-client to alternatywny sterownik (interfejs) C dla MongoDB,
mający nieco inne cele niż oficjalny: libmongo-client ma być stabilną
(zarówno pod kątem API, ABI i jakości), przejrzystą, dobrze
udokumentowaną i dobrze przetestowaną biblioteką współdzieloną,
możliwie najwygodniejszą w większości zastosowań.

%package devel
Summary:	Header files for libmongo-client library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libmongo-client
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.16.0

%description devel
Header files for libmongo-client library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libmongo-client.

%package static
Summary:	Static libmongo-client library
Summary(pl.UTF-8):	Statyczna biblioteka libmongo-client
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmongo-client library.

%description static -l pl.UTF-8
Statyczna biblioteka libmongo-client.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a docs/tutorial/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmongo-client.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_libdir}/libmongo-client.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmongo-client.so.0

%files devel
%defattr(644,root,root,755)
%doc docs/tutorial/*.h
%attr(755,root,root) %{_libdir}/libmongo-client.so
%{_includedir}/mongo-client
%{_pkgconfigdir}/libmongo-client.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libmongo-client.a
