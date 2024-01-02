from flask_app import flask_app
from authentication import jwt

def register_bp(flask_app):
    from hello import hello_bp
    from books import book_bp
    from movies import movies_bp
    from users import user_bp
    flask_app.register_blueprint(hello_bp)
    flask_app.register_blueprint(book_bp)
    flask_app.register_blueprint(movies_bp)
    flask_app.register_blueprint(user_bp)
register_bp(flask_app=flask_app)
if __name__ == '__main__':
     flask_app.run(host='0.0.0.0', port=5000,debug=True) 