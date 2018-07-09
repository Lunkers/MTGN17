from sqlalchemy import Column, Integer, String
from app import app, db

class Video(db.Model):
    id = Column(Integer, primary_key = True)
    video_link = Column(String(256))
    uploaded_by = Column(String(64))
    event = Column(String(256))
    week = Column(Integer)
    thumbnail = Column(String(256))

    def as_dictionary(self):
        vid_dict = {
            "id": self.id,
            "video_link": self.video_link,
            "event": self.event,
            "week":self.week,
            "thumbnail":self.thumbnail
        }

        return vid_dict