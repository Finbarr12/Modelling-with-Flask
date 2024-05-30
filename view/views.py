from flask import Blueprint,request
from model.model import Movies
from _init_ import db

movies_blueprint= Blueprint("movies_blueprint",__name__)


@movies_blueprint.route("/")
@movies_blueprint.route("/home")
def welcome():
    return "Welcome to our Movies Application"

@movies_blueprint.route("/createmovies",methods=['POST'])
def createMovies():
    title = request.form.get('title')
    releasedDate = request.form.get('releasedDate')
    filmMaker = request.form.get('filmMaker')

    movies = Movies(title=title,releasedDate=releasedDate,director=filmMaker)
    db.session.add(movies)
    db.session.commit()

    return "Added"f"{title} movie successfully"
    