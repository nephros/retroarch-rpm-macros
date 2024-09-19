Name:    libretro-rpm-macros
Version: 24.09.19
Release: 1%{?dist}
Summary: RPM macros for libretro and retroarch
License: BSD
BuildArch: noarch
Source0: %{name}-%{version}.tar.gz

Obsoletes:   retroarch-rpm-macros <= %{version}
Conflicts:   retroarch-rpm-macros

%description
%{summary}.

See the packages example .spec file on how to use.

%prep
%autosetup

%build

%install
install -Dpm644 macros.libretro                   %{buildroot}%{_rpmconfigdir}/macros.d/macros.libretro
install -Dpm644 doc/libretro-example.spec.template %{buildroot}%{_docdir}/%{name}/libretro-example.spec
install -Dpm644 doc/libretro-example.desktop.in    %{buildroot}%{_docdir}/%{name}/libretro-example.desktop.in

%files
%{_rpmconfigdir}/macros.d/*
%{_docdir}/%{name}/
