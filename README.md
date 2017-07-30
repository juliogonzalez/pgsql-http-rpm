pgsql-http
==========

CentOS/RH/Amazon RPMs for pgsql-http <https://github.com/pramsey/pgsql-http> and postgresql 9.2 (>=9.2.17), 9.3 (>= 9.3.4), 9.4 (>=9.4.1), and 9.6 (>=9.6.2) from the [official repositories](https://yum.postgresql.org/)

Tested on CentOS 6.4 (unofficial curl packages), CentOS 7.1 and Amazon Linux 2014.03 (x86_64 in all cases)

pgsql-http is a HTTP client for PostgreSQL, able to retrieve a web page from inside the database.

Requirements
------------

Use postgresql92\* packages for PostgreSQL 9.2 (>= 9.2.17), postgresql93\* packages for PostgreSQL 9.3 (>= 9.3.4), posgresql94\* packages for PostgreSQL 9.4 (>= 9.4.1) or posgresql96\* packages for PostgreSQL 9.6 (>= 9.6.2), in all cases from the [official repositories](https://yum.postgresql.org/) (and not from your distribution repositories!)

To build: 

* postgresql92-devel >= 9.2.17, postgresql93-devel >= 9.3.4, postgresql94-devel >= 9.4.1 or postgresql96-devel >= 9.6.2
* curl-devel >= 0.7.20
* automake
* gcc
* git
* rpm-build

To install the RPM for PostgreSQL

* postgresql92 >= 9.2.17, postgresql93 >= 9.3.4, postgresql94 >= 9.4.1 or postgresql96 >= 9.6.2
* postgresql92-server >= 9.2.17, postgresql93-server >= 9.3.4, postgresql94-server >= 9.4.1 or postgresql96-server >= 9.6.2
* postgresql92-libs => 9.2.17, postgresql93-libs >= 9.3.4, postgresql94-libs >= 9.4.1 or postgresql96-libs >= 9.6.2


Building fresh RPMs
-------------------

Clone the repo: 

```
git@github.com:juliogonzalez/pgsql-http-rpm.git
cd pgsql-http-rpm
```

Build the pgsql-http RPM
---------------------

Build the RPMs:

```
./pgsql-http-rpm -p 9.2 # for PostgreSQL 9.2
```

or

```
./pgsql-http-rpm -p 9.3 # for PostgreSQL 9.3
```

or

```
./pgsql-http-rpm -p 9.4 # for PostgreSQL 9.4
```
or

```
./pgsql-http-rpm -p 9.4 # for PostgreSQL 9.6
```
And install:

```
rpm -Uvh RPMS/$HOSTTYPE/postgresql-92-pgsql-http-1.1.2-1*.$HOSTTYPE.rpm # for PostgreSQL 9.2
```

or

```
rpm -Uvh RPMS/$HOSTTYPE/postgresql-93-pgsql-http-1.1.2-1*.$HOSTTYPE.rpm # for PostgreSQL 9.3
```

or

```
rpm -Uvh RPMS/$HOSTTYPE/postgresql-94-pgsql-http-1.1.2-1*.$HOSTTYPE.rpm # for PostgreSQL 9.4
```
or
```
rpm -Uvh RPMS/$HOSTTYPE/postgresql-96-pgsql-http-1.1.2-1*.$HOSTTYPE.rpm # for PostgreSQL 9.6
```
