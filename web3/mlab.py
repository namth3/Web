import mongoengine #database driver, thư viện ở lớp giữa kết nối DB và python

#mongodb+srv://namth3:<password>@cluster0-kondi.mongodb.net/test?retryWrites=true

host = "cluster0-kondi.mongodb.net"
port = 27017
db_name = "cluster0"
user_name = "namth3"
password = "thanhninh"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())