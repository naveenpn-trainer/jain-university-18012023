from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import col, initcap, split, array_distinct
if __name__ == '__main__':
    # Step 01 - Create SparkSession object
    spark = SparkSession.builder.appName("DataFrame Basic Operations").master("local").getOrCreate()
    print(type(spark))

    # Step 02 - Load the data into Spark DataStructure (DataFrame)
    EMPLOYEE_SCHEMA = StructType([
        StructField("id", IntegerType()),
        StructField("name", StringType()),
        StructField("experience", IntegerType()),
        StructField("gender", StringType()),
        StructField("dob", StringType()),
        StructField("company", StringType()),
        StructField("designation", StringType()),
        StructField("doj", StringType()),
        StructField("skills", StringType()),
        StructField("actual_expected_salary", StringType()),
    ])
    employee_df = spark.read.csv(path="./resources/dataset/employee.csv",
                                 header=True,
                                 sep="|",
                                 quote="'",
                                 schema=EMPLOYEE_SCHEMA)
    employee_df.show()
    print("Removing records with missing critical columns")
    employee_df_cleaned = employee_df.dropna(subset=["id","name","experience","company"])
    employee_df_cleaned.show()
    print("Standardize company names")
    employee_df_cleaned = employee_df_cleaned.withColumn("company_name", initcap(col("company"))).drop("company")
    employee_df_cleaned.show()
    print("Derive additional columns")
    employee_df_cleaned = employee_df_cleaned.withColumn("actual_salary", split("actual_expected_salary",",").getItem(0))
    employee_df_cleaned = employee_df_cleaned.withColumn("expected_salary",
                                                         split("actual_expected_salary", ",").getItem(1))
    employee_df_cleaned.show(truncate=False)
    employee_df_cleaned.printSchema()

    print("Remove duplicate skills")
    employee_df_cleaned = employee_df_cleaned.withColumn("skills_new", array_distinct(split("skills",",")))
    employee_df_cleaned.show(truncate=False)