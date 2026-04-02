import anthropic
import os
from dotenv import load_dotenv
# from google.colab import userdata

load_dotenv()
print(anthropic.__version__) 

class Agent:
  "simple ai agent answering question"
  def __init__(self):
    self.client = anthropic.Anthropic(api_key=os.getenv("my_api_key"))
    self.model = "claude-sonnet-4-20250514"
    self.system_message = "You are an assistant that can answer all my problems"

def chat(self, message):
  "Process a string message by the user and return a repsonse"
  response = self.client.message.create(
    model=self.model,
    max_token=1024,
    system=self.system_message,
    message=[
      {"role":"user", "content": message}],
    temperature=0.1,)
  return response

agent = Agent()
response = agent.chat("I have 400 wishes that I want to complete before I die what are oyure wishes?")
print(respose.content[0].text)
    
