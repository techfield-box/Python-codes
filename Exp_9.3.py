from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum

spark = SparkSession.builder.appName("CanteenReport").getOrCreate()

df = spark.read.csv(r"C:\Users\GAURI RADHIKA\Desktop\PYTHON EXPS\sales.csv", 
                    header=True, inferSchema=True)

df = df.withColumn("total", col("quantity") * col("price"))

print("---Total Sales per Day---")
df.groupBy("date").agg(_sum("total").alias("Daily_Revenue")).show()

print("---Most Sold Item---")
df.groupBy("item").agg(_sum("quantity").alias("Total_Qty")) \
  .orderBy(col("Total_Qty").desc()).limit(1).show()

# Total revenue
total_revenue = df.select(_sum("total")).collect()[0][0]
print(f"TOTAL OVERALL REVENUE : {total_revenue}")

spark.stop()