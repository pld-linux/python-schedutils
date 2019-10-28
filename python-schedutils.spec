#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python 2 module to interface with the Linux scheduler
Summary(pl.UTF-8):	Moduł Pythona 2 do komunikacji z linuksowym planistą
Name:		python-schedutils
Version:	0.6
Release:	2
License:	GPL v2
Group:		Libraries/Python
Source0:	https://www.kernel.org/pub/software/libs/python/python-schedutils/%{name}-%{version}.tar.xz
# Source0-md5:	e834aa5b0d026102bd9b04f24019c731
URL:		https://rt.wiki.kernel.org/index.php/Tuna
%if %{with python2}
BuildRequires:	python-devel >= 2
BuildRequires:	python-modules >= 2
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 interface for the Linux scheduler
sched_{get,set}{affinity,scheduler} functions and friends.

%description -l pl.UTF-8
Interfejs Pythona 2 do funkcji linuksowego planisty
sched_{get,set}{affinity,scheduler} oraz pokrewnych.

%package -n python3-schedutils
Summary:	Python 3 module to interface with the Linux scheduler
Summary(pl.UTF-8):	Moduł Pythona 3 do komunikacji z linuksowym planistą
Group:		Libraries/Python

%description -n python3-schedutils
Python 3 interface for the Linux scheduler
sched_{get,set}{affinity,scheduler} functions and friends.

%description -n python3-schedutils -l pl.UTF-8
Interfejs Pythona 3 do funkcji linuksowego planisty
sched_{get,set}{affinity,scheduler} oraz pokrewnych.

%prep
%setup -q

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%if %{with python3}
%py3_install
%endif

%if %{with python2}
%py_install

%py_postclean

#cp -p pchrt.py $RPM_BUILD_ROOT%{_bindir}/pchrt
#cp -p ptaskset.py $RPM_BUILD_ROOT%{_bindir}/ptaskset
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/pchrt
%attr(755,root,root) %{_bindir}/ptaskset
%attr(755,root,root) %{py_sitedir}/schedutils.so
%{_mandir}/man1/pchrt.1*
%{_mandir}/man1/ptaskset.1*
%if "%{py_ver}" > "2.4"
%{py_sitedir}/schedutils-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-schedutils
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{py3_sitedir}/schedutils.cpython-*.so
%{py3_sitedir}/schedutils-%{version}-py*.egg-info
%endif
