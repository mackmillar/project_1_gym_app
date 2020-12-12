from flask import Blueprint, Flask, redirect, render_template, request

from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

# INDEX
@members_blueprint.route("/")
def members():
    members = member_repository.select_all()
    return render_template("/index.html", members=members)

# NEW
@members_blueprint.route("/members/new")
def new_member():
    return render_template("members/new.html")