from flask import Flask
from flask_restful import Api, Resource, reqparse

import mlab
from mongoengine import *
from flask_restful import *
import json

mlab.connect()

app = Flask(__name__)

class Store(Document):
    longitude = StringField()
    latitude = StringField()
    telephone_number = StringField()
    name = StringField()

app = Flask(__name__)

api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("longitude", type=str, location="json")
parser.add_argument("latitude", type=str, location="json")
parser.add_argument("telephone_number", type=str, location="json")
parser.add_argument("name", type=str, location="json")


# n = Store(longitude="20.20", latitude="15.15", telephone_number="0988123123", name = "thien duong")
# n.save()

# for note in Note.objects:
 #   print(note.to_json())


@app.route('/')
def hello_world():
    return 'Hello World!'

class StoreListRes(Resource):
    def get(self): # Get All Notes
        return mlab.list2json(Store.objects)
    def post(self): # post new note
        args = parser.parse_args()
        longitude = args["longitude"]
        latitude = args["latitude"]
        telephone_number = args["telephone_number"]
        name = args["name"]
        new_store = Store(longitude=longitude, latitude=latitude, telephone_number=telephone_number, name=name)
        new_store.save()
        return mlab.item2json(new_store)

class StoreRes(Resource):
    def get(self, note_id):
        all_stores = Store.objects
        found_store = all_stores.with_id(note_id)
        return mlab.item2json(found_store)
    def delete(self, store_id):
        all_stores = Store.objects
        found_store = all_stores.with_id(store_id)
        found_store.delete()
        return {"code" : 1, "status" : "Deleted"}, 200
    def put(self, store_id):
        all_stores = Store.objects
        found_store = all_stores.with_id(store_id)
        args = parser.parse_args()
        longitude = args["longitude"]
        latitude = args["latitude"]
        telephone_number = args["telephone_number"]
        name = args["name"]
        found_store.update(set__longitude=longitude, set__latitude=latitude, set__telephone_number=telephone_number, set__name=name)
        return {"code": 1, "status": "Ok"}, 200

api.add_resource(StoreListRes, "/api/store")
api.add_resource(StoreRes, "/api/store/<store_id>")


if __name__ == '__main__':
    app.run()
