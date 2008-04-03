%define 	module	contract
Summary:	Programming by Contract for Python
Summary(pl.UTF-8):	Programowanie kontraktowe dla Pythona
Name:		python-contract
Version:	1.4
Release:	1
License:	Artistic/LGPL/PSF
Group:		Development/Languages/Python
Source0:	http://www.wayforward.net/pycontract/%{module}-%{version}.tar.gz
# Source0-md5:	eaf94dc5c52e68ae5c99863ee74a36ec
URL:		http://www.wayforward.net/pycontract/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
#%pyrequires_eq  python-libs
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Annotate function docstrings with pre- and post-conditions, and
class/module docstrings with invariants, and this automatically checks
the contracts while debugging.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/%{module}-*.egg-info
