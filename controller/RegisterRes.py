from flask.ext.restful import Resource
from flask.ext.restful import reqparse

from helper.UserHelper import gen_token
from models.User import User

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, location="json")
parser.add_argument("password", type=str, location="json")


class RegisterRes(Resource):
    def post(self):
        args = parser.parse_args()
        username = args["username"]
        password = args["password"]
        user = User.objects(username=username).first()
        if user is not None:
            return {"code": 0, "message": "Fail"}
        else:
            token = gen_token()
            user = User(username=username, password=password, token=token)
            user.save()
            return {"code": 1, "message": "OK", "token": token}
            # n = Store(longitude="20.20", latitude="15.15", telephone_number="0988123123", name = "thien duong")
            # n.save()

            # for note in Note.objects:
            #   print(note.to_json())
