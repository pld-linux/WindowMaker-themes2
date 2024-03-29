Summary:	Pack of themes for WindowMaker
Summary(pl.UTF-8):	Zestaw motywów dla WindowMakera
Name:		WindowMaker-themes2
Version:	1.0
Release:	4
License:	GPL
Group:		Themes
Source0:	http://ep09.pld-linux.org/~havner/%{name}.tar.bz2
# Source0-md5:	714ff093a844c1817e23150164c422f4
Requires:	WindowMaker
Obsoletes:	WindowMaker-themes-pack2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themesdir	%{_datadir}/WindowMaker/Themes

%description
This is a set of 20 themes for WindowMaker made by jensen
<jensen@optushome.com.au>: Glitchscape, GNULinux, Gold Sun, Grassy
Plain, Green Net, Green Understatement, Hocus Pocus, Inkblot Sunset,
Ladybird, Llucy, Mercury Splat, Peach Frequency, Reeds, Seagull,
Silences, Silver Circles, Time Passes, Venturi, Waves, What Dreams.

%description -l pl.UTF-8
Zestaw 20 motywów dla WindowMakera wykonanych przez jensena
<jensen@optushome.com.au>: Glitchscape, GNULinux, Gold Sun, Grassy
Plain, Green Net, Green Understatement, Hocus Pocus, Inkblot Sunset,
Ladybird, Llucy, Mercury Splat, Peach Frequency, Reeds, Seagull,
Silences, Silver Circles, Time Passes, Venturi, Waves, What Dreams.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_themesdir}

cp -R * $RPM_BUILD_ROOT%{_themesdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_themesdir}/*
