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
    usertracks = db.relationship(
        "Tracks", secondary=association_table_track, back_populates="users"
    )

    def __init__(self, **kwargs):
        self.username = kwargs.get("name")

    def serialize(self):
        return {"id": self.id, "name": self.username}


class Tracks(db.Model):
    __tablename__ = "tracks"
    id = Column(Integer, primary_key=True)
    trackname = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    users = db.relationship(
        "Users", secondary=association_table_track, back_populates="usertracks"
    )

    def __init__(self, **kwargs):
        self.trackname = kwargs.get("trackname")
        self.artist = kwargs.get("artist")

    def serialize(self):
        return {"id": self.id, "trackname": self.trackname, "artist": self.artist}
