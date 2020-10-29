#######jessica_entity_linking_example.py########

from jessica_entity_linking import entity_linking

entities = entity_linking("Donald J. Trump is fucking the United States.")

for e in entities:
	print(e)

#######jessica_entity_linking_example.py########
