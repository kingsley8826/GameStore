from flask.ext.restful import Resource
from flask.ext.restful import reqparse

from config import mlab
from models.hotel import Hotel

parser = reqparse.RequestParser()
parser.add_argument("longitude", type=float, location="json")
parser.add_argument("latitude", type=float, location="json")
parser.add_argument("telephone_number", type=str, location="json")
parser.add_argument("name", type=str, location="json")
parser.add_argument("rating", type=float, location="json")
parser.add_argument("address", type=str, location="json")
parser.add_argument("image_url", type=str, location="json")


class HotelListRes(Resource):
    def get(self):  # Get All Hotel
        all_hotels = Hotel.objects
        for hotel in all_hotels:
            hotel.calculate_rate()
        return mlab.list2json(all_hotels)

    def post(self):  # post new hotel
        args = parser.parse_args()
        longitude = args["longitude"]
        latitude = args["latitude"]
        telephone_number = args["telephone_number"]
        name = args["name"]
        rating = args["rating"]
        address = args["address"]
        image_url = args["image_url"]
        new_hotel = Hotel(longitude=longitude, latitude=latitude, telephone_number=telephone_number,
                          name=name, rating=rating, address=address, image_url=image_url)
        new_hotel.save()
        return mlab.item2json(new_hotel)
