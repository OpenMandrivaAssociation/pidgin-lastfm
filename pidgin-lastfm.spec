Summary:  Last.fm Plugin for Pidgin
Group:    Networking/Instant messaging
Name:     pidgin-lastfm
Version:  0.4a
Release:  5
License:  GPLv3+
Requires: pidgin-perl
Source: http://downloads.sourceforge.net/pidgin-lastfm/pidgin-lastfm_%{version}_all.tar.gz
URL: https://pidgin-lastfm.naturalnet.de

#not noarch as the plugin dir is different on x86_64
#BuildArch: noarch
%define debug_package %{nil}

%description
The Pidgin Last.fm Plugin can display information from your Last.fm profile
as a status message in the multi-protocol instant messenger Pidgin.
The most important information might be the most recently scrobbled track.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_libdir}/pidgin
cp src/lastfm.pl %{buildroot}%{_libdir}/pidgin

%files
%doc docs/*
%attr(755,root,root) %{_libdir}/pidgin/lastfm.pl
