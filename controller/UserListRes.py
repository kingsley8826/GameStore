from flask.ext.restful import Resource
from flask.ext.restful import reqparse

from config import mlab
from models.user import User

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, location="json")
parser.add_argument("password", type=str, location="json")


class UserListRes(Resource):
    def get(self):  # Get All User
        return mlab.list2json(User.objects)

    # def post(self):  # post new user
    #     args = parser.parse_args()
    #     username = args["username"]
    #     password = args["password"]
    #     image_url = args["image_url"]
    #     new_user = User(username=username, password=password, image_url=image_url)
    #     new_user.save()
    #     return mlab.item2json(new_user)
