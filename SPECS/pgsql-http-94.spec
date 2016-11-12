Name:           postgresql-94-pgsql-http
Version:        1.1.2
Release:        1%{?dist}
Summary:        HTTP client for PostgreSQL, retrieve a web page from inside the database.

License:        None
URL:            https://github.com/pramsey/pgsql-http
Source:         https://github.com/pramsey/pgsql-http/archive/v%{version}.tar.gz

Requires:       postgresql94 >= 9.4.1
Requires:       postgresql94-server >= 9.4.1
Requires:       postgresql94-libs >= 9.4.1

BuildRequires:  postgresql94-devel
BuildRequires:  curl-devel >= 0.7.20
BuildRequires:	make, gcc

%description
HTTP client for PostgreSQL, retrieve a web page from inside the database.

%global debug_package %{nil}

%prep
%setup -q -n pgsql-http-%{version}


%build
PATH=/usr/pgsql-9.4/bin:$PATH make

%install
rm -rf %{buildroot}
PATH=/usr/pgsql-9.4/bin:$PATH make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/usr/share/doc/%{name}
cp README.md %{buildroot}/usr/share/doc/%{name}/README.md

%clean
rm -rf %{buildroot}

%files
%attr(755, root, root)/usr/pgsql-9.4/lib/http.so
%attr(644, root, root)/usr/pgsql-9.4/share/extension/http--1.1.sql
%attr(644, root, root)/usr/pgsql-9.4/share/extension/http--1.0--1.1.sql
%attr(644, root, root)/usr/pgsql-9.4/share/extension/http.control

%doc /usr/share/doc/%{name}/README.md



%changelog

* Sat Nov 12 2016 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.1.2-1
- 1.1.2 build from https://github.com/pramsey/pgsql-http

* Fri Sep 30 2016 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.1.1-2gita58d9d2
- Build from commit a58d9d2 (latest available)

* Fri Jul 08 2016 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.1.1
- 1.1.1 build from https://github.com/pramsey/pgsql-http
