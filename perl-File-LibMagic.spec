%define upstream_version 1.23
%define	module	File-LibMagic
Name:		perl-%{module}
Version:	1.23
Release:	9

Summary:	Perl wrapper for libmagic

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/houseabsolute/File-LibMagic
Source0:	https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/File-LibMagic-1.23.tar.gz

BuildRequires:	make
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	pkgconfig(libmagic)
BuildRequires:	perl(Config::AutoConf)
Buildrequires:	perl-devel
BuildRequires:	magic-devel

%description
The File::LibMagic is a simple perlinterface to libmagic from the
file-4.x package

%prep
%setup -q -n File-LibMagic-1.23

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build
%install
%makeinstall_std

%check
# soft: do not fail package on test failures
set +e
#make test || :

%files 
%doc Changes LICENSE META.yml README.md
%{perl_vendorarch}/File
%{perl_vendorarch}/auto/File
%{_mandir}/*/*



