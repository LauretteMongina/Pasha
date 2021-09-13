class Articles:
    
    '''
    Articles class that determines the instance of new articles
    '''
    def __init__(self,author,description,title,url,urlToImage,publishedAt,content):
    
        
        self.author = author
        self.description = description
        self.title = title
        self.url = url 
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
        
class Sources:
    '''
    Class to define all news sources
    '''
    
    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name 
        self.description = description
        self.url = url 
        self.category = category
        self.language = language
        self.country = country