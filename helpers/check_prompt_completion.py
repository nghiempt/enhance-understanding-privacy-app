import json

json_file_path = ''


with open(json_file_path, 'r') as file:
    data = json.load(file)

for index, item in enumerate(data):
    print("========================== " +
          str(index + 1) + " times ==========================")
    print(item['completion'])
    if (index > 100): 
        break
