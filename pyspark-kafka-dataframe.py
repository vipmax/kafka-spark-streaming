from pyspark.sql import SparkSession

scala_version = '2.12'  # TODO: Ensure this is correct
spark_version = '3.3.1'
packages = [
    f'org.apache.spark:spark-sql-kafka-0-10_{scala_version}:{spark_version}',
    'org.apache.kafka:kafka-clients:3.3.1'
]

spark = SparkSession.builder\
   .master("local[*]")\
   .appName("kafka-example")\
   .config("spark.jars.packages", ",".join(packages))\
   .getOrCreate()

print(spark)

data = ['Hello', 'World']
df = spark.createDataFrame([{'value': v} for v in data])

topic = 'test10'

df.write.format("kafka")\
  .option("kafka.bootstrap.servers", "localhost:9092")\
  .option("topic", topic)\
  .save()

from pyspark.sql.functions import col, concat, lit

kafkaDf = spark.read.format("kafka")\
  .option("kafka.bootstrap.servers", "localhost:9092")\
  .option("subscribe", topic)\
  .option("startingOffsets", "earliest")\
  .load()

kafkaDf.select("topic", "partition", "offset", col("value").cast("string")).show(n=1000)