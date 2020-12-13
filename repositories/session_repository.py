from db.run_sql import run_sql
from models.session import Session
from models.member import Member
from models.booking import Booking


def save(session):
    sql = "INSERT INTO sessions (title, date, description) VALUES (%s, %s, %s) RETURNING *"
    values = [session.title, session.date, session.description]
    results = run_sql(sql, values)
    id = results[0]['id']
    session.id = id
    return session

def select_all():
    sessions = []
    sql = "SELECT * FROM sessions"
    results = run_sql(sql)
    for result in results:
        session = Session(result["title"], result['date'], result['description'], result["id"])
        sessions.append(session)
    return sessions

def select(id):
    sql = "SELECT * FROM sessions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    session = Session(result["title"], result['date'], result['description'], result["id"])
    return session

def delete(id):
    sql = "DELETE FROM sessions WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)

def update(session):
    sql = "UPDATE sessions SET (title, date, description) = (%s, %s, %s) WHERE id = %s"
    values = [session.title, session.date, session.description, session.id]
    run_sql(sql, values)

def members(session):
    members = []

    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE bookings.session_id = %s"
    values = [session.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['name'], row['email'], row['id'])
        members.append(member)

    return members

def select_attendees_of_session(id):
    attendees = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE bookings.session_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        member = Member(result["name"], result['email'], result["id"])
        attendees.append(member)
    return attendees
