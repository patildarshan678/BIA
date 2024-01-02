from flask import Blueprint,Response, request, make_response
from flask_app import flask_app
from models.models import Books
from database import db
from flask_jwt_extended import jwt_required
book_bp  = Blueprint(
    'books', __name__, url_prefix='/api/books')

@book_bp.route('/get_all',methods=['GET'])
@jwt_required()
def get_all():
    try:
        db_books = Books.query.all()
        book_list = []
        for book in db_books:
            book_list.append(book.serialize())
        return book_list
    except BaseException as err:
        msg = f"Exception occured in get_all API.{err}"
        print(msg)
        return msg
@book_bp.route('/add_book',methods=["POST"])
@jwt_required()
def add_book():
    try:
        req_body = request.get_json()
        if req_body:
            name = req_body.get('name')
            author = req_body.get('author')
            publisher = req_body.get('publisher')
            book = Books(author=author,name=name,publisher=publisher)
            db.session.add(book)
            db.session.commit()
            return book.serialize()
        else:
            return "BAD REQUESET", 400
    except BaseException as err:
        msg = f"Exception occured in add_book.{err}"
        print(msg)
        return msg,500