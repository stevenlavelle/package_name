from flask import Flask, render_template


def create_app():

    app = Flask(__name__)

    @app.route('/')
    def home():
        title = 'hello world'
        return render_template('home.html', title=title)

    return app
