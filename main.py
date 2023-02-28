import openai

# Set your API key
openai.api_key = "your key"
# Use the GPT-3 model
message = input("Your question： ")
completion = openai.Completion.create(
    engine="text-davinci-002",
    prompt=message,
    max_tokens=1024,
    temperature=0.5
)
# Print the generated text
print("Answer: "+completion.choices[0].text)
