from pymongo import MongoClient, errors
# pickle will serialize the dictionary
import pickle
import time, json

start_time = time.time()

def get_video_transcript(filename):
    with open(filename, 'rb') as raw:
        data = raw.read()
        # decode the file as UTF-8 and ignore errors
        data = data.decode("utf-8", errors='ignore')

        # split the transcript file into list
        # first line is always the title
        # second line is always the video link
        # every line after is transcript data
        data = data.split("\n")

        # create an empty Python dict for the entries
        dict_data = {'title': [], 'vidlink': [], 'text': []}

        # iterate over the list of dictionary terms
        for num, line in enumerate(data):  
            if num==0 and line[:5]=="Title":
                # this is the title
                title = line[6:]
                dict_data['title'] = title
            elif num==1 and line[:5]=="Video":
                # this is the video link
                vid_link = line[6:]
                dict_data['vidlink'] = vid_link
            else:
                # this is the transcript text
                dict_data['text'].append(line)

        
get_video_transcript('BBCE_transcripts/_2NtGS8HTc876.txt')