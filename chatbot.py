import requests
import json
class TantrumBot:
  def __init__(self,question):
    self.question = question
    self.res = None

  
  def response_ai(self):
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
      "Authorization": "Bearer your-api-key-here",
      "Content-Type": "application/json"
  },
    data=json.dumps({
      "model": "deepseek/deepseek-r1:free",
      "messages": [
        {
          "role": "user",
          "content": self.question
        }
      ],
    
    })
  )
    self.res = response.json()
    return self.res['choices'][0]['message']['content']
