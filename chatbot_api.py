import requests

url = "https://chatbot19.p.rapidapi.com/chatbot"

payload = "message=Hi%2C%20how%20are%20you%3F%20&language=en&context=%5B%22array%20of%20the%20previous%20messages%22%5D%20"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY",
    'x-rapidapi-host': "chatbot19.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)