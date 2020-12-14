import unittest

from models.session import Session


class TestSession(unittest.TestCase):

    def setUp(self):
        self.session_1 = Session("Swimming", "Fri 24th", "this is a description", 2)

    def test_session_has_capacity(self):
        self.assertEqual(2, self.session_1.get_capacity())