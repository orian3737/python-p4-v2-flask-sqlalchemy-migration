from app import app
from models import db, Department  # Ensure to import the app, db, and Department model

def drop_departments_table():
    with app.app_context():
        Department.__table__.drop(db.engine)

if __name__ == '__main__':
    drop_departments_table()