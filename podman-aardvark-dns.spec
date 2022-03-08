%global debug_package %{nil}

Name: podman-aardvark-dns
Epoch: 100
Version: 1.0.3
Release: 1%{?dist}
Summary: Authoritative DNS server for A/AAAA container records
License: Apache-2.0
URL: https://github.com/containers/aardvark-dns/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: cargo
BuildRequires: gcc
BuildRequires: pkgconfig
BuildRequires: rust
Requires: podman

%description
Authoritative dns server for A/AAAA container records. Forwards other
request to host's /etc/resolv.conf

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
cargo build --release

%install
install -Dpm755 -d %{buildroot}%{_libexecdir}/podman
install -Dpm755 -t %{buildroot}%{_libexecdir}/podman target/release/aardvark-dns

%files
%license LICENSE
%dir %{_libexecdir}/podman
%{_libexecdir}/podman/aardvark-dns

%changelog
