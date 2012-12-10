%define fontname	Aroania
%define name		fonts-otf-%{fontname}
%define version		1.01
%define release		%mkrel 2

%define fontdir		%{_datadir}/fonts/OTF/%{fontname}
%define fontconfdir	%{_sysconfdir}/X11/fontpath.d

Summary:	Unicode Aroania fonts
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://users.teilar.gr/~g1951d/%{fontname}.zip
License:	Public Domain
Group:		System/Fonts/True type
Url:		http://users.teilar.gr/~g1951d/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires: fontconfig
BuildRequires:	mkfontscale, mkfontdir

%description
In 1927, Victor Julius Scholderer (1880 - 1971), on behalf of the
'Society for the Promotion of Greek Studies', got involved in choosing
and consulting the design and production of a Greek type called 'New
Hellenic' cut by the Lanston Monotype Corporation. He chose the
revival of a round, and almost monoline type which had first appeared
in 1492 in the edition of Macrobius, ascribable to the printing shop
of Giovanni Rosso (Joannes Rubeus) in Venice. Aroania is a modern
recast of Victor Scholderer’s 'New Hellenic' font, on the basis of
Verdana. The font covers the Windows Glyph List, Greek Extended,
various typographic extras and is available in regular and bold. The
regular style of the font also covers IPA Extensions, Ancient Greek
Numbers, Byzantine and Ancient Greek Musical Notation and several Open
Type features (Case-Sensitive Forms, Small Capitals, Subscript,
Superscript, Numerators, Denominators, Fractions, Old Style Figures,
Historical Forms, Stylistic Alternates, Ligatures).

%prep
%setup -q -c %{name}-%{version}

%install
%__rm -rf %{buildroot}

%__install -m 0755 -d %{buildroot}%{fontdir}
%__install -m 0644 *.otf %{buildroot}%{fontdir}
mkfontscale %{buildroot}%{fontdir}
mkfontdir %{buildroot}%{fontdir}

%__install -m 0755 -d %{buildroot}%{fontconfdir}
ln -s ../../../%{fontdir} %{buildroot}%{fontconfdir}/otf-%{fontname}:pri=50

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{fontconfdir}/otf*
%{fontdir}/*.otf
%{fontdir}/fonts.*



%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.01-2mdv2011.0
+ Revision: 675508
- br fontconfig for fc-query used in new rpm-setup-build

* Wed Jul 28 2010 Lev Givon <lev@mandriva.org> 1.01-1mdv2011.0
+ Revision: 562711
- import fonts-otf-Aroania

