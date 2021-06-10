import pandas as pd
from pymongo import MongoClient

def read_mongo(db="", collection="", query={}, no_id=True):
    # declare a client instance of the MongoDB PyMongo driver
    client = MongoClient('localhost', 27017)
    db = client["BBCE"]
    col = db["Transcripts"]

    col.create_index([("text", "text")])
    # col.create_index([("title", "text")])
    cur = col.find({ "$text": {"$search": "Tigers" }}).limit(10)

    df = pd.DataFrame(list(cur))

    # delete the id
    if no_id:
        del df['_id']
        df.columns = ['Title', 'Video Link', 'Text']
    else:
        df.columns = ['ID', 'Title', 'Video Link', 'Text']
    
    
    return df