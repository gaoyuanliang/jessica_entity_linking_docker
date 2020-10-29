#######jessica_entity_linking_example.py########

from jessica_entity_linking import entity_linking

text = u"the city of Abu Dhabi"

entities = entity_linking(text)

for e in entities:
	print(e)

'''
{'entity_wikipage_id': '3956428', 'sentence': 'I live at Abu Dhabi but study in Heriot-Watt University Dubai.', 'mention': 'heriot watt university dubai'}
{'entity_wikipage_id': '18950756', 'sentence': 'I live at Abu Dhabi but study in Heriot-Watt University Dubai.', 'mention': 'abu dhabi'}
''' 
#######jessica_entity_linking_example.py########
