from flask import Flask, jsonify


app = Flask(__name__)

books = [
    {"id": 1, "title": "The Hobbit", "available": True},
    {"id": 2, "title": "1984", "available": True},
]


@app.get("/")
def home():
    return "Library Management Application is running"


@app.get("/books")
def list_books():
    return jsonify(books)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
