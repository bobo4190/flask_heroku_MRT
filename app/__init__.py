from flask import Flask
from app.route import hello_world, index, analysis, about, model


def create_app():
    app = Flask(__name__)
    app.add_url_rule('/', '/', hello_world)
    app.add_url_rule('/index', 'index', index)
    app.add_url_rule('/about', 'about', about)
    app.add_url_rule('/analysis', 'analysis', analysis)
    app.add_url_rule('/model', 'model', model)
    
    return app