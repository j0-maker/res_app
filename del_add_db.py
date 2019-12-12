from app import db

def create(database):
    database.create_all()

def dropall(database):
    database.drop_all()

create(db)
#dropall(db)

