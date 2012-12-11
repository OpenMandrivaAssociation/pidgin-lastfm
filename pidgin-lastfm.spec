%define version 0.4a
Summary: Last.fm Plugin for Pidgin
Group: Networking/Instant messaging
Name: pidgin-lastfm
Version: %{version}
Release: %mkrel 3
License: GPLv3+
Requires: pidgin-perl
#gw no noarch as the plugin dir is different on x86_64
#BuildArch: noarch
Source: http://downloads.sourceforge.net/pidgin-lastfm/pidgin-lastfm_%{version}_all.tar.gz
URL: http://pidgin-lastfm.naturalnet.de
Buildroot: %{_tmppath}/%{name}-%{version}-root

%description
The Pidgin Last.fm Plugin can display information from your Last.fm profile
as a status message in the multi-protocol instant messenger Pidgin.
The most important information might be the most recently scrobbled track.

%prep
%setup -q

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


%changelog
* Thu Dec 08 2011 Götz Waschk <waschk@mandriva.org> 0.4a-3mdv2012.0
+ Revision: 738849
- yearly rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4a-2mdv2011.0
+ Revision: 614543
- the mass rebuild of 2010.1 packages

* Sun May 03 2009 Götz Waschk <waschk@mandriva.org> 0.4a-1mdv2010.1
+ Revision: 371268
- new version

* Tue Nov 18 2008 Götz Waschk <waschk@mandriva.org> 0.4-1mdv2009.1
+ Revision: 304201
- new version
- update URL

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.3b-2mdv2009.0
+ Revision: 268973
- rebuild early 2009.0 package (before pixel changes)

* Thu Jun 12 2008 Götz Waschk <waschk@mandriva.org> 0.3b-1mdv2009.0
+ Revision: 218336
- new version

* Wed Apr 30 2008 Götz Waschk <waschk@mandriva.org> 0.3a-1mdv2009.0
+ Revision: 199377
- adapt for Mandriva
- import pidgin-lastfm


* Mon Apr 28 2008 Dominik George <pidgin-lastfm@naturalnet.de>
- First RPM release
