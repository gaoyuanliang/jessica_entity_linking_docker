#######jessica_page_id_filtering.py#######
import csv
from pyspark import *
from pyspark.sql import *
from pyspark.sql.types import *
from pyspark.sql.functions import *

sc = SparkContext("local")
sqlContext = SparkSession.builder.getOrCreate()

print('loading the data')

schema = StructType()\
	.add("subject",StringType(),True)\
	.add("relation",StringType(),True)\
	.add("object",StringType(),True)

instance_types_en_small = sqlContext.read.format('csv')\
	.options(delimiter=' ')\
	.schema(schema)\
	.load('/jessica/instance_types_en_small.ttl')
instance_types_en_small.registerTempTable('instance_types_en_small')

page_ids_en = sqlContext.read.format('csv')\
	.options(delimiter=' ')\
	.schema(schema)\
	.load('/jessica/page_ids_en.ttl')
page_ids_en.registerTempTable('page_ids_en')

sqlContext.sql(u"""
	SELECT page_ids_en.*
	FROM page_ids_en
	JOIN instance_types_en_small 
	ON instance_types_en_small.subject 
	= page_ids_en.subject
	""").write.mode("Overwrite").json("/jessica/page_ids_en_small")

page_ids_en_small = sqlContext.read.json("/jessica/page_ids_en_small")
#456835

page_ids_en_small.registerTempTable("page_ids_en_small")
sqlContext.sql(u"""
	SELECT CONCAT(subject, ' ', relation, ' ', object, ' . ')
	FROM page_ids_en_small
	""").write.format("text").save("/jessica/page_ids_en_small1")

'''
cat /jessica/page_ids_en_small1/* \
> /jessica/page_ids_en_small.ttl
'''
#######jessica_page_id_filtering.py#######
