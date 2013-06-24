%define		pkgname	mozilla_sync
Summary:	Service for synchronization Firefox settings between devices
Name:		owncloud-%{pkgname}
Version:	1.0
Release:	0.1
License:	AGPL
Group:		Development/Languages/PHP
Source0:	http://apps.owncloud.com/CONTENT/content-files/155251-mozilla_sync.zip
# Source0-md5:	143683e18371fa70033cf929501ea50f
URL:		http://apps.owncloud.com/content/show.php/Mozilla+Sync+Service?content=155251
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	owncloud >= 5.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/owncloud/apps/%{pkgname}

%description
Service for synchronization Firefox settings between devices.

%prep
%setup -q -n %{pkgname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}

cp -a * $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
