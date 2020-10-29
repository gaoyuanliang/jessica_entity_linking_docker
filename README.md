# jessica_entity_linking_docker


```bash
docker build -t yan_entity_linking:1.0.1 .

docker run -it \
-p 8080:8080 \
yan_entity_linking:1.0.1 \
bash
```


```python
from jessica_entity_linking import entity_linking

entities = entity_linking("I live at Abu Dhabi but study in Heriot-Watt University Dubai.")

for e in entities:
	print(e)

'''
{'entity_wikipage_id': '3956428', 'sentence': 'I live at Abu Dhabi but study in Heriot-Watt University Dubai.', 'mention': 'heriot watt university dubai'}
{'entity_wikipage_id': '18950756', 'sentence': 'I live at Abu Dhabi but study in Heriot-Watt University Dubai.', 'mention': 'abu dhabi'}
''' 
```

<http://dbpedia.org/resource/Heriot-Watt_University_Dubai> <http://dbpedia.org/ontology/wikiPageID> "3956428"^^<http://www.w3.org/2001/XMLSchema#integer> .
