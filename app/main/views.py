from flask import render_template
from . import main
from ..requests import get_sources, get_articles, get_articles_from_source, get_articles_depending_on_category


@main.route('/')
def index():
    

    '''
    View root page function that returns the index page and its data
    '''
    
    my_sources=get_sources()
    technology=get_articles_depending_on_category('technology')
    return render_template('index.html',my_sources=my_sources,technology=technology)

