import unittest

from models.session import Session
from models.member import Member
from models.booking import Booking


class TestBooking(unittest.TestCase):

    def setUp(self):
        self.session_1 = Session("Swimming", "Fri 24th", "this is a description", 2)
        self.session_2 = Session("Swimming", "Fri 24th", "this is a description", 3)
        self.session_3 = Session("Swimming", "Fri 24th", "this is a description", 2)

        self.member_1 = Member("john jones", "fake@gmai.com")
        self.member_2 = Member("john jones", "fake@gmai.com")
        self.member_3 = Member("mary bell", "mary@fake.com")   

        self.booking_1 = Booking(self.member_1, self.session_1)
        self.booking_2 = Booking(self.member_2, self.session_1)

        self.bookings = [self.booking_1, self.booking_2]


    def test_booking(self):
        self.assertEqual(self.member_1, self.booking_1.member)

# def return_number_booked(self, bookings, session):
#     counter = 0
#     for booking in bookings:
#         if bookind.id = session.id:
#             counter += 1
#     return counter

    def test_number_booked(self):

        self.assertEqual(2 , self.return_number_booked(session_1))