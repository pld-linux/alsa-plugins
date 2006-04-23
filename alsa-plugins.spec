Summary:	Advanced Linux Sound Architecture - plugins
Summary(pl):	Advanced Linux Sound Architecture - wtyczki
Name:		alsa-plugins
Version:	1.0.11
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	ftp://ftp.alsa-project.org/pub/plugins/%{name}-%{version}.tar.bz2
# Source0-md5:	4ca9ebb9f59b6d9bd85c904134a78305
URL:		http://www.alsa-project.org/
BuildRequires:	alsa-lib-devel >= 1.0.11
BuildRequires:	automake
BuildRequires:	ffmpeg-devel
BuildRequires:	jack-audio-connection-kit-devel >= 0.98
BuildRequires:	libsamplerate-devel
BuildRequires:	polypaudio-devel >= 0.8
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ALSA plugins.

%description -l pl
Wtyczki ALSA.

%package a52
Summary:	A52 output plugin for ALSA
Summary(pl):	Wtyczka wyj¶ciowa A52 dla systemu ALSA
Group:		Libraries
Requires:	alsa-lib >= 1.0.11

%description a52
A52 output plugin for ALSA.

%description a52 -l pl
Wtyczka wyj¶ciowa A52 dla systemu ALSA.

%package jack
Summary:	JACK <--> ALSA PCM plugin
Summary(pl):	Wtyczka PCM JACK <--> ALSA
Group:		Libraries
Requires:	alsa-lib >= 1.0.11
Requires:	jack-audio-connection-kit >= 0.98

%description jack
This plugin converts the ALSA API over JACK (Jack Audio Connection
Kit) API. ALSA native applications can work transparently together
with jackd for both playback and capture.

%description jack -l pl
Ta wtyczka konwertuje API ALSA na API JACK (Jack Audio Connection
Kit). Aplikacje korzystaj±ce natywnie z biblioteki ALSA mog± w sposób
przezroczysty dzia³aæ z jackd zarówno przy odtwarzaniu d¼wiêku, jak i
nagrywaniu.

%package mix
Summary:	Up/down mixing plugins for ALSA
Summary(pl):	Wtyczki up/down-mix dla systemu ALSA
Group:		Libraries
Requires:	alsa-lib >= 1.0.11

%description mix
Up/down mixing plugins for ALSA.

%description mix -l pl
Wtyczki up/down-mix dla systemu ALSA.

%package oss
Summary:	OSS <--> ALSA plugins
Summary(pl):	Wtyczki OSS <--> ALSA
Group:		Libraries
Requires:	alsa-lib >= 1.0.11

%description oss
These plugins converts the ALSA API over OSS API. ALSA native
applications can run on OSS drivers.

%description oss -l pl
Te wtyczki konwertuj± API ALSA na API OSS. Aplikacje korzystaj±ce
natywnie z biblioteki ALSA mog± dzia³aæ na sterownikach OSS.

%package polyp
Summary:	Polypaudio <--> ALSA plugins
Summary(pl):	Wtyczki Polypaudio <--> ALSA
Group:		Libraries
Requires:	alsa-lib >= 1.0.11

%description polyp
These plugins allows any program that uses the ALSA API to access a
Polypaudio sound daemon. In other words, native ALSA applications can
play and record sound across a network.

%description polyp -l pl
Te wtyczki umo¿liwiaj± dowolnemu programowi korzystaj±cego z API ALSA
dostêp do demona d¼wiêku Polypaudio. Innymi s³owy, aplikacje ALSA mog±
odtwarzaæ i nagrywaæ d¼wiêk poprzez sieæ.

%package samplerate
Summary:	Rate converter plugin for ALSA
Summary(pl):	Wtyczka konwertera tempa dla systemu ALSA
Group:		Libraries
Requires:	alsa-lib >= 1.0.11

%description samplerate
Rate converter plugin for ALSA.

%description samplerate -l pl
Wtyczka konwertera tempa dla systemu ALSA.

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

%files a52
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_pcm_a52.so

%files jack
%defattr(644,root,root,755)
%doc doc/README-jack
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_pcm_jack.so

%files mix
%defattr(644,root,root,755)
%doc doc/{upmix,vdownmix}.txt
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_pcm_upmix.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_pcm_vdownmix.so

%files oss
%defattr(644,root,root,755)
%doc doc/README-pcm-oss
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_ctl_oss.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_pcm_oss.so

%files polyp
%defattr(644,root,root,755)
%doc doc/README-polyp
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_ctl_polyp.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_pcm_polyp.so

%files samplerate
%defattr(644,root,root,755)
%doc doc/samplerate.txt
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_samplerate.so
