from flask import Flask
from flask_restful import Api, Resource, reqparse

import mlab
from mongoengine import *
from flask_restful import *
import hmac
from datetime import datetime
import json

mlab.connect()

class Hotel(Document):
    longitude = FloatField()
    latitude = FloatField()
    telephone_number = StringField()
    name = StringField()
    address = StringField()
    image_url = StringField()

class User(Document):
    username = StringField()
    password = StringField()
    token = StringField()
    image_url = StringField()

app = Flask(__name__)

api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("longitude", type=float, location="json")
parser.add_argument("latitude", type=float, location="json")
parser.add_argument("telephone_number", type=str, location="json")
parser.add_argument("name", type=str, location="json")
parser.add_argument("rating", type=float, location="json")
parser.add_argument("address", type=str, location="json")
parser.add_argument("image_url", type=str, location="json")

parser.add_argument("username", type=str, location="json")
parser.add_argument("password", type=str, location="json")


def gen_token():
    return hmac.new(str.encode(str(datetime.now()))).hexdigest()

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

class RegisterRes(Resource):
    def post(self):
        args = parser.parse_args()
        username = args["username"]
        password = args["password"]
        user = User.objects(username=username).first()
        if user is not None:
            return {"code": 0, "message": "Fail"}
        else:
            token = gen_token()
            user = User(username=username, password=password, token=token)
            user.save()
            return {"code": 1, "message": "OK", "token": token}
 #n = Store(longitude="20.20", latitude="15.15", telephone_number="0988123123", name = "thien duong")
 #n.save()

# for note in Note.objects:
 #   print(note.to_json())


@app.route('/')
def hello_world():
    return 'Luu ham'

class UserListRes(Resource):

    def get(self): # Get All User
        return mlab.list2json(User.objects)

    def post(self): # post new user
        args = parser.parse_args()
        username = args["username"]
        password = args["password"]
        image_url = args["image_url"]
        new_user = User(username=username, password=password, image_url=image_url)
        new_user.save()
        return mlab.item2json(new_user)

# class RatingListRes(Resource):
#     def get(self): # Get All Rating
#         return mlab.list2json(Rating.objects)
#
#     def post(self): # post new rating
#         args = parser.parse_args()
#         user_id = args["user_id"]
#         store_id = args["store_id"]
#         rating = args["rating"]
#         new_rating = Rating(user_id=user_id, store_id=store_id, rating=rating)
#         new_rating.save()
#         return mlab.item2json(new_rating)


class HotelListRes(Resource):
    def get(self): # Get All Hotel
        return mlab.list2json(Hotel.objects)

    def post(self): # post new hotel
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

class HotelRes(Resource):
    def get(self, hotel_id): # get a hotel
        all_hotels = Hotel.objects
        found_hotel = all_hotels.with_id(hotel_id)
        return mlab.item2json(found_hotel)

    def delete(self, hotel_id):
        all_hotels = Hotel.objects
        found_hotel = all_hotels.with_id(hotel_id)
        found_hotel.delete()
        return {"code" : 1, "status" : "Deleted"}, 200

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
        found_hotel.update(set__longitude = longitude, set__latitude = latitude,set__telephone_number = telephone_number,
                            set__name = name, set__rating = rating, set__address = address, set__image_url = image_url)
        return {"code": 1, "status": "Ok"}, 200


api.add_resource(HotelListRes, "/api/hotel")
api.add_resource(HotelRes, "/api/hotel/<hotel_id>")

api.add_resource(RegisterRes, "/api/register")
api.add_resource(LoginRes, "/api/login")

if __name__ == '__main__':
    app.run()
