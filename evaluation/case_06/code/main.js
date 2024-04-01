const axios = require("axios");
const fs = require("fs");

const apiUrl = "https://www.llama2.ai/api";

const input_json = "";
const output_json = "";

// Read prompts from input.json
const prompts = JSON.parse(fs.readFileSync(input_json));

// Define an array to store the results
const results = [];

// Define a function to make the API request and save the result
async function processPrompt(prompt, index) {
  // Log the index
  console.log(
    `===================== start ${index + 1} time =====================`
  );

  let requestData = {
    prompt: `[INST] ${prompt.prompt} [/INST]`,
    version: "2796ee9483c3fd7aa2e171d38f4ca12251a30609463dcfd4cd76703f22e96cdf",
    systemPrompt:
      "You are an assistant who analyzes and evaluates the correct, complete, and consistency between the Data Safety information provided compared to the information provided by the Privacy Policy of applications on the Google Play Store.",
    temperature: 0.75,
    topP: 0.9,
    maxTokens: 800,
    image: null,
  };

  try {
    const response = await axios.post(apiUrl, requestData, {
      headers: {
        "Content-Type": "application/json",
      },
    });

    // Create an object with the desired structure
    const resultObj = {
      prompt: prompt.prompt,
      completion: response.data, // Modify this to match your response structure
      package_name: prompt.package_name, // Modify this to match your response structure
    };

    console.log(response.data);

    // Add the result object to the results array
    results.push(resultObj);

    // Check if all prompts have been processed
    if (results.length === prompts.length) {
      // Save the results to output.json
      fs.writeFileSync(output_json, JSON.stringify(results, null, 2));
      console.log("Results saved to output.json");
    }
  } catch (error) {
    console.error("Error:", error);
  }
}

// Loop through each prompt and process them sequentially
async function processPrompts() {
  for (let i = 0; i < prompts.length; i++) {
    await processPrompt(prompts[i], i);
  }
}

// Call the function to start processing prompts
processPrompts();
