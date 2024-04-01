# Importing the required `json` module to handle JSON data.
import json

# Defining the file path of the JSON file we want to read.
json_file_path = ''

# Opening the JSON file in read mode.
with open(json_file_path, 'r') as file:
    # Loading the contents of the JSON file into the `data` variable.
    data = json.load(file)

# Iterating over each item in the `data` list using its index and value.
for index, item in enumerate(data):
    # Setting the "completion" key of each item to an empty string.
    item["completion"] = ""

# Opening a new or existing file named 'dataset_predict.json' in write mode.
with open(json_file_path, 'w') as json_file:
    # Writing the modified `data` to the file in a formatted manner using an indent of 4 spaces.
    json.dump(data, json_file, indent=4)
