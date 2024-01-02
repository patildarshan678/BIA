from flask import Blueprint,Response, request, make_response,send_file
from flask_app import flask_app
from models.models import Movie
from database import db
from flask_jwt_extended import jwt_required
from Movies.movie import Movie
movies_bp  =Blueprint(
    'movies', __name__, url_prefix='/api/movies')

@movies_bp.route('/get_all',methods=['GET'])
@jwt_required()
def get_all():
    try:
        db_movies = Movie.query.all()
        movie_list = []
        for movie in db_movies:
            movie_list.append(movie.serialize())
        return movie_list
    except BaseException as err:
        msg = f"Exception occured in get_all API.{err}"
        print(msg)
        return msg, 500
    
@movies_bp.route('/add_movie',methods=['POST'])
@jwt_required()
def add_movie():
    try:
        req_body = request.get_json()
        if req_body:
            name = req_body.get('name')
            actor = req_body.get('actor')
            director = req_body.get('director')
            movie = Movie(actor=actor,director=director,name=name)
            db.session.add(movie)
            db.session.commit()
            return movie.serialize()
        else:
            return "BAD REQUESET", 400
    except BaseException as err:
        msg = f"Exception occured in get_all API.{err}"
        print(msg)
        return msg, 500
    
@movies_bp.route('/create_movie',methods=['POST'])
@jwt_required()
def create_movie():
    try:
        files = request.files
        if files:
            video = files['file']
            moviesObj = Movie()
            outputfile = moviesObj.add_effects(file=video)
            return send_file(outputfile, as_attachment=True)

        else:
            return "BAD REQUESET", 400
    except BaseException as err:
        msg = f"Exception occured in get_all API.{err}"
        print(msg)
        return msg, 500
