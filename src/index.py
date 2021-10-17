def get_users(arguments):
    return [{"id": "hogehoge", "name": "ししぃ"}]  # ダミー


def add_user(arguments):
    return dict(**arguments)  # ダミー


resolvers = {
    "getUsers": get_users,
    "addUser": add_user,
}


def handler(event, context):
    return resolvers[event["info"]["fieldName"]](event["arguments"])
