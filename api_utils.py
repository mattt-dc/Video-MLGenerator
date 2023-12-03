import requests
import base64

def encode_video(video_file):
    with open(video_file, "rb") as video:
        return base64.b64encode(video.read()).decode()

def post_video(encoded_string):
    return requests.post("http://127.0.0.1:7860/run/upload", json={
        "data": [
            {"name": "video.mp4", "data": "video/mp4;base64," + encoded_string},
            None,
            "",
            None,
            [],
            False,
        ]
    })

def get_video_description(data):
    send_response = requests.post("http://127.0.0.1:7860/run/send", json={
        "data": [
            "What actions are taken in the video?",
            [],
            None,
        ]
    }).json()

    answer_response = requests.post("http://127.0.0.1:7860/run/answer", json={
        "data": [
            send_response["data"][1],
            None,
            None,
            1,
            1
        ]
    }).json()

    return answer_response["data"][0][0][1]
