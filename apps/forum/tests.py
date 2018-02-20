from django.test import TestCase
from django.contrib.auth.models import User
from .models import Board, Thread, Post

# Create your tests here.

class BoardTestCase(TestCase):
    """
    Tests the ORM functionality for the Board model
    """
    def setUp(self):
        """
        set up for the tests
        """
        Board.objects.create(name="Technology",
                             abbreviation = "g",
                             slug="g",
                             )
    def test_board_exists(self):
        '''
        A simple test to make sure our ORM is working and that the board object
        gets created
        '''
        board = Board.objects.get(name="Technology")
        self.assertEqual(board.name, 'Technology')
    


class ThreadTestCase(TestCase):
    """
    Tests the ORM functionality for the Thread model
    """

    def setUp(self):
        """
        set up for the tests
        """


class PostTestCase(TestCase):
    """
    Tests the OR functionality for the Post model
    """

    def setUp(self):
        """
        set up for the tests
        """
