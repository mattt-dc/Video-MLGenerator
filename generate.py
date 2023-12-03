import requests
import base64
import os
import json
import shutil

def GetVideoDescription(video_file):
    with open(video_file, "rb") as video:
        encoded_string = base64.b64encode(video.read()).decode()
    
    requests.post("http://127.0.0.1:7860/run/upload", json={
	"data": [
		{"name": "video.mp4", "data": "video/mp4;base64," + encoded_string},
		None,
		"",
		None,
		[],
		False,
	]
})

    response = requests.post("http://127.0.0.1:7860/run/send", json={
	"data": [
		"What actions are taken in the video?",
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
    answer = answer_data[0][0][1]
    return answer


# Directories
video_dir = 'Videos'
text_dir = 'ActionLogs'
output_dir = 'OutputVideos'

# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Scan video directory
video_files = sorted([f for f in os.listdir(video_dir) if f.endswith('.mp4')])

# Process files
json_data = []

for i, video_file in enumerate(video_files):
    base_name = os.path.splitext(video_file)[0]

    # Copy video to output folder
    src_video_path = os.path.join(video_dir, video_file)
    dest_video_path = os.path.join(output_dir, video_file)
    if not os.path.exists(dest_video_path):
        shutil.copy(src_video_path, dest_video_path)

    # Get the filename for the next video and text file
    if not base_name[-1].isdigit():
        next_base_name = base_name + '-0'
    else:
        parts = base_name.split('-')
        incremented_number = int(parts[-1]) + 1
        next_base_name = '-'.join(parts[:-1]) + '-' + str(incremented_number)
        
    src_next_video_path = os.path.join(video_dir, next_base_name + '.mp4')
    src_next_text_path = os.path.join(text_dir, next_base_name + '.txt')
    if not os.path.exists(src_next_video_path) & os.path.exists(src_next_text_path):
        continue

    with open(src_next_text_path, 'r') as file:
        text_content = file.read()

    next_description = GetVideoDescription(src_next_video_path)
        
    qa_content = {"q": "list the button presses to get the player character to: " + next_description, "a": text_content}

    # Add to JSON data
    json_entry = {"video": dest_video_path, "QA": [qa_content]}
    json_data.append(json_entry)

# Save JSON data to a file
with open('output.json', 'w') as outfile:
    json.dump(json_data, outfile, indent=4)
