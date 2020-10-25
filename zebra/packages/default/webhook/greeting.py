import requests
import json

def checkIfMessageIsGreeting(message):
	if message.startswith('hi') or message.startswith('hey') or message.startswith('hello'):
		return True
	else:
		return False

def sendReplyToGreeting(params, sender_id):
	headers = {
		"Content-Type": "application/json"
		}
		
	data = json.dumps({
			'recipient': {
				'id': sender_id
			},
			'message': {"text":"Hey there! I'll help you with recent news doing the rounds around any topic. Just type in some keywords you would want to fetch news for."}
	})
	r = requests.post("https://graph.facebook.com/me/messages", params=params, headers=headers, data=data)
	if r.status_code != 200:
		print(r.status_code)
		print(r.text)
	return "ok"