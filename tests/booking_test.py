import unittest

from models.session import Session
from models.member import Member
from models.booking import Booking


class TestBooking(unittest.TestCase):

    def setUp(self):
        self.session_1 = Session("Swimming", "Fri 24th", "this is a description", 2)
        self.session_2 = Session("Swimming", "Fri 24th", "this is a description", 3)
        self.session_3 = Session("Swimming", "Fri 24th", "this is a description", 2)

        self.member_1 = Member("john jones", "fake@gmai.com", False)
        self.member_2 = Member("john jones", "fake@gmai.com", False)
        self.member_3 = Member("mary bell", "mary@fake.com", True)   

        self.booking_1 = Booking(self.member_1, self.session_1)
        self.booking_2 = Booking(self.member_2, self.session_1)

        self.bookings = [self.booking_1, self.booking_2]


    def test_booking(self):
        self.assertEqual(self.member_1, self.booking_1.member)

