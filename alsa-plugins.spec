Summary:	Advanced Linux Sound Architecture - plugins
Summary(pl.UTF-8):	Advanced Linux Sound Architecture - wtyczki
Name:		alsa-plugins
Version:	1.1.6
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	ftp://ftp.alsa-project.org/pub/plugins/%{name}-%{version}.tar.bz2
# Source0-md5:	8387279e99feeb2ecffaac5f293223d7
Source1:	%{name}-pulse.conf
URL:		http://www.alsa-project.org/
BuildRequires:	alsa-lib-devel >= 1.0.18
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	dbus-devel >= 0.35
BuildRequires:	ffmpeg-devel >= 0.4.9-4.20080822.1
BuildRequires:	jack-audio-connection-kit-devel >= 0.98
BuildRequires:	libsamplerate-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.11
# for <speex/speex_types.h>
BuildRequires:	speex-devel >= 1:1.2
BuildRequires:	speexdsp-devel >= 1:1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ALSA plugins.

%description -l pl.UTF-8
Wtyczki ALSA.

%package a52
Summary:	A52 output plugin for ALSA
Summary(pl.UTF-8):	Wtyczka wyjściowa A52 dla systemu ALSA
Group:		Libraries
Requires:	alsa-lib >= 1.0.18

%description a52
A52 output plugin for ALSA.

%description a52 -l pl.UTF-8
Wtyczka wyjściowa A52 dla systemu ALSA.

%package arcam-av
Summary:	Controls for an Arcam AV amplifier
Summary(pl.UTF-8):	Kontrolki do wzmacniacza Arcam AV
Group:		Libraries
Requires:	alsa-lib >= 1.0.18

%description arcam-av
This plugin exposes the controls for an Arcam AV amplifier (see:
http://www.arcam.co.uk/) as an ALSA mixer device.

%description arcam-av -l pl.UTF-8
Wtyczka ta umożliwia kontrolę nad wzmacniaczem Arcam AV
(http://www.arcam.co.uk/) tak jakby to było urządzenie miksujące ALSA.

%package jack
Summary:	JACK <--> ALSA PCM plugin
Summary(pl.UTF-8):	Wtyczka PCM JACK <--> ALSA
Group:		Libraries
Requires:	alsa-lib >= 1.0.18
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
Requires:	alsa-lib >= 1.0.18

%description lavcrate
libavcodec-based rate converter plugin for ALSA.

%description lavcrate -l pl.UTF-8
Wtyczka konwertera tempa dla systemu ALSA oparta na libavcodec.

%package maemo
Summary:	ALSA plugins for Nokia DSP
Summary(pl.UTF-8):	Wtyczki systemu ALSA dla DSP Nokii
Group:		Libraries
Requires:	alsa-lib >= 1.0.18

%description maemo
ALSA plugins for Nokia DSP.

%description maemo -l pl.UTF-8
Wtyczki systemu ALSA dla DSP Nokii.

%package mix
Summary:	Up/down mixing plugins for ALSA
Summary(pl.UTF-8):	Wtyczki up/down-mix dla systemu ALSA
Group:		Libraries
Requires:	alsa-lib >= 1.0.18

%description mix
Up/down mixing plugins for ALSA.

%description mix -l pl.UTF-8
Wtyczki up/down-mix dla systemu ALSA.

%package oss
Summary:	OSS <--> ALSA plugins
Summary(pl.UTF-8):	Wtyczki OSS <--> ALSA
Group:		Libraries
Requires:	alsa-lib >= 1.0.18

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
Requires:	alsa-lib >= 1.0.18
Requires:	pulseaudio-libs >= 0.9.11
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
Requires:	alsa-lib >= 1.0.18

%description samplerate
libsamplerate-based rate converter plugin for ALSA.

%description samplerate -l pl.UTF-8
Wtyczka konwertera tempa dla systemu ALSA oparta na libsamplerate.

%package speex
Summary:	speex-based PCM plugin for ALSA
Summary(pl.UTF-8):	Wtyczka PCM speex dla systemu ALSA
License:	BSD
Group:		Libraries
Requires:	alsa-lib >= 1.0.18
Requires:	speexdsp >= 1:1.2

%description speex
speex-based PCM plugin for ALSA.

%description speex -l pl.UTF-8
Wtyczka PCM speex dla systemu ALSA.

%package speexrate
Summary:	speex-based rate converter plugin for ALSA
Summary(pl.UTF-8):	Wtyczka konwertera tempa dla systemu ALSA oparta na bibliotece speex
License:	BSD
Group:		Libraries
Requires:	alsa-lib >= 1.0.18
Requires:	speexdsp >= 1:1.2

%description speexrate
speex-based rate converter plugin for ALSA.

%description speexrate -l pl.UTF-8
Wtyczka konwertera tempa dla systemu ALSA oparta na bibliotece speex.

%package usb_stream
Summary:	usb_stream PCM I/O plugin for ALSA
Summary(pl.UTF-8):	Wtyczka wejścia-wyjścia PCM usb_stream dla systemu ALSA
Group:		Libraries
Requires:	alsa-lib >= 1.0.18

%description usb_stream
usb_stream PCM I/O plugin for ALSA.

%description usb_stream -l pl.UTF-8
Wtyczka wejścia-wyjścia PCM usb_stream dla systemu ALSA.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-maemo-plugin \
	--enable-maemo-resource-manager \
	--with-speex=lib

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/alsa

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/alsa-lib/*.la
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/alsa/pulse-default.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files a52
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_pcm_a52.so

%files arcam-av
%defattr(644,root,root,755)
%doc doc/README-arcam-av
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_ctl_arcam_av.so

%files jack
%defattr(644,root,root,755)
%doc doc/README-jack
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_pcm_jack.so

%files lavcrate
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_lavcrate.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_lavcrate_fast.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_lavcrate_faster.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_lavcrate_high.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_lavcrate_higher.so

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
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_conf_pulse.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_ctl_pulse.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_pcm_pulse.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/alsa/pulse-default.conf
%{_datadir}/alsa/alsa.conf.d/50-pulseaudio.conf
#%{_datadir}/alsa/alsa.conf.d/99-pulseaudio-default.conf.example

%files samplerate
%defattr(644,root,root,755)
%doc doc/samplerate.txt
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_samplerate.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_samplerate_best.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_samplerate_linear.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_samplerate_medium.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_samplerate_order.so

%files speex
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_pcm_speex.so

%files speexrate
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_speexrate.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_speexrate_best.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_speexrate_medium.so

%files usb_stream
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_pcm_usb_stream.so
