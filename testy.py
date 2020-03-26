from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/blog')
def blog():
    return render_template('blog.html', author='kim')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
