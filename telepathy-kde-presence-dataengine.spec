%define rel 1

Summary:	Plasma dataengine for managing Telepathy account presence
Name:		telepathy-kde-presence-dataengine
Version:	0.2.0
Release:	%mkrel %{rel}
Url:		https://projects.kde.org/projects/playground/network/telepathy/telepathy-presence-dataengine
Source0:	ftp://ftp.kde.org/pub/kde/unstable/telepathy-kde/%version/src/%{name}-%version.tar.bz2
License:	GPLv2+
Group:		Graphical desktop/KDE
BuildRequires:	kdelibs4-devel
BuildRequires:	telepathy-qt4-devel
Provides:	plasma-dataengine-presence = %{version}-%{release}
Obsoletes:      telepathy-presence-dataengine < 0.2.0-0
Provides:       telepathy-presence-dataengine = %version-%release

%description
Plasma dataengine for managing Telepathy account presence.

%files
%{_kde_libdir}/kde4/plasma_engine_presence.so
%{_kde_appsdir}/plasma/services/presence.operations
%{_kde_services}/plasma-dataengine-presence.desktop

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build



