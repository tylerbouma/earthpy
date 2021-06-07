from pymongo import MongoClient, errors
# pickle will serialize the dictionary
import pickle
import time, json
import os

start_time = time.time()

def get_video_transcript(filename):
    with open(filename, 'rb') as raw:
        data = raw.read()
        # decode the file as UTF-8 and ignore errors
        data = data.decode("utf-8", errors='ignore')

        # split the transcript file into list
        data = data.split("\n")

        # create an empty Python dict for the entries
        dict_data = {'title': [], 'vidlink': [], 'text': []}
        text = ""

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
                # create one long string for dictionary insertion
                text += " " + line
        dict_data['text'] = text
    
    return dict_data

# declare a client instance of the MongoDB PyMongo driver
client = MongoClient('localhost', 27017)

# # make sure the host settings are correct
# # print("\nserver_info():", json.dumps(client.server_info(), indent=4))

db = client["BBCE"]
col = db["Transcripts"]

directory = 'BBCE_transcripts'        
# iterate through all documents and add them to the DB
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        t_data = get_video_transcript(os.path.join(directory, filename))
        result = col.insert_one(t_data)
    else:
        continue        