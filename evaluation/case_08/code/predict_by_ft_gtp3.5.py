# Import necessary libraries
import json
from dotenv import load_dotenv
import os
import requests

# Load environment variables from a .env file
load_dotenv()

# Define the file paths for input and output JSON files (provide actual paths)
input_json_file_path = ''
output_json_file_path = ''

# Define the API endpoint URL
url = "https://api.openai.com/v1/chat/completions"

# Define the request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + os.getenv("OPENAI_API_KEY")
}

# Open and read the input JSON file
with open(input_json_file_path, 'r') as file:
    data = json.load(file)

# Loop through each item in the loaded JSON data
for index, item in enumerate(data):
    # Get the "prompt" from the current item
    prompt = item.get("prompt")

    # Print an identification header for the current item
    print("======================== " + str(index + 1) + " times ___ " + str(item['package_name']) +
          " ========================")

    # Define the request data
    dataPrompt = {
        "model": os.getenv("GPT3.5FT_BY_4.0"),
        "messages": [
            {
                "role": "system",
                "content": "You are an assistant who analyzes and evaluates the correct, complete, and consistency between the Data Safety information provided compared to the information provided by the Privacy Policy of applications on the Google Play Store."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    # Send the POST request to the OpenAI API
    response = requests.post(url, json=dataPrompt, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        # Request was successful
        result = response.json()
        item["completion"] = assistant_reply = result.get(
            "choices")[0].get("message").get("content")
    else:
        # Request encountered an error
        print("Error:", response.status_code)
        print(response.text)

    # Print a success message
    print("~~~ Successfully ~~~\n")

# Save the updated data (now with completions from the assistant) back into the output JSON file
# The data is saved with an indentation of 4 spaces for better readability
with open(output_json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)
