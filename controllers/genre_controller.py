from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.record import Record
import repositories.record_repository as record_repository
import repositories.artist_repository as artist_repository


genre_blueprint= Blueprint("genre", __name__)

@genre_blueprint.route("/genre/add")
def add_genre():
    return render_template("genre/add.html")

@genre_blueprint.route("/genre")
def genre():
    return render_template("genre/index.html")