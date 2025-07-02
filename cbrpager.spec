Summary:	Small viewer of CBR (comic book archive) files
Summary(pl.UTF-8):	Mała przeglądarka plików CBR (comic book archive)
Name:		cbrpager
Version:	0.9.22
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://downloads.sourceforge.net/cbrpager/%{name}-%{version}.tar.gz
# Source0-md5:	01ff3cffbfc00a6e314b0f868eb403b2
Source1:	%{name}.desktop
URL:		https://cbrpager.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	pkgconfig
Requires:	unrar
Requires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small viewer of CBR (comic book archive) files.

%description -l pl.UTF-8
Mała przeglądarka plików CBR (comic book archive).

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} 

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/cbrpager
%{_desktopdir}/cbrpager.desktop
