TOPDIR=$(shell rpm --eval "%{_topdir}")

PACKAGE_NAME=mendeleydesktop


all:
	rpmdev-setuptree
	spectool -g -R $(PACKAGE_NAME).spec
	cp README.md $(TOPDIR)/SOURCES/.
	cp *.patch $(TOPDIR)/SOURCES/
	rpmbuild -bs $(PACKAGE_NAME).spec


.PHONY: all
