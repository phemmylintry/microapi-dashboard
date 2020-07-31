import json

with open("docs.json") as read_file:
	data = json.load(read_file)

def check_microapi(microapi, data):
	if microapi:
		if microapi in data['microapi']:
			documentation = data['microapi'][microapi]
			return "Success"
		else:
			return "Microapi is not in Database"
	else:
		return "Invalid Entry"

check_microapi('comments', data)