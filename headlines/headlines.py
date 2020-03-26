from flask import Flask, render_template, request
import feedparser

app = Flask(__name__)

feeds = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
         'nation': 'https://www.nation.co.ke/rss',
         'standard': 'https://www.standardmedia.co.ke/rss/kenya.php'}


@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
    feed = feedparser.parse(feeds[publication])

    return render_template('home.html', article=feed['entries'], source=publication)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
