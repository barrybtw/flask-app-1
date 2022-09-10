from flask import Flask, render_template
import requests
import json
import os

app = Flask(__name__)


def get_meme():
    url = "https://meme-api.herokuapp.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit


@app.route('/')
def index():
    meme_pic, subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
