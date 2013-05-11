Name:           fontcacheproto
Version:        0.1.3
Release:        0
License:        MIT
Summary:        X.org FontcacheProto protocol headers
Url:            http://www.x.org
Group:          Development/X11 Protocols
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros)

%description
%{summary}.

%prep
%setup -q

%build
%configure --disable-static \
             --libdir=%{_datadir} \
             --without-xmlto

make %{?_smp_mflags}

%install
%make_install

%remove_docs


%files
%license COPYING
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/*.h
%{_datadir}/pkgconfig/*.pc
