%global debug_package %{nil}

Name:		newsraft
Version:	0.31
Release:	1
Source0:	https://codeberg.org/newsraft/newsraft/archive/%{name}-%{version}.tar.gz
Summary:	Feed reader with text-based user interface.
URL:		https://codeberg.org/newsraft/newsraft
License:	ISC
Group:		Reader

BuildRequires:  gperf
BuildRequires:  scdoc
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(gumbo)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(expat)

Requires:   curl
Requires:   expat
Requires:   lib64sqlite3_0
Requires:   gumbo-parser

%description
Newsraft is a feed reader with text-based user interface. It's greatly inspired by Newsboat and tries to be its lightweight counterpart.

%prep
%autosetup -p1 -n %{name}

%build
%make_build

%install
%make_install

%files
/usr/local/bin/newsraft
/usr/local/share/icons/hicolor/scalable/apps/newsraft.svg
/usr/local/share/man/man1/newsraft.1
/usr/local/share/newsraft/examples/config
/usr/local/share/newsraft/examples/feeds
