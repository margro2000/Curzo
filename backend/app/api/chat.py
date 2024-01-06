import os
import openai

openai.api_key = "479085ca0bf64f51ae880580bf765581"
openai.api_base = "https://llmsforall2openai.openai.azure.com/"
openai.api_type = 'azure'
openai.api_version = '2023-09-01-preview' # this might change in the future

deployment_name = 'Curzo' # This will correspond to the custom name you chose for your deployment when you deployed a model.

# Send a completion call to generate an answer
print('Sending a test completion job')
prompt = "You are an AI assistant that generates course content for users looking to learn about a new subject with a set of modules given by the user. Add resources for each output. Have output in JSON format for each response."

result = openai.Completion.create(
    prompt=prompt,
    temperature=0.7,
    max_tokens=100,
    engine=deployment_name
)

print(result.choices[0].text.strip())