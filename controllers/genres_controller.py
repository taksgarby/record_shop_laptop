from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.record import Record
import repositories.record_repository as record_repository
import repositories.artist_repository as artist_repository


genres_blueprint= Blueprint("genres", __name__)

@genres_blueprint.route("/genres/add")
def add_genre():
    return render_template("genres/add.html")

@genres_blueprint.route("/genres")
def genres():
    return render_template("genres/index.html")