def path_hack():
    import os, sys, inspect
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0,parentdir) 
    # print('path added:', sys.path[0])

path_hack()


from apis import sendgrid
import unittest
import time

class TestSendgrid(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSendgrid, self).__init__(*args, **kwargs)

    def test_can_import_sendgrid(self, *args, **kwargs):
        from sendgrid import SendGridAPIClient
        from sendgrid.helpers.mail import Mail
        self.assertNotEqual(str(Mail).find('Mail'), -1)

    def test_can_import_sendgrid_api_module(self, *args, **kwargs):
        self.assertNotEqual(str(sendgrid.send_mail).find('function send_mail'), -1)

if __name__ == '__main__':
    unittest.main()


