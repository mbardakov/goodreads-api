from flask import Flask, jsonify
import goodreads


app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'hello'

@app.route('/tbr/<int:userid>/', methods=['GET'])
def get_tbr(userid):
    return jsonify(goodreads.get_shelf(userid, 'to-read'))

if __name__ == '__main__':
    app.run()