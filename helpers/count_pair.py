import json

json_file_path = ''

with open(json_file_path, 'r') as file:
    data = json.load(file)

for index, item in enumerate(data):
    print(index + 1)