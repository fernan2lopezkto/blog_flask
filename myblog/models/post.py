from myblog import db
from datetime import datetime


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.column(db.Integer, primary_key=True)
    author = db.column(db.Integer, db.foreigKey('user.id'), nullable=False)
    title = db.column(db.String(100))
    body = db.column(db.Text)
    created = db.column(db.DataTime, nullable=False, default=datetime.utcnow)

    def __init__(self, author, title, body) -> None:
        self.author = author
        self.title = title
        self.body = body

    def __repr__(self) -> str:
        return f'Post {self.title}'
