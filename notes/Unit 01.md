# Basics of RDBMS

## What is a Database

> A Database refers to the collection of structured or unstructured data

A database is a collection of related data which is categorized into two

1. Structured data
2. Unstructured data

while the DBMS is the software managing the database.

## Database Management System

Oracle, SQL Server, MySQL, MongoDB they are not database; they are DBMS

Database + Management System = Database System

> A DBMS is a software designed to manage, organize, store, retrieve and manipulate data
>
>  A DBMS is the software that would be installed on a server which manages one or more databases.

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe5Xc562uwzCq3I04CN6kUMrPBE4yQj78b0Zsq1h4OxhDbFo8U2ReHeQOOn_7pRtNZiAmliOAR9x6QEMXcQt_xBMJtWAy-gGWGYf2kbkmgW9BWJ7ixFHI5aBq39YgZKsup0oh86fGhhdGuOSv0wqh6uq3fJ?key=fmbHaZXyYTSWY9g1Zr88KA)

### Key Characteristics of DBMS

1. **Data Storage** : Stores data is structured or semi-structured formats such as files, key-value pairs, objects or hierarchical structured
2. **Data Management** : Provides tools to CRUD
3. **Data Access** : Supports multiple applications accessing the database.
4. **Security** : Ensures that data access is restricted to authorized users

### Different Types of DBMS

There are different DBMS

1. File System Database
2. <mark>RDBMS</mark>
3. Hierarchical Database
4. Network Database System
5. Object Oriented Database System
6. <mark>NoSQL Database Systems </mark>

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcVO9WVE4RmKXK0WdTghTNDtJSAfW1RNiET3pCS9cQx2HyfUf-krIZdbdY1sCB3u1pX8MDnR9Dgf0UnX7KdYpMS4Mo4IcDr0W2Tyae_BYYunuGUhGzX8udpWdlHtQ2ZyR_zZfhCPUX37Cwxb1tOofaoUhQU?key=fmbHaZXyYTSWY9g1Zr88KA)

#### File System Database

> A DBMS that stores data is flat files or directories, rather than in structured tables.

**Example**

* Window File System or LFS where data is stored in files and folders

#### Hierarchical Database Systems

> Data is organized in a tree-like structure, where each record has a single parent, and reach parent can have multiple children

**Example**

* IBM Information Management System
* Window Registry

#### Network Database System

> Similar to HDS but allows complex relationships between data

**Example**

* IDS (Integrated Data Store)

#### NoSQL Database

> NoSQL databases provide a way to store data in formats that aren't restricted to relational tables. they handle structured or semi-structured data.

**Example**

* MongoDB (Document based)
* Redis (Key-value store)
* Cassandra
* Couch DB

#### Object Oriented Database Systems

> These DBMS uses object-oriented programming concepts to store data as objects, 

```
CREATE TABLE student(
id INT,
name STRING)

class Stuedent{
	id int,
	name string
}
```

**Examples**

* ObjectDB
* Versant Object Databases

#### XML Databases

> Specifically designed to store XML documents

**Examples**

* BaseX
* [eXist-db ](http://exist-db.org/)

### Applications of DBMS

1. Banking and Finance
2. Education and Academic Institutions
3. AI

## 2 Tier and 3 Tier

> 2 tier and 2 tier architectures are architecture patterns used to design applications and systems

* A tier refers to the physical separation of an application

### 2 Tier

> 2 tier architecture also know as client server architecture, is a software architecture pattern that divides an application into two main tiers or layers

1. Client Layer (User Interface)
2. Database Layer

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcrmkBFJpP30qPzfjxnWe4p4_7n04TDc1G-hzmW5tAdWn4X3DUim7SUiU_-33J5kudqMiTNyeOa6Q9vAu4gaTlhgSL7ObpRYULTtUOys1lfmUl-qRmc4EFmsNGmjohhSInW6O2zBFKURm05wIVZ854W9Ha1?key=fmbHaZXyYTSWY9g1Zr88KA)



### 3 Tier

> In a 3-tier architecture, the application is divided into three layers

1. Presentation Layer (Client / User Interface)
2. Application Layer (Business Layr)
3. Database Layer : (Data Storage)

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfYRFygHnuqw2VU8AlXvSje9qJFfwXh6aCUSyqwPu8I5GjIgMJiNa3Aomw29Kuc0Xklnk0G5SWa7HQrpo1yUjjC727XAGayNnBUIZ07_ED-aDY1r3cw2huLwfv47RyNl4iRb02XBJ31JmWkMJvLJBIDWY6X?key=fmbHaZXyYTSWY9g1Zr88KA)

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdFIcNt-TNMxPTjfWTYeytZvEmfdPKzXjbnhdfGd8ZkN8-ItmL6WXvqUGZvPQ00_dXjaslkogMS7w9FffjKDYlwNzHIn1MxBiDiN__nZ6GlDbml_huuvkJOtlvknLCnctgRWZFROVtj8By7PkqwxvBjRiXU?key=fmbHaZXyYTSWY9g1Zr88KA)

## Constraints

> In RDBMS, Key Constraints are rules applied to table columns to ensure the validity, consistency and integrity of the data.

1. Primary Key Constraint

2. Foreign Key Constraint

3. Unique Constraints

4. Composite Key

   ```
   CREATE TABLE orderdetails(
   	orderid INT,
   	productid INT,
   	....
   	....
   	PRIMARY
   )
   ```

   