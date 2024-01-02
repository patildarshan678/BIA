from flask import Blueprint,Response, request, make_response
from flask_app import flask_app
hello_bp  = Blueprint(
    'hello', __name__, url_prefix='/api/hello')

@hello_bp.route('/message')
def message():
    try:
        return "Hello Flask"
    except BaseException as err:
        msg = f"Exception occured in message API.{err}"
        print(msg)
        return msg
