%define oname mkcue-1

Name:		mkcue
Version:	1.8
Release:	1
License:	LGPL-2.1-or-later
Group:		Sound/Utilities
Summary:	Generates cue sheets from a CD's TOC (Table Of Contents)
URL:		https://diplodocus.org/projects/audio/
# Currently maintained at https://tracker.debian.org/pkg/mkcue
Source0:	https://httpredir.debian.org/debian/pool/main/m/mkcue/mkcue_1.orig.tar.gz
Source1:	https://httpredir.debian.org/debian/pool/main/m/mkcue/mkcue_1-8.debian.tar.xz
# All the upstream mkcue_-1-8 patches rolled into one.
Patch0:		mkcue-1-8-fixes.patch

BuildRequires:	autoconf automake slibtool
BuildRequires:	make
Suggests:	abcde

%description
mkcue generates cue sheets from a CD's TOC (Table Of Contents).

It uses code borrowed from the MusicBrainz client library,
and is thus released under the terms of the GNU GPL.

Usage is quite simple.  By default, list all tracks from /dev/cdrom in
the cue sheet.  An optional device argument overrides /dev/cdrom.

The -t track-count option only lists up to track-count tracks in the cue
sheet, which is handy for CDs with data tracks you want to ignore.

It is a perfect companion for abcde to generate backups of your audio CDs
using the FLAC codec and the single track option.

%prep
%setup -q -n %{oname}.orig -a1
%autopatch -p1

%build
export DESTDIR=%{buildroot}%{_bindir}
%ifarch aarch64
./configure --prefix=/usr --build=aarch64-unknown-linux-gnu
%else
./configure --prefix=/usr
%endif
%make_build all

%install
export DESTDIR=%{buildroot}%{_bindir}
export bindir=%{_bindir}
install -D mkcue %{buildroot}%{_bindir}/mkcue

%files
%{_bindir}/%{name}
%doc README
%doc debian/changelog
%license COPYING debian/copyright