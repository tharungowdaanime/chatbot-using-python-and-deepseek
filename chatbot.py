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
      "Authorization": "Bearer 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",
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
