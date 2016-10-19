# World of Warcraft
# Mythic Dungeon Runs to Legendaries Owned

import requests
import json
import re

API_KEY = '8nm9qefsmsvnn5s4k7qa3p6gsp8pa2wf'
BASE_URI = 'https://us.api.battle.net/wow/character/{}/{}?fields={}&locale=en_US&apikey={}'
REALM = 'Icecrown'
CHARACTER = 'Renray'

valid_dungeons = [
				  'Eye of Azshara', 
				  'Darkheart Thicket', 
				  'Arcway', 
				  'Court of Stars',
				  'Maw of Souls',
				  'Neltharion\'s Lair',
				  'Assault on Violet Hold',
				  'Vault of the Wardens',
				  'Black Rook Hold',
				  'Halls of Valor'
				 ]
fields = ['statistics']
uri = BASE_URI.format(REALM, CHARACTER, ','.join(fields), API_KEY)

print('Querying > {}'.format(uri))

req = requests.get(uri)
json = req.json()
data = json['statistics']['subCategories'][5]['subCategories'][6]['statistics']

rgx = re.compile('[A-Za-z\'\s]+ (kills|defeats) \(Mythic [{}]+\)'.format('|'.join(valid_dungeons)))
valid_fields = [x for x in data if rgx.match(x['name'])]
specific_counts = '\n'.join(['{}: {}'.format(x['name'].split('(')[0], x['quantity']) for x in valid_fields])
total_mythic_dungos = sum(x['quantity'] for x in valid_fields)
#valid_fields = [x['name'] for x in data]

ids = [x['id'] for x in valid_fields]

print(valid_fields)
print(ids)
#print(specific_counts)
#print(total_mythic_dungos)
#print(data)


