%define upstream_version 1.23
%define	module	File-LibMagic
Name:		perl-%{module}
Version:	1.23
Release:	1

Summary:	Perl wrapper for libmagic

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/houseabsolute/File-LibMagic
Source0:	https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/File-LibMagic-1.23.tar.gz

BuildRequires:	make
Buildrequires:	perl-devel
BuildRequires:	magic-devel

%description
The File::LibMagic is a simple perlinterface to libmagic from the
file-4.x package

%prep
%setup -q -n %{module}-%{version}

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



