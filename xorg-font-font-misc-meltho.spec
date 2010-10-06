Summary:	Meltho Syriac fonts
Summary(pl.UTF-8):	Fonty syryjskie Meltho
Name:		xorg-font-font-misc-meltho
Version:	1.0.2
Release:	1
License:	distributable if unmodified
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-misc-meltho-%{version}.tar.bz2
# Source0-md5:	b6d53e8bcc06e25f868130a0c4619ab2
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	fontconfig
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.1
BuildRequires:	xorg-util-util-macros >= 1.3
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/OTF
Obsoletes:	XFree86-fonts-Syriac
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Meltho Syriac fonts in OTF format. They come from Beth Mardutho: The
Syriac Institute and are covered by a license which permits
redistribution but prohibits modification.  Please see the license in
COPYING file.

%description -l pl.UTF-8
Fonty syryjskie Meltho w formacie OTF. Pochodzą z Beth Mardutho: The
Syriac Institute. Ich licencja zezwala na rozpowszechnianie, ale
zabrania modyfikacji - szczegóły w pliku COPYING.

%prep
%setup -q -n font-misc-meltho-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--build=%{_host} \
	--host=%{_host} \
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
