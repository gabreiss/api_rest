from flask_restful import Resource, reqparse
from resources.AirportModel import AirportModel

class Airports(Resource):
    def get(self):
        return {'airports': [airport.json() for airport in AirportModel.query.all()]}
    
class Airport(Resource):
    args = reqparse.RequestParser()
    args.add_argument('name')
    args.add_argument('city')
    args.add_argument('country')

    def get(self, id):
        airport = AirportModel.find_airport(id)
        if airport:
            return airport.json()
        return {"message": "airport not found"}, 404
    
    def post(self, id):
        if AirportModel.find_airport(id):
            return {"message": f"Hotel id {id} already exists"}
        
        data = Airport.args.parse_args()
        airport = AirportModel(id, **data)
        
        try:
            airport.save_airport()
        except:
            return {"message": "An internal error occured trying to save"}, 500
       
        return airport.json(), 201
    
    def put(self, id):
        data = Airport.args.parse_args()
        airport_found = AirportModel.find_airport(id)
        if airport_found:
            airport_found.update_airport(**data)
            airport_found.save_airport()
            return airport_found.json(), 201
        airport = AirportModel(id, **data)
        try:
            airport.save_airport()
        except:
            return {"message": "An internal error occured trying to save"}, 500
        return airport.json(), 201     
    
    def delete(self, id):
        airport = AirportModel.find_airport(id)
        if airport:
            try:
                airport.delete_airport()
            except:
                return {"message": "An internal error occured trying to delete the airport"}, 500
            return {"message": "airport deleted"}
        return {"message": "airport not found"}, 404