%define __libtoolize :

%define glib2_version 2.0.1

%define po_package libgtop-2.0

Name:		libgtop2
Summary:        libgtop library (version 2)
Version: 	2.28.0
Release: 	3%{?dist}
License: 	GPLv2+
URL:            http://download.gnome.org/sources/libgtop/2.28
Group:          System Environment/Libraries
Source: 	http://download.gnome.org/sources/libgtop/2.28/libgtop-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	glib2-devel >= %{glib2_version}
BuildRequires:  texinfo libtool gettext
BuildRequires:  intltool

Patch0:         add-more-cpus.patch
Patch1:		translation-fixes.patch

%description
libgtop is a library for portably obtaining information about processes,
such as their PID, memory usage, etc.

%package devel
Summary: Libraries and include files for developing with libgtop
Group: Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= %{glib2_version}
Requires: 	pkgconfig
Requires:	gtk-doc

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with libgtop.

%prep
%setup -q -n libgtop-%{version}

%patch0 -p1 -b .add-more-cpus
%patch1 -p1 -b .translation-fixes

%build
%configure --disable-gtk-doc --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{po_package}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{po_package}.lang

%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%{_libdir}/*.so
%{_includedir}/libgtop-2.0
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/html/libgtop
# not worth fooling with
%exclude %{_datadir}/info

%changelog
* Tue Jun 29 2010 Soren Sandmann <ssp@redhat.com> - 2.28.0-3
- Add translation fixes from bug 589223

* Tue Jun 29 2010 Soren Sandmann <ssp@redhat.com> - 2.28.0-2
- Add patch to increase number of CPUs to 256

* Mon Sep 21 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 31 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.3-1
- Update to 2.27.3
- http://download.gnome.org/sources/libgtop/2.27/libgtop-2.27.3.news

* Mon May 18 2009 Bastien Nocera <bnocera@redhat.com> 2.27.2-1
- Update to 2.27.2

* Mon May 18 2009 Bastien Nocera <bnocera@redhat.com> 2.27.1-1
- Update to 2.27.1

* Mon Apr 13 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.1-1
- Update to 2.26.1
- See http://download.gnome.org/sources/libgtop/2.26/libgtop-2.26.1.news

* Mon Mar  2 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.91-1
- Update to 2.25.91

* Wed Dec 17 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-4
- Rebuild for pkg-config auto-provides

* Sun Nov  9 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-3
- Read /proc/cpuinfo completely (#467455)

* Tue Sep 23 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Fri Aug 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.90-1
- Update to 2.23.90

* Tue Jul  1 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.4-1
- Update to 2.23.4

* Tue May 27 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.2-1
- Update to 2.23.2

* Mon Apr  7 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.1-1
- Update to 2.22.1

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.0-1
- Update to 2.22.0

* Mon Feb 25 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.92-1
- Update to 2.21.92

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.21.5-2
- Autorebuild for GCC 4.3

* Mon Jan 14 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.5-1
- Update to 2.21.5

* Tue Nov 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.1-1
- Update top 2.21.1

* Sun Sep 16 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-1
- Update to 2.20.0

* Mon Sep  3 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.92-1
- Update to 2.19.92

* Wed Aug 22 2007 Adam Jackson <ajax@redhat.com> - 2.19.5-3
- Rebuild for PPC toolchain bug

* Wed Aug  8 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.5-2
- Update the license field

* Tue Jul 10 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.5-1
- Update to 2.19.5

* Mon Jun 18 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.4-1
- Update to 2.19.4

* Mon Jun  4 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.3-1
- Update to 2.19.3

* Sat May 19 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.2-1
- Update to 2.19.2

* Tue Feb 27 2007 Matthias Clasen <mclasen@redhat.com> - 2.14.8-1
- Update to 2.14.8

* Mon Feb 12 2007 Matthias Clasen <mclasen@redhat.com> - 2.14.7-1
- Update to 2.14.7

* Sun Jan 14 2007 Matthias Clasen <mclasen@redhat.com> - 2.14.6-1
- Update to 2.14.6

* Tue Dec  5 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.5-1
- Update to 2.14.5
- Require pkgconfig in the -devel package

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 2.14.4-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Wed Sep 20 2006 Soren Sandmann <sandmann@redhat.com> - 2.14.4-1.fc6
- Update to 2.14.4. The only change from 2.14.3 is the fix for 
  b.r.c 206616 / b.g.o 255290. 

* Tue Sep  5 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.3-1.fc6
- Update to 2.14.3

* Thu Aug  3 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2-1.fc6
- Update to 2.14.2

* Wed Jul 13 2006 Jesse Keating <jkeating@redhat.com> - 2.14.1-4
- rebuild
- add missing br libtool gettext

* Tue Jun  6 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.1-3
- Rebuild

* Mon Apr 10 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.1-2
- Update to 2.14.1

* Mon Mar 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.0-1
- Update to 2.14.0

* Mon Feb 27 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.92-1
- Update to 2.13.92

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.13.3-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.13.3-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Thu Jan 24 2006 Matthias Clasen <mclasen@redhat.com>
- Update to 2.13.3

* Tue Jan 03 2006 Matthias Clasen <mclasen@redhat.com>
- Update to 2.13.2

* Thu Dec 15 2005 Matthias Clasen <mclasen@redhat.com>
- Update to 2.13.1

* Wed Dec 14 2005 Matthias Clasen <mclasen@redhat.com>
- Update to 2.13.0

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Dec  1 2005 Matthias Clasen <mclasen@redhat.com> - 2.12.2-1
- Update to 2.12.2
- Drop static libraries

* Wed Sep  7 2005 Matthias Clasen <mclasen@redhat.com> - 2.12.0-1
- Update to 2.12.0

* Tue Aug 16 2005 Matthias Clasen <mclasen@redhat.com> 
- New upstream version

* Thu Aug  4 2005 Matthias Clasen <mclasen@redhat.com> - 2.11.90-1
- New upstream version

* Tue Jul 12 2005 Matthias Clasen <mclasen@redhat.com> - 2.11.1-1
- Update to newer upstream version

* Fri Apr 29 2005 David Zeuthen <davidz@redhat.com> - 2.10.1-1
- New upstream version (#155188)

* Fri Mar 18 2005 David Zeuthen <davidz@redhat.com> - 2.10.0-2
- Rebuilt

* Fri Mar 18 2005 David Zeuthen <davidz@redhat.com> - 2.10.0-1
- Even newer upstream version

* Fri Mar 18 2005 David Zeuthen <davidz@redhat.com> - 2.9.92-1
- New upstream version

* Fri Mar  4 2005 David Zeuthen <davidz@redhat.com> - 2.9.91-2
- Rebuild

* Wed Feb  9 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.91-1
- Update to 2.9.91

* Thu Jan 27 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.90-1
- Update to 2.9.90

* Wed Sep 22 2004 Alexander Larsson <alexl@redhat.com> - 2.8.0-1
- update to 2.8.0

* Tue Aug 31 2004 Alex Larsson <alexl@redhat.com> 2.7.92-1
- update to 2.7.92

* Thu Aug  5 2004 Mark McLoughlin <markmc@redhat.com> 2.7.90-1
- Update to 2.7.90

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Apr 13 2004 Warren Togami <wtogami@redhat.com> 2.5.2-2
- BR libtool texinfo gettext

* Fri Mar 12 2004 Alex Larsson <alexl@redhat.com> 2.5.2-1
- update to 2.5.2

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 25 2004 Alexander Larsson <alexl@redhat.com> 2.5.1-1
- update to 2.5.1

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jan 26 2004 Alexander Larsson <alexl@redhat.com> 2.5.0-1
- update to 2.5.0

* Wed Jul 23 2003 Havoc Pennington <hp@redhat.com>
- automated rebuild

* Fri Jul 18 2003 Havoc Pennington <hp@redhat.com> 2.0.2-1
- 2.0.2
- forward port prog_as patch
- attempted fix to handle >4mb on IA32, #98676

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 11 2003 Bill Nottingham <notting@redhat.com> 2.0.0-10
- fix URL (#79390)

* Mon Feb  3 2003 Havoc Pennington <hp@redhat.com> 2.0.0-9
- rebuild

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 19 2002 Elliot Lee <sopwith@redhat.com> 2.0.0-7
- More missing libXau hackery (prog_as.patch so we can run auto* to pull 
in an updated libtool)
- _smp_mflags

* Wed Dec  4 2002 Havoc Pennington <hp@redhat.com>
- rebuild more, woot!

* Mon Dec  2 2002 Havoc Pennington <hp@redhat.com>
- rebuild to try and fix weird undefined Xau symbols

* Fri Nov  8 2002 Havoc Pennington <hp@redhat.com>
- rebuild
- remove nonexistent doc files
- fix uninstalled but unpackaged files

* Tue Jun 25 2002 Owen Taylor <otaylor@redhat.com>
- Fix missing po files

* Sat Jun 15 2002 Havoc Pennington <hp@redhat.com>
- 2.0.0
- check file list, lose libgnomesupport

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue May 21 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Thu Apr 18 2002 Havoc Pennington <hp@redhat.com>
- .la files evil

* Thu Apr 18 2002 Havoc Pennington <hp@redhat.com>
- rebuild for glib 2.0

* Thu Feb 14 2002 Havoc Pennington <hp@redhat.com>
- 1.90.2

* Mon Jan 28 2002 Havoc Pennington <hp@redhat.com>
- Initial build

