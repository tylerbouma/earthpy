from apiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
 
api_key = "AIzaSyCcaq5p47xgD_YoRhGntQ8ASfUo8Tvo0wM"  # replace it with your API key
channel_id = 'UCwmZiChSryoWQCZMIQezgTg'  # replace it with your channel id
youtube = build('youtube', 'v3', developerKey=api_key)
 
def get_channel_videos(channel_id):
 
    # get Uploads playlist id
    res = youtube.channels().list(id=channel_id,
                                  part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    videos = []
    next_page_token = None
 
    while 1:
        res = youtube.playlistItems().list(playlistId=playlist_id,
                                           part='snippet',
                                           maxResults=50,
                                           pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')
 
        if next_page_token is None:
            break
 
    return videos
 
videos = get_channel_videos(channel_id)
video_ids = []  # list of all video_id of channel
 
for video in videos:
    video_ids.append(video['snippet']['resourceId']['videoId'])
 
for video_id in video_ids:
    try:
        responses = YouTubeTranscriptApi.get_transcript(
            video_id, languages=['en'])
        print('\n'+"Video: "+"https://www.youtube.com/watch?v="+str(video_id)+'\n'+'\n'+"Captions:")
        for response in responses:
            text = response['text']
            # Write transcripts out for each video to a 
    except Exception as e:
	    print(e)