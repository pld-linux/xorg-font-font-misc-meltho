Summary:	Meltho Syriac fonts
Summary(pl.UTF-8):	Fonty syryjskie Meltho
Name:		xorg-font-font-misc-meltho
Version:	1.0.1
Release:	1
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-misc-meltho-%{version}.tar.bz2
# Source0-md5:	345f1a78312e30cd2c41d24ea3f3276f
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	fontconfig
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/OTF
Obsoletes:	XFree86-fonts-Syriac
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Meltho Syriac fonts in OTF format.

%description -l pl.UTF-8
Fonty syryjskie Meltho w formacie OTF.

%prep
%setup -q -n font-misc-meltho-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--build=%{_host_platform} \
	--host=%{_host_platform} \
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
