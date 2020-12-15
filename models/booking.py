class Booking:
    def __init__(self, member, session, id=None):
        self.member = member
        self.session = session
        self.id = id


def add_member_to_session(self, member, session):
    new_booking = Booking(member, session)
    return new_booking


