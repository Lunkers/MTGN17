#Importera moduler
from app.webapp import app as webapp
from flask import jsonify, request, send_from_directory
import json
from app import news
import os


#definiera filsökväg till content
static_dir = os.path.join(os.getcwd(), "static", "Schmeck")


#Definiera olika URL-er och vad de leder till
@webapp.route("/")
def index():
    return send_from_directory(static_dir, "index.html")

#Routes för asset-hämtning (Javascript, CSS, Media)
@webapp.route("/css/<filename>")
def get_css(filename):
    return send_from_directory(os.path.join(static_dir, "css"), filename)

@webapp.route("/js/<filename>")
def get_js(filename):
    return send_from_directory(os.path.join(static_dir, "js"), filename)

@webapp.route("/media/<file_path>")
def get_media(file_path):
    return send_from_directory(os.path.join(static_dir, "media"), file_path)

@webapp.route("/news/all")
def get_news():
    return jsonify(news.get_news(None))

@webapp.route("/news/<id>")
def get_news_by_id(id):
    try:
        return jsonify(news.get_news(id)), 201
    except:
        return "PROBLEM!", 500

@webapp.route("/news/upload")
def add_news():
    
    resp = news.save_to_db(request.json)
    if resp:
        return "WOO DET FUNKADE", 201
    else:
        return "PROBLEM", 500

