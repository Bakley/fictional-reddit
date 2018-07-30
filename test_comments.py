import unittest
from comments import Comment
import datetime

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the comments class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_comment = Comment("Antony","Impresive blog",datetime.datetime.now()) 
    
    def test_init(self):
        """Method to test the object initialises correctly"""
        self.assertEqual(self.new_comment.author,"Antony")
        self.assertEqual(self.new_comment.message,"Impresive blog")
    
    def test_save_comment(self):
        """test to save a single comment"""
        self.new_comment.save_comment() # saving the new comment
        self.assertEqual(len(Comment.comment_list),1)


if __name__ == '__main__':
    unittest.main()