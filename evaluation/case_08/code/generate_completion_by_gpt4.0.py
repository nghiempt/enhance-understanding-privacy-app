# Import necessary libraries
import json
import openai
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Define the file paths for input and output JSON files (provide actual paths)
input_json_file_path = ''
output_json_file_path = ''

# Set the OpenAI API key using the value from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

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

    # Generate a response using OpenAI ChatCompletion
    response = openai.ChatCompletion.create(
        model=os.getenv("MODEL_GPT4.0"),
        messages=[
            {"role": "system", "content": "You are an assistant who analyzes and evaluates the correct, complete, and consistency between the Data Safety information provided compared to the information provided by the Privacy Policy of applications on the Google Play Store."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract the assistant's reply from the response
    assistant_reply = response.choices[0].message['content']

    # Update the "completion" key of the current item with the assistant's reply
    item["completion"] = assistant_reply

    # Print a success message
    print("~~~ Successfully ~~~\n")

# Save the updated data (now with completions from the assistant) back into the output JSON file
# The data is saved with an indentation of 4 spaces for better readability
with open(output_json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)
