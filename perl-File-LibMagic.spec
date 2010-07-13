%define upstream_name	 File-LibMagic
%define upstream_version 0.96

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2

Summary:	Perl wrapper for libmagic
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tgz

Buildrequires: perl-devel
BuildRequires: libmagic-devel
BuildRequires: db4-devel
BuildRequires: gdbm-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The File::LibMagic is a simple perlinterface to libmagic from the
file-4.x package

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
%makeinstall_std

%check
make test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorarch}/File
%{perl_vendorarch}/auto/File
%{_mandir}/*/*

