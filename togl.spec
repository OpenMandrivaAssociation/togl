Name:		togl
Group:		Sciences/Other
Version:	2.0
Release:	%mkrel 1
Summary:	Togl - a Tk OpenGL widget
License:	BSD like
URL:		http://togl.sourceforge.net/index.html
Source0:	Togl2.0-src.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	GL-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	X11-devel
%py_requires -d

Patch0:		Togl2.0-build.patch

%description
Togl is a Tk widget for OpenGL rendering. Togl was originally based on OGLTK,
written by Benjamin Bederson at the University of New Mexico. Togl's main
features are:

    * unifies Microsoft Windows, X11 (Linux/IRIX/...), and Mac OS X Aqua support
    * support for requesting stencil, accumulation, alpha buffers, etc.
    * multiple OpenGL drawing windows
    * simple stereo rendering support
    * simple, portable font support
    * color-index mode support including color allocation functions
    * overlay plane support
    * OpenGL extension testing from Tcl
    * Tcl Extension Architecture (TEA) 3 compliant 

Togl does almost no OpenGL drawing itself, instead it manages OpenGL drawing
by calling various Tcl commands (a.k.a., callback functions). Those commands
can be C functions that call OpenGL (in)directly or another Tcl package
(e.g., Tcl3D).

Togl is copyrighted by Brian Paul (brian_e_paulATyahooDOTcom),
Benjamin Bederson (bedersonATcsDOTumdDOTedu), and Greg Couch
(gregcouchATusersDOTsourceforgeDOTnet). See the LICENSE file for details.

#-----------------------------------------------------------------------
%prep
%setup -q -n Togl%{version}

%patch0 -p1

#-----------------------------------------------------------------------
%build
%configure --disable-static --enable-shared
%make

#-----------------------------------------------------------------------
%clean
rm -rf %{buildroot}

#-----------------------------------------------------------------------
%install
%makeinstall_std
mkdir -p %{buildroot}%{_docdir}/togl
mv -f %{buildroot}%{_libdir}/Togl2.0/LICENSE %{buildroot}%{_docdir}/togl
cp -fa doc/* %{buildroot}%{_docdir}/togl
mv -f %{buildroot}%{_libdir}/Togl2.0/* %{buildroot}%{_libdir}

#-----------------------------------------------------------------------
%files
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/*.tcl
%{_includedir}/*.h
%dir %{_docdir}/togl
%{_docdir}/togl/*
