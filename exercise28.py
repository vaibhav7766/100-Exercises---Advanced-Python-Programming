import json

def filter_active_users():
    with open("users.json", "r") as file:
        x = json.load(file)

    active_users = [user for user in x if user["is_active"]]

    with open("active_users.json", "w") as file:
        json.dump(active_users, file, indent=2)
