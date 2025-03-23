# Apache Spark

> Apache Spark is an in-memory <mark>cluster computing framework</mark> designed to <u>handle a wide range of big data workloads</u>.

**Applications of Spark**

1. Data Integration and ETL
2. High Performance Batch Computation
3. Machine Learning Analytics
4. Stream processing framework

**Important Points**

* Apache Spark is natively written using Scala Programming.
* Apache Spark is built on top of MapReduce and it extends MapReduce to efficiently process data.
* The main feature of Apache Spark is its **in-memory** cluster computing framework

## What is PySpark

> PySpark is the python API for Apache Spark

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeizcnqTQmM7Qbn-0jjZoKn5vCd-rvsDLId8hZCNnB8clRMCWnBMw4JqjwwvsUW3bb7lJepQu0zwR_dbrDHQvdsZgWSwzMhNKsVu2J8EGoNJ8afboDhFnJQFN87sg0GIE4XXW-dAOZrFi9pskepXfAnaDJG?key=_he-T4Jq934AhrSZa-Be-g)

## Spark Ecosystem

Spark comes with bunch of libraries and interfaces

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcFIIRDyQwCgXg-tBBqyhJjRL-2ZFTjTBeC_Bssvcq6OTeEyxAL0t_hqhjEPtXBsL6m_QAQwoeu26KMwMp5ITiK9dmdUatBjN5PBksdpywnIQ333s5dVt4dQzrCHBfS-MOOGt621iz3Gyf7t6-Laqdl-7C1?key=_he-T4Jq934AhrSZa-Be-g)

## Spark Interactive Shell

1. Spark Shell (Scala)
2. PySpark Shell : (Python)

## Spark API's

1. Low Level (RDD's) - Deprecated
2. High Level  - (DataFrame, Dataset API)



## Building a Spark Application

1. Load the data
2. Process the data
3. Write the results to different destination systems

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe76oTQ4TCQt0lNYQa7gQTIa74Z-WSmTCAMQdVzPyVCci2N2RGu30rtrn_xl9cOODQJGTYOqkaenPMEsfXBGLsOpjJOk4UqzDrMPxl3CyCzLhx0vg5UQbPsMhiQvfA426Vpien8nd2-U3kePApg3PwZu9A?key=_he-T4Jq934AhrSZa-Be-g)

## RDD's (Resilient Distributed Dataset)

> RDD's are the fundamental data structure in Apache Spark,

* Resilient - Fault tolerant
* Distributed : Data is spread among multiple nodes
* Dataset : Collection of partitioned data

## Partitions

RDD is a collection of objects that is partitioned and distributed across nodes  in a cluster

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe5I5aGKc7AYFU0QNGe0nZnzzQ0f8bHpvo0DbbtX8O0WeqvhbIMPR6l_QpQKdCErFq49MefWJpSXHRk9JiGR5_JuLsruzU9z4mhzhfgDZxyIwIC24o4vNnmUMrrNcdg7PuBf9cUpg-Hvzs4fvPavecqUlOP?key=Dxp7lTxgvspH2ig-I7LuEw)

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc3WtT7cwdxQJ9SzJVjDwzD0mZy4aaWnzx2hmzJCBTU6dO42a6bDwDOaS800JWuqwKyZBHLMWxVhek72JREG_EQnEY9r05L8mNSfJCT75BMzVnrKK7OZCzEsLsvDWJdJuBc3VTFothKjXktJ9ZbQEw3FNaS?key=Dxp7lTxgvspH2ig-I7LuEw)

## RDD Creations

1. Create an RDD from Collection

   ```
   L = [1,3,2,4,3,4,5,6]
   rdd = sc.parallelize(L)
   print(type(rdd))
   ```

2. Create an RDD from external source

   ```
   rdd = sc.textFile("c:/abc.txt")
   type(rdd)
   ```

   

**Note**

* All the methods to create RDD is present inside SparkContext (sc)

## RDD Operations

1. Transformations
2. Actions

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXft0wW8GIYcRuC1sN6OBJvVHbmPGoaK669bbjADtpOTqwBBqR3_DzcPxhADIQFvEty2O5JkfFHSxLUnF3KVxhRWC2jzfyg5uiEBhvLZs0U_LZ-p4pJ_KIq5eky6DhikgFwAKcq9FXAl_gc8jszQUsFqE6Yr?key=Dxp7lTxgvspH2ig-I7LuEw)



### Transformation

* Transformation creates a new RDD
* Transformations are lazy.

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdg3tgCBdxAf5h4IMvikfNH2D_pIXWKkO6Li94NTDb9r3yQqetgGHmdggop9J3XFV093TfeXFfulRujy-cm37fYUkQ9n-d4xJQKh1OLj4L8QdsuqFnXRTnXg5tMfPN0vprkgn1TyB81uynGlaAnyBSdVkgt?key=Dxp7lTxgvspH2ig-I7LuEw)

### Actions

* Final computation happens only when you execute an action.