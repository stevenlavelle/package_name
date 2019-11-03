from flask import Flask, render_template


def create_app():

    app = Flask('package_name')

    @app.route('/')
    def home():
        title = 'hello world'
        return render_template('home.html', title=title)

    @app.route('/test')
    def test():
        return 'hello world'

    return app
