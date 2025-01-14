import  openai
from config import apikey

openai.api_key = apikey

response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Use a valid model, e.g., "gpt-3.5-turbo" or "gpt-4"
            messages=[
                {"role": "system", "content": "You are Jarvis AI, a helpful assistant."},
                {"role": "user", "content": "hey there how are you?"}
            ]
        )

print(response['choices'][0]['message']['content'])
