from flask import Flask, jsonify
import goodreads


app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def get_date():
    return jsonify(goodreads.get_books())

if __name__ == '__main__':
    app.run()