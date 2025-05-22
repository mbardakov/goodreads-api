from flask import Flask, jsonify, request
import goodreads


app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    page = request.args.get('page')
    return 'hello ' + page

@app.route('/tbr/<int:userid>/', methods=['GET'])
def get_tbr(userid):
    page = request.args.get('page')
    return jsonify(goodreads.get_shelf(userid, 'to-read', page))

@app.route('/book/<string:bookid>/', methods=['GET'])
def get_book(bookid):
    return jsonify(goodreads.get_book(bookid))

@app.route('/author/<string:authorid>/', methods=['GET'])
def get_author(authorid):
    return jsonify(goodreads.get_author(authorid))

if __name__ == '__main__':
    app.run()