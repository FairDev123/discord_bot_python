import time
import json

with open("members.json", "r") as f:
    members = json.load(f)
    print(members)

while True:
    time.sleep(1)

    print("ok")