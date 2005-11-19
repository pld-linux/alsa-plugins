Summary:	Advanced Linux Sound Architecture - plugins
Summary(pl):	Advanced Linux Sound Architecture - wtyczki
Name:		alsa-plugins
Version:	1.0.10
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	ftp://ftp.alsa-project.org/pub/plugins/%{name}-%{version}.tar.bz2
# Source0-md5:	f778eb35e652fc3e4b726bb021b1ce9d
URL:		http://www.alsa-project.org/
BuildRequires:	alsa-lib-devel >= 1.0.10
BuildRequires:	automake
BuildRequires:	jack-audio-connection-kit-devel >= 0.90
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ALSA plugins.

%description -l pl
Wtyczki ALSA.

%package jack
Summary:	JACK <--> ALSA PCM plugin
Summary(pl):	Wtyczka PCM JACK <--> ALSA
Group:		Libraries
Requires:	alsa-lib >= 1.0.10
Requires:	jack-audio-connection-kit >= 0.90

%description jack
This plugin converts the ALSA API over JACK (Jack Audio Connection
Kit) API. ALSA native applications can work transparently together
with jackd for both playback and capture.

%description jack -l pl
Ta wtyczka konwertuje API ALSA na API JACK (Jack Audio Connection
Kit). Aplikacje korzystaj±ce natywnie z biblioteki ALSA mog± w sposób
przezroczysty dzia³aæ z jackd zarówno przy odtwarzaniu d¼wiêku, jak i
nagrywaniu.

%package oss
Summary:	OSS <--> ALSA plugins
Summary(pl):	Wtyczki OSS <--> ALSA
Group:		Libraries
Requires:	alsa-lib >= 1.0.10

%description oss
These plugins converts the ALSA API over OSS API. ALSA native
applications can run on OSS drivers.

%description oss -l pl
Te wtyczki konwertuj± API ALSA na API OSS. Aplikacje korzystaj±ce
natywnie z biblioteki ALSA mog± dzia³aæ na sterownikach OSS.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/alsa-lib/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files jack
%defattr(644,root,root,755)
%doc pcm/jack/README
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_pcm_jack.so

%files oss
%defattr(644,root,root,755)
%doc pcm/oss/README
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_ctl_oss.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_pcm_oss.so
