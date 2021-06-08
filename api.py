from flask import Flask, request, jsonify
import pymongo
from bson.json_util import dumps
from __main__ import app


app.config["DEBUG"] = True

client = pymongo.MongoClient('localhost', 27017)
db = client["BBCE"]
col = db["Transcripts"]

# A route to return all of the available entries
@app.route('/api/v1/resources/transcripts/all', methods=['GET'])
def api_all():
    cur = col.find()
    list_cur = list(cur)
    return dumps(list_cur)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/api/v1/resources/transcripts', methods=['GET'])
def api_filter():
    # Get the query request from the URL
    query_params = request.args

    # Items that can be used to filter
    title = query_params.get('title')
    vid_link = query_params.get('vidlink')

    to_filter = {}
    big_list = []

    if title:
        to_filter = { "title": title }
    if vid_link:
        to_filter = { "vidlink": vid_link }
    if not (title or vid_link):
        return page_not_found(404)

    # check database for item
    cur = col.find(to_filter)
    list_cur = list(cur)
    return dumps(list_cur)
    
app.run()