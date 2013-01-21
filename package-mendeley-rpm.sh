#!/bin/bash


echo Parameters are $0 $1 $2 $2

BASEDIR=$(dirname $0)


rpmdev-setuptree

mendeley_binary_archive=mendeleydesktop-1.7.1-linux-x86_64.tar.bz2
mendeley_binary=mendeleydesktop-1.7.1-linux-x86_64

tar -xf ${mendeley_binary_archive}



version=`grep Version mendeley.spec | awk '{print $2}'`
mkdir -p ./BUILD/mendeley-${version}

cp -R ${mendeley_binary}/* ./BUILD/mendeley-${version}/.
cp mendeley-0.1.0-install.patch ./BUILD/mendeley-${version}/.
cp mendeley.spec ./BUILD/mendeley-${version}/.
#cp LICENSE ./BUILD/mendeley-${version}/.

cp mendeley.spec ~/rpmbuild/SPECS/.

cp mendeley-0.1.0-install.patch ~/rpmbuild/SOURCES/.

tar czf ~/rpmbuild/SOURCES/mendeley-${version}.tar.gz -C ./BUILD mendeley-${version}


#mendeley_binary=`grep Source1 mendeley.spec | awk '{print $2}'`

#cp ${mendeley_binary} ~/rpmbuild/SOURCES/.

rpmbuild -ba ~/rpmbuild/SPECS/mendeley.spec
