from flask import Flask, render_template
from pymongo import MongoClient

from database import read_all_flats

app = Flask(__name__)

client = MongoClient()
db = client['flat_base']
offers = db['offersoto']


@app.route('/')
def hello_world():
    return render_template('index.html', offers=read_all_flats(offers))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')