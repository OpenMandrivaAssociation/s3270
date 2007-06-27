Summary:	Scripted 3270 Emulator
Name:		s3270
Version:	3.3.6
Release:	%mkrel 1
License:	GPL
Group:		Terminals
URL:		http://www.geocities.com/SiliconValley/Peaks/7814/
Source0:	s3270-%{version}.tgz
Requires:	x3270 =< %{version}
BuildRequires:	X11-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Complete IBM 3278/3279 emulation, TN3270E support, structured
fields, color xterm emulation, highly configurable

%prep

%setup -q -n %{name}-3.3

# fix strange perms
find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

perl -p -i -e "s|^#!/usr/local|#!/usr|g" Examples/cms_cmd.expect

%build

%configure2_5x

%make %{name}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m755 %{name} %{buildroot}%{_bindir}/
install -m644 %{name}.man %{buildroot}%{_mandir}/man1/%{name}.1

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc html/Bugs.html html/Build.html html/FAQ.html html/Intro.html
%doc html/Lineage.html html/New.html html/README.html
%doc html/s3270-man.html html/Wishlist.html README
%doc Examples/cms_cmd.expect
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
