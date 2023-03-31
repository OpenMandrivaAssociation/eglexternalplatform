%global debug_package %{nil}

Summary:	EGL External Platform Interface headers
Name:		eglexternalplatform
Version:	1.1
Release:	2
Group:		System/Libraries
License:	MIT
URL:		https://github.com/NVIDIA
Source0:	https://github.com/NVIDIA/eglexternalplatform/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch

%description
%summary.

%package devel
Summary:	Development files for %{name}
Group:		Development/C

%description devel
The %{name}-devel package contains the header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version} -p1

%build

%install
mkdir -p %{buildroot}%{_includedir}/
install -p -m 0644 interface/eglexternalplatform.h %{buildroot}%{_includedir}/
install -p -m 0644 interface/eglexternalplatformversion.h %{buildroot}%{_includedir}/
mkdir -p %{buildroot}%{_datadir}/pkgconfig/
install -p -m 0644 eglexternalplatform.pc %{buildroot}%{_datadir}/pkgconfig/

%files devel
%doc README.md samples
%license COPYING
%{_includedir}/*
%{_datadir}/pkgconfig/eglexternalplatform.pc
