%define module	etsproxy
%define name 	python-%{module}
%define version 0.1.0
%define release %mkrel 1

Summary: 	Enthought Tool Suite - proxy modules for backwards compatibility
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://www.enthought.com/repo/ets/%{module}-%{version}.tar.gz
License: 	BSD
Group: 	 	Development/Python
Url: 	 	http://code.enthought.com/projects/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: 	noarch
BuildRequires: 	python-setuptools >= 0.6c8

%description
This package contains proxy modules for all ETS projects which map the
old enthought namespace imports to the namespace-refactored ETS
packages. For convenience this package also contains a refactor tool
to convert projects to the new namespace.

This module will be removed in the future; old-style
(enthought.xxx) imports should be converted (over time) to the new
ones.

%prep
%setup -q -n %{module}-%{version}

%build
PYTHONDONTWRITEBYTECODE= %__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt *.rst 
%_bindir/ets3to4
%py_sitedir/enthought/*
%py_sitedir/%{module}*
