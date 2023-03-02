Summary:	Meltho Syriac fonts
Summary(pl.UTF-8):	Fonty syryjskie Meltho
Name:		xorg-font-font-misc-meltho
Version:	1.0.4
Release:	1
License:	distributable if unmodified
Group:		Fonts
Source0:	https://xorg.freedesktop.org/releases/individual/font/font-misc-meltho-%{version}.tar.xz
# Source0-md5:	9068872dedee1c14756e0fd8adf1d068
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	fontconfig
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.2
BuildRequires:	xorg-util-util-macros >= 1.20
BuildRequires:	xz
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/OTF
Obsoletes:	XFree86-fonts-Syriac < 4.9
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
%if "%{_gnu}" != "-gnux32"
	--build=%{_host} \
	--host=%{_host} \
%endif
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
%doc COPYING ChangeLog README.md
%{_fontsdir}/OTF/SyrCOM*.otf
