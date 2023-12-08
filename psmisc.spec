#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0x022166C0FF3C84E3 (csmall@debian.org)
#
Name     : psmisc
Version  : 23.6
Release  : 28
URL      : https://sourceforge.net/projects/psmisc/files/psmisc/psmisc-23.6.tar.xz
Source0  : https://sourceforge.net/projects/psmisc/files/psmisc/psmisc-23.6.tar.xz
Source1  : https://sourceforge.net/projects/psmisc/files/psmisc/psmisc-23.6.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: psmisc-bin = %{version}-%{release}
Requires: psmisc-license = %{version}-%{release}
Requires: psmisc-locales = %{version}-%{release}
Requires: psmisc-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : dejagnu
BuildRequires : expect
BuildRequires : ncurses-dev
BuildRequires : tcl
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Fix-dejagnu-error.patch

%description


%package bin
Summary: bin components for the psmisc package.
Group: Binaries
Requires: psmisc-license = %{version}-%{release}

%description bin
bin components for the psmisc package.


%package license
Summary: license components for the psmisc package.
Group: Default

%description license
license components for the psmisc package.


%package locales
Summary: locales components for the psmisc package.
Group: Default

%description locales
locales components for the psmisc package.


%package man
Summary: man components for the psmisc package.
Group: Default

%description man
man components for the psmisc package.


%prep
%setup -q -n psmisc-23.6
cd %{_builddir}/psmisc-23.6
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702062378
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1702062378
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/psmisc
cp %{_builddir}/psmisc-%{version}/COPYING %{buildroot}/usr/share/package-licenses/psmisc/74a8a6531a42e124df07ab5599aad63870fa0bd4 || :
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
/usr/bin/pslog
/usr/bin/pstree
/usr/bin/pstree.x11

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/psmisc/74a8a6531a42e124df07ab5599aad63870fa0bd4

%files man
%defattr(0644,root,root,0755)
/usr/share/man/da/man1/prtstat.1
/usr/share/man/da/man1/pslog.1
/usr/share/man/de/man1/fuser.1
/usr/share/man/de/man1/killall.1
/usr/share/man/de/man1/peekfd.1
/usr/share/man/de/man1/prtstat.1
/usr/share/man/de/man1/pslog.1
/usr/share/man/de/man1/pstree.1
/usr/share/man/fr/man1/fuser.1
/usr/share/man/fr/man1/killall.1
/usr/share/man/fr/man1/peekfd.1
/usr/share/man/fr/man1/prtstat.1
/usr/share/man/fr/man1/pslog.1
/usr/share/man/fr/man1/pstree.1
/usr/share/man/hr/man1/fuser.1
/usr/share/man/hr/man1/killall.1
/usr/share/man/hr/man1/peekfd.1
/usr/share/man/hr/man1/prtstat.1
/usr/share/man/hr/man1/pslog.1
/usr/share/man/hr/man1/pstree.1
/usr/share/man/ko/man1/fuser.1
/usr/share/man/ko/man1/killall.1
/usr/share/man/ko/man1/peekfd.1
/usr/share/man/ko/man1/prtstat.1
/usr/share/man/ko/man1/pslog.1
/usr/share/man/ko/man1/pstree.1
/usr/share/man/man1/fuser.1
/usr/share/man/man1/killall.1
/usr/share/man/man1/peekfd.1
/usr/share/man/man1/prtstat.1
/usr/share/man/man1/pslog.1
/usr/share/man/man1/pstree.1
/usr/share/man/pt_BR/man1/fuser.1
/usr/share/man/pt_BR/man1/killall.1
/usr/share/man/pt_BR/man1/peekfd.1
/usr/share/man/pt_BR/man1/prtstat.1
/usr/share/man/pt_BR/man1/pslog.1
/usr/share/man/pt_BR/man1/pstree.1
/usr/share/man/ro/man1/fuser.1
/usr/share/man/ro/man1/killall.1
/usr/share/man/ro/man1/peekfd.1
/usr/share/man/ro/man1/prtstat.1
/usr/share/man/ro/man1/pslog.1
/usr/share/man/ro/man1/pstree.1
/usr/share/man/ru/man1/fuser.1
/usr/share/man/ru/man1/killall.1
/usr/share/man/ru/man1/peekfd.1
/usr/share/man/ru/man1/prtstat.1
/usr/share/man/ru/man1/pslog.1
/usr/share/man/ru/man1/pstree.1
/usr/share/man/sr/man1/fuser.1
/usr/share/man/sr/man1/killall.1
/usr/share/man/sr/man1/peekfd.1
/usr/share/man/sr/man1/prtstat.1
/usr/share/man/sr/man1/pslog.1
/usr/share/man/sr/man1/pstree.1
/usr/share/man/sv/man1/fuser.1
/usr/share/man/sv/man1/killall.1
/usr/share/man/sv/man1/peekfd.1
/usr/share/man/sv/man1/prtstat.1
/usr/share/man/sv/man1/pslog.1
/usr/share/man/sv/man1/pstree.1
/usr/share/man/uk/man1/fuser.1
/usr/share/man/uk/man1/killall.1
/usr/share/man/uk/man1/peekfd.1
/usr/share/man/uk/man1/prtstat.1
/usr/share/man/uk/man1/pslog.1
/usr/share/man/uk/man1/pstree.1

%files locales -f psmisc.lang
%defattr(-,root,root,-)

