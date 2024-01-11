Name:		plasma6-akonadi-notes
Version:	24.01.90
Release:	1
Summary:	Akonadi Notes Integration
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/KDE
URL:		https://www.kde.org/
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/akonadi-notes-%{version}.tar.xz
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(KPim6Akonadi)
BuildRequires:	cmake(KPim6Mime)
BuildRequires:	boost-devel
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant

%define major 6
%define libname %mklibname KPim6AkonadiNotes

Requires: %{libname} = %{EVRD}

%description
Akonadi Notes Integration.

%files -f akonadinotes6.lang

#--------------------------------------------------------------------

%package -n %{libname}
Summary:      Akonadi Notes Integration main library
Group:        System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
Akonadi Notes Integration main library.

%files -n %{libname}
%{_libdir}/libKPim6AkonadiNotes.so*

#--------------------------------------------------------------------

%define develname %mklibname KPim6AkonadiNotes -d

%package -n %{develname}
Summary:        Devel stuff for %{name}
Group:          Development/KDE and Qt
Requires:       %{libname} = %{EVRD}

%description -n %{develname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{develname}
%{_includedir}/KPim6/AkonadiNotes
%{_libdir}/cmake/KPim6AkonadiNotes/

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n akonadi-notes-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang akonadinotes6
