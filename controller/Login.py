from flask_jwt import JWT, current_identity, jwt_required, JWTError
from flask_restful import Resource, reqparse
from flask import jsonify
from collections import OrderedDict

from models.user import User

class LoginCredentials:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


def authenticate(username, password):
    user = User.objects(username=username, password=password).first()
    if user is not None:
        return LoginCredentials(id=str(user.id), username=username, password=password)


def identity(payload):
    user_id = payload['identity']
    user = User.objects.with_id(user_id)
    if user is not None:
        return LoginCredentials(id=str(user.id), username=user.username, password=user.password)


def handle_user_exception_again(e):
    if isinstance(e, JWTError):
        return jsonify(OrderedDict([
            ('status_code', e.status_code),
            ('error', e.error),
            ('description', e.description),
        ])), e.status_code, e.headers
    return e