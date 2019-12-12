from app import db

class Restaurants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    r_username = db.Column(db.String(20), nullable=False)
    r_password = db.Column(db.String(200), nullable=False)
    r_name = db.Column(db.String(50), nullable = False)
    r_adress = db.Column(db.String(100), nullable = False)
    r_ownername = db.Column(db.String(50), nullable = False)
    r_key = db.Column(db.String(15), nullable = False, unique= True)
    r_reservations = db.relationship('Reservations', backref = 'restaurant')
    
    def __repr__(self):
        return "<Title: {}>".format(self.r_name)

class Reservations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    s_day = db.Column(db.Date)
    s_r_id = db.Column(db.String(15), db.ForeignKey('restaurants.r_key'), nullable=False)
