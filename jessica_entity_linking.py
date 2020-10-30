##############jessica_entity_linking.py########
import os
import requests

print('loading the entity linking models')
os.system(u"""
	java -Xmx3000m -jar dexter-2.1.0.jar &
	""")

'''
wikipage_id_to_dbpedia_id("4531823")

15,797,814 page_ids_en.ttl
'''

def wikipage_id_to_dppedia_id_type(input):
	output = {"dbpedia_type":None, "dbpedia_id":None}
	try:
		line = os.popen(u"""
		grep  "<http://dbpedia.org/ontology/wikiPageID> \\"%s\\"^^<" dbpedia_page_type.ttl 
		"""%(input)).read()
	except:
		return output
	try:
		output["dbpedia_type"] = re.search(
			r'type\> \<http\:\/\/dbpedia\.org\/ontology\/(?P<dbpedia_type>[^\<\>]+)\> ', 
			line).group('dbpedia_type')
	except:
		pass
	try:
		output["dbpedia_id"] = re.search(
			r'^\<(?P<dbpedia_id>[^\<\>]+)\> ', 
			line).group('dbpedia_id')
	except:
		pass
	return output

'''
wikipage_id_to_dppedia_id_type("29465759")
'''

def entity_linking(text):
	output = []
	try:
		r = requests.post("http://localhost:8080/dexter-webapp/api/rest/annotate", 
			data = {
				"text":text,
				"n":50, "wn":False, "debug":False, "format":"text", "min-conf":"0.5",
			})
		#print(r.json())
		entities = r.json()['spots']
		entity_wikipage_ids = list(set([str(s['entity']) for s in entities]))
		entity_dbpedia_id_lookup = {}
		entity_dbpedia_type_lookup = {}
		for e in entity_wikipage_ids:
			dbpedia = wikipage_id_to_dppedia_id_type(e)
			entity_dbpedia_id_lookup[e] = dbpedia['dbpedia_id']
			entity_dbpedia_type_lookup[e] = dbpedia['dbpedia_type']
		for s in entities:
			output.append({'mention':s['mention'],
			'entity_wikipage_id':str(s['entity']),
			'sentence':text,
			'entity_dbpedia_id':entity_dbpedia_id_lookup[str(s['entity'])],
			'entity_dbpedia_type':entity_dbpedia_type_lookup[str(s['entity'])],
			})
		return output
	except:
		return output

'''
for e in entity_linking("I study at Heriot-Watt University Dubai, but I live at Abu Dhabi. I want to work at Apple. I was born in China, 1997"):
	print(e)

for e in entity_linking("I live at the Al Reem Island of Abu Dhabi and work in the Aldar headquarters building."):
	print(e)
'''
##############jessica_entity_linking.py########
