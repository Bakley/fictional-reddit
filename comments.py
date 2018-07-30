import datetime
class Comment:
    """
    Class that generates new instances of comments.
    """

    comment_list = [] # Empty comment list

    def __init__(self,author,message):
        #method to initialize a comment
        self.author = author
        self.message = message
        self.time_stamp = datetime.datetime.now()
    
 
    def save_comment(self):

        '''
        save_comment method saves comment objects into comment_list
        '''

        Comment.comment_list.append(self)


    
  