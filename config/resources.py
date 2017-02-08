from flask.ext.restful import Api

from controller.HotelListRes import HotelListRes
from controller.HotelRes import HotelRes
from controller.UserRes import UserRes


def config_resources(app):
    api = Api(app)
    api.add_resource(HotelListRes, "/api/hotels")
    api.add_resource(HotelRes, "/api/hotel/<hotel_id>", "/api/hotel/<latitude>/<longitude>",
                     "/api/hotel/top/<rate>/<number>")

    # api.add_resource(RegisterRes, "/api/register")
    # api.add_resource(LoginRes, "/api/login")
    # api.add_resource(UserListRes, "/api/users")
    api.add_resource(UserRes, "/api/user/<action>", "/api/user/update/<token>")
