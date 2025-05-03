from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import col
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
    print(type(employee_df))
    print("---Print Schema---")
    employee_df.printSchema()

    # Step 03 - Operations on the DataFrame
    employee_df.show(truncate=False)

    employee_df.select("name","company").show(n=4)
    print(f"Total No. of records= {employee_df.count()}")

    print(f"Column name= {employee_df.columns}")

    print("---Selecting few columns---")
    employee_df.select(col("name").alias("full_name"),col("company")).show()
