SPEC_NAME=mendeleydesktop.spec


all:
	rpmdev-setuptree
	spectool -g -R *.spec
	cp README.md ~/rpmbuild/SOURCES/.
	#cp *.spec ~/rpmbuild/SPECS/
	#cp *.tar.* ~/rpmbuild/SOURCES/
	cp *.patch ~/rpmbuild/SOURCES/
	#rpmbuild -bs ~/rpmbuild/SPECS/mendeleydesktop.spec
	rpmbuild -bs $(SPEC_NAME)


.PHONY: all
