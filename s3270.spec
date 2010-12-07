Summary:	Scripted 3270 Emulator
Name:		s3270
Version:	3.3.9ga12
Release:	%mkrel 3
License:	GPL
Group:		Terminals
URL:		http://www.geocities.com/SiliconValley/Peaks/7814/
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
