from flask.ext.restful import Resource
from flask.ext.restful import reqparse

from config import mlab
from models.hotel import Hotel

parser = reqparse.RequestParser()
parser.add_argument("longitude", type=float, location="json")
parser.add_argument("latitude", type=float, location="json")
parser.add_argument("telephone_number", type=str, location="json")
parser.add_argument("name", type=str, location="json")
parser.add_argument("address", type=str, location="json")
parser.add_argument("image_url", type=str, location="json")
parser.add_argument("rating", type=float, location="json")
parser.add_argument("images", type=list, location="json")


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
        address = args["address"]
        images = args["images"]

        new_hotel = Hotel(longitude=longitude, latitude=latitude, telephone_number=telephone_number,
                          images=images,name=name, address=address)
        new_hotel.save()
        return mlab.item2json(new_hotel)
