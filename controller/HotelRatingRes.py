from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from models.hotelrating import HotelRating
from models.hotel import Hotel
from models.user import User
from config import mlab

class HotelRatingRes(Resource):

    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name="hotel_id", type=str, location="json")
        parser.add_argument(name="rate", type=int, location="json")
        args = parser.parse_args()

        hotel_id = args["hotel_id"]
        rate = args["rate"]

        user = User.objects().with_id(current_identity.id)
        hotel = Hotel.objects().with_id(hotel_id)

        hotel_rating = HotelRating(user=user, hotel=hotel, rate=rate)
        hotel_rating.save()

        return mlab.item2json(HotelRating.objects().with_id(hotel_rating.id))

