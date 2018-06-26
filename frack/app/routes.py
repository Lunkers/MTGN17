#Importera moduler
from app import app
from flask import jsonify, request, send_from_directory
import json
from app import db
import os
from app.models import News
import app.news_functions as news_functions
from sqlalchemy import desc



STATIC_DIR = os.path.join(os.getcwd(), "static", "Schmeck")


#Definiera olika URL-er och vad de leder till
@app.route("/")
def index():
    return send_from_directory(STATIC_DIR, "index.html")

#ladda CSS
@app.route("/css/<filename>")
def get_css(filename):
    return send_from_directory(os.path.join(STATIC_DIR, "css"), filename)

#ladda JavaScript
@app.route("/js/<filename>")
def get_js(filename):
    return send_from_directory(os.path.join(STATIC_DIR, "js"), filename)

#ladda media (bild, film, osv)
@app.route("/mediaApi/<file_path>")
def get_media(file_path):
    return send_from_directory(os.path.join(STATIC_DIR, "media"), file_path)

@app.route("/news")
def news_page():
    return send_from_directory(STATIC_DIR, "news.html")

@app.route("/news/<id>")
def news_page_specific(id):
    return send_from_directory(STATIC_DIR, "news.html")

@app.route("/news/edit/<id>")
def edit_page(id):
    return send_from_directory(STATIC_DIR, "edit.html")

@app.route("/newsApi/all")
def get_news():
    return news_functions.get_all_news()

@app.route("/newsApi/<id>")
def get_news_by_id(id):
    return get_news_by_id(id), 201

@app.route("/newsApi/upload", methods=["POST"])
def add_news():
    return news_functions.add_news(request.json), 200


@app.route("/newsApi/delete/<id>")
def delete_news(id):
    return news_functions.delete_news(id), 200

@app.route("/newsApi/edit/<id>", methods=["POST"])
def edit_news(id):
    return news_functions.edit_news(id, request.json), 201
    

