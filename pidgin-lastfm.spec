%define version 0.3b
Summary: Last.fm Plugin for Pidgin
Group: Networking/Instant messaging
Name: pidgin-lastfm
Version: %{version}
Release: %mkrel 1
License: GPLv3+
Requires: pidgin-perl
#gw no noarch as the plugin dir is different on x86_64
#BuildArch: noarch
Source: http://pidgin-lastfm.naturalnet.de/download/pidgin-lastfm-%{version}_all.tar.gz
URL: http://pidgin-lastfm.naturalnet.de
Buildroot: %{_tmppath}/%{name}-%{version}-root

%description
The Pidgin Last.fm Plugin can display information from your Last.fm profile
as a status message in the multi-protocol instant messenger Pidgin.
The most important information might be the most recently scrobbled track.

%prep
%setup -q -n %name

%build

%install
rm -rf %buildroot
mkdir -p $RPM_BUILD_ROOT%{_libdir}/pidgin
cp src/lastfm.pl $RPM_BUILD_ROOT%{_libdir}/pidgin

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc docs/*
%attr(755,root,root) %{_libdir}/pidgin/lastfm.pl
