Name:       mendeley
Version:    0.1.0
Release:    1%{?dist}
Summary:    Unofficial Mendeley RPM package.

#Group:		
#License:    MIT
URL:        https://github.com/hmaarrfk/mendeley-rpm
Source0:    mendeley-%{version}.tar.gz

# This patch stops the "install" script from executing everytime
# by simply making it exit cleanly when called
Patch0:     mendeley-0.1.0-install.patch


BuildRequires:	desktop-file-utils
Requires:   libpng-compat>=1.5
#Requires:  libpng10>=1.0
Requires:   qt-x11 >=4.8.4
Requires:   qt >= 4.8.4
Requires:   qtwebkit >= 2.2.2
Requires:   openssl >= 0.9.8

%description
This is a repackaged version of what is available on the Mendeley website and attempts to make use of system libraries instead of the ones packaged with Mendeley.


%prep
%setup -q
%patch0 -p1


%build
# Need to remove the useless files
ls -lah
rm -rf ./lib/qt
rm -rf ./lib/ssl


%install
cp -R share/doc/*           %{buildroot}%{_defaultdocdir}
cp -R share/icons           %{buildroot}%{_datadir}
cp -R share/mendeleydesktop %{buildroot}%{_datadir}
cp -R lib/*                 %{buildroot}%{_libdir}
cp -R bin/*                 %{buildroot}%{_bindir}

desktop-file-install --delete-original --dir=${RPM_BUILD_ROOT}%{_datadir}/applications ./share/applications/mendeleydesktop.desktop

%clean
rm -rf %{buildroot}

%post
%{_bindir}/xdg-icon-resource forceupdate --theme hicolor 2> /dev/null || :

%postun
%{_bindir}/xdg-icon-resource forceupdate --theme hicolor 2> /dev/null || :


%files
%doc README LICENSE



%changelog

