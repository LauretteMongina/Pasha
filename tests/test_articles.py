import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the class
    '''
    
    def setUp(self):
        '''
        setUp method that will run before every test
        '''
        self.new_article = Articles("Walter Thompson","Podcast advertising has a business intelligence gap","Widespread misinformation and misconceptions are delaying ad revenue growth for podcast creators, publishers and networks.","http://techcrunch.com/2020/10/08/podcast-advertising-has-a-business-intelligence-gap/","https://techcrunch.com/wp-content/uploads/2020/10/GettyImages-691121157.jpg?w=502","2020-10-08T18:46:00Z","There are sizable, meaningful gaps in the knowledge collection and publication of podcast listening and engagement statistics.")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))
