from sqlalchemy.sql.expression import false, null
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


db = SQLAlchemy()

association_table_track = db.Table(
    "association_table_track",
    db.Model.metadata,
    Column("user_id", Integer, db.ForeignKey("users.id")),
    Column("track_id", Integer, db.ForeignKey("tracks.id")),
)


class Users(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    apikey = Column(String)

    usertracks = db.relationship(
        "Tracks", secondary=association_table_track, back_populates="users"
    )

    def __init__(self, **kwargs):
        self.username = kwargs.get("name")
        self.apikey = kwargs.get("apikey")

    def serialize(self):
        return {"id": self.id, "name": self.username, "apikey": self.apikey}


class Tracks(db.Model):
    __tablename__ = "tracks"
    id = Column(Integer, primary_key=True)
    trackname = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    album = Column(String, nullable=False)
    counter = Column(Integer, nullable=False)
    users = db.relationship(
        "Users", secondary=association_table_track, back_populates="usertracks"
    )

    def __init__(self, **kwargs):
        self.trackname = kwargs.get("trackname")
        self.artist = kwargs.get("artist")
        self.counter = 1
        self.album = kwargs.get("album")

    def serialize(self):
        return {
            "id": self.id,
            "trackname": self.trackname,
            "artist": self.artist,
            "counter": self.counter,
            "album": self.album,
        }
