# jessica_entity_linking_docker


```bash
docker build -t jessica_entity_linking:1.0.1 .

docker run -it \
-p 8080:8080 \
jessica_entity_linking:1.0.1 \
bash
```


```python
from jessica_entity_linking import entity_linking

for e in entity_linking("I study at Heriot-Watt University Dubai, but I live at Abu Dhabi. I want to work at Apple. I was born in China, 1997"):
	print(e)

'''
{'entity_wikipage_id': '3956428', 'sentence': 'I study at Heriot-Watt University Dubai, but I live at Abu Dhabi. I want to work at Apple. I was born in China, 1997', 'entity_dbpedia_type': None, 'mention': 'heriot watt university dubai', 'entity_dbpedia_id': None}
{'entity_wikipage_id': '5405', 'sentence': 'I study at Heriot-Watt University Dubai, but I live at Abu Dhabi. I want to work at Apple. I was born in China, 1997', 'entity_dbpedia_type': None, 'mention': 'china', 'entity_dbpedia_id': None}
{'entity_wikipage_id': '18950756', 'sentence': 'I study at Heriot-Watt University Dubai, but I live at Abu Dhabi. I want to work at Apple. I was born in China, 1997', 'entity_dbpedia_type': None, 'mention': 'abu dhabi', 'entity_dbpedia_id': None}
{'entity_wikipage_id': '856', 'sentence': 'I study at Heriot-Watt University Dubai, but I live at Abu Dhabi. I want to work at Apple. I was born in China, 1997', 'entity_dbpedia_type': None, 'mention': 'apple', 'entity_dbpedia_id': None}
'''
```

<http://dbpedia.org/resource/Heriot-Watt_University_Dubai> <http://dbpedia.org/ontology/wikiPageID> "3956428"^^<http://www.w3.org/2001/XMLSchema#integer> .
