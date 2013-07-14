mendeley-rpm
============

About
============

This is an unofficial package designed for Fedora that packages
Mendeley Desktop freely available from the web.

It attempts to maximize the use of system libraries and to adhere to Fedora guidelines.

The only files I wrote were the .spec and a fresh mendeleydesktop executable (that essentially does nothing). Therefore I won't bother putting a license on my files. The license for the files obtained from Mendeley is included as part of this install.

How to install
============
Go to the releases in GitHub and download the appropriate rpm

How to build the RPM
============
Download the "source" (really a binary from mendeley) and run the ./package-mendeley-rpm.sh script


The issue of having an RPM has been raised to Mendeley in the past:
General Linux 2012
http://support.mendeley.com/customer/portal/questions/567256-linux-make-a-linux-installer
Gentoo 2012
http://support.mendeley.com/customer/portal/questions/199131-on-distribution-policy-and-download-link
Fedora 2013
http://support.mendeley.com/customer/portal/questions/758741-packaging-for-fedora


The first version was written by
Mark Harfouche
2013.01.21

A few collaborators helped along the way

Chris Fallin

Filipe Manco

Git Repository at:
https://github.com/hmaarrfk/mendeley-rpm

Get ther tarball from
mendeley.com

Devellopment Notes
============

It might be instructive to look at what was done by the Gentoo community.
http://gentoo-overlays.zugaina.org/funtoo/sci-misc.html.en#mendeleydesktop

Looking at their .ebuild script (seems to be the equivalent of a spec file)
http://data.gpo.zugaina.org/funtoo/sci-misc/mendeleydesktop/mendeleydesktop-1.9.1.ebuild
they have a different strategy to deal with the system QT vs bundled qt problem.


  # force use of system Qt libraries
  sed -i "s:sys\.argv\.count(\"--force-system-qt\") > 0:True:" \
    bin/mendeleydesktop || die "failed to patch startup script"

  # fix library paths
  sed -i \
    -e "s:lib/mendeleydesktop:$(get_libdir)/mendeleydesktop:g" \
    -e "s:MENDELEY_BASE_PATH + \"/lib/\":MENDELEY_BASE_PATH + \"/$(get_libdir)/\":g" \
    bin/mendeleydesktop || die "failed to patch library path"

Honestly, I think we might be doing it better since we don't install into /opt.
I always feel like installing into /opt is a hack.

Then again, they don't like packaging noobs like we are :D.
