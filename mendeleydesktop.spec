Name:       mendeleydesktop
Version:    1.9.1
# Make sure to use rpmdev-bumpspec to update this
Release:    13%{?dist}
Summary:    Unofficial Mendeley RPM package.

#Group:
License:    Proprietary
URL:        https://github.com/hmaarrfk/mendeley-rpm
Source0:    %{name}-%{version}-linux-%{_target_cpu}.tar.bz2
Source1:    README.md
Patch0:     mendeleydesktop-desktopfile.patch

# FIXME: Build also for 32bits
ExclusiveArch: x86_64 i486


%description
This is a repackaged version of what is available
on the Mendeley website and attempts to make use
of system libraries instead of the ones packaged
with Mendeley.

%global debug_package %{nil}


%prep
%setup -q -n %{name}-%{version}-linux-%{_target_cpu}
cp -p %SOURCE1 .
%patch0


%build
# Remove unecessary libs
rm -rf lib/qt
rm -rf lib/ssl

# Remove the launching script not used in this distribution
rm -f  bin/mendeleydesktop
# and the stupid link-handler
# TODO: emulate link handler functionality in the spec file
rm -f  bin/install-mendeley-link-handler.sh

# Rename binary and move it to the proper location
mv     lib/mendeleydesktop/libexec/mendeleydesktop.%{_target_cpu} bin/mendeleydesktop

# Remove the problematic icons 48x48 and 64x64 look bad because they have a white border
rm  -rf share/icons/hicolor/48x48
rm  -rf share/icons/hicolor/64x64

# Remove libexec including the Updater binary
# Update should be done using the package manager
rm -rf lib/mendeleydesktop/libexec

# Change them as executable so that the packager treats them as such
# The packager consideres executable libraries as libraries the package provides
chmod +x lib/libPDFNetC.*
chmod +x lib/libMendeley.*


%install
mkdir -p %{buildroot}%{_defaultdocdir}
mkdir -p %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_bindir}

cp -R share/doc/*           %{buildroot}%{_defaultdocdir}%{name}-%{version}
cp -R README.md             %{buildroot}%{_defaultdocdir}%{name}-%{version}/README-DIST.md
cp -R share/icons           %{buildroot}%{_datadir}
cp -R share/mendeleydesktop %{buildroot}%{_datadir}
cp -R lib/*                 %{buildroot}%{_libdir}
cp -R bin/*                 %{buildroot}%{_bindir}

desktop-file-install --delete-original          \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
share/applications/mendeleydesktop.desktop


%clean
rm -rf %{buildroot}


%post
# Update shared libraries
/sbin/ldconfig

/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
# Update shared libraries
/sbin/ldconfig

/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*


# Make sure to use rpmdev-bumpspec to update this
%changelog
* Sun Jul 14 2013 Mark Harfouche - 1.9.1-13
- Added the /sbin/ldconfig lines to the %post and %postrun sections

* Sat Jul 13 2013 Mark Harfouche - 1.9.1-12
- Spec file should be i686 compatible

* Sat Jul 13 2013 Mark Harfouche - 1.9.1-11
- Removed the 48x48 and 64x64 icons because they looked bad (they used white
  instead of alpha making them look horrible)

* Sat Jul 13 2013 Filipe Manco - 1.9.1-10
- Cleanup spec file.

* Sat Jul 13 2013 Filipe Manco - 1.9.1-9
- Greatly simplify spec file.

* Sat Jul 13 2013 Mark Harfouche - 1.9.1-8
- Fixed the .desktop file so that it would have the option --unix-distro-build
  at the end of the exec command

* Sat Jul 13 2013 Mark Harfouche - 1.9.1-7
- I dont think we need the dummy launcher, mendeley seems to run well without
  it, so I moved the executable from libexec to bin

* Sat Jul 13 2013 Mark Harfouche - 1.9.1-6
- Changed the name of the desktopfile to reflect the correct name of the wmclass

* Sat Jul 13 2013 Mark Harfouche - 1.9.1-5
- Removed the explicit dependencies since I think the packager finds them
  automatically

* Sat Jul 13 2013 Mark Harfouche - 1.9.1-4
- Changed the libexec name to mendeleydestop as suggested in Revision 2 but
  added the appropriate modifications to the spec file.

* Sat Jul 13 2013 Mark Harfouche - 1.9.1-3
- Undid the modifications of the previous version

* Fri Jul 12 2013 Filipe Manco - 1.9.1-2
- Binary use mendeleydesktop instead of mendelydesktop.x86_64

* Fri Jul 12 2013 Filipe Manco - 1.9.1-1
- Update to Mendeley version 1.9.1

* Sun Apr 7 2013 Chris Fallin - 1.8.4-1
- Updated to Mendeley version 1.8.4

* Thu Mar 21 2013 Chris Fallin - 1.8.3-1
- Updated to Mendeley version 1.8.3

* Wed Mar 13 2013 Mark Harfouche - 1.8.2-2
- Cleaned up the spec file

* Wed Mar 13 2013 Chris Fallin - 1.8.2-1
- Updated to Mendeley version 1.8.2

* Thu Jan 31 2013 Mark Harfouche - 1.8.0-1
- Updated to Mendeley version 1.8.0

* Tue Jan 22 2013 Mark Harfouche - 0.1.0-2
- Fixed the dependency for libpng.so.3


