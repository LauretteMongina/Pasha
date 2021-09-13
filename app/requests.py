import urllib.request,json
from .models import Articles,Sources
import os

api_key = None
base_url_source = None
base_url_articles = None

def configure_request(app):
    global api_key,base_url_source,base_url_articles
    api_key = app.config['NEWS_API_KEY']
    base_url_source = app.config['NEWS_API_SOURCE_URL']
    base_url_articles = app.config['NEWS_API_ARTICLES_URL']
    

def get_sources():
    """
    function that gets response from the api call
    """    
    get_sources_url = 'https://newsapi.org/v2/sources?apiKey={}'.format(api_key)
    print(get_sources_url)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results_sources(sources_results_list)
    return sources_results

def process_results_sources(sources_list):
    sources_results = []

    for source_item in sources_list:
        id = source_item.get("id")
        name = source_item.get("name")
        description = source_item.get("description")
        url = source_item.get("url")
        category = source_item.get("category")
        language = source_item.get("language")
        country = source_item.get("country")
        
        new_source = Sources(id,name,description,url,category,language,country)
        sources_results.append(new_source)
    
    return sources_results

def get_articles(id):

    '''
    Function that gets the json response to our url request
    '''
    # get_articles_url = base_url_articles.format(source_id, api_key)
    get_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(
        id, api_key)
    # get_articles_url = base_url_articles.format(source_id, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        # load the data into a json object
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results_articles(articles_results_list)
    return articles_results  # return the results

def process_new_articles(articles_list):
    articles_results = []

    for article_item in articles_list:
        
        author = article_item.get("author")
        description = article_item.get("description")
        title = article_item.get("title")
        url = article_item.get("url")
        urlToImage = article_item.get("urlToImage")
        publishedAt = article_item.get("publishedAt")
        content = article_item.get("content")
    
        if urlToImage:
            new_articles = Articles(
            author, title, description, url, urlToImage, publishedAt,content)
            articles_results.append(new_articles)

    return articles_results

# get news relating to specific source and country

def get_articles_from_source(source):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(source,
                                                                                                      api_key)
    # get_articles_url = base_url_articles.format(source_id, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        # load the data into a json object
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results_articles(articles_results_list)
    return articles_results  # return the results

# get news depending on category

def get_articles_depending_on_category(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = 'https://newsapi.org/v2/top-headlines?category={}&apiKey={}'.format(
        category,api_key)
    # get_articles_url = base_url_articles.format(source_id, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        # load the data into a json object
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_new_articles(articles_results_list)
    return articles_results  # return the results


def process_category_results(articles_list):
    '''
    function that processes the json files of articles from the api key
    '''
    articles_results = []
    for article_item in articles_list:
       
        author = article_item.get('author')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        title = article_item.get ('title')
        content= article_item.get('content')
        if url:
            new_articles = Articles(
            author, title, description, url, urlToImage, publishedAt,content)
            articles_results.append(new_articles)

    return articles_results