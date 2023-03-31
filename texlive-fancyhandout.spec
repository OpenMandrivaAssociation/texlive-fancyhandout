Name:		texlive-fancyhandout
Version:	46411
Release:	2
Summary:	A LaTeX class for producing nice-looking handouts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fancyhandout
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyhandout.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyhandout.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package breaks with some of LaTeX's principles and
redefines basic LaTeX commands with the aim of producing
well-designed and clearly structured handouts: A sans-serif
font is used by default; sections are not numbered, but
highlighted by underlining; head- and footline display document
information; and in order to avoid too much whitespace around
the text the margin sizes are adjusted to smaller values. All
in all, fancyhandout provides a means of typesetting documents
not exclusively consisting of running text in a beautiful way.
fancyhandout depends on the following other LaTeX packages:
csquotes, enumitem, etoolbox, fancyhdr, geometry, and xcolor.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/fancyhandout
%doc %{_texmfdistdir}/doc/latex/fancyhandout

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
