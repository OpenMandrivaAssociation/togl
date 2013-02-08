# required by netgen
%define	compat_17	1

Name:		togl
Group:		Sciences/Other
Version:	2.0
Release:	3
Summary:	Togl - a Tk OpenGL widget
License:	BSD like
URL:		http://togl.sourceforge.net/index.html
Source0:	Togl2.0-src.tar.gz
Source1:	Togl-1.7.tar.gz

BuildRequires:	GL-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	libx11-devel
BuildRequires:	libxmu-devel
Patch0:		Togl2.0-build.patch

%description
Togl is a Tk widget for OpenGL rendering. Togl was originally based on OGLTK,
written by Benjamin Bederson at the University of New Mexico. Togl's main
features are:

    * unifies MS Windows, X11 (Linux/IRIX/...), and Mac OS X Aqua support
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
%setup -q -n Togl%{version} -a 1

%patch0 -p1

#-----------------------------------------------------------------------
%build
%configure2_5x --disable-static --enable-shared
%make
%if %{compat_17}
  pushd Togl-1.7
    %configure2_5x --disable-static --enable-shared
    %make
  popd
%endif

#-----------------------------------------------------------------------
%clean
rm -rf %{buildroot}

#-----------------------------------------------------------------------
%install
%if %{compat_17}
  pushd Togl-1.7
    %makeinstall_std
    mkdir -p %{buildroot}%{_includedir}/Togl1.7
    rm -f %{buildroot}%{_includedir}/togl_ws.h
    mv -f %{buildroot}%{_includedir}/togl.h %{buildroot}%{_includedir}/Togl1.7
    mv -f %{buildroot}%{_libdir}/Togl1.7/* %{buildroot}%{_libdir}
    mv -f %{buildroot}%{_libdir}/{,Togl1.7-}pkgIndex.tcl
    rmdir %{buildroot}%{_libdir}/Togl1.7
  popd
%endif
%makeinstall_std
mkdir -p %{buildroot}%{_docdir}/togl
mv -f %{buildroot}%{_libdir}/Togl2.0/LICENSE %{buildroot}%{_docdir}/togl
cp -fa doc/* %{buildroot}%{_docdir}/togl
mv -f %{buildroot}%{_libdir}/Togl2.0/* %{buildroot}%{_libdir}
mv -f %{buildroot}%{_libdir}/{,Togl2.0-}pkgIndex.tcl
rmdir %{buildroot}%{_libdir}/Togl2.0

#-----------------------------------------------------------------------
%files
%defattr(-,root,root)
%{_libdir}/libTogl2.0.so
%{_libdir}/lib*.a
%{_libdir}/*.tcl
%{_includedir}/*.h
%dir %{_docdir}/togl
%{_docdir}/togl/*
%if %{compat_17}
  %{_libdir}/libTogl1.7.so
  %dir %{_includedir}/Togl1.7
  %{_includedir}/Togl1.7/*.h
%endif


%changelog
* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 2.0-2mdv2011.0
+ Revision: 594031
- fix build

* Thu Feb 25 2010 Paulo Andrade <pcpa@mandriva.com.br> 2.0-2mdv2010.1
+ Revision: 511369
- Add Togl1.7 compat and non conflicting build

* Wed Feb 24 2010 Paulo Andrade <pcpa@mandriva.com.br> 2.0-1mdv2010.1
+ Revision: 510775
- Import togl
- togl

