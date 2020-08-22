import unittest
from test_authentication import TestAuthentication
from test_spotify import TestSpotify
from test_yelp import TestYelp
from test_sendgrid import TestSendgrid

if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTests([
        TestAuthentication('test_token'),
        TestAuthentication('test_get_key'),
        TestAuthentication('test_malformed_query_yields_errors'),
        TestSpotify('test__issue_get_request_only_one'),
        TestYelp('test_execute_business_queries_just_one_simplified'),
        TestSendgrid('test_can_import_sendgrid'),
        TestSendgrid('test_can_import_sendgrid_api_module')
    ])
    unittest.TextTestRunner(verbosity=2).run(suite)