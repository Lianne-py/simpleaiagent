from google import genai

client = genai.Client(api_key="AIzaSyBvTOheE0jfvfQYFst1MOcZ6Z7a-0qRWGE")
chat = client.chats.create(model="gemini-flash-latest")

response = chat.send_message("Hello World!")
print(response.text)

response = chat.send_message("Explain how an apple decays and is able to conserve its chemical energy by being enclosed in a box")
print(response.text)


for messages in chat.get_history():
    print(f'role - {message.role}', end='')
    print(message.parts[0].text)
