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
Easy way:
https://copr.fedoraproject.org/coprs/hmaarrfk/mendeleydesktop/

Hard way: Build the RPM yourself.

How to build the RPM
============
Download the "source" (really a binary from mendeley) and run the ./package-mendeley-rpm.sh script
Then use mock on the source rpm.

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


Packaging Situation
============
At one point in time, this package was hosted on COPR. This broke their guidelines so I had to remove it. 

I was trying to upload it to rpmfusion but hit a small snag that I don't particularly have time to solve.
If you want to, you can merge Dominik's spec file with this one, add both of you to the author list (or at least credit Dominik for his good work) and revive the issue on the bug request below.

https://bugzilla.rpmfusion.org/show_bug.cgi?id=4041

Since Mendeley doesn't update too often, manually downloading the RPM didn't seem like a bad solution.
