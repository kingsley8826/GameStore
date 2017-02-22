from mongoengine import Document, FloatField, StringField, IntField, BooleanField, EmbeddedDocumentField, ListField
from models.hotelrating import HotelRating

class Service(Document):
    wifi = BooleanField()
    air_conditioner = BooleanField()
    water_heater = BooleanField()
    food_service = BooleanField()
    condom = BooleanField()

class HotelStatRate(Document):
    rate = IntField()
    count = IntField()

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
    service = EmbeddedDocumentField("Service")
    images = ListField(StringField())
    rates = ListField(EmbeddedDocumentField("HotelStatRate"))

    def calculate_rate(self):
        # self.rating = HotelRating.objects(hotel=self).average("rate")
        self.rates = []
        for rate in range(1, 6):
            count = HotelRating.objects(hotel=self, rate=rate).count()
            self.rates.append(HotelStatRate(rate=rate, count=count))