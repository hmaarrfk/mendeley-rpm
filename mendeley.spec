Name:       mendeley
Version:    0.1.0
Release:    1%{?dist}
Summary:    Unofficial Mendeley RPM package.

#Group:		
License:    Proprietary
URL:        https://github.com/hmaarrfk/mendeley-rpm
Source0:    mendeley-%{version}.tar.gz
#Source1:    mendeleydesktop-1.7.1-linux-x86_64.tar.bz2

# This patch stops the "install" script from executing everytime
# by simply making it exit cleanly when called
Patch0:     mendeley-0.1.0-install.patch


Provides: libPDFNetC
Provides: libMendeley
#BuildRequires:  desktop-file-utils
#Requires:libpng-compat >= 1.5
#Requires:libpng10>=1.0
#Requires:qt-x11>=4.8.4
#Requires:qt>= 4.8.4
#Requires:qtwebkit>= 2.2.2
#Requires:openssl>= 0.9.8
Requires: libpng-compat >= 1.5, qt-x11, qt, qtwebkit, openssl, libPDFNetC, libPDFNetC, libMendeley


%description
This is a repackaged version of what is available on the Mendeley website and attempts to make use of system libraries instead of the ones packaged with Mendeley.

%global debug_package %{nil}


%prep
%setup -q
%patch0 -p1


%build
# Need to remove the useless files
ls -lah
rm -rf ./lib/qt
rm -rf ./lib/ssl
#rm ./lib/mendeleydesktop/libexec/Updater


%install
mkdir -p %{buildroot}%{_defaultdocdir}
mkdir -p %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_bindir}
cp -R share/doc/*           %{buildroot}%{_defaultdocdir}
cp -R share/icons           %{buildroot}%{_datadir}
cp -R share/mendeleydesktop %{buildroot}%{_datadir}
cp -R lib/*                 %{buildroot}%{_libdir}
chmod +x %{buildroot}%{_libdir}/libPDFNetC.so
chmod +x %{buildroot}%{_libdir}/libMendeley.so.1.7.1
cp -R bin/*                 %{buildroot}%{_bindir}
chmod +x %{buildroot}%{_bindir}/install-mendeley-link-handler.sh
chmod +x %{buildroot}%{_bindir}/mendeleydesktop

desktop-file-install --delete-original --dir=${RPM_BUILD_ROOT}%{_datadir}/applications ./share/applications/mendeleydesktop.desktop

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
%doc README LICENSE
%{_bindir}/install-mendeley-link-handler.sh
%{_bindir}/mendeleydesktop
%{_libdir}/libMendeley.*
%{_libdir}/libPDFNetC.so
%{_libdir}/mendeleydesktop
%{_datadir}/applications/mendeleydesktop.desktop
%{_defaultdocdir}/mendeleydesktop
%{_datadir}/icons/hicolor/*/apps/mendeleydesktop.png
%{_datadir}/mendeleydesktop


%changelog

