%define module	etsproxy

Summary: 	Enthought Tool Suite - proxy modules for backwards compatibility
Name: 	 	python-%{module}
Version: 	0.1.2
Release: 	2
Source0: 	https://www.enthought.com/repo/ets/etsproxy-%{version}.tar.gz
License: 	BSD
Group: 	 	Development/Python
Url: 	 	https://github.com/enthought/etsproxy/
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
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST
%doc *.txt *.rst 


%changelog
* Tue Jan 10 2012 Lev Givon <lev@mandriva.org> 0.1.1-1mdv2012.0
+ Revision: 759471
- Update to 0.1.1.

* Tue Oct 18 2011 Lev Givon <lev@mandriva.org> 0.1.0-1
+ Revision: 705241
- imported package python-etsproxy


