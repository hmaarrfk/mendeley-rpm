mendeley-rpm
============

Git Repository at: [mendeley-rpm](https://github.com/hmaarrfk/mendeley-rpm).

This is an unofficial package designed for Fedora that packages [Mendeley
Desktop](https://www.mendeley.com/) freely available from the web.

It attempts to maximize the use of system libraries and to adhere to Fedora
guidelines.

The only files I wrote were the .spec and a fresh mendeleydesktop executable
(that essentially does nothing). Therefore I won't bother putting a license on
my files. The license for the files obtained from Mendeley is included as part
of this install.

Installation
============

Easy way (Recommended)
----------------------
Mendeley Desktop is availabe in rpmfusion repository.
1. Visit [RPM Fusion](https://rpmfusion.org/Configuration) to install the repository when needed.
2. Simply browse for Mendeley on GNOME Software or your favourite frontend package manager.
3. Alternately from a terminal, execute the command `sudo dnf install mendeleydesktop` or `pkcon install mendeleydesktop`.

Medium way
----------
1. Download the latest RPM file for your computer architecture from
   https://github.com/hmaarrfk/mendeley-rpm/releases
2. Open a terminal and navigate to the folder which contains the RPM file, for
   example: `cd ~/Downloads`
3. Now, install the RPM file, for example with `sudo dnf install
   mendeleydesktop-VERSION.ARCHITECTURE.rpm` (where you have to replace
   VERSION and ARCHITECTURE).
  
 

Hard way: Build the RPM yourself
--------------------------------
You need the tool `mock` that you can read more about [here](https://fedoraproject.org/wiki/Using_Mock_to_test_package_builds)
1. Clone: `git clone https://github.com/hmaarrfk/mendeley-rpm.git`.
2. `make`.
3. Run `mock` with the generated `srpm`.

Screenshots
===========
![Login session](https://github.com/hmaarrfk/mendeley-rpm/blob/master/images/mendeley-desktop_0.png)

Login session

![Welcome dialog](https://github.com/hmaarrfk/mendeley-rpm/blob/master/images/mendeley-desktop_1.png)

Welcome dialog when opened for the first

![Mendeley Desktop in default Library as Table view](https://github.com/hmaarrfk/mendeley-rpm/blob/master/images/mendeley-desktop_2.png)

Mendeley Desktop in default Library as Table view

![Mendeley Desktop in Library as Citation view](https://github.com/hmaarrfk/mendeley-rpm/blob/master/images/mendeley-desktop_3.png)

Mendeley Desktop in Library as Citation view


Wish official support
=====================

The issue of having an RPM has been raised to Mendeley in the past:

* [General Linux
  2012](http://support.mendeley.com/customer/portal/questions/567256-linux-make-a-linux-installer)
* [Gentoo
  2012](http://support.mendeley.com/customer/portal/questions/199131-on-distribution-policy-and-download-link)
* [Fedora
  2013](http://support.mendeley.com/customer/portal/questions/758741-packaging-for-fedora)

Collaborators
=============

The first version was written by Mark Harfouche (2013.01.21). A few
collaborators helped along the way: Chris Fallin, Filipe Manco and Luya Tshimbalanga.

Development Notes
=================

It might be instructive to look at what was done by the Gentoo community.
http://gentoo-overlays.zugaina.org/funtoo/sci-misc.html.en#mendeleydesktop

Honestly, I think we might be doing it better since we don't install into /opt.
I always feel like installing into /opt is a hack.

Then again, they are not like packaging noobs like we are :D.

Packaging Situation
===================

At one point in time, this package was hosted on COPR. This broke their
guidelines so I had to remove it.

I was trying to upload it to rpmfusion but hit a small snag that I don't
particularly have time to solve.

https://bugzilla.rpmfusion.org/show_bug.cgi?id=4041

After several revisions to adhere to rpmfusion guideline, Mendeley Desktop finally landed to [rpmfusion
repository](http://koji.rpmfusion.org/koji/packageinfo?packageID=594) first in devel branch and update-testing for each active Fedora (29 and 30) and Red Hat Enterprise 8 releases.

Other ways to obtain Mendeley
=============================
Flathub:
https://flathub.org/apps/details/com.elsevier.MendeleyDesktop

AppImage: (Seems a little out of date though)
https://bintray.com/probono/AppImages/Mendeley_Desktop/


Known Bugs
==========
None.
