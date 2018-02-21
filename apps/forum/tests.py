from django.test import TestCase
from django.contrib.auth.models import User

from .models import Board, Thread, Post

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
        User.objects.create_user(username='john',
                                email='jlennon@beatles.com',
                                password='glassonion'
                                )
        Board.objects.create(name="Technology",
                             abbreviation = "g",
                             )
        Thread.objects.create(title="/g/ related memes",
                              creator = User.objects.get(username = 'john'),
                              board = Board.objects.get(abbreviation = 'g')
                              )

    def test_thread_exists_under_board(self):
        '''
        A Simple test to see that our thread exists on our board
        as the latest thread created
        '''
        latestThread = Board.objects.get(name = "Technology").latestPost()
        self.assertEqual(latestThread, Thread.objects.get(title = '/g/ related memes'))

    def test_update_board(self):
        '''
        This test adds a new thread under the board to see if
        our updates in the ORM work
        '''
        Thread.objects.create(title = "headphone general",
                              creator = User.objects.get(username = 'john'),
                              board = Board.objects.get(abbreviation = 'g')
                              )

        newLatestThread = Board.objects.get(name = "Technology").latestPost()
        self.assertEqual(newLatestThread, Thread.objects.get(title = 'headphone general'))


class PostTestCase(TestCase):
    """
    Tests the OR functionality for the Post model
    """

    def setUp(self):
        """
        set up for the tests
        """
        User.objects.create_user(username='john',
                                email='jlennon@beatles.com',
                                password='glassonion'
                                )
        Board.objects.create(name="Technology",
                             abbreviation = "g",
                             )
        Thread.objects.create(title="/g/ related memes",
                              creator = User.objects.get(username = 'john'),
                              board = Board.objects.get(abbreviation = 'g')
                              )
        Post.objects.create(content = 'install memetoo',
                            creator = User.objects.get(username = 'john'),
                            thread = Thread.objects.get(title = "/g/ related memes"),
                            )

    def test_thread_reply(self):
        '''
        Test to make sure that the thread replies are being counted
        '''
        testThread = Thread.object.get(title = '/g/ related memes')
        numberOfReplies = testThread.numberOfReplies
        self.assertEqual(numberOfReplies, 1)
        Post.objects.create(content = 'lol funny',
                            creator = User.objects.get(username = 'john'),
                            thread = Thread.objects.get(title = "/g/ related memes")
                            )
        numberOfReplies = testThread.numberOfReplies
        self.assertEqual(numberOfReplies, 2)
        newPost = Post.objects.get(content = 'lol funny')
        self.assertEqual(testThread.getLatestReply(), newPost)
        self.assertEqual(testThread.latestReplyTime, newPost.created)
