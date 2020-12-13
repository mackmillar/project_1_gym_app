from flask import Blueprint, Flask, redirect, render_template, request

from models.session import Session
import repositories.session_repository as session_repository
from models.member import Member
import repositories.member_repository as member_repository

sessions_blueprint = Blueprint("sessions", __name__)

@sessions_blueprint.route("/")
def sessions():
    sessions = session_repository.select_all()
    return render_template("/index.html", sessions = sessions)

#  SHOW
@sessions_blueprint.route("/sessions/<id>")
def show(id):
    session = session_repository.select(id)
    attending = session_repository.members(session)
    members = member_repository.select_all()
    return render_template("sessions/show.html", session=session, attending=attending, members=members)

# NEW
@sessions_blueprint.route("/sessions/new")
def new_session():
    sessions = session_repository.select_all()
    return render_template("sessions/new.html", sessions = sessions)

# CREATE
@sessions_blueprint.route("/sessions", methods=["POST"])
def create_session():
    title = request.form["title"]
    date = request.form["date"]
    description = request.form['description']
    new_session = Session(title, date, description)
    session_repository.save(new_session)
    return redirect("/")

# EDIT
@sessions_blueprint.route("/sessions/<id>/edit")
def edit_session(id):
    members = member_repository.select_all()
    session = session_repository.select(id)
    return render_template('sessions/edit.html', members=members, session=session)

# UPDATE
@sessions_blueprint.route("/sessions/<id>", methods=["POST"])
def update_session(id):
    title = request.form["title"]
    date = request.form["date"]
    description = request.form['description']
    new_session = Session(title, date, description)
    session_repository.save(new_session)
    return redirect("/")