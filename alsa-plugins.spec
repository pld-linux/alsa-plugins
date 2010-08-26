Summary:	Advanced Linux Sound Architecture - plugins
Summary(pl.UTF-8):	Advanced Linux Sound Architecture - wtyczki
Name:		alsa-plugins
Version:	1.0.14
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	ftp://ftp.alsa-project.org/pub/plugins/%{name}-%{version}.tar.bz2
# Source0-md5:	fa678da6b91c9f3c7204bc8d14e5b53f
URL:		http://www.alsa-project.org/
Patch0:		%{name}-ffmpeg.patch
BuildRequires:	alsa-lib-devel >= 1.0.14
BuildRequires:	automake
BuildRequires:	dbus-devel >= 0.35
BuildRequires:	ffmpeg-devel
BuildRequires:	jack-audio-connection-kit-devel >= 0.98
BuildRequires:	libsamplerate-devel
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.2
BuildRequires:	speex-devel >= 1:1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ALSA plugins.

%description -l pl.UTF-8
Wtyczki ALSA.

%package a52
Summary:	A52 output plugin for ALSA
Summary(pl.UTF-8):	Wtyczka wyjściowa A52 dla systemu ALSA
Group:		Libraries
Requires:	alsa-lib >= 1.0.14

%description a52
A52 output plugin for ALSA.

%description a52 -l pl.UTF-8
Wtyczka wyjściowa A52 dla systemu ALSA.

%package jack
Summary:	JACK <--> ALSA PCM plugin
Summary(pl.UTF-8):	Wtyczka PCM JACK <--> ALSA
Group:		Libraries
Requires:	alsa-lib >= 1.0.14
Requires:	jack-audio-connection-kit >= 0.98

%description jack
This plugin converts the ALSA API over JACK (Jack Audio Connection
Kit) API. ALSA native applications can work transparently together
with jackd for both playback and capture.

%description jack -l pl.UTF-8
Ta wtyczka konwertuje API ALSA na API JACK (Jack Audio Connection
Kit). Aplikacje korzystające natywnie z biblioteki ALSA mogą w sposób
przezroczysty działać z jackd zarówno przy odtwarzaniu dźwięku, jak i
nagrywaniu.

%package lavcrate
Summary:	libavcodec-based rate converter plugin for ALSA
Summary(pl.UTF-8):	Wtyczka konwertera tempa dla systemu ALSA oparta na libavcodec
Group:		Libraries
Requires:	alsa-lib >= 1.0.14

%description lavcrate
libavcodec-based rate converter plugin for ALSA.

%description lavcrate -l pl.UTF-8
Wtyczka konwertera tempa dla systemu ALSA oparta na libavcodec.

%package maemo
Summary:	ALSA plugins for Nokia DSP
Summary(pl.UTF-8):	Wtyczki systemu ALSA dla DSP Nokii
Group:		Libraries
Requires:	alsa-lib >= 1.0.14

%description maemo
ALSA plugins for Nokia DSP.

%description maemo -l pl.UTF-8
Wtyczki systemu ALSA dla DSP Nokii.

%package mix
Summary:	Up/down mixing plugins for ALSA
Summary(pl.UTF-8):	Wtyczki up/down-mix dla systemu ALSA
Group:		Libraries
Requires:	alsa-lib >= 1.0.14

%description mix
Up/down mixing plugins for ALSA.

%description mix -l pl.UTF-8
Wtyczki up/down-mix dla systemu ALSA.

%package oss
Summary:	OSS <--> ALSA plugins
Summary(pl.UTF-8):	Wtyczki OSS <--> ALSA
Group:		Libraries
Requires:	alsa-lib >= 1.0.14

%description oss
These plugins converts the ALSA API over OSS API. ALSA native
applications can run on OSS drivers.

%description oss -l pl.UTF-8
Te wtyczki konwertują API ALSA na API OSS. Aplikacje korzystające
natywnie z biblioteki ALSA mogą działać na sterownikach OSS.

%package pulse
Summary:	PulseAudio <--> ALSA plugins
Summary(pl.UTF-8):	Wtyczki PulseAudio <--> ALSA
Group:		Libraries
Requires:	alsa-lib >= 1.0.14
Requires:	pulseaudio-libs >= 0.9.2
Obsoletes:	alsa-plugins-polyp

%description pulse
These plugins allows any program that uses the ALSA API to access a
PulseAudio sound daemon. In other words, native ALSA applications can
play and record sound across a network.

%description pulse -l pl.UTF-8
Te wtyczki umożliwiają dowolnemu programowi korzystającego z API ALSA
dostęp do demona dźwięku PulseAudio. Innymi słowy, aplikacje ALSA mogą
odtwarzać i nagrywać dźwięk poprzez sieć.

%package samplerate
Summary:	libsamplerate-based rate converter plugin for ALSA
Summary(pl.UTF-8):	Wtyczka konwertera tempa dla systemu ALSA oparta na libsamplerate
Group:		Libraries
Requires:	alsa-lib >= 1.0.14

%description samplerate
libsamplerate-based rate converter plugin for ALSA.

%description samplerate -l pl.UTF-8
Wtyczka konwertera tempa dla systemu ALSA oparta na libsamplerate.

%package speexrate
Summary:	speex-based rate converter plugin for ALSA
Summary(pl.UTF-8):	Wtyczka konwertera tempa dla systemu ALSA oparta na bibliotece speex
License:	BSD
Group:		Libraries
Requires:	alsa-lib >= 1.0.14
Requires:	speex >= 1:1.2

%description speexrate
speex-based rate converter plugin for ALSA.

%description speexrate -l pl.UTF-8
Wtyczka konwertera tempa dla systemu ALSA oparta na bibliotece speex.

%prep
%setup -q
%patch0 -p1

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

%files lavcrate
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_lavcrate.so

%files maemo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_ctl_dsp_ctl.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_pcm_alsa_dsp.so

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

%files pulse
%defattr(644,root,root,755)
%doc doc/README-pulse
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_ctl_pulse.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_pcm_pulse.so

%files samplerate
%defattr(644,root,root,755)
%doc doc/samplerate.txt
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_samplerate.so

%files speexrate
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_speexrate.so
