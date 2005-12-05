Summary:	Meltho Syriac fonts
Summary(pl):	Fonty syryjskie Meltho
Name:		xorg-font-font-misc-meltho
Version:	0.99.2
Release:	0.1
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/font/font-misc-meltho-%{version}.tar.bz2
# Source0-md5:	cc2b3370104fea946f283f2a8ec822a6
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	fontconfig
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/OTF
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Meltho Syriac fonts in OTF format.

%description -l pl
Fonty syryjskie Meltho w formacie OTF.

%prep
%setup -q -n font-misc-meltho-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-fontdir=%{_fontsdir}/OTF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst OTF

%postun
fontpostinst OTF

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%{_fontsdir}/OTF/SyrCOM*.otf
