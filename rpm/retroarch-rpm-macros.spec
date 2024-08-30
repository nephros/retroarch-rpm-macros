Name:    retroarch-rpm-macros
Version: 24.08.29
Release: 1%{?dist}
Summary: RPM macros for libretro and retroarch
License: BSD
BuildArch: noarch
Source0: %{name}-%{version}.tar.gz
Source1: macros.retroarch
Source2: libretro-example.spec.template
Source3: libretro-example.desktop.in

%description
%{summary}.

See the packages example .spec file on how to use.

%prep
%setup -q -n %{name}

%build

%install
install -Dpm644 %SOURCE1 %{buildroot}%{_rpmconfigdir}/macros.d/macros.retroarch
install -Dpm644 %SOURCE2 %{buildroot}%{_docdir}/%{name}/libretro-example.spec
install -Dpm644 %SOURCE3 %{buildroot}%{_docdir}/%{name}/libretro-example.desktop.in

%files
%{_rpmconfigdir}/macros.d/*
%{_docdir}/%{name}/
