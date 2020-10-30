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
{'entity_dbpedia_type': 'University', 'entity_dbpedia_id': 'http://dbpedia.org/resource/Heriot-Watt_University_Dubai', 'sentence': 'I study at Heriot-Watt University Dubai, but I live at Abu Dhabi. I want to work at Apple. I was born in China, 1997', 'mention': 'heriot watt university dubai', 'entity_wikipage_id': '3956428'}
{'entity_dbpedia_type': 'Country', 'entity_dbpedia_id': 'http://dbpedia.org/resource/China', 'sentence': 'I study at Heriot-Watt University Dubai, but I live at Abu Dhabi. I want to work at Apple. I was born in China, 1997', 'mention': 'china', 'entity_wikipage_id': '5405'}
{'entity_dbpedia_type': 'City', 'entity_dbpedia_id': 'http://dbpedia.org/resource/Abu_Dhabi', 'sentence': 'I study at Heriot-Watt University Dubai, but I live at Abu Dhabi. I want to work at Apple. I was born in China, 1997', 'mention': 'abu dhabi', 'entity_wikipage_id': '18950756'}
{'entity_dbpedia_type': 'Company', 'entity_dbpedia_id': 'http://dbpedia.org/resource/Apple_Inc.', 'sentence': 'I study at Heriot-Watt University Dubai, but I live at Abu Dhabi. I want to work at Apple. I was born in China, 1997', 'mention': 'apple', 'entity_wikipage_id': '856'}
'''
```

<http://dbpedia.org/resource/Heriot-Watt_University_Dubai> <http://dbpedia.org/ontology/wikiPageID> "3956428"^^<http://www.w3.org/2001/XMLSchema#integer> .
