from openai import OpenAI

client = OpenAI(api_key="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")

# Set your API key

response = client.chat.completions.create(model="gpt-4",
messages=[{"role": "user", "content": "What's the weather like today?"}],
temperature=0.5,
max_tokens=50)

print(response.choices[0].message.content)
