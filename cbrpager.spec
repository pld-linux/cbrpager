Summary:	Small viewer of CBR (comic book archive) files
Summary(pl.UTF-8):   Mała przeglądarka plików CBR (comic book archive)
Name:		cbrpager
Version:	0.9.14
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/cbrpager/%{name}-%{version}.tar.gz
# Source0-md5:	0ce88fc52025b44812d090d10244b2a4
Source1:	%{name}.desktop
URL:		http://cbrpager.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libgnomeui-devel >= 2.0.0
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

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} 

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog CONTRIBUTORS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
