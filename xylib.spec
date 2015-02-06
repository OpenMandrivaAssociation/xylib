%define		major 3
%define		libname %mklibname xy %{major}
%define		develname %mklibname xy -d

Name:		xylib
Version:	1.1
Release:	2
Summary:	A C++ x-y data reading library
License:	LGPLv2
Group:		System/Libraries
Url:		http://www.unipress.waw.pl/fityk/xylib/
Source0:	http://downloads.sourceforge.net/fityk/%{name}-%{version}.tar.bz2
BuildRequires:	boost-devel
BuildRequires:	zlib-devel
BuildRequires:	bzip2-devel

%description
Xylib is a portable C++ library for reading files that contain x-y 
data from powder diffraction, spectroscopy or other experimental 
methods.

Supported formats:

    * plain text (CSV or TSV or space-separated-values)
    * Crystallographic Information File for Powder Diffraction (pdCIF)
    * Siemens/Bruker UXD
    * Siemens/Bruker RAW ver. 1/2/3/4
    * Philips UDF
    * Philips RD (raw scan) V3
    * Rigaku DAT
    * Sietronics Sieray CPI
    * DBWS/DMPLOT data file
    * Canberra MCA (only one of Canberra MCA formats?)
    * XFIT/Koalariet XDD
    * RIET7/LHPM/CSRIET/ILL_D1A5/PSI_DMC DAT
    * Vamas ISO14976 (only experiment modes: SEM or MAPSV or MAPSVDP 
      are supported; only REGULAR scan_mode is supported)
    * Princeton Instruments WinSpec SPE (only 1-D data is supported)


%package util
Summary:	An utility to convert files supported by xylib to TSV
Group:		Sciences/Chemistry
Provides:	xyconv = %{version}-%{release}

%description util
This package contains xyconv, an utility provided with the xylib 
library to convert the files it supports to TSV.

%package -n %{libname}
Summary:	A C++ x-y data reading library
Group:		System/Libraries

%description -n %{libname}
Xylib is a portable C++ library for reading files that contain x-y
data from powder diffraction, spectroscopy or other experimental
methods.

Supported formats:

    * plain text (CSV or TSV or space-separated-values)
    * Crystallographic Information File for Powder Diffraction (pdCIF)
    * Siemens/Bruker UXD
    * Siemens/Bruker RAW ver. 1/2/3/4
    * Philips UDF
    * Philips RD (raw scan) V3
    * Rigaku DAT
    * Sietronics Sieray CPI
    * DBWS/DMPLOT data file
    * Canberra MCA (only one of Canberra MCA formats?)
    * XFIT/Koalariet XDD
    * RIET7/LHPM/CSRIET/ILL_D1A5/PSI_DMC DAT
    * Vamas ISO14976 (only experiment modes: SEM or MAPSV or MAPSVDP 
      are supported; only REGULAR scan_mode is supported)
    * Princeton Instruments WinSpec SPE (only 1-D data is supported)

This package contains the xylib shared library.

%package -n %{develname}
Summary:	Development files for xylib
Group:		Development/C++
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
This package contains the development files for xylib.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files util
%{_bindir}/xyconv
%{_mandir}/man1/xyconv*

%files -n %{libname}
%{_libdir}/libxy.so.%{major}*

%files -n %{develname}
%{_libdir}/libxy.so
%{_includedir}/*

