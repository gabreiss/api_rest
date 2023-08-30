import json

with open("resources\\data.json", 'r', encoding='utf8') as arquivo:
            airports_json = json.load(arquivo)

for airport in airports_json:
        print(airport['id'])

print(airports_json)