import math
import operator
from itertools import count

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


class HotelRes(Resource):
    # get hotel with id
    def get(self, hotel_id):  # get a hotel
        all_hotels = Hotel.objects
        found_hotel = all_hotels.with_id(hotel_id)
        return mlab.item2json(found_hotel)

    # get hotel around point with latitude and longitude
    def get(self, latitude, longitude):
        max_distance = 30
        all_hotels = Hotel.objects
        near_hotels = []
        flatitude = float(latitude)
        flongitude = float(longitude)
        for hotel in all_hotels:
            latitude_distance = math.fabs(hotel['latitude'] - flatitude)
            longitude_distance = math.fabs(hotel['longitude'] - flongitude)
            if latitude_distance <= max_distance and longitude_distance <= max_distance:
                near_hotels.append(hotel)
        return mlab.list2json(near_hotels)

    # get number of top hotel with rate
    def get(self, rate, number):
        all_hotels = Hotel.objects
        result_hotels = []
        frate = float(rate)
        inumber = int(number)
        for hotel in all_hotels:
            if hotel['rating'] >= frate:
                result_hotels.append(hotel)
        top_hotels = sorted(result_hotels, key=operator.itemgetter('rating'))[:inumber]
        return mlab.list2json(top_hotels)

    def delete(self, hotel_id):
        all_hotels = Hotel.objects
        found_hotel = all_hotels.with_id(hotel_id)
        found_hotel.delete()
        return {"code": 1, "status": "Deleted"}, 200

    def put(self, hotel_id):
        all_hotels = Hotel.objects
        found_hotel = all_hotels.with_id(hotel_id)
        args = parser.parse_args()
        longitude = args["longitude"]
        latitude = args["latitude"]
        telephone_number = args["telephone_number"]
        name = args["name"]
        rating = args["rating"]
        address = args["address"]
        image_url = args["image_url"]
        found_hotel.update(set__longitude=longitude, set__latitude=latitude, set__telephone_number=telephone_number,
                           set__name=name, set__rating=rating, set__address=address, set__image_url=image_url)
        return {"code": 1, "status": "Ok"}, 200
