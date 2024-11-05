%define major 1
%define libname %mklibname rdkafka
%define devname %mklibname rdkafka -d

%define _disable_lto 1
%define _disable_ld_no_undefined 1

Name: librdkafka
Version: 2.6.0
Release: 1
Source0: https://github.com/confluentinc/librdkafka/archive/refs/tags/v%{version}.tar.gz
Summary: C library implementing the Apache Kafka protocol
URL: https://kafka.apache.org/
License: Apache-2.0
Group: System/Libraries
BuildRequires: cmake ninja

%description
C library implementing the Apache Kafka protocol

%package -n %{libname}
Summary: C library implementing the Apache Kafka protocol
Group: System/Libraries

%description -n %{libname}
C library implementing the Apache Kafka protocol

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1
%cmake \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*
%license %{_datadir}/licenses/%{name}
