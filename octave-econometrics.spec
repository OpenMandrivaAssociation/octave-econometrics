%global octpkg econometrics

Summary:	Econometrics functions for Octave
Name:		octave-econometrics
Version:	1.1.2
Release:	3
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/econometrics/
Source0:	https://downloads.sourceforge.net/octave/econometrics-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.4.0
BuildRequires:  octave-optim

Requires:	octave(api) = %{octave_api}
Requires:  	octave-optim

Requires(post): octave
Requires(postun): octave

%description
Econometrics functions for Octave including MLE and GMM based techniques.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

