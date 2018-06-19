from flask import Flask
import os

UPLOAD_FOLDER = os.path.join(os.getcwd(), "static", "Schmeck", "media")

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


from app import routes
from app import news