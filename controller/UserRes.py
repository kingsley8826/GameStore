from flask_restful import reqparse, Resource

from helper.UserHelper import gen_token
from models.user import User

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, location="json")
parser.add_argument("password", type=str, location="json")
parser.add_argument("token", type=str, location="json")
parser.add_argument("image_url", type=str, location="json")


class UserRes(Resource):
    def post(self, action):
        args = parser.parse_args()
        username = args["username"]
        password = args["password"]
        user = User.objects(username=username).first()
        if action == "login":
            if user is None:
                return {"code": 0, "message": "Fail"}
            else:
                if user.password != password:
                    return {"code": 0, "message": "Fail"}
                else:
                    token = gen_token()
                    user.update(set__token=token)
                    return {"code": 1, "message": "OK", "token": token}
        elif action == "register":
            if user is not None:
                return {"code": 0, "message": "Fail"}
            else:
                token = gen_token()
                user = User(username=username, password=password, token=token)
                user.save()
                return {"code": 1, "message": "OK", "token": token}


    # update password and image_url
    def put(self, token):
        args = parser.parse_args()
        token = args["token"]
        user = User.objects(token=token).first()
        if user is not None:
            password = args["password"]
            image_url = args["image_url"]
            user.update(set__password=password, set__image_url=image_url)
            return {"code": 1, "status": "Ok"}, 200
