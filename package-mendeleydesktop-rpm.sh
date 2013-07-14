#!/bin/bash

rpmdev-setuptree

cp mendeleydesktop.spec ~/rpmbuild/SPECS/
cp *.tar.bz2 ~/rpmbuild/SOURCES/
cp mendeleydesktop-desktopfile.patch ~/rpmbuild/SOURCES/
cp README.md ~/rpmbuild/SOURCES/


# build for both archetectures
rpmbuild -bb --target x86_64 ~/rpmbuild/SPECS/mendeleydesktop.spec
rpmbuild -bb --target i486   ~/rpmbuild/SPECS/mendeleydesktop.spec

