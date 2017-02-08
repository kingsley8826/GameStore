from mongoengine import StringField, Document


class User(Document):
    username = StringField()
    password = StringField()
    token = StringField()
    image_url = StringField()
