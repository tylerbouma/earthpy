from apiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
import config
 
api_key = config.api_key
channel_id = 'UCwmZiChSryoWQCZMIQezgTg'  # BBC Earth channel ID
youtube = build('youtube', 'v3', developerKey=api_key)
 
def get_channel_videos(channel_id):
 
    # gather all playlists on the channel
    res = youtube.channels().list(id=channel_id,
                                  part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    videos = []
    next_page_token = None
 
    # create a list containing all video ids found in the playlists
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
video_dict = []  # dict of all video_id:title pairs of the channel
 
for video in videos:
    video_dict.append({video['snippet']['resourceId']['videoId']:video['snippet']['title']})
 
counter = 0
for video in video_dict:
    try:
        responses = YouTubeTranscriptApi.get_transcript(video[0], languages=['en'])
        #vid = youtube.videos().list(id=video[0], 
        #                            part='snippet').execute()

        # use the video_id to find the video title
        vid_title = "Title: "+video[1]+str("\n")  
        vid_link = "Video: "+"https://www.youtube.com/watch?v="+str(video[0])+'\n'+'\n'
        
        # open a text file for each video and write the title, link, and transcript out
        file_obj = open(r"BBCE_transcripts/" + str(video[0]) + str(counter)+".txt", "a")
        file_obj.write(vid_title)
        file_obj.write(vid_link)
        for response in responses:
            text = response['text']
            # Write transcripts out
            file_obj.write(text+str("\n"))
        file_obj.close()

    except Exception as e:
	    print(e)