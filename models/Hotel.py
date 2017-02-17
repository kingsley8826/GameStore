from mongoengine import Document, FloatField, StringField, IntField, BooleanField, EmbeddedDocument

class Service(Document):
    wifi = BooleanField()
    air_conditioner = BooleanField()
    water_heater = BooleanField()
    food_service = BooleanField()
    condom = BooleanField()


class Hotel(Document):
    longitude = FloatField()
    latitude = FloatField()
    telephone_number = StringField()
    name = StringField()
    rating = FloatField()
    address = StringField()
    image_url = StringField()
    status = IntField()
    verification = IntField()
    service = EmbeddedDocument("Service")
