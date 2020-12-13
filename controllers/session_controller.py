from flask import Blueprint, Flask, redirect, render_template, request

from models.session import Session
import repositories.session_repository as session_repository

sessions_blueprint = Blueprint("sessions", __name__)

@sessions_blueprint.route("/")
def sessions():
    sessions = session_repository.select_all()
    return render_template("/index.html", sessions = sessions)

@sessions_blueprint.route("/sessions/<id>")
def show(id):
    session = session_repository.select(id)
    members = session_repository.members(session)
    return render_template("sessions/show.html", session=session, members=members)