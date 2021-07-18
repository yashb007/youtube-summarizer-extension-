from flask import Flask
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

def getTrans(id):
    trans = YouTubeTranscriptApi.get_transcript(id)

    
    result = ""
    for i in trans:
        result += ' ' + i['text']
    #print(result)
    print(result)

    return result

def get_summarize(text):
    summarization = pipeline("summarization")
    summary_text = summarization(text)[0]['summary_text']
    print("Summary:", summary_text)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

text = getTrans('FVnfVmw45Ng')

get_summarize(text)

if __name__ == "main":
    
    app.run(debug=True)

