#Importera moduler
from app import app
from flask import jsonify, request, send_from_directory, g
import json
from app import db
import os
from app.models.news import News
import app.news_functions as news_functions
import app.image_functions as image_functions
import app.user_functions as user_functions
import app.document_functions as document_functions
from sqlalchemy import desc
from app.authentication import requires_auth, requires_auth_token, check_auth

STATIC_DIR = os.path.join(os.getcwd(), "static", "Schmeck")


#Definiera olika URL-er och vad de leder till
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return send_from_directory(STATIC_DIR, "index.html")

#ladda CSS
@app.route("/css/<filename>")
def get_css(filename):
    return send_from_directory(os.path.join(STATIC_DIR, "css"), filename)

#ladda JavaScript
@app.route("/js/<filename>")
def get_js(filename):
    return send_from_directory(os.path.join(STATIC_DIR, "js"), filename)

#ladda templates
@app.route("/templates/<filename>")
def get_templates(filename):
    return send_from_directory(os.path.join(STATIC_DIR, "templates"), filename)

@app.route("/images/<filename>")
def get_images(filename):
    return send_from_directory(os.path.join(STATIC_DIR, "images"), filename)

#ladda media (bild, film, osv)
@app.route("/media/<file_path>")
def get_media(file_path):
    return send_from_directory(os.path.join(STATIC_DIR, "media"), file_path)

@app.route("/blandaren/<file_path>")
def get_blandaren(file_path):
    return send_from_directory(os.path.join(STATIC_DIR, "bländaren"), file_path)

@app.route("/api/blandaren", methods = ["GET", "POST"])
def blandar_route():
    if request.method == "POST":
        document_functions.upload_document(request)
        return jsonify({"message":"fil(er) laddades upp!"}), 200
    if request.method == "GET":
        document_response = document_functions.get_documents()
        print(document_response)
        return jsonify(document_response), 200

@app.route("/api/media", methods = ["GET", "POST"]) #Hämta media eller ladda upp media
def media_path():
    week_filter = request.args.get("week")
    event_filter = request.args.get("event")
    type_filter = request.args.get("type")
    uploader_filter = request.args.get("uploader")
    if week_filter is None and event_filter is None and type_filter is None and uploader_filter is None:
        if request.method == "GET":
            image_response = image_functions.get_media()
            return jsonify(image_response), 200
        if request.method == "POST":
            image_functions.upload_media(request)
            return jsonify({"Message":"Bild(er) laddades upp!"}), 200
    else:
        image_response = image_functions.get_media(week_filter = week_filter, event_filter = event_filter, media_type = type_filter, uploaded_by=uploader_filter)
        return jsonify(image_response), 200

@app.route("/api/weeks", methods = ["GET"])
def get_weeks():
    return jsonify(image_functions.get_weeks())

@app.route("/api/events", methods = ["GET"])
def get_events():
    return jsonify(image_functions.get_events())

@app.route("/api/news/", methods=["GET", "POST", "DELETE", "PUT"])
@requires_auth_token
def news_route():
    id = request.args.get("id")
    if request.method == "GET":
        if id == None:
            return news_functions.get_all_news()
        else:
            return news_functions.get_news_by_id(id), 201
    elif request.method == "POST":
        return news_functions.add_news(request.json), 200
    elif request.method == "DELETE":
        return news_functions.delete_news(id), 200
    elif request.method == "PUT":
        return news_functions.edit_news(id, request.json), 201

@app.route("/api/user/", methods=["GET", "POST", "DELETE", "PUT"])
@requires_auth_token
def user_route():
    if request.method == "GET":
        if len(request.args) > 0:
            return user_functions.get_user_by_filter(request.args)
        else:
            return user_functions.get_all_users()
    elif request.method == "POST":
        return user_functions.add_user(request.json)
    elif request.method == "DELETE":
        return user_functions.delete_user(request.args)
    elif request.method == "PUT":
        return user_functions.edit_user(request.args, request.json)

@app.route("/api/currentUser/", methods=["GET"])
@requires_auth_token
def current_user():
    return g.user.to_json()

@app.route('/api/token')
@requires_auth
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({ 'token': token.decode('ascii') })

@app.route('/api/checkToken', methods=["POST"])
def check_token():
    return jsonify({"valid": check_auth(request.json["token"], "", True)})

@app.route("/api/hemlig")
@requires_auth_token
def hemlig():
    return "Välkommen " + g.user.username + "!"
