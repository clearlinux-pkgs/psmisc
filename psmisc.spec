#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : psmisc
Version  : 22.21
Release  : 12
URL      : http://downloads.sourceforge.net/psmisc/psmisc-22.21.tar.gz
Source0  : http://downloads.sourceforge.net/psmisc/psmisc-22.21.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: psmisc-bin
Requires: psmisc-locales
Requires: psmisc-doc
BuildRequires : dejagnu
BuildRequires : expect
BuildRequires : ncurses-dev
BuildRequires : tcl

%description
psmisc
======
This package contains five little utilities that use the proc FS:
fuser     identifies processes using files or sockets (similar to Sun's
or SGI's fuser)
killall   kills processes by name, e.g. killall -HUP named
pstree    shows the currently running processes as a tree
peekfd    shows the data travelling over a file descriptor

%package bin
Summary: bin components for the psmisc package.
Group: Binaries

%description bin
bin components for the psmisc package.


%package doc
Summary: doc components for the psmisc package.
Group: Documentation

%description doc
doc components for the psmisc package.


%package locales
Summary: locales components for the psmisc package.
Group: Default

%description locales
locales components for the psmisc package.


%prep
%setup -q -n psmisc-22.21

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang psmisc

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fuser
/usr/bin/killall
/usr/bin/peekfd
/usr/bin/prtstat
/usr/bin/pstree
/usr/bin/pstree.x11

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files locales -f psmisc.lang 
%defattr(-,root,root,-)

