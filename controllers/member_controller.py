from flask import Blueprint, Flask, redirect, render_template, request

from models.member import Member
import repositories.member_repository as member_repository
from models.session import Session
import repositories.session_repository as session_repository

members_blueprint = Blueprint("members", __name__)

# INDEX
@members_blueprint.route("/")
def members():
    members = member_repository.select_all()
    sessions = session_repository.select_all()
    return render_template("/index.html", members=members, sessions = sessions)

# NEW
@members_blueprint.route("/members/new")
def new_member():
    members = member_repository.select_all()
    return render_template("members/new.html", members = members)

# CREATE
@members_blueprint.route("/members", methods=["POST"])
def create_member():
    name = request.form["name"]
    email = request.form["email"]
    premium = request.form['premium']
    new_member = Member(name, email, premium)
    member_repository.save(new_member)
    return redirect("/")

# EDIT
@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    members = member_repository.select_all()
    member = member_repository.select(id)
    return render_template('members/edit.html', member=member, members=members)

# UPDATE
@members_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    name = request.form["name"]
    email = request.form["email"]
    premium = request.form['premium']
    member = Member(name, email, premium, id)
    member_repository.update(member)
    return redirect("/")