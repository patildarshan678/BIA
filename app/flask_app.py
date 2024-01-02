from flask import Flask
from flask_cors import CORS
from database import db
from models.models import Books
flask_app = Flask(__name__)
CORS(flask_app , support_credentials=True )
environment_configuration = 'config.Developement'
flask_app.config.from_object(environment_configuration)
db.init_app(flask_app)
with flask_app.app_context():
    db.create_all() 
    db.session.commit()