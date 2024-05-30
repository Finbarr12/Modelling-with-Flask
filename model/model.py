from _init_ import db

class Movies (db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255),nullable=False)
    dateRealeased = db.Column(db.Date,nullable=False)
    director = db.Column(db.String(255),nullable=False)

    def __repr__(self):
        return f"<Movie {self.title}>"