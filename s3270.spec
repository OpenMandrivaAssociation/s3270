Summary:	Scripted 3270 Emulator
Name:		s3270
Version:	3.3.9ga12
Release:	4
License:	GPL
Group:		Terminals
URL:		https://www.geocities.com/SiliconValley/Peaks/7814/
Source0:	http://downloads.sourceforge.net/project/x3270/x3270/%version/suite3270-%version.tgz
Requires:	x3270 <= %{version}
BuildRequires:	openssl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Complete IBM 3278/3279 emulation, TN3270E support, structured
fields, color xterm emulation, highly configurable

%prep
%setup -q -n %{name}-3.3
perl -p -i -e "s|^#!/usr/local|#!/usr|g" Examples/cms_cmd.expect

%build
%configure2_5x
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall_std

rm -f %buildroot%_bindir/x3270if

install -d %{buildroot}%{_mandir}/man1
install -m644 %{name}.man %{buildroot}%{_mandir}/man1/%{name}.1

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc html/*.html README
%doc Examples/cms_cmd.expect
%{_bindir}/*
%{_mandir}/man1/%{name}.*


%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.9ga12-3mdv2011.0
+ Revision: 614804
- the mass rebuild of 2010.1 packages

* Mon Apr 12 2010 Funda Wang <fwang@mandriva.org> 3.3.9ga12-2mdv2010.1
+ Revision: 533651
- rebuild for openssl 1.0

* Wed Aug 12 2009 Funda Wang <fwang@mandriva.org> 3.3.9ga12-1mdv2010.0
+ Revision: 415337
- new version 3.3.9ga12

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 3.3.6-4mdv2009.0
+ Revision: 260481
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 3.3.6-3mdv2009.0
+ Revision: 251859
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 3.3.6-1mdv2008.1
+ Revision: 140755
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jun 27 2007 Funda Wang <fwang@mandriva.org> 3.3.6-1mdv2008.0
+ Revision: 44875
- New version
- Import s3270



* Thu Apr 20 2006 Lenny Cartier <lenny@mandriva.com> 3.3.4p6-1mdk
- 3.3.4p6

* Wed Nov 30 2005 Oden Eriksson <oeriksson@mandriva.com> 3.3.4p3-2mdk
- rebuilt against openssl-0.9.8a

* Thu Jul 07 2005 Lenny Cartier <lenny@mandriva.com> 3.3.4p3-1mdk
- 3.3.4p3

* Tue Jun 08 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 3.3.2p1-1mdk
- new version
- fix strange perms
- fix deps

* Fri Jul 11 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 3.2.20-1mdk
- 3.2.20
- use the %%configure2_5x macro

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 3.2.19-3mdk
- rebuild

* Mon Jan 27 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 3.2.19-2mdk
- build release
- misc spec file fixes

* Thu May 16 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 3.2.19-1mdk
- new version
- misc spec file fixes
- rebuilt with latest system compiler (gcc3.1)

* Tue Jan  1 2002  Oden Eriksson <oden.eriksson@kvikkjokk.net> 3.2.18-1mdk
- new version

* Mon Sep 24 2001 Lenny Cartier <lenny@mandrakesoft.com> 3.2.17-1mdk
- added by Oden Eriksson <oden.eriksson@kvikkjokk.net> :
	- initial cooker contrib
