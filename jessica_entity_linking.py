##############jessica_entity_linking.py########
import requests

def entity_linking(text):
	try:
		r = requests.post("http://localhost:8080/dexter-webapp/api/rest/annotate", 
			data = {
				"text":text,
				"n":50, "wn":False, "debug":False, "format":"text", "min-conf":"0.5",
			})
		#print(r.json())
		return [
			{'mention':s['mention'],
			'entity_wikipage_id':str(s['entity']),
			'sentence':text,
			} for s in r.json()['spots']]
	except:
		return None
##############jessica_entity_linking.py########
