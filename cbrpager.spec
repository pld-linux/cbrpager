Summary:	Small viewer of CBR (comic book archive) files
Summary(pl):	Ma³a przegl±darka plików CBR (comic book archive)
Name:		cbrpager
Version:	0.9.9
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/cbrpager/%{name}-%{version}.tar.gz
# Source0-md5:	e2b3e36a1042e4c3d74f652a654b647c
Source1:	%{name}.desktop
URL:		http://cbrpager.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgnomeui-devel >= 2.0.0
Requires:	unrar
Requires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small viewer of CBR (comic book archive) files.

%description -l pl
Ma³a przegl±darka plików CBR (comic book archive).

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
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
