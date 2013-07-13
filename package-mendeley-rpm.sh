#!/bin/bash

rpmdev-setuptree

cp mendeley.spec ~/rpmbuild/SPECS/
cp *.tar.bz2 ~/rpmbuild/SOURCES/
cp mendeleydesktop-desktopfile.patch ~/rpmbuild/SOURCES/
cp README.md ~/rpmbuild/SOURCES/

rpmbuild -ba ~/rpmbuild/SPECS/mendeley.spec

