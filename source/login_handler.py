"""
Login Handler
"""

import logging

logger = logging.getLogger(__name__)

class Login(object):
    """
    Login Class
    """
    def __init__(self, usernames=None):
        self.usernames = usernames
        self.logged_in = False

    def login(self, username=None, password=None):
        """
        Attempt Login
        :param username: Name of user
        :type username: str

        :param password: password of user
        :type password: str

        :return: None
        """
        if username in self.usernames.keys():
            if password == self.usernames[username]:
                self.logged_in = True
                logger.info('Login Worked')
        else:
            logger.error('Login Failed')
