
all:
	rpmdev-setuptree
	spectool -g *.spec
	cp *.spec ~/rpmbuild/SPECS/
	cp *.tar.* ~/rpmbuild/SOURCES/
	cp *.patch ~/rpmbuild/SOURCES/
	rpmbuild -bs ~/rpmbuild/SPECS/mendeleydesktop.spec


.PHONY: all
