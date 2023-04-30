from flask import Flask, request, render_template, redirect, url_for, abort, jsonify

from forms import LibraryForms
from models import library

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config["SECRET_KEY"] = "nininini"

@app.route("/", methods=["GET"])
def library_list():
    return render_template("library.html", books=library.all())

@app.route("/borrow/<int:book_id>", methods=["POST"])
def borrow(book_id):
    if library.update(book_id,  True):
        return render_template("library.html", books=library.all())
    else:
        abort(404)

@app.route("/return_book/<int:book_id>", methods=["POST"])
def return_book(book_id):
    if library.update(book_id,  False):
        return render_template("library.html", books=library.all())
    else:
        abort(404)

@app.route("/remove_book/<int:book_id>", methods=["POST"])
def remove_book(book_id):
    if library.delete(book_id):
        return render_template("library.html", books=library.all())
    else:
        abort(404)

@app.route("/add_new_book", methods=["POST"])
def add_new_book():
    form = LibraryForms()
    if request.form["btn"] == "Add book" and request.method == 'POST':
        return render_template("add_new_book.html", form=form)
    elif request.form["btn"] == "Add" and request.method == "POST":
        if form.validate_on_submit():
            title = request.form["title"]
            author = request.form["author"]
            library.add_book(title, author)
            return render_template("library.html", books=library.all())
    return render_template("library.html", books=library.all())


if __name__ == '__main__':
    app.run(debug=True)