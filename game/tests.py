from django.test import TestCase
from extractor.extractor import md5, file_repeated
from game.models import FileHistory


class TestExtractor(TestCase):

    def setUp(self):
        self.pgn_file = '/home/awemulya/Documents/chess/samplepgn/asample.pgn'
        FileHistory.objects.create(checksum=md5(self.pgn_file))


    def test_file_repeated(self):
        self.assertTrue(file_repeated(self.pgn_file))
