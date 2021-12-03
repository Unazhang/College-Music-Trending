from flask.globals import request
from db import db, Users, Tracks
from flask import Flask
import json


app = Flask(__name__)
db_filename = "music.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()


def success_response(body, status_code=200):
    return json.dumps(body), status_code


def failure_response(message, status_code=400):
    return json.dumps({"error": message}), status_code


def nonexist_response():
    return json.dumps({"error": "Not Found"}), 404


@app.route("/api/users/<int:user_id>/")
def get_user_data(user_id):
    user = Users.query.filter_by(id=user_id).first()

    if user is None:
        return nonexist_response()

    return success_response(user.serialize())


@app.route("/api/users/", methods=["POST"])
def create_user():
    body = json.loads(request.data)

    if body.get("name") is None:
        return failure_response("Name not provided.", 400)

    user = Users(name=body.get("name"), apikey=body.get("apikey"))

    db.session.add(user)
    db.session.commit()

    return success_response(user.serialize())


@app.route("/api/tracks/")
def get_tracks():
    return success_response({"Tracks": [t.serialize() for t in Tracks.query.all()]})


# @app.route("/api/tracks/<int:track_id>/")
# def get_spec_track(track_id):
#     track = Tracks.query.filter_by(id=track_id).first()
#     if track is None:
#         return failure_resp("Track not found")
#     return success_response(tracks.serialize())


@app.route("/api/top_tracks/add/", methods=["POST"])
def add_track():
    # track = Tracks.query.filter_by(id=track_id).first()
    # if track is None:
    #     return failure_response("Track not found")

    body = json.loads(request.data)
    trackname = body.get("trackname")
    artist = body.get("artist")

    if trackname is None:
        return failure_response("Trackname Needed", 400)

    if artist is None:
        return failure_response("Artist Needed", 400)

    track = Tracks.query.filter_by(trackname=trackname).first()

    if track is None:
        new_track = Tracks(
            trackname=trackname,
            artist=artist,
        )
        db.session.add(new_track)
        db.session.commit()
        return success_response(new_track.serialize(), 201)
    else:
        track.counter += 1
        db.session.add(track)
        db.session.commit()
        return success_response(track.serialize(), 201)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
