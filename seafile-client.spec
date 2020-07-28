%global __cmake_in_source_build 1
%global _hardened_build 1

Name:           seafile-client
Version:        7.0.4
Release:        4%{?dist}
Summary:        Seafile cloud storage desktop client

License:        ASL 2.0
URL:            https://www.seafile.com/
Source0:        https://github.com/haiwen/%{name}/archive/v%{version}.tar.gz
Source1:        seafile.appdata.xml
Patch0:         fix-qt-build.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  cmake
BuildRequires:  sqlite-devel
BuildRequires:  jansson-devel
BuildRequires:  openssl-devel
BuildRequires:  libuuid-devel
BuildRequires:  libsearpc-devel
BuildRequires:  ccnet-devel
BuildRequires:  seafile-devel = %{version}
BuildRequires:  qt5-qtbase
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qttools-devel

Requires:       seafile = %{version}


%description
Seafile is a next-generation open source cloud storage system, with advanced
support for file syncing, privacy protection and teamwork.

Seafile allows users to create groups with file syncing, wiki, and discussion
to enable easy collaboration around documents within a team.


%prep
%autosetup -p1 -n %{name}-%{version}


%build
%cmake -DUSE_QT5=ON -DCMAKE_BUILD_TYPE=Release -DBUILD_SHIBBOLETH_SUPPORT=ON .
make CFLAGS="%{optflags}" %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/seafile.desktop
mkdir -p %{buildroot}%{_datarootdir}/appdata/
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/seafile.appdata.xml
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/seafile.appdata.xml

%files
%doc README.md
%license LICENSE
%{_bindir}/seafile-applet
%{_datadir}/applications/seafile.desktop
%{_datadir}/icons/hicolor/scalable/apps/seafile.svg
%{_datadir}/icons/hicolor/16x16/apps/seafile.png
%{_datadir}/icons/hicolor/22x22/apps/seafile.png
%{_datadir}/icons/hicolor/24x24/apps/seafile.png
%{_datadir}/icons/hicolor/32x32/apps/seafile.png
%{_datadir}/icons/hicolor/48x48/apps/seafile.png
%{_datadir}/icons/hicolor/128x128/apps/seafile.png
%{_datadir}/pixmaps/seafile.png
%{_datadir}/appdata/seafile.appdata.xml


%changelog
* Sat Jul 25 2020 Marie Loise Nolden <loise@kde.org> - 7.0.4-4
- fix qt 5.15 build (append Patch0)

* Fri Jul 24 2020 Jeff Law <law@redhat.com> - 7.0.4-3
- Use __cmake_in_source_build

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 03 2019 Julien Enselme <jujens@jujens.eu> - 7.0.4-1
- Update to 7.0.4
- Make this package compatible with Python3

* Tue Aug 20 2019 Julien Enselme <jujens@jujens.eu> - 7.0.2-1
- Update to 7.0.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 23 2019 Julien Enselme <jujens@jujens.eu> - 6.2.11-1
- Update to 6.2.11

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Julien Enselme <jujens@jujens.eu> - 6.2.5-1
- Update to 6.2.5

* Wed Aug 01 2018 Julien Enselme <jujens@jujens.eu> - 6.2.3-1
- Update to 6.2.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 13 2018 Julien Enselme <jujens@jujens.eu> - 6.1.6-2
- Build with OpenSSL 1.1

* Tue Mar 13 2018 Julien Enselme <jujens@jujens.eu> - 6.1.6-1
- Update to 6.1.6

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.1.4-2
- Remove obsolete scriptlets

* Wed Dec 27 2017 Julien Enselme <jujens@jujens.eu> - 6.1.4-1
- Update to 6.1.4

* Mon Nov 06 2017 Julien Enselme <jujens@jujens.eu> - 6.1.3-1
- Update to 6.1.3

* Fri Aug 11 2017 Kalev Lember <klember@redhat.com> - 6.1.0-2
- Bump and rebuild for an rpm signing issue

* Thu Aug 10 2017 Julien Enselme <jujens@jujens.eu> - 6.1.0-1
- Update to 6.1.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Julien Enselme <jujens@jujens.eu> - 6.0.6-2
- Revert to SSL10 compat.

* Sun May 07 2017 Julien Enselme <jujens@jujens.eu> - 6.0.6-1
- Update to 6.0.6
- Build with openSSL 1.0

* Tue Mar 07 2017 Julien Enselme <jujens@jujens.eu> - 6.0.4-2
- Use correct version of ccnet and seafile

* Tue Mar 07 2017 Julien Enselme <jujens@jujens.eu> - 6.0.4-1
- Update to 6.0.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Julien Enselme - 6.0.0-3
- Enable Shibboleth sign on

* Sun Oct 30 2016 Julien Enselme - 6.0.0-2
- Compile against compat-openssl10 until it is compatible with OpenSSL 1.1

* Sun Oct 30 2016 Julien Enselme - 6.0.0-1
- Update to 6.0.0
- Unretire package

* Wed Jun 08 2016 Richard Hughes <richard@hughsie.com> - 5.1.1-4
- Fix AppData file to have the same application ID as the desktop file and
  update it to a more modern format.

* Fri Jun 03 2016 Nikos Roussos <comzeradd@fedoraproject.org> - 5.1.1-3
- Update icons cache

* Fri Jun 03 2016 Nikos Roussos <comzeradd@fedoraproject.org> - 5.1.1-2
- Use https for upstream url
- Add appdata file

* Wed Jun 01 2016 Nikos Roussos <comzeradd@fedoraproject.org> - 5.1.1-1
- Update to 5.1.1
- Switch to qt5

* Mon Feb 08 2016 Nikos Roussos <comzeradd@fedoraproject.org> - 5.0.4-1
- Update to 5.0.4

* Wed Sep 16 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 4.3.4-1
- Update to 4.3.4

* Sat Apr 11 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 4.1.4-1
- Update to 4.1.4
- Hardened build

* Wed Nov 05 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 3.1.8-1
- Update to 3.1.8

* Tue Aug 12 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 3.1.4-1
- Initial version of the package
