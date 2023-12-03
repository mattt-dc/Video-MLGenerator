import os
import json
import shutil
import api_utils

# Constants
VIDEO_DIR = 'Videos'
TEXT_DIR = 'ActionLogs'
OUTPUT_DIR = 'OutputVideos'

def ensure_dir_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        
def process_videos(video_files):
    json_data = []

    for video_file in video_files:
        base_name = os.path.splitext(video_file)[0]

        # Copy video to output folder
        src_video_path = os.path.join(VIDEO_DIR, video_file)
        dest_video_path = os.path.join(OUTPUT_DIR, video_file)
        if not os.path.exists(dest_video_path):
            shutil.copy(src_video_path, dest_video_path)

        # Determine the filename for the next video and text file
        if not base_name[-1].isdigit():
            next_base_name = base_name + '-0'
        else:
            parts = base_name.split('-')
            incremented_number = int(parts[-1]) + 1
            next_base_name = '-'.join(parts[:-1]) + '-' + str(incremented_number)

        src_next_video_path = os.path.join(VIDEO_DIR, next_base_name + '.mp4')
        src_next_text_path = os.path.join(TEXT_DIR, next_base_name + '.txt')

        if not os.path.exists(src_next_video_path) or not os.path.exists(src_next_text_path):
            continue

        # Read text content
        with open(src_next_text_path, 'r') as file:
            text_content = file.read()

        # Get video description
        encoded_video = api_utils.encode_video(src_next_video_path)
        api_utils.post_video(encoded_video)
        next_description = api_utils.get_video_description(src_next_video_path)

        qa_content = {"q": "list the button presses to get the player character to: " + next_description, "a": text_content}

        # Add to JSON data
        json_entry = {"video": dest_video_path, "QA": [qa_content]}
        json_data.append(json_entry)

    return json_data

def main():
    ensure_dir_exists(OUTPUT_DIR)
    video_files = sorted([f for f in os.listdir(VIDEO_DIR) if f.endswith('.mp4')])
    json_data = process_videos(video_files)

    with open('output.json', 'w') as outfile:
        json.dump(json_data, outfile, indent=4)

if __name__ == "__main__":
    main()
