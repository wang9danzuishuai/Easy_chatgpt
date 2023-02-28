import openai

# Set your API key
openai.api_key = "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"
# Use the GPT-3 model
message = input("请输入您的问题： ")
completion = openai.Completion.create(
    engine="text-davinci-002",
    prompt=message,
    max_tokens=1024,
    temperature=0.5
)
# Print the generated text
print(completion.choices[0].text)