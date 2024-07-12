from collections import namedtuple
import json
import pickle


with open("users.json", "r") as file:
    content = json.load(file)

headers = tuple(content[0].keys())
User = namedtuple("User", headers)
values = [tuple(user.values()) for user in content]
users = [User(*user) for user in values]


with open("users.pickle", "wb") as file:
    pickle.dump(users, file)

with open("users.pickle", "rb") as file:
    content = pickle.load(file)

result = tuple(filter(lambda obj: obj.id == 4, content))[0]
print(result)
