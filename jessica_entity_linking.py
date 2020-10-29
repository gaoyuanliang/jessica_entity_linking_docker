##############jessica_entity_linking.py########
import rdflib
import requests

g = rdflib.Graph()
g.parse("page_ids_en_small.ttl", format='ttl')

def wikipage_id_to_dbpedia_id(entity_id):
	try:
		dbpedia_entity_id = [t[0].toPython() for t in 
			g.query(u"""
			SELECT ?dbpedia_entity_id
			WHERE {
			?dbpedia_entity_id 
			<http://dbpedia.org/ontology/wikiPageID>
			"%s"^^<http://www.w3.org/2001/XMLSchema#integer> .
			} LIMIT 1
			"""%(entity_id))]
		dbpedia_entity_id = dbpedia_entity_id[0]
		return dbpedia_entity_id
	except:
		return None

'''
wikipage_id_to_dbpedia_id("4531823")
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
		for s in entities:
			output.append({'mention':s['mention'],
			'entity_wikipage_id':str(s['entity']),
			'sentence':text,
			'entity_dbpedia_id':wikipage_id_to_dbpedia_id(str(s['entity'])),
			})
		return output
	except:
		return output

'''
entity_linking("I will go to Dubai of the United Arab Emirates.")
'''
##############jessica_entity_linking.py########
