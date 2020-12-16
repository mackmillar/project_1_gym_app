import unittest

from models.session import Session
from models.member import Member
from models.booking import Booking


class TestSession(unittest.TestCase):

    def setUp(self):
        self.session_1 = Session("Swimming", "Fri 24th", "this is a description", 2)
        self.session_2 = Session("Swimming", "Fri 24th", "this is a description", 3)
        self.session_3 = Session("Swimming", "Fri 24th", "this is a description", 2)

        self.member_1 = Member("john jones", "fake@gmai.com", False)
        self.member_2 = Member("john jones", "fake@gmai.com", False)
        self.member_3 = Member("mary bell", "mary@fake.com", True)   

        self.booking_1 = Booking(self.member_1, self.session_1)
        self.booking_2 = Booking(self.member_2, self.session_1)


    def test_session_has_capacity(self):
        self.assertEqual(2, self.session_1.get_capacity())

    def test_session_has_counter(self):
        self.assertEqual(0, self.session_1.counter)

    def test_can_add_to_counter(self):
        self.session_1.add_to_counter()
        self.assertEqual(1, self.session_1.counter)

    def test_counter_equals_or_greater_than_capacity(self):
        self.session_1.add_to_counter()
        self.session_1.add_to_counter()
        self.assertEqual(self.session_1.capacity, self.session_1.counter)

    def test_counter_works(self):
        self.session_1.add_to_counter()
        self.session_1.add_to_counter()
        self.assertEqual(self.session_1.counter, 2)
