#######jessica_entity_linking_example.py########

from jessica_entity_linking import entity_linking

entities = entity_linking("I live at Abu Dhabi but study in Heriot-Watt University Dubai.")

for e in entities:
	print(e)

#######jessica_entity_linking_example.py########
