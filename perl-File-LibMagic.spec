%define module	File-LibMagic
%define name	perl-%{module}
%define version	0.82
%define release	%mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perlwrapper for libmagic
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/F/FI/FITZNER/%{module}-%{version}.tar.bz2
Patch0:         %name.ldflags.patch
Url:		http://search.cpan.org/dist/%{module}
BuildRoot:	%{_tmppath}/%{name}-buildroot/
Buildrequires: perl-devel
BuildRequires: libmagic-devel
BuildRequires: db2-devel
BuildRequires: gdbm-devel
%description
The File::LibMagic is a simple perlinterface to libmagic from the
file-4.x package

%prep
%setup -q -n %{module}-%{version}
%patch0 -b .ldflags -p0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%check
make test

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/*
%{_mandir}/*/*

