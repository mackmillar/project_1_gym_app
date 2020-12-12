from db.run_sql import run_sql

from models.member import Member

def save(member):
    sql = "INSERT INTO members (name, email) VALUES (%s, %s) RETURNING *"
    values = [member.name, member.email]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member

def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for result in results:
        member = Member(result["name"], result['email'], result["id"])
        members.append(member)
    return members

def select(id):
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    member = Member(result["name"], result['email'], result["id"])
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(member):
    sql = "UPDATE members SET (name, email) = (%s, %s) WHERE id = %s"
    values = [member.name, member.email, author.id]
    run_sql(sql, values)


