from flask import Blueprint, Flask, redirect, render_template, request
import pdb

from models.booking import Booking
from models.session import Session
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

bookings_blueprint = Blueprint("bookings", __name__)

# CREATE
@bookings_blueprint.route("/bookings", methods=["POST"])
def create_booking():
    session_id = request.form["session_id"]
    member_id = request.form["member_id"]
    member = member_repository.select(member_id)
    session = session_repository.select(session_id)
    if session_repository.how_many_members(session_id) < session.capacity:
        new_booking = Booking(member, session)
        booking_repository.save(new_booking)
        return redirect("/")
    else:
        return render_template('bookings/full.html')


    