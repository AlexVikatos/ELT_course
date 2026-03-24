import requests
import json

API_KEY="AIzaSyBBokfUXbWvAC96kAXOp_Y60eC_GiBk0-U"
CHANNEL_HANDLE='MrBeast'

url=f'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}'

response=requests.get(url)
print(response)

data=response.json()

print(json.dumps(data,indent=4))

channel_items=data['items'][0]

channel_playlistID=channel_items['contentDetails']['relatedPlaylists']['uploads']
print(channel_playlistID)