# Pig

> Apache Pig is a high level platform for creating MapReduce programs used with Hadoop.

* It is mainly used for analyzing large datasets.
* Pig scripts are written in **Pig Latin**, a language that abstracts the complexity of writing raw MapReduce programs

**Pig Execution Modes**

1. Local Mode
2. MapReduce Mode (Default)
3. Tez Mode (Tez is an execution engine)

**Pig Latin Data Types**

* int
* long
* float
* doublw
* chararray (string)

**Complex Types**

* Tuple : A record (1,"Ram")
* Bag : A collection of tuples { (), () }
* Map : Key-value pairs [name#Ram , age#25



## Hands-on

**Example 01** - Load the data

```bash
grunt> movies_raw = LOAD '/user/hadoop/movies_data.csv' USING PigStorage(',')
grunt> DESCRIBE movies_raw;
Schema for movies_raw unknown.
grunt> DUMP movies_raw;


movies_raw = LOAD '/user/hadoop/movies_data.csv' USING PigStorage(',')
AS (movie_id:int, title:chararray, year:int, rating:float, votes:int);

DESCRIBE movies_raw;
grunt> top_4_movies = LIMIT movies_raw 4;
grunt> DUMP top_4_movies
grunt> STORE top_4_movies INTO '/user/hadoop/output_001' USING PigStorage(',') ;
```

**Filter**

```
grunt> movies_after_1995 = FILTER movies_raw BY year >1995;
grunt> top_4_records = LIMIT movies_after_1995 4
grunt> DUMP top_4_records;

```

**Average Rating of all movies**

```
ratings = FOREACH movies_raw GENERATE rating;
average_rating = FOREACH(GROUP ratings ALL) GENERATE AVG(ratings.rating);
DUMP average_rating;
```

**Group movies by year and count **

```
group_by_year = GROUP movies_raw by year;
count_by_year = FOREACH group_by_year GENERATE group as year, COUNT(movies_raw) as movie_count;
DUMP count_by_year;
```

**Store**

```
grunt> movies_raw = LOAD '/user/hadoop/movies_data.csv' USING PigStorage(',')
AS (movie_id:int, title:chararray, year:int, rating:float, votes:int);
grunt> top_4_movies = LIMIT movies_raw 4;
grunt> DUMP top_4_movies
grunt> STORE top_4_movies INTO '/user/hadoop/output_001' USING PigStorage(',') ;
```

**Sorting**

```
sorted_movies = ORDER movies_raw BY rating DESC;
DUMP sorted_movies;
```

```
sorted_by_votes = ORDER movies_raw BY votes DESC;
top_3_voted = LIMIT sorted_by_votes 3;
DUMP top_3_voted;
```

**FInd MOvies whose title starts with 'The'**

```
the_movies = FILTER movies_raw BY STARTSWITH(title,'The')
DUMP the_movies
```



```
log_titles = FILTER movies_raw BY SIZE(title)>68;
DUMP log_titles;
```



```
oldest_sorted = ORDER movies_raw BY year ASC;
oldest_movie = LIMIT oldest_sorted 1;
DUMP oldest_movie;
```

