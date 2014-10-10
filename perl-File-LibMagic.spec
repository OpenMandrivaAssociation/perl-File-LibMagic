%define	module	File-LibMagic
%define upstream_version 1.01

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl wrapper for libmagic

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/File/File-LibMagic-%{upstream_version}.tar.gz

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



