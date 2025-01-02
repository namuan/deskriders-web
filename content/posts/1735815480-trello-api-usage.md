+++ 
date = 2025-01-02T10:58:00Z
title = "Using Trello API"
description = "How to set up and connect to Trello API"
slug = "" 
tags = ["trello", "api"]
categories = ["productivity", "tools"]
externalLink = ""
series = []
+++

Create a new API Key

https://trello.com/power-ups/admin

Once the API Key is created, there is a link to create API Token

![images/2025/01/02/1735815846-1.png](/images/2025/01/02/1735815846-1.png)

[Trello REST API Reference](https://developer.atlassian.com/cloud/trello/rest/api-group-actions/#api-group-actions)

Here is a simple Python script to list all the cards under a certain list.

```python
#!/usr/bin/env -S uv run --quiet --script
# /// script
# dependencies = [
#   "requests",
# ]
# ///
import os
import requests


def get_trello_cards():
    # Get environment variables
    api_key = os.environ.get('TRELLO_KEY')
    api_token = os.environ.get('TRELLO_TOKEN')
    board_name_to_match = os.environ.get('TRELLO_BOARDNAME')
    list_name_to_match = os.environ.get('TRELLO_LISTNAME')
    username = os.environ.get('TRELLO_USER')

    # Common parameters for all requests
    base_params = {
        'key': api_key,
        'token': api_token
    }

    def make_request(url, params=None):
        request_params = base_params.copy()
        if params:
            request_params.update(params)
        
        response = requests.get(url, params=request_params)
        response.raise_for_status()
        return response.json()

    # Get user's boards
    boards_url = f"https://api.trello.com/1/members/{username}/boards"
    boards = make_request(boards_url)

    # Find the specific board
    board_id = None
    for board in boards:
        if board['name'] == board_name_to_match:
            board_id = board['id']
            break

    if not board_id:
        raise Exception(f"Board '{board_name_to_match}' not found")

    # Get lists on the board
    lists_url = f"https://api.trello.com/1/boards/{board_id}/lists"
    lists = make_request(lists_url)

    # Find the specific list
    list_id = None
    for list_ in lists:
        if list_['name'] == list_name_to_match:
            list_id = list_['id']
            break

    if not list_id:
        raise Exception(f"List '{list_name_to_match}' not found")

    # Get cards in the list
    cards_url = f"https://api.trello.com/1/lists/{list_id}/cards"
    cards = make_request(cards_url)

    # Print cards
    for card in cards:
        print(f"{card['name']} | href={card['shortUrl']}")


if __name__ == "__main__":
    try:
        get_trello_cards()
    except Exception as e:
        print(f"Error: {str(e)}")
```

We can also get a JSON representation of the board by requesting a `.json` url.

Eg. https://trello.com/b/7lQSoeS/boardname to https://trello.com/b/7lQSoeS/boardname.json

