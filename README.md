# jessica_entity_linking_docker


```bash
docker build -t jessica_entity_linking:1.0.1 .

docker run -it \
-p 8080:8080 \
jessica_entity_linking:1.0.1 \
bash

java -Xmx3000m -jar dexter-2.1.0.jar &

```


```python
from jessica_entity_linking import entity_linking

entities = entity_linking("I live at Abu Dhabi but study in Heriot-Watt University Dubai.")

for e in entities:
	print(e)

'''
{'sentence': 'I live at Abu Dhabi but study in Heriot-Watt University Dubai.', 'entity_wikipage_id': '3956428', 'mention': 'heriot watt university dubai', 'entity_dbpedia_id': None}
{'sentence': 'I live at Abu Dhabi but study in Heriot-Watt University Dubai.', 'entity_wikipage_id': '18950756', 'mention': 'abu dhabi', 'entity_dbpedia_id': 'http://dbpedia.org/resource/Abu_Dhabi'}
```

<http://dbpedia.org/resource/Heriot-Watt_University_Dubai> <http://dbpedia.org/ontology/wikiPageID> "3956428"^^<http://www.w3.org/2001/XMLSchema#integer> .
