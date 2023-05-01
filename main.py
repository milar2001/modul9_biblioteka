from flask import Flask, request, render_template, redirect, url_for, abort, jsonify

from models import library

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config["SECRET_KEY"] = "nininini"

@app.route("/library", methods=["GET"])
def library_list():
    return jsonify(library.all())

@app.route("/library/<int:book_id>/borrow", methods=["PATCH"])
def borrow(book_id):
    if library.update(book_id,  True):
        return jsonify({"message": "Book borrowed successfully"})
    else:
        abort(404)

@app.route("/library/<int:book_id>/return", methods=["PATCH"])
def return_book(book_id):
    if library.update(book_id,  False):
        return jsonify({"message": "Book returned successfully"})
    else:
        abort(404)

@app.route("/library/<int:book_id>", methods=["DELETE"])
def remove_book(book_id):
    if library.delete(book_id):
        return jsonify({'message': 'Book successfully deleted.'}), 200
    else:
        return jsonify({'error': 'Book not found.'}), 404

@app.route("/library", methods=["POST"])
def add_new_book():
    data = request.get_json()
    if data and "title" in data and "author" in data:
        title = data["title"]
        author = data["author"]
        library.add_book(title, author)
        return jsonify({"message": "Book added successfully"})
    else:
        return jsonify({"error": "Invalid form data"})

if __name__ == '__main__':
    app.run(debug=True)
