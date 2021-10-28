import os, datetime
from pyspark.sql.dataframe import DataFrame
from pyspark.sql import SparkSession
from pyspark.context import SparkContext
from pyspark.conf import SparkConf


if __name__ == "__main__":
    conf = SparkConf() \
    .setMaster("local[1]") \
    .setAppName("Test") \
    .set("spark.hadoop.google.cloud.auth.service.account.enable", "true") \
    .set("com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem", "fs.gs.impl") \
    .set("spark.hadoop.google.cloud.auth.service.account.json.keyfile", os.environ['SERVICE_ACCOUNT_PATH'])
    sc = SparkContext(conf=conf)
    spark = SparkSession.builder.appName("KoalasPostgresDemo").config(conf=sc.getConf()).getOrCreate()
    df = spark.read.option("header",True).csv(f"gs://{os.environ['BUCKET_NAME']}/Tests/dummie.csv")
    print("showing number of rows in df: ", df.count())
    print("showing 5 records: ", df.show())

    

