%global debug_package %{nil}

Summary:	EGL External Platform Interface headers
Name:		eglexternalplatform
Version:	1.2
Release:	1
Group:		System/Libraries
License:	MIT
URL:		https://github.com/NVIDIA
Source0:	https://github.com/NVIDIA/eglexternalplatform/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
Patch0:         https://src.fedoraproject.org/rpms/eglexternalplatform/blob/rawhide/f/eglexternalplatform-noarch.patch
BuildRequires:  meson
BuildArch:      noarch

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
%meson
%meson_build

%install
%meson_build

%files devel
%doc README.md samples
%license COPYING
%{_includedir}/*
%{_datadir}/pkgconfig/eglexternalplatform.pc
