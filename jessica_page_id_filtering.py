#######jessica_page_id_filtering.py#######
'''
https://wiki.dbpedia.org/downloads-2016-10
'''
import re
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

page_ids_en = sqlContext.read.format('csv')\
	.options(delimiter=' ')\
	.schema(schema)\
	.load('/jessica/page_ids_en.ttl')
page_ids_en.registerTempTable('page_ids_en')

'''
grep "type> <http://dbpedia.org/ontology/" instance_types_en.ttl > instance_types_en_ontology.ttl
'''

instance_types_en = sqlContext.read.format('csv')\
	.options(delimiter=' ')\
	.schema(schema)\
	.load('/jessica/instance_types_en_ontology.ttl')
instance_types_en.registerTempTable('instance_types_en')

out_degree_en = sqlContext.read.format('csv')\
	.options(delimiter=' ')\
	.schema(schema)\
	.load('/jessica/out_degree_en.ttl')
out_degree_en.registerTempTable('out_degree_en')

def extract_outdegree(input):
	try:
		input = input.strip()
		outdegree = re.search(r'\"(?P<outdegree>\d+)\"\^\^', input).group('outdegree')
		outdegree = int(outdegree)
		return outdegree
	except:
		return None

'''
input = u"""
"1"^^<http://www.w3.org/2001/XMLSchema#nonNegativeInteger>"""
extract_outdegree(input)
'''

udf_extract_outdegree = udf(extract_outdegree, IntegerType())

out_degree_en.withColumn('outdegree', udf_extract_outdegree('object')).write.mode("Overwrite").json("/jessica/out_degree_en1")
sqlContext.read.json("/jessica/out_degree_en1").registerTempTable("out_degree_en1")

sqlContext.sql(u"""
	SELECT *, ROW_NUMBER() OVER ( ORDER BY outdegree DESC ) AS outdegree_rank
	FROM out_degree_en1
	""").write.mode("Overwrite").json("/jessica/out_degree_en2")
sqlContext.read.json("/jessica/out_degree_en2").registerTempTable("out_degree_en2")

sqlContext.sql(u"""
	SELECT DISTINCT 
	page_ids_en.subject AS entity_id,
	page_ids_en.relation AS wikipage_relation,
	page_ids_en.object AS wikipage_id,
	instance_types_en.relation AS type_relation,
	instance_types_en.object AS type_id,
	out_degree_en2.relation AS outdegree_relation,
	out_degree_en2.object AS outdegree_id,
	out_degree_en2.outdegree_rank
	FROM page_ids_en 
	LEFT JOIN instance_types_en  
	ON page_ids_en.subject = instance_types_en.subject
	LEFT JOIN out_degree_en2 
	ON page_ids_en.subject = out_degree_en2.subject
	""").write.mode("Overwrite").json("/jessica/dbpedia_page_type")
sqlContext.read.json("/jessica/dbpedia_page_type").registerTempTable("dbpedia_page_type")

sqlContext.sql(u"""
	SELECT COUNT(*),
	COUNT(DISTINCT entity_id)
	FROM dbpedia_page_type
	""").show()
'''
+--------+-------------------------+                   
|count(1)|count(DISTINCT entity_id)|
+--------+-------------------------+
|15797814|                 15797807|
+--------+-------------------------+
'''

sqlContext.sql(u"""
	SELECT 
	CASE 
		WHEN type_relation IS NOT NULL AND type_id IS NOT NULL 
		THEN 
		CONCAT(entity_id, ' ', 
		wikipage_relation, ' ', wikipage_id, ' ; ',
		type_relation, ' ', type_id, ' . ')
		ELSE 
		CONCAT(entity_id, ' ', 
		wikipage_relation, ' ', wikipage_id, ' . ')
	END
	FROM dbpedia_page_type
	""").write.mode("Overwrite").format("text").save("/jessica/dbpedia_page_type1")

'''
cat dbpedia_page_type1/* > dbpedia_page_type.ttl
15797814 dbpedia_page_type.ttl
'''

'''
2274166
3660637
4780541
100000
'''

sqlContext.sql(u"""
	SELECT 
	CASE 
		WHEN type_relation IS NOT NULL AND type_id IS NOT NULL 
		THEN 
		CONCAT(entity_id, ' ', 
		wikipage_relation, ' ', wikipage_id, ' ; ',
		type_relation, ' ', type_id, ' . ')
		ELSE 
		CONCAT(entity_id, ' ', 
		wikipage_relation, ' ', wikipage_id, ' . ')
	END
	FROM dbpedia_page_type
	WHERE outdegree_rank <= 2274166
	""").write.mode("Overwrite").format("text").save("/jessica/dbpedia_page_type_small")

'''
cat dbpedia_page_type_small/* > dbpedia_page_type_small.ttl
2274169 dbpedia_page_type_small.ttl
'''

#######jessica_page_id_filtering.py#######
