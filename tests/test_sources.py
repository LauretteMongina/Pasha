import unittest
from app.models import Sources


class SourcesTest(unittest.TestCase):
    def setUp(self):
        self.new_source = Sources("bbc-news", "BBC News", "Afghanistan people", "https://abcnews.go.com", "general","English","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Sources))
