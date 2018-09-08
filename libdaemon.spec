#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libdaemon
Version  : 0.14
Release  : 2
URL      : http://0pointer.de/lennart/projects/libdaemon/libdaemon-0.14.tar.gz
Source0  : http://0pointer.de/lennart/projects/libdaemon/libdaemon-0.14.tar.gz
Summary  : a lightweight C library that eases the writing of UNIX daemons
Group    : Development/Tools
License  : LGPL-2.1
Requires: libdaemon-lib
Requires: libdaemon-license

%description
libdaemon 0.14
de>
* [1]License
* [2]News
* [3]Overview
* [4]Current Status
* [5]Documentation
* [6]Requirements
* [7]Installation
* [8]Acknowledgements
* [9]Download

%package dev
Summary: dev components for the libdaemon package.
Group: Development
Requires: libdaemon-lib
Provides: libdaemon-devel

%description dev
dev components for the libdaemon package.


%package doc
Summary: doc components for the libdaemon package.
Group: Documentation

%description doc
doc components for the libdaemon package.


%package lib
Summary: lib components for the libdaemon package.
Group: Libraries
Requires: libdaemon-license

%description lib
lib components for the libdaemon package.


%package license
Summary: license components for the libdaemon package.
Group: Default

%description license
license components for the libdaemon package.


%prep
%setup -q -n libdaemon-0.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536451125
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1536451125
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/libdaemon
cp LICENSE %{buildroot}/usr/share/doc/libdaemon/LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libdaemon/daemon.h
/usr/include/libdaemon/dexec.h
/usr/include/libdaemon/dfork.h
/usr/include/libdaemon/dlog.h
/usr/include/libdaemon/dnonblock.h
/usr/include/libdaemon/dpid.h
/usr/include/libdaemon/dsignal.h
/usr/lib64/libdaemon.so
/usr/lib64/pkgconfig/libdaemon.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libdaemon/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdaemon.so.0
/usr/lib64/libdaemon.so.0.5.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/libdaemon/LICENSE
