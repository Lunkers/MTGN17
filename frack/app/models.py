from app import db

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Text)
    headline = db.Column(db.Text)
    text = db.Column(db.Text)
    tags = db.Column(db.String(64))

    def __repr__(self):
        return '<Nyhet skriven av {}>'.format(self.author)

    def as_dictionary(self):
        news_dict = {
            "id" : self.id,
            "author" : self.author,
            "text" : self.text,
            "tags": self.tags,
            "headline" :self.headline
        }

        return news_dict