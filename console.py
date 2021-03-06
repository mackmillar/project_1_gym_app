from models.booking import Booking
import repositories.booking_repository as booking_repository
from models.member import Member
import repositories.member_repository as member_repository
from models.session import Session
import repositories.session_repository as session_repository

booking_repository.delete_all()
member_repository.delete_all()
session_repository.delete_all()

member_1 = Member("James Graham", "jamesgraham@fake.com", False)
member_repository.save(member_1)
member_2 = Member("Toby Brown", "tobybrown@fake.com", False)
member_repository.save(member_2)
member_3 = Member("Tony Keith", "tony@fake.com", False)
member_repository.save(member_3)
member_4 = Member("Brian Douglas", "brian@fake.com", True)
member_repository.save(member_4)

session_1 = Session("Swimming", "Tue 24th", "An adults swim session in the deep end of the pool, available for primarily fitness swimming.", 2)
session_repository.save(session_1)


session_2 = Session("Circuit Training", "Wed 25th", "A combination of high intensity body weight exercises with resistance work.", 4)
session_repository.save(session_2)
session_3 = Session("Spin Class", "Wed 25th", "A combination of high intensity spinning exercises with music." , 5)
session_repository.save(session_3)

booking_1 = Booking(member_1, session_1)
booking_repository.save(booking_1)
booking_2 = Booking(member_2, session_1)
booking_repository.save(booking_2)
# # session_1.add_to_counter(session_1)



# print(session_2.capacity)
# print(session_2.session_has_room(session_2))

