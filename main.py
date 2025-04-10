from pyChatReworked import ChatGPT

session_token = "" //replace this his from your browser's cookies

api = ChatGPT(session_token)

response = api.send_message("Write a wow macro")
print(response['message'])
