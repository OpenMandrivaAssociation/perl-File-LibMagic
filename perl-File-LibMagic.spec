%define	module	File-LibMagic
%define	upstream_version 0.96

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl wrapper for libmagic
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/File/%{module}-%{upstream_version}.tgz

Buildrequires:	perl-devel
BuildRequires:	magic-devel

%description
The File::LibMagic is a simple perlinterface to libmagic from the
file-4.x package

%prep
%setup -q -n %{module}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
#make test

%files 
%doc README
%{perl_vendorarch}/File
%{perl_vendorarch}/auto/File
%{_mandir}/*/*


%changelog
* Thu Feb 02 2012 Per 脴yvind Karlsen <peroyvind@mandriva.org> 0.960.0-4
+ Revision: 770602
- drop gdbm-devel & db4-devel buildrequires as we never actually link against
  either..
- drop %%check, too lazy to update strings to test against..
- clean up spec
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 J茅r么me Quelin <jquelin@mandriva.org> 0.960.0-3mdv2011.0
+ Revision: 555822
- rebuild for perl 5.12

* Tue Jul 13 2010 J茅r么me Quelin <jquelin@mandriva.org> 0.960.0-2mdv2011.0
+ Revision: 552186
- rebuild

* Sun Jul 12 2009 J茅r么me Quelin <jquelin@mandriva.org> 0.960.0-1mdv2010.0
+ Revision: 395152
- update to 0.96
- using %%perl_convert_version
- fixed license field

* Fri May 01 2009 J茅r么me Quelin <jquelin@mandriva.org> 0.91-1mdv2010.0
+ Revision: 369735
- update to 0.91

* Fri Aug 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.89-1mdv2009.0
+ Revision: 272334
- new version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.82-9mdv2009.0
+ Revision: 268509
- rebuild early 2009.0 package (before pixel changes)

* Tue May 20 2008 Oden Eriksson <oeriksson@mandriva.com> 0.82-8mdv2009.0
+ Revision: 209546
- get rid of the db1-devel and db2-devel build deps, db4-devel is enough

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.82-7mdv2008.1
+ Revision: 152077
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 0.82-6mdv2008.0
+ Revision: 64798
- rebuild


* Mon Oct 10 2005 Nicolas L閏ureuil <neoclust@mandriva.org> 0.82-5mdk
- Fix previous mistake

* Fri Sep 30 2005 Nicolas L閏ureuil <neoclust@mandriva.org> 0.82-4mdk
- buildrequires fix

* Thu Sep 29 2005 Nicolas L閏ureuil <neoclust@mandriva.org> 0.82-3mdk
- fix url
- fix buildrequires

* Sun Jun 19 2005 Olivier Thauvin <nanardon@mandriva.org> 0.82-2mdk
- patch0: add search ldflags
- BuildRequires libmagic-devel

* Wed Jun 15 2005 Olivier Thauvin <nanardon@mandriva.org> 0.82-1mdk
- First mandriva spec

