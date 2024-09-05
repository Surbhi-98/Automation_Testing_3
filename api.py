from flask import Flask
from src.books_view import Books
app = Flask(__name__)

app.add_url_rule("/books", "books", Books.get_books, methods=["GET"])

if __name__ == '__main__':
  app.run(debug=True)