import facts

def Handle(data):
	res_temp = {"headers": {'content-type': 
				'application/json; charset=UTF-8'}, 
				}
	message=data.get("text", "")

	if message == "":
		res_temp["body"] = "text cannot be empty"
		res_temp["statusCode"] = 400
		return res_temp

	p = facts.processDataFromInputMessage("nil", "nil", message, False)
	res_temp["body"] = p
	return res_temp
