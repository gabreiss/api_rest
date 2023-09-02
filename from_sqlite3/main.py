from flask import Flask
from flask_restful import Api
from resources.airports import Airports, Airport

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

@app.before_request
def create():
    db.create_all()

api.add_resource(Airports, '/airports')
api.add_resource(Airport, '/airport/<string:id>')

if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)
