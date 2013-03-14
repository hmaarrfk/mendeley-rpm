#!/bin/bash


echo Parameters are $0 $1 $2 $2

BASEDIR=$(dirname $0)


rpmdev-setuptree

mendeley_binary_archive=`grep Source1 mendeley.spec | awk '{print $2}'`

rpm -rf ~/rpmbuild


version=`grep Version mendeley.spec | awk '{print $2}'`
mkdir -p ./BUILD/mendeley-${version}

#cp -R ${mendeley_binary_archive} ./BUILD/mendeley-${version}/.
cp README.md ./BUILD/mendeley-${version}/README
cp mendeleydesktop ./BUILD/mendeley-${version}/.
cp mendeley.spec ./BUILD/mendeley-${version}/.


cp mendeley.spec ~/rpmbuild/SPECS/.

tar czf ~/rpmbuild/SOURCES/mendeley-${version}.tar.gz -C ./BUILD mendeley-${version}
cp ${mendeley_binary_archive} ~/rpmbuild/SOURCES/

rm -rf ./BUILD

rpmbuild -ba ~/rpmbuild/SPECS/mendeley.spec

