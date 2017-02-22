from mongoengine import Document, StringField, IntField, ReferenceField, FloatField


class HotelRating(Document):
    user = ReferenceField("User")
    hotel = ReferenceField("Hotel")
    rate = IntField()

def dump_rating():
    print("Dummping rating...")
    from models.hotel import Hotel
    from models.user import User
    users = User.objects()
    for hotel in Hotel.objects():
        from config import mlab
        import random
        print("Dumping rating for ", mlab.item2json(hotel))
        r_rate = random.randint(3, 6)
        for i in range(r_rate):
            user = random.choice(users)
            rate = random.randint(1, 5)
            hotel_rate = HotelRating(user=user, hotel=hotel, rate=rate)
            hotel_rate.save()
            print("Rate", mlab.item2json(hotel_rate))

def print_all_rates():
    for hotel_rate in HotelRating.objects():
        from config import mlab
        print("Rate", mlab.item2json(hotel_rate))