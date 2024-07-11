import json

def json_to_csv():
    with open("users.json", "r") as f:
        x = json.load(f)
    s = ",".join(x[0].keys())
    s += "\n"
    for i in x:
        for j in i:
            s += str(i[j]) + ","
        s = s[:-1]
        s += "\n"
    with open("users.csv", "w") as f:
        f.write(s)
