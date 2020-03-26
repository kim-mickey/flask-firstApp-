from flask import Flask, render_template
import feedparser

app = Flask(__name__)

feeds = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
         'nation': 'https://www.nation.co.ke/rss',
         'standard': 'https://www.standardmedia.co.ke/rss/kenya.php'}


@app.route('/')
@app.route('/bbc')
def bbc():
    return get_news('bbc')


@app.route('/standard')
def standard():
    return get_news('standard')


@app.route('/nation')
def nation():
    return get_news('nation')


def get_news(publication):
    feed = feedparser.parse(feeds[publication])
    article = feed['entries'][0]
    return '''
    <html>
        <body>
            <h1>Updates</h1>
            <b>{0}</b><br/>
            <i>{1}</i><br/>
            <p>{2}</p><br/>
        </body>
    </html>
    '''.format(article.get('title'), article.get('published'), article.get('summary'))


if __name__ == "__main__":
    app.run(port=8080, debug=True)
