#Importera moduler
from app import app
from flask import jsonify, request, send_from_directory
import json
from app import db
import os
from app.models import News



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
    news_list = News.query.all()
    print(news_list)
    res_list =[]
    for news in news_list:
        res_list.append(news.as_dictionary())
    return jsonify(res_list)

@app.route("/newsApi/<id>")
def get_news_by_id(id):
    try:
        return jsonify(news.get_news(id)), 201
    except:
        return "PROBLEM!", 500

@app.route("/newsApi/upload")
def add_news():
    req_json = request.json
    print(req_json)
    n = News(author = req_json["author"])
    db.session.add(n)
    db.session.commit()
    return jsonify(req_json)


@app.route("/newsApi/delete/<id>")
def delete_news(id):
    resp = news.delete_news(id)
    if resp:
        return "nyheten med id " + id + " raderades!", 200
    else:
        return "något gick fel", 500

@app.route("/newsAPI/edit/<id>")
def edit_news(id):
    resp = news.edit_news(id, request.json)

