%global commit0 a58d9d24acb982ab71ffb95c45fb48063f5a86a6
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           postgresql-92-pgsql-http
Version:        1.1.1
Release:        2git%{shortcommit0}%{?dist}
Summary:        HTTP client for PostgreSQL, retrieve a web page from inside the database.

License:        None
URL:            https://github.com/pramsey/pgsql-http
Source:         https://github.com/pramsey/pgsql-http/archive/%{commit0}.tar.gz

Requires:       postgresql92 >= 9.2.17
Requires:       postgresql92-server >= 9.2.17
Requires:       postgresql92-libs >= 9.2.17

BuildRequires:  postgresql92-devel,
BuildRequires:  curl-devel >= 0.7.20
BuildRequires:	make, gcc

%description
HTTP client for PostgreSQL, retrieve a web page from inside the database.

%global debug_package %{nil}

%prep
%setup -q -n pgsql-http-%{commit0}


%build
PATH=/usr/pgsql-9.2/bin:$PATH make

%install
rm -rf %{buildroot}
PATH=/usr/pgsql-9.2/bin:$PATH make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/usr/share/doc/%{name}
cp README.md %{buildroot}/usr/share/doc/%{name}/README.md

%clean
rm -rf %{buildroot}

%files
%attr(755, root, root)/usr/pgsql-9.2/lib/http.so
%attr(644, root, root)/usr/pgsql-9.2/share/extension/http--1.1.sql
%attr(644, root, root)/usr/pgsql-9.2/share/extension/http--1.0--1.1.sql
%attr(644, root, root)/usr/pgsql-9.2/share/extension/http.control

%doc /usr/share/doc/%{name}/README.md



%changelog

* Fri Sep 30 2016 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.1.1-2gita58d9d2
- Build from commit a58d9d2 (latest available)

* Fri Jul 08 2016 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.1.1
- 1.1.1 build from https://github.com/pramsey/pgsql-http
