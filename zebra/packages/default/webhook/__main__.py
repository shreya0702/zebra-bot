import facts, postback, greeting
import json
import os
import postmanHandler

def main(data):
	if data.get("__ow_headers").get('x-app-id') and data.get("__ow_headers")['x-app-id'] == 'POSTMAN':
		p = postmanHandler.Handle(data)
		return p
	try:
		if data.get("__ow_method").lower() == "get":
			res_temp = {"headers": {'content-type': 
				'application/json; charset=UTF-8'}, 
				"body": ""}
			verify_token = data.get("hub.verify_token")
			if verify_token == os.getenv('WEBHOOK_VERIFY_TOKEN'):
				res_temp["body"] = data.get("hub.challenge")
				return res_temp
			else:
				res_temp["body"] = 'Unable to authorise.'
				return res_temp

		params = {
		"access_token": os.getenv('TOKEN')
		}

		sender_id = data['entry'][0]['messaging'][0]['sender']['id']

		res_temp = {"headers": {'content-type': 
				'application/json; charset=UTF-8'}, 
				"body": ""}
		res_temp["body"]="ok"

		if data['entry'][0]['messaging'][0].get("postback"):
			postbackPayload = data['entry'][0]['messaging'][0]["postback"]['payload']
			p = postback.processPostbackPayloadData(params, sender_id, postbackPayload)
			return res_temp

		message = data['entry'][0]['messaging'][0]['message']
		if message.get('text'):
			if greeting.checkIfMessageIsGreeting(message['text'].lower()):
				p = greeting.sendReplyToGreeting(params, sender_id)
			else:
				p = facts.processDataFromInputMessage(params, sender_id, message['text'], True)
			return res_temp

		return res_temp
	except:
		return res_temp
