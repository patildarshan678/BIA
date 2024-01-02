from flask import Blueprint,Response, request, make_response
from flask_app import flask_app
from models.models import User
from flask_jwt_extended import create_access_token
from database import db

from werkzeug.security import generate_password_hash, check_password_hash
user_bp = Blueprint(
    'user', __name__, url_prefix='/api/user')

@user_bp.route('add_user',methods=['POST'])
def add_user():
    try:
        req_body = request.get_json()
        if req_body:
            name = req_body.get('name')
            username = req_body.get('username')
            password = req_body.get('password')
            hashed_password = generate_password_hash(password=password, method='sha256')
            user = User(name=name,Uname=username,Upass=hashed_password)
            db.session.add(user)
            db.session.commit()
            return user.serialize()
        else:
            return "BAD REQUEST" ,400
    except BaseException as err:
        msg = f"Exception occured in add_user.{err}"
        print(msg)
        return msg,500
@user_bp.route('/login',methods=['POST'])
def login():
    try:
        req_body = request.get_json()
        if req_body:
            username = req_body.get('username')
            password = req_body.get('password')
            db_user = User.query.filter_by(Uname=username).first()
            is_user_valid = check_password_hash( pwhash=db_user.Upass,password=password)
            if is_user_valid:
                access_token = create_access_token(identity=username)
                return access_token
            else:
                return "Invalid credentials"
        else:
            return "BAD REQUEST" ,400
    except BaseException as err:
        msg = f"Exception occured in add_user.{err}"
        print(msg)
        return msg,500