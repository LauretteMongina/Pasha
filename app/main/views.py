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

@main.route('/news/<id>')
def news_articles(id):

    """
    View articles function
    """
    articles=get_articles(id)
    
    return render_template('articles.html',articles=articles)
@main.route('/entertainment')
def entertainment():
    '''
    View entertainment page function that returns the entertainment page and its data
    '''
    entertainment = get_articles_depending_on_category('entertainment')
    title = 'Entertainment - Welcome to The best Hot News in the world'
    return render_template('entertainment.html',
                           title=title,
                           entertainment = entertainment
                           )
@main.route('/sports')
def sports():
    '''
    View sports page function that returns the sports page and its data
    '''
    sports = get_articles_depending_on_category('sports')
    title = 'Sports - Welcome to The best Hot News in the world'
    return render_template('sports.html',
                           title=title,
                           sports = sports
                           )

@main.route('/health')
def health():
    '''
    View health page function that returns the health page and its data
    '''
    health = get_articles_depending_on_category('health')
    title = 'Health - Welcome to The best Hot News in the world'
    return render_template('health.html',
                           title=title,
                           health = health
                           )