%define		source_name gmpc-dynamic-playlist
Summary:	Add similar songs to playlist
Name:		gmpc-plugin-dynamic-playlist
Version:	0.19.0
Release:	2
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://bitbucket.org/misery/dynamic-playlist/downloads/%{source_name}-%{version}.tar.gz
# Source0-md5:	e47552a45376a52935e1f5c6add0e7d9
URL:		http://gmpc.wikia.com/wiki/GMPC_PLUGIN_DYNAMIC_PLAYLIST
BuildRequires:	cmake
BuildRequires:	gmpc-devel >= 0.18.100
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	libmpd-devel >= 0.18.100
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This GMPC plugin will search for »similar songs/artists/genres« with last.fm or
with genre-tag and add it to the playlist if there is no new song at the end of
that playlist.

If no similar song is found - a random one will be added.

%prep
%setup -qn %{source_name}-%{version}

%build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/gmpc

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{source_name}
%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{source_name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/plugins/*.so
%{_libdir}/gmpc/plugins/*.xml
