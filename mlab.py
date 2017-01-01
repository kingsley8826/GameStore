
import mongoengine


# mongodb://<dbuser>:<dbpassword>@ds151048.mlab.com:51048/game-store
host = "ds151048.mlab.com"
port = 51048
db_name = "game-store"
user_name = "kingsley8826"
password = "anhtuan8826"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]

def item2json(item):
    import json
    return json.loads(item.to_json())