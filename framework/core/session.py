"""
SMIP Spark Session
"""

from pyspark.sql import SparkSession

spark = SparkSession.getActiveSession()

if spark is None:

    spark = SparkSession.builder.getOrCreate()