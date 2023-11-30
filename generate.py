import requests
import base64

with open("/tmp/e19134aad6c0cc729e646ae200e2e2bcdea10543/tmpnztt55ha.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()
    
upload_response = requests.post("http://127.0.0.1:7860/run/upload", json={
	"data": [
		None,
		"data:image/png;base64," + encoded_string,
		"hello world",
		None,
		[],
		False,
	]
}).json()

upload_data = upload_response["data"]


response = requests.post("http://127.0.0.1:7860/run/send", json={
	"data": [
		"What is in the image?",
		[],
		None,
	]
}).json()

data = response["data"]

answer_response = requests.post("http://127.0.0.1:7860/run/answer", json={
	"data": [
		data[1],
		None,
		None,
        1,
        1
	]
}).json()

answer_data = answer_response["data"]