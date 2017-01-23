PACKAGE_NAME=mendeleydesktop


all:
	rpmdev-setuptree
	spectool -g -R $(PACKAGE_NAME).spec
	cp README.md ~/rpmbuild/SOURCES/.
	cp *.patch ~/rpmbuild/SOURCES/
	rpmbuild -bs $(PACKAGE_NAME).spec


.PHONY: all
