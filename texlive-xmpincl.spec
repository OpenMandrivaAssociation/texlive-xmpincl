%global tl_name xmpincl
%global tl_revision 60593

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4
Release:	%{tl_revision}.1
Summary:	Include eXtensible Metadata Platform data in pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xmpincl
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xmpincl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xmpincl.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xmpincl.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The XMP (eXtensible Metadata platform) is a framework to add metadata to
digital material to enhance the workflow in publication. The essence is
that the metadata is stored in an XML file, and this XML stream is then
embedded in the file to which it applies. How you create this XML file
is up to you, but the author started investigating this because he
wanted to embed licensing information in the files he created. The
license the author chose is one of the Creative Commons licenses, and
their web-site offers this information in a valid XML-file, suitable for
direct inclusion.

