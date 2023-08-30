from flask import Flask
from flask_restful import Api
from resources.airports import Airport, Airports

app = Flask(__name__)
api = Api(app)

api.add_resource(Airports, '/airports')
api.add_resource(Airport, '/airport/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)