import os
import openai

prompt_return = input("Enter Prompt: \n\n$")

openai.api_key = "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"

print(os.getenv('API_KEY'))

response = openai.Completion.create(
    model="code-davinci-002",
    prompt=prompt_return,
    temperature=0,
    max_tokens=2505,
    top_p=1,
    frequency_penalty=2,
    presence_penalty=0
)
print(response)