from mongoengine import Document, FloatField, StringField, IntField


class Hotel(Document):
    longitude = FloatField()
    latitude = FloatField()
    telephone_number = StringField()
    name = StringField()
    rating = FloatField()
    address = StringField()
    image_url = StringField()
    status = IntField()
