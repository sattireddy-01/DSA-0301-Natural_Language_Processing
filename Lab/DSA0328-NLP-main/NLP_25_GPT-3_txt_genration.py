import openai
import os

# Set your OpenAI API key (alternatively, set the environment variable 'OPENAI_API_KEY')
openai.api_key = os.getenv("OPENAI_API_KEY") or "YOUR_API_KEY_HERE"

# Define a prompt
prompt = "Once upon a time in a land far, far away"

# Generate text using GPT-3 (using the 'text-davinci-003' engine)
response = openai.Completion.create(
    engine="text-davinci-003",  # You can try other engines like "davinci"
    prompt=prompt,
    max_tokens=150,
    temperature=0.7,
    n=1,
    stop=None
)

# Extract and display generated text
generated_text = response.choices[0].text.strip()
print("Generated Text:")
print(generated_text)
