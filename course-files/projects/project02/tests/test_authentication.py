def path_hack():
    import os, sys, inspect
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0,parentdir) 
    # print('path added:', sys.path[0])

path_hack()

import unittest
import urllib
from apis import authentication
import time
from unittest.mock import MagicMock

class TestAuthentication(unittest.TestCase):

    def test_token(self):
        self.assertTrue(authentication.API_TUTOR_TOKEN is not None)

    def test_get_key(self):
        yelp_key = authentication.get_token('https://www.apitutor.org/yelp/key')
        self.assertEqual(len(yelp_key), 128)
        time.sleep(1.0)
        spotify_key = authentication.get_token('https://www.apitutor.org/spotify/key')
        self.assertEqual(len(spotify_key), 144)
        time.sleep(1.0)

    def test_malformed_query_yields_errors(self):
        with self.assertRaises(Exception) as cm:
            authentication.get_token('https://www.apitutor.org/yelp/ke')
        self.assertIn(
            'This URL is invalid: https://www.apitutor.org/yelp/ke', str(cm.exception)
        )
        time.sleep(1.0)
        with self.assertRaises(Exception) as cm:
            authentication.get_token('https://www.apitutor.org/spotify/ke')
        self.assertIn(
            'This URL is invalid: https://www.apitutor.org/spotify/ke', str(cm.exception)
        )

if __name__ == '__main__':
    unittest.main()