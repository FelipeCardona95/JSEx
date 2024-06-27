import xml.etree.ElementTree as ET
import json

# Parse the XML file
tree = ET.parse('mobs.xml')
root = tree.getroot()

mobs = []

for index, mob in enumerate(root.findall('Mob')):
    mob_data = {
        'id': index,  # Add an ID based on the index
        'uniquename': mob.attrib.get('uniquename'),
        'tier': mob.attrib.get('tier'),
        'mobtypecategory': mob.attrib.get('mobtypecategory'),
        'fame': mob.attrib.get('fame'),
        'prefab': mob.attrib.get('prefab'),
        'avatar' : mob.attrib.get('avatar')
    }
    mobs.append(mob_data)

# Save as JSON
with open('mobs.json', 'w') as json_file:
    json.dump(mobs, json_file, indent=4)
