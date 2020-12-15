class Booking:
    def __init__(self, member, session, id=None):
        self.member = member
        self.session = session
        self.id = id



def add_member_to_session(self, member, session):
    new_booking = Booking(member, session)
    return new_booking

def return_number_booked(self, bookings, session):
    counter = 0
    for booking in bookings:
        if booking(id) == session(id):
            counter += 1
    return counter




        


# def number_of_mebers_attending(self, session):
#         return len(self.session.booking)