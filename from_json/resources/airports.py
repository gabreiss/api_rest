from flask_restful import Resource, reqparse
import json

class Airports(Resource):
    def get(self):
        with open("resources\\data.json", 'r', encoding='utf8') as arquivo:
            airports_json = json.load(arquivo)
        return {"airports": airports_json}
    
class Airport(Resource):
    args = reqparse.RequestParser()
    args.add_argument('name')
    args.add_argument('city')
    args.add_argument('country')

    def _open_json():
        with open("resources\\data.json", 'r', encoding='utf8') as arquivo:
            airports_json = json.load(arquivo)
        return airports_json 
    
    def _find_airport(id):
        airports_json = Airport._open_json()
        for airport in airports_json:
            if airport['id'] == id:
                return airport, airports_json
        return None, airports_json
    
    def _write_json(airports_json):
        with open("resources\\data.json", 'w', encoding='utf-8') as f:
            json.dump(airports_json, f, ensure_ascii=False)

    def get(self, id):
        airport, *args = Airport._find_airport(id)
        if airport:
            return airport
        return {"message": "airport not found"}, 404
    
    def post(self, id):
        airports_json = Airport._open_json()
        data = Airport.args.parse_args()
        new_airport = {'id': id, **data}
        airports_json.append(new_airport)
        Airport._write_json(airports_json)
        return new_airport, 200
    
    def put(self, id):
        data = Airport.args.parse_args()
        new_airport = {'id': id, **data}
        airport, airports_json = Airport._find_airport(id)
        if airport:
            airport.update(new_airport)
        else:
            airports_json.append(new_airport)
        Airport._write_json(airports_json)
        return new_airport, 201
    
    def delete(self, id):
        airports_json = Airport._open_json()
        airports_json = [airport for airport in airports_json if airport['id'] != id]
        Airport._write_json(airports_json)
        return {"message": "airport deleted"}, 200