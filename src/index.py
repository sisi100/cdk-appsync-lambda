def getUsers(arguments):
    return [{"id": "hogehoge", "name": "ししぃ"}]  # ダミー


def addUser(arguments):
    return dict(**arguments)  # ダミー


def handler(event, context):
    return globals()[event["info"]["fieldName"]](event["arguments"])
