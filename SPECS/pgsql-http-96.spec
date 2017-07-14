Name:           postgresql-96-pgsql-http
Version:        1.1.2
Release:        1%{?dist}
Summary:        HTTP client for PostgreSQL, retrieve a web page from inside the database.

License:        None
URL:            https://github.com/pramsey/pgsql-http
Source:         https://github.com/pramsey/pgsql-http/archive/v%{version}.tar.gz

Requires:       postgresql96 >= 9.6.2
Requires:       postgresql96-server >= 9.6.2
Requires:       postgresql96-libs >= 9.6.2

BuildRequires:  postgresql96-devel
BuildRequires:  curl-devel >= 0.7.20
BuildRequires:	make, gcc

%description
HTTP client for PostgreSQL, retrieve a web page from inside the database.

%global debug_package %{nil}

%prep
%setup -q -n pgsql-http-%{version}


%build
PATH=/usr/pgsql-9.6/bin:$PATH make

%install
rm -rf %{buildroot}
PATH=/usr/pgsql-9.6/bin:$PATH make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/usr/share/doc/%{name}
cp README.md %{buildroot}/usr/share/doc/%{name}/README.md

%clean
rm -rf %{buildroot}

%files
%attr(755, root, root)/usr/pgsql-9.6/lib/http.so
%attr(644, root, root)/usr/pgsql-9.6/share/extension/http--1.1.sql
%attr(644, root, root)/usr/pgsql-9.6/share/extension/http--1.0--1.1.sql
%attr(644, root, root)/usr/pgsql-9.6/share/extension/http.control

%doc /usr/share/doc/%{name}/README.md



%changelog

* Sun Jul 30 2017 Kevin Shaw <shawmanz32na@gmail.com> - 1.1.2-1
- 1.1.2 build from https://github.com/pramsey/pgsql-http

* Fri Sep 30 2016 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.1.1-2gita58d9d2
- Build from commit a58d9d2 (latest available)

* Fri Jul 08 2016 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.1.1
- 1.1.1 build from https://github.com/pramsey/pgsql-http
