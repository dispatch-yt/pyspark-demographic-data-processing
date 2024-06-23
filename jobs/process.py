from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg

# Create a Spark session
spark = SparkSession.builder \
    .appName("Demographic Insights") \
    .getOrCreate()

basepath = "/opt/bitnami/spark/jobs"

# Read the CSV file into a DataFrame
df = spark.read.csv(basepath + "/demographic_divident.csv", header=True, inferSchema=True)

# Average Life Expectancy by Location
avg_life_expectancy = df.groupBy("Location") \
    .agg(avg("LEx").alias("AvgLifeExpectancy")) \
    .orderBy("Location")

# Save average life expectancy to CSV
avg_life_expectancy.write.csv(basepath + "/out/avg_life_expectancy.csv", header=True, mode="overwrite")

# Total Births and Deaths by Location
total_births_deaths = df.groupBy("Location") \
    .agg(
        sum("Births").alias("TotalBirths"),
        sum("Deaths").alias("TotalDeaths")
    ) \
    .orderBy("Location")

# Save total births and deaths to CSV
total_births_deaths.write.csv(basepath + "/out/total_births_deaths.csv", header=True, mode="overwrite")

# Stop the Spark session
spark.stop()
