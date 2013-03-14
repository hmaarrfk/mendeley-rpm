Name:       mendeley
Version:    1.8.2
# Make sure to use rpmdev-bumpspec to update this
Release:    4%{?dist}
Summary:    Unofficial Mendeley RPM package.

#Group:
License:    Proprietary
URL:        https://github.com/hmaarrfk/mendeley-rpm
Source0:    mendeley-%{version}.tar.gz
Source1:    mendeleydesktop-1.8.2-linux-x86_64.tar.bz2

Provides: libPDFNetC
Provides: libMendeley
Requires: libpng >= 1.5
Requires: qt-x11 >= 4.8.4
Requires: qt >= 4.8.4
Requires: qtwebkit >= 2.2.2
Requires: openssl >= 0.9.8
Requires: libPDFNetC
Requires: libMendeley


%description
This is a repackaged version of what is available on the Mendeley website and attempts to make use of system libraries instead of the ones packaged with Mendeley.

%global debug_package %{nil}


%prep
%setup -q
tar -xf %SOURCE1


%build
# Need to remove the useless files
mendeley_extract_directory=$(basename "%SOURCE1")
mendeley_extract_directory="${mendeley_extract_directory%.*}"
mendeley_extract_directory="${mendeley_extract_directory%.*}"
rm -rf ${mendeley_extract_directory}/lib/qt
rm -rf ${mendeley_extract_directory}/lib/ssl
rm -f  ${mendeley_extract_directory}/lib/mendeleydesktop/libexec/Updater
rm -rf ${mendeley_extract_directory}/lib/mendeleydesktop/plugins
rm -f  ${mendeley_extract_directory}/bin/*
cp mendeleydesktop ${mendeley_extract_directory}/bin/.
chmod +x ${mendeley_extract_directory}/bin/mendeleydesktop
chmod +x ${mendeley_extract_directory}/lib/libPDFNetC.so
chmod +x ${mendeley_extract_directory}/lib/libMendeley.so.1.8.2



%install
mendeley_extract_directory=$(basename "%SOURCE1")
mendeley_extract_directory="${mendeley_extract_directory%.*}"
mendeley_extract_directory="${mendeley_extract_directory%.*}"
mkdir -p %{buildroot}%{_defaultdocdir}
mkdir -p %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_bindir}
cp -R ${mendeley_extract_directory}/share/doc/*           %{buildroot}%{_defaultdocdir}
cp -R ${mendeley_extract_directory}/share/icons           %{buildroot}%{_datadir}
cp -R ${mendeley_extract_directory}/share/mendeleydesktop %{buildroot}%{_datadir}
cp -R ${mendeley_extract_directory}/lib/*                 %{buildroot}%{_libdir}
cp -R ${mendeley_extract_directory}/bin/*                 %{buildroot}%{_bindir}

desktop-file-install --delete-original --dir=${RPM_BUILD_ROOT}%{_datadir}/applications ./${mendeley_extract_directory}/share/applications/mendeleydesktop.desktop

%clean
rm -rf %{buildroot}

%post
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
#%doc README LICENSE
%doc README
%{_bindir}/mendeleydesktop
%{_libdir}/libMendeley.*
%{_libdir}/libPDFNetC.so
%{_libdir}/mendeleydesktop
%{_datadir}/applications/mendeleydesktop.desktop
%{_defaultdocdir}/mendeleydesktop
%{_datadir}/icons/hicolor/*/apps/mendeleydesktop.png
%{_datadir}/mendeleydesktop



# Make sure to use rpmdev-bumpspec to update this
%changelog
* Wed Mar 13 2013 Mark Harfouche - 1.8.2-2
- Cleaned up the spec file

* Wed Mar 13 2013 Chris Fallin - 1.8.2-1
- Updated to Mendeley version 1.8.2

* Thu Jan 31 2013 Mark Harfouche - 1.8.0-1
- Updated to Mendeley version 1.8.0

* Tue Jan 22 2013 Mark Harfouche - 0.1.0-2
- Fixed the dependency for libpng.so.3


