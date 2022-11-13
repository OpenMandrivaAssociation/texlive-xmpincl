Name:		texlive-xmpincl
Version:	60593
Release:	1
Summary:	Include eXtensible Metadata Platform data in PDFLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xmpincl
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xmpincl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xmpincl.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xmpincl.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The XMP (eXtensible Metadata platform) is a framework to add
metadata to digital material to enhance the workflow in
publication. The essence is that the metadata is stored in an
XML file, and this XML stream is then embedded in the file to
which it applies. How you create this XML file is up to you,
but the author started investigating this because he wanted to
embed licensing information in the files he created. The
license the author chose is one of the Creative Commons
licenses, and their web-site offers this information in a valid
XML-file, suitable for direct inclusion.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xmpincl/xmpincl.sty
%doc %{_texmfdistdir}/doc/latex/xmpincl/README
%doc %{_texmfdistdir}/doc/latex/xmpincl/license.xmp
%doc %{_texmfdistdir}/doc/latex/xmpincl/xmpincl.pdf
#- source
%doc %{_texmfdistdir}/source/latex/xmpincl/xmpincl.dtx
%doc %{_texmfdistdir}/source/latex/xmpincl/xmpincl.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
