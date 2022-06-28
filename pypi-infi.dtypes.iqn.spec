#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-infi.dtypes.iqn
Version  : 0.4.0
Release  : 5
URL      : https://files.pythonhosted.org/packages/2e/0d/e05be651c207a35013f88be3f8938693d1beee3e1fad8f21a42b948d5d9c/infi.dtypes.iqn-0.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/2e/0d/e05be651c207a35013f88be3f8938693d1beee3e1fad8f21a42b948d5d9c/infi.dtypes.iqn-0.4.0.tar.gz
Summary  : Datatype for IQN
Group    : Development/Tools
License  : Python-2.0
Requires: pypi-infi.dtypes.iqn-python = %{version}-%{release}
Requires: pypi-infi.dtypes.iqn-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
No detailed description available

%package python
Summary: python components for the pypi-infi.dtypes.iqn package.
Group: Default
Requires: pypi-infi.dtypes.iqn-python3 = %{version}-%{release}

%description python
python components for the pypi-infi.dtypes.iqn package.


%package python3
Summary: python3 components for the pypi-infi.dtypes.iqn package.
Group: Default
Requires: python3-core
Provides: pypi(infi.dtypes.iqn)

%description python3
python3 components for the pypi-infi.dtypes.iqn package.


%prep
%setup -q -n infi.dtypes.iqn-0.4.0
cd %{_builddir}/infi.dtypes.iqn-0.4.0
pushd ..
cp -a infi.dtypes.iqn-0.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656382014
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
