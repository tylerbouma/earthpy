### What?
Data Pipeline that collects Youtube Transcripts for videos released by BBC Earth.

### How?
The YouTubeTranscriptApi is used on top of the standard Youtube API to pull all transcripts from a channel (in this case BBC Earth). An API key is required to make the calls.
The transcript for each video is then written out to a text file - saved under **BBCE_transcripts**

We use **make_db.py** to write all of our newly created text files out to a MongoDB database. Hosting to come soon

The data is then made available via an API call created in **api.py**. *Flask* is used as the web template.
API calls exist of `/api/v1/resources/transcripts/all` or `/api/v1/resources/transcripts?<your query here>`

### Dependencies
- Youtube API - `from apiclient.discovery import build`
- Youtube Transcripts API - `from youtube_transcript_api import YouTubeTranscriptApi`
- Flask - `from flask import Flask, request, jsonify, render_template`
- markdown package - `import markdown.extensions.fenced_code`
- pymongo (make calls to MongoDB instance) - `from pymongo import MongoClient, errors`
- bson to return MongoDB cursor as JSON - `from bson.json_util import dumps`

##### Other dependencies
```import pickle, time, json, os```

