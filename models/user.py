from mongoengine import StringField, Document


class User(Document):
    full_name = StringField()
    username = StringField()
    password = StringField()
    token = StringField()
    image_url = StringField()
