Summary: Last.fm Plugin for Pidgin
%define version 0.3a
Group: Productivity/Networking/AOLInstantMessenger
Name: pidgin-lastfm
License: GPL
Prefix: /usr
Provides: pidgin-lastfm
Release: 1
Requires: perl, pidgin
BuildArch: noarch
Source: http://pidgin-lastfm.naturalnet.de/download/pidgin-lastfm_%{version}_all.tar.gz
URL: http://pidgin-lastfm.naturalnet.de
Version: %{version}
Buildroot: %{_tmppath}/%{name}-%{version}-root
%description
The Pidgin Last.fm Plugin can display information from your Last.fm profile
as a status message in the multi-protocol instant messenger Pidgin.
The most important information might be the most recently scrobbled track.

%prep
%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/doc/pidgin-lastfm-%{version}
mkdir -p $RPM_BUILD_ROOT/usr/lib/pidgin
cp src/lastfm.pl $RPM_BUILD_ROOT/usr/lib/pidgin
cp docs/GPL.txt $RPM_BUILD_ROOT/usr/doc/pidgin-lastfm-%{version}
cp docs/CREDITS.txt $RPM_BUILD_ROOT/usr/doc/pidgin-lastfm-%{version}
cp docs/RELEASE.txt $RPM_BUILD_ROOT/usr/doc/pidgin-lastfm-%{version}
cp docs/CHANGELOG.txt $RPM_BUILD_ROOT/usr/doc/pidgin-lastfm-%{version}

%files
%attr(0755 root root) /usr/lib/pidgin/lastfm.pl
%attr(0644 root root) %doc /usr/doc/pidgin-lastfm-%{version}/*

