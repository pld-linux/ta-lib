Summary:	Technical Analysis Library
Name:		ta-lib
Version:	0.4.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/ta-lib/%{name}-%{version}-src.tar.gz
# Source0-md5:	308e53b9644213fc29262f36b9d3d9b9
URL:		http://ta-lib.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TA-Lib provides common functions for the technical analysis of
stock/future/commodity market data.

%package devel
Summary:	Header files for ta-lib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ta-lib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files fock ta-lib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ta-lib.

%package static
Summary:	Static ta-lib library
Summary(pl.UTF-8):	Statyczna biblioteka ta-lib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ta-lib library.

%description static -l pl.UTF-8
Statyczna biblioteka ta-lib.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG.TXT HISTORY.TXT
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ta-lib-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
