import requests
import base64

with open("/tmp/c0a63d8f1b4abb3545811c7e8668d9f61c5bcc7e/birthday.mp4", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()
    
upload_response = requests.post("http://127.0.0.1:7860/run/upload", json={
	"data": [
		{"name": "birthday.mp4", "data": "video/mp4;base64," + encoded_string},
		None,
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