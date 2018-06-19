#Importera moduler
from app.webapp import app as webapp
from flask import jsonify, request, send_from_directory
import json
from app import news
import os



static_dir = os.path.join(os.getcwd(), "static", "Schmeck")


#Definiera olika URL-er och vad de leder till
@webapp.route("/")
def index():
    return send_from_directory(static_dir, "index.html")


@webapp.route("/css/<filename>")
def get_css(filename):
    return send_from_directory(os.path.join(static_dir, "css"), filename)

@webapp.route("/js/<filename>")
def get_js(filename):
    return send_from_directory(os.path.join(static_dir, "js"), filename)

@webapp.route("/mediaApi/<file_path>")
def get_media(file_path):
    return send_from_directory(os.path.join(static_dir, "media"), file_path)

@webapp.route("/newsApi/all")
def get_news():
    return jsonify(news.get_news(None))

@webapp.route("/newsApi/<id>")
def get_news_by_id(id):
    try:
        return jsonify(news.get_news(id)), 201
    except:
        return "PROBLEM!", 500

@webapp.route("/newsApi/upload")
def add_news():
    
    resp = news.save_to_db(request.json)
    if resp:
        return "WOO DET FUNKADE", 201
    else:
        return "PROBLEM", 500

@webapp.route("/newsApi/delete/<id>")
def delete_news(id):
    resp = news.delete_news(id)
    if resp:
        return "nyheten med id " + id + " raderades!", 200
    else:
        return "något gick fel", 500

@webapp.route("/newsAPI/edit/<id>")
def edit_news(id):
    resp = news.edit_news(id, request.json)

@webapp.route("/news/edit/<id>")
def edit_page():
    return send_from_directory(static_dir, "edit.html")