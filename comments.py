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

    
    def delete_comment(self):

        '''
        delete_comment method deletes a saved comment from the comment_list
        '''

        Comment.comment_list.remove(self)

    @classmethod
    def display_comments(cls):
        '''
        method that returns the contact list
        '''
        print(cls.comment_list)
        return cls.comment_list

