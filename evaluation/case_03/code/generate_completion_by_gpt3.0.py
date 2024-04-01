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
    # Print an identification header for the current item
    print("======================== " + str(index + 1) + " times ___ " + str(item['package_name']) +
          " ========================")

    # Get the "prompt" from the current item
    prompt = item.get("prompt")

    # Generate text using the OpenAI GPT-3.0 model
    completion = openai.Completion.create(
        model=os.getenv("MODEL_GPT3.0"),
        prompt=prompt,
        n=1,
        stop=None,
        temperature=1.0,
        max_tokens=150
    )

    # Extract the generated text from the API response
    generated_text = completion.choices[0].text

    # Update the "completion" key of the current item with the generated text
    item["completion"] = generated_text

    # Print a success message
    print("~~~ Successfully ~~~\n")

# Save the updated data (now with completions) back into the output JSON file
# The data is saved with an indentation of 4 spaces for better readability
with open(output_json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)
