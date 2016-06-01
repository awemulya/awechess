from django.test import TestCase
from extractor.extractor import md5


class TestExtractor(TestCase):

    def setUp(self):
        self.pgn_file = '/home/awemulya/Documents/chess/samplepgn/asample.pgn'


    def test_md5(self):
        self.assertIsInstance(md5(self.pgn_file),str)

    def test_md5_length(self):
        self.assertGreaterEqual(256, len(md5(self.pgn_file)))
