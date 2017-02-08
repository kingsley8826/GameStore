from flask.ext.restful import reqparse, Resource
from helper.UserHelper import gen_token
from models.User import User

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, location="json")
parser.add_argument("password", type=str, location="json")


class LoginRes(Resource):
    def post(self):
        args = parser.parse_args()
        username = args["username"]
        password = args["password"]
        user = User.objects(username=username).first()
        if user is None:
            return {"code": 0, "message": "Fail"}
        else:
            if user.password != password:
                return {"code": 0, "message": "Fail"}
            else:
                token = gen_token()
                user.update(set__token=token)
                return {"code": 1, "message": "OK", "token": token}
