from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import AddPetForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///flask_wtforms"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def homepage():
    """Show homepage links."""
    pets = Pet.query.all()
    return render_template("home.html", pets = pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        # this checks for a submitted url. if there isn't one, it will set it equal to none, which will allow postreSQL to set the default photo
        if form.photo_url.data:
            photo_url = form.photo_url.data
        else:
            photo_url = None
        notes = form.notes.data
        # this checks for pet availability. if available isn't selected, it will set available to false (otherwise, postreSQL will set it to the default value of true.)
        if not form.available.data: 
            available = False 
        else:
            available = True
        pet = Pet(name = name, species = species, age = age, photo_url = photo_url, notes = notes, available = available)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    # this handles the get request
    else:
        return render_template(
            "add_pet.html", form=form)


@app.route("/<int:pid>", methods=["GET", "POST"])
def edit_user(pid):
    """Show pet and edit form. Handle edit."""

    pet = Pet.query.get_or_404(pid)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        if form.photo_url.data:
            photo_url = form.photo_url.data
        else:
            photo_url = None
        notes = form.notes.data
        if not form.available.data: 
            available = False 
        else:
            available = True
        # this is now assigning all of the form info to the pet object acquired from the database using the pet id.
        pet.name = name
        pet.species = species
        pet.age = age
        pet.notes = notes
        pet.photo_url = photo_url
        pet.available = available
        db.session.add(pet)
        db.session.commit()
        flash(f"Pet {pid} updated!")
        return redirect(f"/{pid}")

    else:
        return render_template("pet.html", form=form, pet = pet)
