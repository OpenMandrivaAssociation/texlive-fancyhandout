%global tl_name fancyhandout
%global tl_revision 46411

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A LaTeX class for producing nice-looking handouts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fancyhandout
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyhandout.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyhandout.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package breaks with some of LaTeX's principles and redefines basic
LaTeX commands with the aim of producing well-designed and clearly
structured handouts: A sans-serif font is used by default; sections are
not numbered, but highlighted by underlining; head- and footline display
document information; and in order to avoid too much whitespace around
the text the margin sizes are adjusted to smaller values. All in all,
fancyhandout provides a means of typesetting documents not exclusively
consisting of running text in a beautiful way. fancyhandout depends on
the following other LaTeX packages: csquotes, enumitem, etoolbox,
fancyhdr, geometry, and xcolor.

