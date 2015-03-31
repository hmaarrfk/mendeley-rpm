#!/bin/bash

rpmdev-setuptree

cp mendeleydesktop.spec ~/rpmbuild/SPECS/
cp *.tar.bz2 ~/rpmbuild/SOURCES/
cp mendeleydesktop-desktopfile.patch ~/rpmbuild/SOURCES/
cp README.md ~/rpmbuild/SOURCES/


# build for both archetectures
rpmbuild -bs ~/rpmbuild/SPECS/mendeleydesktop.spec

