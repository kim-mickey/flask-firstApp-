import feedparser
from flask import Flask, render_template, request

app = Flask(__name__)

feeds = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
         'nation': 'https://www.nation.co.ke/rss',
         'standard': 'https://www.standardmedia.co.ke/rss/kenya.php'}


@app.route('/')
def get_news():
    query = request.args.get('publication')

    if not query or query.lower() not in feeds:
        publication = 'bbc'

    else:
        publication = query.lower()

    feed = feedparser.parse(feeds[publication])

    return render_template('home.html', article=feed['entries'], source=publication)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
