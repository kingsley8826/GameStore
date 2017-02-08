import hmac
from datetime import datetime


def gen_token():
    return hmac.new(str.encode(str(datetime.now()))).hexdigest()
