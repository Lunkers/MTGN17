import os
from sqlalchemy import desc, asc
from app.models.image import Image
from app.models.video import Video
from app import db
from app.config import basedir
from PIL import Image as Img

UPLOAD_FOLDER = os.path.join(os.getcwd(),"static","Schmeck","media")

def upload_media(request):
    latest_files = request.files.getlist("files")
    name = request.form.get("uploadedby")
    event = request.form.get("event")
    week = request.form.get("week")
    if latest_files is not None:
        for uploaded_file in latest_files:
            file_name = uploaded_file.filename
            uploaded_file.save(os.path.join(UPLOAD_FOLDER,file_name))
            thumb = generate_thumbnail(file_name)
            new_img = Image(filename = uploaded_file.filename,uploaded_by = name,event = event,week = week, thumbnail = thumb)
            db.session.add(new_img)

    latest_videos = request.form.getlist("videos")
    if latest_videos is not None:
        for video in latest_videos:
            embed_link, thumbnail = handle_video(video)
            new_vid = Video(video_link = embed_link, uploaded_by = name,
            event = event,
            week = week,
            thumbnail = thumbnail)
            db.session.add(new_vid)


    db.session.commit()
    return True

def get_media(week_filter = None, event_filter = None, media_type = None, uploaded_by = None):
    output = []
    if media_type is None or media_type == "image":
        image_query = Image.query.filter()
        
        if week_filter is not None:
            image_query = image_query.filter(Image.week == week_filter)
        if event_filter is not None:
            image_query = image_query.filter(Image.event == event_filter)
        if uploaded_by is not None:
            image_query = image_query.filter(Image.uploaded_by == uploaded_by)
        image_query = image_query.all()
        for result in image_query:
            res_dict = result.as_dictionary()
            res_dict["type"] = "image"
            output.append(res_dict)

    if media_type is None or media_type == "video":
        video_query = Video.query.filter()

        if week_filter is not None:
            video_query = video_query.filter(Video.week == week_filter)
        if event_filter is not None:
            video_query = video_query.filter(Video.event == event_filter)
        if uploaded_by is not None:
            video_query = video_query.filter(Video.uploaded_by == uploaded_by)
        video_query = video_query.all()
        for video_result in video_query:
            res_dict = video_result.as_dictionary()
            res_dict["type"] = "video"
            output.append(res_dict)

    return output

def generate_thumbnail(filename):
    im = Img.open(os.path.join(UPLOAD_FOLDER, filename))
    size = (200, 200) # thumbnail-storleken
    filename = filename.split(".")[0]
    outfile = os.path.splitext(im.filename)[0]
    try:
        im = im.resize(size)
        im.save(outfile + "_thumb.jpg", "JPEG")
    except IOError:
        print("en liten fucky wucky")

    return filename + "_thumb.jpg"

def get_weeks():
    output = []
    for value in db.session.query(Image.week).distinct().order_by(Image.week.asc()):
        output.append(value[0])
    return output

def get_events():
    output = []
    for value in db.session.query(Image.event).distinct().order_by(Image.week.asc()):
        output.append(value[0])
    return output

def handle_video(video_link):
    video_id = video_link.split("v=")[1]
    print(video_id)
    embed_link = "youtube.com/embed/" + video_id
    thumbnail = "http://img.youtube.com/vi/" + video_id + "/maxresdefault.jpg"

    return embed_link, thumbnail