Name:           accel-ppp
Version:        1.8.0
Release:        1.akta
Summary:        High performance PPTP/L2TP/PPPoE server

License:        GPLv2+
URL:            http://sourceforge.net/projects/accel-ppp/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:  libnl-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel

%description
The ACCEL-PPP v1.0 is completly new implementation of PPTP/PPPoE/L2TP
which was written from scratch. Userspace daemon has its own PPP
implementation, so it does not uses pppd and one process (multi-threaded)
manages all connections. ACCEL-PPP uses only kernel-mode implementations
of pptp/l2tp/pppoe.

Features:
- PPTP server
- PPPoE server
- L2TPv2 server
- Radius CoA/DM(PoD)
- Built-in shaper (tbf)
- Command line interface (telnet)
- SNMP
- IPv6 (including builtin Neighbor Discovery and DHCPv6)

%prep
%setup -q

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} \
      -DSHAPER=TRUE \
      -DLOG_PGSQL=FALSE \
      -DRADIUS=TRUE \
      ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot} 
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%files
%doc COPYING README
%{_sysconfdir}/accel-ppp.conf.dist
%{_sbindir}/accel-pppd
%{_bindir}/accel-cmd
%{_libdir}/accel-ppp/
%{_datadir}/accel-ppp/
%{_mandir}/man5/accel-ppp.conf.5*
%{_mandir}/man1/accel-cmd.1*


%changelog
* Mon Oct 24 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.4.0-1
- Initial RPM release

