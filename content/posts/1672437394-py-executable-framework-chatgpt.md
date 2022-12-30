+++
date = 2022-12-30T21:56:34Z
title = "Implementing py-executable workflow using ChatGPT"
description = "ChatGPT defines the workflow and implements all the steps given to it in a checklist format."
slug = "" 
tags = ["workflow"]
categories = ["chatgpt"]
externalLink = ""
series = []
+++

>_Teaching [ChatGPT](https://chat.openai.com/chat) How to write workflows using [py-executable-checklist](https://namuan.github.io/py-executable-checklist/) framework._

****You (🗣️):
I'm writing a Python application which defines a workflow as a series of steps defined by a class for each step.****

Here is what the definition of a whole workflow looks like

```python
def workflow():
    return [
        DoSomething,
    ]
```

DoSomething is a step in the workflow and is defined as

```python
class DoSomething(WorkflowBase):
"""
Go to this page
Copy the command
Run the command
Copy the output and paste it into the email
"""

    username: str

    def execute(self):
        logging.info(f"Hello {self.username}")

        # output
        return {"greetings": f"Hello {self.username}"}

```

Where username is the input to this workflow and execute method implements the workflow.
Each step can return some state by returning a dictionary of key value pairs.

Based on the above description, can you write a workflow for the following scenario

* Gather JSON data from `r/listentothis` subreddit, specifically the top songs from the past month
* Parse that JSON data such that I have an array of URLs
* Creates a file based on the name of the month in the local directory
* For each URL, the file is downloaded in ALAC format (best iTunes quality possible) and added to said folder
* When the folder contains 20 songs, the top photo from `r/earthporn` subreddit is grabbed from the reddit API
* Text (title, month, year) is added to the photo in a random color
* For each song, metadata including album name and album art is added
* The entire monthly folder is added to the "automatically add to itunes" folder

**ChatGPT (🤖):**
Here is an example of how you could define the workflow for the scenario you described using the WorkflowBase class:

```python
import logging
import requests
import json
import os
from PIL import Image, ImageDraw, ImageFont

class GatherJSONData(WorkflowBase):
    """
    Gather JSON data from the r/listentothis subreddit for the top songs of the past month.
    """
    def execute(self):
        # Send a GET request to the r/listentothis subreddit API
        response = requests.get("https://www.reddit.com/r/listentothis/top.json", params={"t": "month"})

        # Parse the JSON data from the response
        data = json.loads(response.text)

        # Extract the list of URLs from the data
        urls = [item["data"]["url"] for item in data["data"]["children"]]

        # Return the list of URLs as output
        return {"urls": urls}

class CreateMonthlyFolder(WorkflowBase):
    """
    Create a file based on the name of the month in the local directory.
    """
    def execute(self):
        # Get the current month and year
        current_month = datetime.datetime.now().strftime("%B")
        current_year = datetime.datetime.now().year

        # Create the folder for the current month in the local directory
        os.makedirs(f"{current_month}_{current_year}", exist_ok=True)

        # Return the name of the created folder as output
        return {"folder_name": f"{current_month}_{current_year}"}

class DownloadSongs(WorkflowBase):
    """
    For each URL, download the song in ALAC format and add it to the specified folder.
    """
    folder_name: str
    urls: List[str]

    def execute(self):
        # Iterate over the list of URLs
        for url in self.urls:
            # Download the song in ALAC format and save it to the specified folder
            download_song(url, self.folder_name, "ALAC")

        # Return the folder name as output
        return {"folder_name": self.folder_name}

class GrabTopPhoto(WorkflowBase):
    """
    Grab the top photo from the r/earthporn subreddit from the reddit API.
    """
    def execute(self):
        # Send a GET request to the r/earthporn subreddit API
        response = requests.get("https://www.reddit.com/r/earthporn/top.json", params={"t": "day"})

        # Parse the JSON data from the response
        data = json.loads(response.text)

        # Extract the URL of the top photo from the data
        photo_url = data["data"]["children"][0]["data"]["url"]

        # Download the photo
        response = requests.get(photo_url)
        photo_data = response.content

        # Return the photo data as output
        return {"photo_data": photo_data}

class AddTextToPhoto(WorkflowBase):
    """
    Add text (title, month, year) to the photo in a random
```

**You (🗣️):
Can you implement the following step?**

* Text (title, month, year) is added to the photo in a random color

**ChatGPT (🤖):**
Sure! Here is an example of how you could implement the step to add text (title, month, year) to a photo in a random color using the Python Pillow library:

```python
import random
from PIL import Image, ImageDraw, ImageFont

class AddTextToPhoto(WorkflowBase):
    """
    Add text (title, month, year) to the photo in a random color.
    """
    photo_data: bytes
    title: str
    month: str
    year: str

    def execute(self):
        # Open the photo data as an image
        image = Image.open(io.BytesIO(self.photo_data))

        # Create an ImageDraw object to draw on the image
        draw = ImageDraw.Draw(image)

        # Choose a random color for the text
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Set the font and font size for the text
        font = ImageFont.truetype("arial.ttf", 20)

        # Get the width and height of the image
        width, height = image.size

        # Calculate the x and y positions for the text
        x = 10
        y = 10

        # Add the title, month, and year to the image
        draw.text((x, y), self.title, fill=color, font=font)
        draw.text((x, y + 30), self.month, fill=color, font=font)
        draw.text((x, y + 60), self.year, fill=color, font=font)

        # Save the modified image to a temporary file
        with tempfile.NamedTemporaryFile() as temp_file:
            image.save(temp_file, "JPEG")

            # Read the modified image data from the temporary file
            modified_photo_data = temp_file.read()

        # Return the modified photo data as output
        return {"modified_photo_data": modified_photo_data}
```

This step assumes that you have an Arial font file named "arial.ttf" in the same directory as your Python script. You can modify the font and font size to your liking. The text is added to the image at the top left corner (x = 10, y = 10) with a vertical spacing of 30 pixels between each line of text. The random color is generated using the `random.randint()` function. The modified image is saved to a temporary file and the modified image data is read from the file and returned as output.

**You (🗣️):
Can you follow on and implement this step?**

* For each song, metadata including album name and album art is added

**ChatGPT (🤖):**
Sure! Here is an example of how you could implement a step to add metadata including album name and album art to each song in a folder using the Python Mutagen library:

```python
import mutagen

class AddMetadataToSongs(WorkflowBase):
    """
    For each song in the specified folder, add metadata including album name and album art.
    """
    folder_name: str
    album_name: str
    album_art: bytes

    def execute(self):
        # Iterate over the files in the specified folder
        for file_name in os.listdir(self.folder_name):
            # Skip non-audio files
            if not file_name.endswith(".mp3"):
                continue

            # Load the audio file using Mutagen
            audio_file = mutagen.File(os.path.join(self.folder_name, file_name))

            # Set the album name and album art in the metadata
            audio_file["album"] = self.album_name
            audio_file.tags.add(mutagen.id3.APIC(3, "image/jpeg", 3, "Front cover", self.album_art))

            # Save the modified metadata to the audio file
            audio_file.save()

```

This step assumes that you have installed the Mutagen library (`pip install mutagen`) and that the folder specified in the `folder_name` input contains only audio files with the ".mp3" file extension. The step iterates over the files in the folder, skips non-audio files, and uses Mutagen to load the audio file. It then sets the `album` field in the metadata to the value of the `album_name` input and adds the `album_art` image data as the front cover to the metadata using the Mutagen `APIC` tag. Finally, it saves the modified metadata to the audio file.

**You (🗣️):
Following on from above, can you implement this step?**
* The entire monthly folder is added to the "automatically add to itunes" folder

**ChatGPT (🤖):**
Sure! Here is an example of how you could implement a step to move the entire monthly folder to the "automatically add to itunes" folder on macOS using the Python shutil library:

```python
import shutil

class AddFolderToiTunes(WorkflowBase):
    """
    Add the specified folder to the "automatically add to itunes" folder.
    """
    folder_name: str

    def execute(self):
        # Get the path to the "automatically add to itunes" folder
        iTunes_folder = os.path.expanduser("~/Music/iTunes/iTunes Media/Automatically Add to iTunes")

        # Move the specified folder to the "automatically add to itunes" folder
        shutil.move(self.folder_name, iTunes_folder)
```

This step assumes that you are using macOS and that the "automatically add to itunes" folder is located at "~/Music/iTunes/iTunes Media/Automatically Add to iTunes" on your system. The step uses the `shutil.move()` function to move the specified folder to the "automatically add to itunes" folder.

Note that this step will only work on macOS systems. If you are using a different operating system, you will need to use a different method to move the folder to the equivalent location on your system.

**You (🗣️):
Now can you collect all the above steps and generate the following function**

def workflow():
return [
DoSomething,
]

**ChatGPT (🤖):**
Sure! Here is an example of how you could define the workflow for the scenario you described using the steps that I provided above:

```python
def workflow():
    return [
        GatherJSONData,
        CreateMonthlyFolder,
        DownloadSongs,
        GrabTopPhoto,
        AddTextToPhoto,
        AddMetadataToSongs,
        AddFolderToiTunes
    ]
```

This workflow will first gather the JSON data for the top songs of the past month from the r/listentothis subreddit, create a folder based on the current month and year in the local directory, download the songs in the ALAC format and add them to the folder, grab the top photo from the r/earthporn subreddit, add text (title, month, year) to the photo in a random color, add metadata including album name and album art to each song in the folder, and finally move the entire folder to the "automatically add to itunes" folder.

You can customize the workflow by modifying the input parameters of each step or by adding additional steps as needed.

**You (🗣️):
How can I use requests with a known user agent?**

**ChatGPT (🤖):**
To use the `requests` library with a known user agent, you can pass the `headers` parameter to the `get()` or `post()` function and specify the user agent in the `"User-Agent"` header.

For example, to send a GET request to a URL with the Chrome user agent, you could do the following:

```python
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get("https://www.example.com", headers=headers)
```

This will send the request with the specified user agent string in the `"User-Agent"` header. You can specify any user agent string that you want in this header.

Note that some websites may block or throttle requests with certain user agents, so it is important to use a user agent that is appropriate for the website that you are trying to access.

## Credits

Original idea from https://github.com/purplefloyd14/reddit_music_scrape
