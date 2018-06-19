from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = os.path.join(os.getcwd(), "static", "Schmeck", "media")

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
db = SQLAlchemy(app)


from app import routes
from app import models
db.create_all() #OBS UTAV BARA HELVETE denna ska inte finnas med i prod, den dumpar och skapar en ny databas