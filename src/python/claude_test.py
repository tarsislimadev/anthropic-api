import anthropic
import os

try:
  client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

  message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000, 
    temperature=0.0,
    system="Respond only in Yoda-speak.",
    messages=[
      {"role": "user", "content": "How are you today?"}
    ]
  )

  print(message.content)
except Exception as error:
  print(error)
