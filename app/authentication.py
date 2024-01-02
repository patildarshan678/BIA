from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_app import flask_app

jwt = JWTManager(flask_app)

@jwt.invalid_token_loader
def invalid_token_loader(callbackfn):
    return jsonify({"msg":"accesstoken is expired or invalid"})