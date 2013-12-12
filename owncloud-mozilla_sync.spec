%define		pkgname	mozilla_sync
%define		pkgid	161793
Summary:	Service for synchronization Firefox settings between devices
Name:		owncloud-%{pkgname}
Version:	1.2.2
Release:	0.1
License:	AGPL
Group:		Development/Languages/PHP
Source0:	http://apps.owncloud.com/CONTENT/content-files/%{pkgid}-mozilla_sync-%{version}.zip
# Source0-md5:	906b504f96df137f8922315a43c93d9f
URL:		http://apps.owncloud.com/content/show.php/Mozilla+Sync+Service?content=161793
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
