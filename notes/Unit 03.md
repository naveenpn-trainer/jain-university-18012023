# NoSQL - Cassandra

>In computing, NoSQL (mostly interpreted as **Not only SQL**) is a broad class of database management system which is non-relational

* NoSQL today used as an umbrella terminology for all databases and datastores that don't follow RDBMS principles

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeqCGYMivQaQWjiq3wU3pGkZMy_aywIPwLsZXQ_q3YO4Un6eaGmpxuBlBpQf8CRQ6zMoETZyoHx05KWdA81ML_BDqShw4qJ03OFFAWZ8I6zJy1ZsB9aIUGPGUJacFGYreG1IwfLeUlpBycVF6mDbKh13QQV?key=vIDkk8rWlcI2o5POMy6F3Q)

## Types of NoSQL

There are 4 types of NoSQL databases

1. Key value
2. Document Based
3. Column Based
4. Graph Based

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc6UiP4SDmBPjNvJP0mduDTqRre4BSHi9amniMLdcVFWwidp0XwvTqgBPCKdfeci8Gfml3c6dOPveZ8EAshwzjpWiUUDT9qQKvRJdYFWML2We_5mnLGyZf68Ste6Tw1FTuZXndfXqHfL3QnSyrXhpKC9Kd2?key=vIDkk8rWlcI2o5POMy6F3Q)

### Key-Value Store

* It is simple of all the NoSQL Database
* The data is stored in key value pair
* **Example** : Redis

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXft8oNYU0xPBEYCroEfzyxPGpNQUQM9s0jKV7qVcuKCXnrK_8FpaGZ6fQrnjgHwdr82mUrUYeLLe34ciXAd-fnAKVdKUFODrsrsr7ZTNgShn-EcV90n2Z5c3uK3uKLzvbdH7PgIMQVxIq9_OtYtTwNnLQ_H?key=vIDkk8rWlcI2o5POMy6F3Q)

### Document Database

> Document Oriented Database is a data storage system used for storing, managing and retrieving documents (JSON)

* Is can be used to store semi-structured data
* **Examples** : MongoDB, CouchDB

### Column Based Databases

> In column based database, DB is designed for storing data as section of columns, rather than as rows of data.

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc5PfDStjYOglNXQIrXJfceIjJFVLHlCh-38ySsij5D6bp6vPhQhmJ9zIVYD0DfR68X80kEBA5IVezRvKOSZM0sdU4MofD0VCgTSeELYJsDATgl8r5o7V7giBcgfcTEi3uBbkDxdVAG8Kw-HuNsV4Yk4FQ?key=vIDkk8rWlcI2o5POMy6F3Q)

### Graph based Database

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcv4AIBGTY1VtNa410xal4M6Oedw8dqPrkHeg9ivpYigxyykhMOUyDnLY7YBi_BVAbFM6Uzcy_oiUbl1sPOKhAM_jvpi6pOk_eHL-47MOrX9uxiIDbygRrsXGDQHeH9rLOHJFIFD-CMktbvd1neG5sRCHL_?key=vIDkk8rWlcI2o5POMy6F3Q)

## Cassandra

> Apache Cassandra, is an open source distributed **NoSQL Database management system** designed to handle large amounts of data across multiple nodes providing High Availability and Fault Tolerance

* It was developed by FB

**Key Characteristics**

* NoSQL Database

* Distributed Architecture

* HA

* Scalability

  ![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdL-hC39QLF7BNQp4qEIVwUuWLTwe9TObNKrEqunuVX50lKrf8eKI3oivELdmnvS6yPwDgxdKYQUuy7xPeoeA3A0-BGJ8jeftGdIOVhqEcLpIWUKzAKGlkWeSPMLMoXPotZRxE2nrbIclrorfMWvlqrG514?key=arOpVOqsQKhZxgZ5mDuBiQ)

  ## Key COmponents

  1. Node : Nodes are individual instances of Cassandra running on Physical servers
  2. Data center : It is a logical grouping of nodes
  3. Cluster : It is a collection of nodes
  4. 



```
CREATE KEYSPACE analytics_ksp WITH REPLICATION = {'class':'SImpleStrategy','replication_factor':'1'};

DESCRIBE analytics_ksp;

CREATE TABLE employee(id INT, name TEXT, age INT, PRIMARY KEY(id));

insert into employee(id,name,age) values (1, ' Ram',22);
insert into employee(id,name,age) values (2, ' Krishna',23);

 select * from employee where name=' Ram' ALLOW FILTERING;
```





```
CREATE TABLE books_by_author (
author_name TEXT,
publish_year INT,
book_id UUID,
book_name TEXT,
rating FLOAT,
PRIMARY KEY((author_name),publish_year,book_id)
) WITH CLUSTERING ORDER BY (publish_year DESC, book_id ASC);


INSERT INTO books_by_author (author_name, publish_year, book_id, book_name,rating)
VALUES('James Patterson',2020, uuid(),'Witch & Wizard',4);


INSERT INTO books_by_author (author_name, publish_year, book_id, book_name,rating)
VALUES('James Patterson',2021, uuid(),'Cross',4.5);


INSERT INTO books_by_author (author_name, publish_year, book_id, book_name,rating)
VALUES('James Patterson',2022, uuid(),'The President is Missing',3.5);


SELECT * FROM books_by_author where author_name='James Patterson' and
publish_year < 2022;


SELECT * FROM books_by_author where author_name='James Patterson' and
publish_year < 2023 and publish_year > 2020;

SELECT * FROM books_by_author where author_name='James Patterson' and
publish_year < 2021 and rating > 4;


SELECT * FROM books_by_author where publish_year < 2022 ALLOW FILTERING;

```

