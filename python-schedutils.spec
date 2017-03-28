#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (enable when useful - now scripts use python2 shebang)

Summary:	Python 2 module to interface with the Linux scheduler
Summary(pl.UTF-8):	Moduł Pythona 2 do komunikacji z linuksowym planistą
Name:		python-schedutils
Version:	0.5
Release:	1
License:	GPL v2
Group:		Libraries/Python
Source0:	https://www.kernel.org/pub/software/libs/python/python-schedutils/%{name}-%{version}.tar.xz
# Source0-md5:	e4a6fd6ad5307732e96c723e89056759
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

%if %{with python2}
%py_install

%py_postclean

cp -p pchrt.py $RPM_BUILD_ROOT%{_bindir}/pchrt
cp -p ptaskset.py $RPM_BUILD_ROOT%{_bindir}/ptaskset
%endif

%if %{with python3}
%py3_install
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
%if "%{py_ver}" > "2.4"
%{py_sitedir}/schedutils-0.4-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-schedutils
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{py3_sitedir}/schedutils.cpython-*.so
%{py3_sitedir}/schedutils-0.4-py*.egg-info
%endif
