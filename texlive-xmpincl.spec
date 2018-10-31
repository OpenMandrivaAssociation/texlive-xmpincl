# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/xmpincl
# catalog-date 2008-05-10 20:43:24 +0200
# catalog-license gpl
# catalog-version 2.2
Name:		texlive-xmpincl
Version:	2.2
Release:	11
Summary:	Include eXtensible Metadata Platform data in PDFLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xmpincl
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xmpincl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xmpincl.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xmpincl.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.2-2
+ Revision: 757665
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.2-1
+ Revision: 719946
- texlive-xmpincl
- texlive-xmpincl
- texlive-xmpincl

