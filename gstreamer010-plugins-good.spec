%include	/usr/lib/rpm/macros.gstreamer

%define		gstname		gst-plugins-good
%define		gst_major_ver	0.10
%define		gst_req_ver	0.10.35
%define		gstpb_req_ver	0.10.35

Summary:	Good GStreamer Streaming-media framework plugins
Name:		gstreamer010-plugins-good
Version:	0.10.31
Release:	6
License:	LGPL
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-good/%{gstname}-%{version}.tar.xz
# Source0-md5:	555845ceab722e517040bab57f9ace95
Patch0:		%{name}-compile-fix.patch
URL:		http://gstreamer.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gstreamer010-devel >= %{gst_req_ver}
BuildRequires:	gstreamer010-plugins-base-devel >= %{gstpb_req_ver}
BuildRequires:	gtk-doc
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	orc-devel >= 0.4.5
BuildRequires:	pkg-config
#
BuildRequires:	cairo-devel
BuildRequires:	dbus-devel
BuildRequires:	flac-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	ladspa-devel
BuildRequires:	libavc1394-devel
BuildRequires:	libcdio-devel
BuildRequires:	libiec61883-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libraw1394-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	rpm-gstreamerprov
BuildRequires:	speex-devel
BuildRequires:	taglib-devel
BuildRequires:	wavpack-devel
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXdamage-devel
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXfixes-devel
BuildRequires:	zlib-devel
Requires:	gstreamer010 >= %{gst_req_ver}
Requires:	gstreamer010-plugins-base >= %{gstpb_req_ver}
Provides:	gstreamer-plugins-good = %{version}-%{release}
Obsoletes:	gstreamer-plugins-good < %{version}-%{release}
Obsoletes:	gstreamer010-plugins-good-gconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gstdatadir 	%{_datadir}/gstreamer-%{gst_major_ver}
%define		gstlibdir 	%{_libdir}/gstreamer-%{gst_major_ver}

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plugins.

%package apidocs
Summary:	gstreamer-plugins-good API documentation
Group:		Documentation
Requires:	gtk-doc-common
Provides:	gstreamer-plugins-good-apidocs = %{version}-%{release}
Obsoletes:	gstreamer-plugins-good-apidocs < %{version}-%{release}

%description apidocs
gstreamer-plugins-good API documentation.

%prep
%setup -qn %{gstname}-%{version}
%patch0 -p1

%build
%{__autopoint}
%{__patch} -p0 < common/gettext.patch
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	ac_cv_lib_jpeg_mmx_jpeg_set_defaults=no	\
	--disable-aalib				\
	--disable-esd				\
	--disable-examples			\
	--disable-gst_v4l2 			\
	--disable-libcaca			\
	--disable-oss				\
	--disable-oss4				\
	--disable-silent-rules			\
	--disable-static			\
	--enable-experimental			\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# We don't need plugins' *.la files
rm -f $RPM_BUILD_ROOT%{gstlibdir}/*.la

%find_lang %{gstname}-%{gst_major_ver}

%clean
rm -rf $RPM_BUILD_ROOT

%%files -f %{gstname}-%{gst_major_ver}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE

%attr(755,root,root) %{gstlibdir}/libgst1394.so
%attr(755,root,root) %{gstlibdir}/libgstalaw.so
%attr(755,root,root) %{gstlibdir}/libgstalpha.so
%attr(755,root,root) %{gstlibdir}/libgstalphacolor.so
%attr(755,root,root) %{gstlibdir}/libgstannodex.so
%attr(755,root,root) %{gstlibdir}/libgstapetag.so
%attr(755,root,root) %{gstlibdir}/libgstaudiofx.so
%attr(755,root,root) %{gstlibdir}/libgstaudioparsers.so
%attr(755,root,root) %{gstlibdir}/libgstauparse.so
%attr(755,root,root) %{gstlibdir}/libgstautodetect.so
%attr(755,root,root) %{gstlibdir}/libgstavi.so
%attr(755,root,root) %{gstlibdir}/libgstcairo.so
%attr(755,root,root) %{gstlibdir}/libgstcutter.so
%attr(755,root,root) %{gstlibdir}/libgstdebug.so
%attr(755,root,root) %{gstlibdir}/libgstdeinterlace.so
%attr(755,root,root) %{gstlibdir}/libgstefence.so
%attr(755,root,root) %{gstlibdir}/libgsteffectv.so
%attr(755,root,root) %{gstlibdir}/libgstequalizer.so
%attr(755,root,root) %{gstlibdir}/libgstflac.so
%attr(755,root,root) %{gstlibdir}/libgstflv.so
%attr(755,root,root) %{gstlibdir}/libgstflxdec.so
%attr(755,root,root) %{gstlibdir}/libgstgdkpixbuf.so
%attr(755,root,root) %{gstlibdir}/libgstgoom.so
%attr(755,root,root) %{gstlibdir}/libgstgoom2k1.so
%attr(755,root,root) %{gstlibdir}/libgsticydemux.so
%attr(755,root,root) %{gstlibdir}/libgstid3demux.so
%attr(755,root,root) %{gstlibdir}/libgstimagefreeze.so
%attr(755,root,root) %{gstlibdir}/libgstinterleave.so
%attr(755,root,root) %{gstlibdir}/libgstisomp4.so
%attr(755,root,root) %{gstlibdir}/libgstjack.so
%attr(755,root,root) %{gstlibdir}/libgstjpeg.so
%attr(755,root,root) %{gstlibdir}/libgstlevel.so
%attr(755,root,root) %{gstlibdir}/libgstmatroska.so
%attr(755,root,root) %{gstlibdir}/libgstmonoscope.so
%attr(755,root,root) %{gstlibdir}/libgstmulaw.so
%attr(755,root,root) %{gstlibdir}/libgstmultifile.so
%attr(755,root,root) %{gstlibdir}/libgstmultipart.so
%attr(755,root,root) %{gstlibdir}/libgstnavigationtest.so
%attr(755,root,root) %{gstlibdir}/libgstpng.so
%attr(755,root,root) %{gstlibdir}/libgstpulse.so
%attr(755,root,root) %{gstlibdir}/libgstreplaygain.so
%attr(755,root,root) %{gstlibdir}/libgstrtp.so
%attr(755,root,root) %{gstlibdir}/libgstrtpmanager.so
%attr(755,root,root) %{gstlibdir}/libgstrtsp.so
%attr(755,root,root) %{gstlibdir}/libgstshapewipe.so
%attr(755,root,root) %{gstlibdir}/libgstsmpte.so
%attr(755,root,root) %{gstlibdir}/libgstsouphttpsrc.so
%attr(755,root,root) %{gstlibdir}/libgstspectrum.so
%attr(755,root,root) %{gstlibdir}/libgstspeex.so
%attr(755,root,root) %{gstlibdir}/libgsttaglib.so
%attr(755,root,root) %{gstlibdir}/libgstudp.so
%attr(755,root,root) %{gstlibdir}/libgstvideobox.so
%attr(755,root,root) %{gstlibdir}/libgstvideocrop.so
%attr(755,root,root) %{gstlibdir}/libgstvideofilter.so
%attr(755,root,root) %{gstlibdir}/libgstvideomixer.so
%attr(755,root,root) %{gstlibdir}/libgstwavenc.so
%attr(755,root,root) %{gstlibdir}/libgstwavpack.so
%attr(755,root,root) %{gstlibdir}/libgstwavparse.so
%attr(755,root,root) %{gstlibdir}/libgstximagesrc.so
%attr(755,root,root) %{gstlibdir}/libgsty4menc.so
%{gstdatadir}/presets/*.prs

%if 0
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gst-plugins-good-plugins-*
%endif

