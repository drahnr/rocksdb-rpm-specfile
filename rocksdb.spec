#%{?scl:%scl_package rocksdb}
%{!?scl:%global pkg_name %{name}}

Name: rocksdb		
Version: 6.6.4
Release: %{?release}%{!?release:6}%{?dist}
Summary: RocksDB	

Group: Application/Databases		
License: BSD
URL: http://rocksdb.org/	
%if 0%{?gh_commit:1}
Source0: https://github.com/facebook/rocksdb/archive/%{gh_commit}.tar.gz#/%{name}-%{version}.tar.gz	
%else
Source0: https://github.com/facebook/rocksdb/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif

BuildRequires: %{?scl_prefix}gcc, %{?scl_prefix}binutils, %{?scl_prefix}gcc-c++, zlib-devel, bzip2-devel, snappy-devel, lz4-devel
Requires: zlib, bzip2, snappy, lz4

%description

%package devel
Group: Development/Libraries
Summary: Files needed for building projects with RocksDB 
Requires: %{name}, zlib-devel, bzip2-devel, snappy-devel, lz4-devel

%description devel

%package static
Group: Application/Databases
Summary: RocksDB statically compiled library
BuildRequires: zlib-devel, bzip2-devel, snappy-devel, lz4-devel, lz4-static, bzip2-static

%description static

%prep
%if 0%{?gh_commit:1}
%setup -n %{pkg_name}-%{gh_commit} -q
%else
%setup -n %{pkg_name}-%{version} -q
%endif

%build

%{?scl:scl enable %{scl} - << \EOF}
CFLAGS="${CFLAGS} -fPIC" \
PORTABLE=1 make %{?_smp_mflags} shared_lib
%{?scl:EOF}
%{?scl:scl enable %{scl} - << \EOF}
#CFLAGS="${CFLAGS} -fPIC $(pkg-config --static --cflags bzip2 liblz4 jemalloc zlib libzstd) -DBZ2 -DBZIP2=1 -DLZ4=1 -DROCKSDB_JEMALLOC=1 -DZLIB=1 -DZSTD=1" \
#LDFLAGS="${LDFLAGS} $(pkg-config --static --libs bzip2 liblz4 jemalloc zlib libzstd)" \
CFLAGS="${CFLAGS} -fPIC" \
PORTABLE=1 make %{?_smp_mflags} static_lib
%{?scl:EOF}

%install
INSTALL_PATH=%{buildroot}/%{_usr} make install-shared
INSTALL_PATH=%{buildroot}/%{_usr} make install-static
# RocksDB hard coded "lib" as the lib directory, without taking account 64 bit systems, or other systems
# where the lib directory might be different.
if [[ "%{_lib}" != "lib" ]]; then
	mv %{buildroot}/%{_usr}/lib %{buildroot}/%{_usr}/%{_lib}
fi

%files
%doc
%{_usr}/%{_lib}/librocksdb.so* 

%files static
%doc
%{_usr}/%{_lib}/librocksdb.a*

%files devel
%{_usr}/include/rocksdb

%changelog
