from flask import Flask, jsonify

books = [
    {
        "id": 1,
        "title": "CS50",
        "description": "Intro to CS and art of programming!",
        "author": "Havard",
        "borrowed": False
    },
    {
        "id": 2,
        "title": "Python 101",
        "description": "little python code book.",
        "author": "Will",
        "borrowed": False
    }
]

#@app.route("/books", methods=['GET'])
class Books:
  def get_books():
    """ function to get all books """
    return jsonify({"Books_details": books})
