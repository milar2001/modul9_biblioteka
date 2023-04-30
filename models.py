import json

class Library:
    def __init__(self):
        try:
            with open("library.json", "r") as f:
                self.library = json.load(f)
        except FileNotFoundError:
            self.library = []

    def all(self):
        return self.library

    def get(self, id):
        return next((book for book in self.library if book['id'] == id), None)

    def add_book(self, title, author, borrowed=False):
        new_book = {
            "id": len(self.library) + 1,
            "title": title,
            "author": author,
            "borrowed": borrowed
        }
        self.library.append(new_book)
        self.save_all()

    def save_all(self):
        with open("library.json", "w") as f:
            json.dump(self.library, f)

    def update(self, id, borrowed=True):
        book = self.get(id)
        if book:
            book["borrowed"] = borrowed
            self.save_all()
            return True
        return False

    def delete(self, id):
        book = self.get(id)
        if book:
            self.library.remove(book)
            self.save_all()
            return True
        return False

library = Library()