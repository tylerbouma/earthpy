import pandas as pd
from pymongo import MongoClient

def read_mongo(no_id=True):
    # declare a client instance of the MongoDB PyMongo driver
    client = MongoClient('localhost', 27017)
    db = client["BBCE"]
    col = db["Transcripts"]

    col.create_index([("text", "text" )])
    cur = col.find({ "$text": {"$search": "Penguins" }}).limit(10)

    df = pd.DataFrame(list(cur))

    # delete the id
    #if no_id:
        # del df['_id']
    
    return df