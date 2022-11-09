from pyspark.sql import SparkSession

scala_version = '2.12'  # TODO: Ensure this is correct
spark_version = '3.3.1'
packages = [
    f'org.apache.spark:spark-sql-kafka-0-10_{scala_version}:{spark_version}',
    'org.apache.kafka:kafka-clients:3.3.1'
]
spark = SparkSession.builder\
    .master("local")\
    .appName("kafka-example")\
    .config("spark.jars.packages", ",".join(packages))\
    .getOrCreate()

print(spark)

topic = 'test10'

df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", topic) \
    .load()

df.selectExpr("topic", "partition", "CAST(key AS STRING)", "CAST(value AS STRING)")\
    .writeStream \
    .format('console') \
    .start().awaitTermination()
