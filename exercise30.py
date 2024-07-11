from collections import namedtuple
import json

class User:
    def __init__(self, id, first_name, last_name, email, gender, is_active):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.is_active = is_active

    def __repr__(self):
        return f"User({self.id}, {self.first_name}, {self.last_name}, {self.email}, {self.gender}, {self.is_active})"


def json_to_object():
    with open("users.json", "r") as f:
        data = json.load(f)
        if data:
            User = namedtuple("User", data[0].keys())
            users = [User(**user) for user in data]
    return users
