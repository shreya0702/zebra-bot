import requests
import json

def processPostbackPayloadData(params, sender_id, postback):
	headers = {
		"Content-Type": "application/json"
		}
	if postback == "GET_STARTED":
		data = json.dumps({
		'recipient': {
			'id': sender_id
		},
		'message': {
			"text": "Hi! Welcome to the fact check world. Please type in some topics or keywords for which you want to get verdicts on the recent news which is floating around. Stay safe from hoaxes!"
		}
		})

	elif postback == "HELP":
		data = json.dumps({
		'recipient': {
			'id': sender_id
		},
		'message': {
			"text": "Hey there! Don't worry! We're here to help you :) Please type in some topics or keywords for which you want to get verdicts on the recent news which is floating around. For example any of these: health, covid-19, united nations, education etc."
		}
		})
	else :
		data = json.dumps({
		'recipient': {
			'id': sender_id
		},
		'message': {
			"text": "Sorry! This input is not supported"
		}
		})
	r = requests.post("https://graph.facebook.com/me/messages", params=params, headers=headers, data=data)
	return "ok"
	
