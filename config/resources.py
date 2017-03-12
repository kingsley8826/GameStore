from flask_restful import Api

from controller.HotelListRes import HotelListRes
from controller.HotelRes import HotelRes
from controller.UserRes import UserRes
from controller.HotelRatingRes import HotelRatingRes
from flask_jwt import JWT, current_identity, jwt_required, JWTError

from controller.Login import *


def config_resources(app):
    api = Api(app)
    app.config['SECRET_KEY'] = 'Xk]ysC8ad1pO!&`AN|Ak1T;=L6ezZ12R'
    app.config["JWT_AUTH_URL_RULE"] = "/api/login"
    app.handle_user_exception = handle_user_exception_again
    jwt = JWT(
        app=app,
        authentication_handler=authenticate,
        identity_handler=identity)

    api.add_resource(HotelListRes, "/api/hotels")
    api.add_resource(HotelRes, "/api/hotel/<hotel_id>")
    # api.add_resource(HotelRes, "/api/hotel/<hotel_id>", "/api/hotel/<latitude>/<longitude>",
    #                  "/api/hotel/top/<rate>/<number>")

    # api.add_resource(RegisterRes, "/api/register")
    # api.add_resource(LoginRes, "/api/login")
    # api.add_resource(UserListRes, "/api/users")
    api.add_resource(UserRes, "/api/user/<action>", "/api/user/update/<token>")

    api.add_resource(HotelRatingRes, "/api/rating")



