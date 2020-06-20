import os
from dotenv import load_dotenv


from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import logging
from pymongo import MongoClient




# Setting .env file to
# load dotenv in the base root
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

# app.config['MONGO_URI'] = "mongodb+srv://randellCrapy:burnoutX123@junctionx-mnnrf.mongodb.net/<dbname>?retryWrites=true&w=majority"
logging.basicConfig(level=logging.DEBUG)
client = MongoClient(os.getenv('MONGO_URI'))
db = client.gettingStarted

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_all_stars():
    app.logger.info('hi')
    people = db.people

    output = []
    for s in people.find():
        output.append({'name' : s['name']})
        app.logger.info(s)

    return jsonify({'result' : output})
    # return jsonify(people.find_one({ "name.last": "Turing" })['name'])

@app.route('/star/', methods=['GET'])
def get_one_star(name):
  star = mongo.db.stars
  s = star.find_one({'name' : name})
  if s:
    output = {'name' : s['name'], 'distance' : s['distance']}
  else:
    output = "No such name"
  return jsonify({'result' : output})

@app.route('/star', methods=['POST'])
def add_star():
  star = mongo.db.stars
  name = request.json['name']
  distance = request.json['distance']
  star_id = star.insert({'name': name, 'distance': distance})
  new_star = star.find_one({'_id': star_id })
  output = {'name' : new_star['name'], 'distance' : new_star['distance']}
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)