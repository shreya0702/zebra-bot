import requests
import json
import constants
import images
import os

def getClaimReviews(formattedKeywords):
	print("In getClaimReviews")
	print(os.getenv('API_KEY'))
	response = requests.get(
		url=constants.URL,
		params=dict(
			key=os.getenv('API_KEY'),
			languageCode=constants.LANGUAGECODE,
			query=formattedKeywords))
	return response.json()

def formatString(keyword):
	print("In formatString")
	return '%20'.join(s for s in keyword)

def prettyPrint(jsonContent):
	return json.dumps(jsonContent)


def getFacts(content):
	print("In getFacts")
	keywords=content.split()

	if len(keywords)>15:
		keywords=keywords[:15]

	claimReviews = getClaimReviews(formatString(keywords))
	return claimReviews

def processDataFromInputMessage(params, sender_id, message, sendReplyToFB=True):
	print("In processDataFromInputMessage")
	facts = getFacts(message)
	elements=[]

	if not facts:
		facts="Sorry there is no relevant news with these keywords! Please try with a different set of words."
		data = json.dumps({
			'recipient': {
				'id': sender_id
			},
			'message': {"text":facts}
		})
	else:
		for fact in facts['claims']:
			element = {
			"title": fact['text'],
			"subtitle": "Verdict: " + fact['claimReview'][0]['textualRating'],
			"image_url": images.getImageUrl(),
			"default_action": {
				"type":"web_url",
				"url": fact['claimReview'][0]['url'],
				"webview_height_ratio": "tall"
				}
			}
			elements.append(element)

		data = json.dumps({
			'recipient': {
				'id': sender_id
			},
			'message': {
				"attachment": {
					"type": "template",
					"payload" : {
						"template_type": "generic",
						"elements": elements
					}
				}}
		})

	headers = {
		"Content-Type": "application/json"
		}

	if sendReplyToFB == True:
		r = requests.post("https://graph.facebook.com/me/messages", params=params, headers=headers, data=data)
		if r.status_code != 200:
			print(r.status_code)
			print(r.text)
		return "ok"
	else:
		return data

