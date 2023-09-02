from sql_alchemy import db

class AirportModel(db.Model):
    __tablename__ = 'airports'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(100))
    country = db.Column(db.String(100))

    def __init__(self, id, name, city, country):
        self.id = id
        self.name = name
        self.city = city
        self.country = country

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "city": self.city,
            "country": self.country
        }
    
    @classmethod
    def find_airport(cls, id):
        airport = cls.query.filter_by(id=id).first()
        if airport:
            return airport
        return None
    
    def save_airport(self):
        db.session.add(self)
        db.session.commit()

    def update_airport(self, name, city, country):
        self.name = name
        self.city = city
        self.country = country

    def delete_airport(self):
        db.session.delete(self)
        db.session.commit()