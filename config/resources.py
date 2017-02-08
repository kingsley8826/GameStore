from flask.ext.restful import Api

from controller.HotelListRes import HotelListRes
from controller.HotelRes import HotelRes
from controller.LoginRes import LoginRes
from controller.RegisterRes import RegisterRes


def config_resources(app):
    api = Api(app)
    api.add_resource(HotelListRes, "/api/hotels")
    api.add_resource(HotelRes, "/api/hotels/<hotel_id>")

    api.add_resource(RegisterRes, "/api/register")
    api.add_resource(LoginRes, "/api/login")
