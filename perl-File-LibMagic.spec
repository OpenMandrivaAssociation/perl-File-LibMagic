%define module	File-LibMagic
%define name	perl-%{module}
%define version	0.89
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl wrapper for libmagic
License:	GPL or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/File/%{module}-%{version}.tgz
Buildrequires: perl-devel
BuildRequires: libmagic-devel
BuildRequires: db4-devel
BuildRequires: gdbm-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The File::LibMagic is a simple perlinterface to libmagic from the
file-4.x package

%prep
%setup -q -n %{module}-%{version}

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

