# Video-MLGenerator
## Overview

This application is designed to generate datasets for training machine learning models to play any game, with potential applications extending beyond gaming into any interactive environment. 

Video files and their associated button press logs from gameplay footage are used to create structured JSON data for training ML models. 

The input is a video to provide context combined with a text description of the objective (e.g enter the inn). The output is the button presses required to achieve the objective.

The output from Video-LLaMA is not yet consistent enough to create usable data but I hope to develop this more in future as ML video analysis improves.

## Features

* Processes video files and button press logs stored in the Videos and ActionLogs folders.
* Integrates with the Video-LLaMA API to get action descriptions from videos.
* Generates structured JSON data suitable for Video-LLaMA training.

## Prerequisites

Before running this application, ensure you have the following:

* Python 3.6 or higher installed.
* Access to the Video-Llama API (see modifications required for API access in the related repositories list).
* The video files and corresponding button press logs. (See the repository for generating required videos and logs).

## Usage

To run the application, use the following command:

``python main.py``

## Output

The script generates a JSON file (output.json) with the following structure for each video:
```
{
  "video": "OutputVideos/video.mp4",
  "QA": [
    {
      "q": "list the button presses to get the player character to: [action description]",
      "a": "[button press log content]"
    }
  ]
}
```
e.g (the action description is theoretical as it has not be possible to generate this specific output from Video-LLaMA so far).
```
{
  "video": "OutputVideos/OdFulgHWlE-1.mp4",
  "QA": [
    {
      "q": "list the button presses to get the player character to: Walk through the gate",
      "a": "a[hold for 0.2 seconds] (left)\nw[hold for 0.2 seconds] (forward)\nw[hold for 0.2 seconds] (forward)\nrotate_camera_left (look left)\nrotate_camera_left (look left)\nrotate_camera_left (look left)\nrotate_camera_right (look right)\na[hold for 0.2 seconds] (left)\nleft_click (action)\nrotate_camera_left (look left)\n"
    }
  ]
}
```
## Related Repositories

* [Video and Log Generator Repository](https://github.com/mattt-dc/playwatchvm)
* [Video-Llama API Access Modifications](https://github.com/mattt-dc/Video-LLaMA/tree/apisupport)
