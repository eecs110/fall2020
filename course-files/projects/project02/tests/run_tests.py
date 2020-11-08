# For some reason, this file is displaying linter errors, but it works.
# Frustrating.
import unittest
from test_authentication import TestAuthentication
from test_yelp import TestYelp
from test_spotify import TestSpotify


if __name__ == '__main__':
    unittest.main()

# Note: to run on command line: 
# $ python3 run_tests.py -v
# $ python3 run_tests.py TestAuthentication -v
# $ python3 run_tests.py TestYelp -v
# $ python3 run_tests.py TestSpotify -v
