# (un)define the next line to either build for the newest or all current kernels

%define modname sunhme2g

Name:           %{modname}-kmod-common

Version:        0.0.1
Release:        1%{?dist}.1
Summary:        Common files for modified version of sunhme driver

Group:          System Environment/Kernel

License:        GPL
#URL:            
Source0:        sunhme-0.0.1.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
A patched version of sunhme driver that works on machines 
with more than 2GB of ram

%prep
%setup -q -c -T -a 0

%build

%install
rm -rf ${RPM_BUILD_ROOT}

install -D -m 755 sunhme/blacklist-sunhme.conf  ${RPM_BUILD_ROOT}%{_sysconfdir}/modprobe.d/blacklist-sunhme.conf

%files
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/modprobe.d/blacklist-sunhme.conf

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Apr 05 2013 Sebastian Mäki <sebastian@tico.fi> - 0.0.1-1
- initial spec
