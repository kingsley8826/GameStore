from flask import Flask

from config import mlab
from config import resources

mlab.connect()

app = Flask(__name__)
resources.config_resources(app)


@app.route('/')
def hello_world():
    return 'Luu ham'


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

if __name__ == '__main__':
    app.run()
