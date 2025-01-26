import json


with open("configuration.json", 'r') as f:
    contents = json.loads(f.read())
    print(contents['request'])
