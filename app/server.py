import flask
from flask import request, jsonify
import main

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Creating starting route
@app.route('/', methods=['GET'])
def home():
    return "basic magister api"

@app.route('/api/auth', methods=['GET'])
def auth():
    if 'username' in request.args and 'password' in request.args and 'school' in request.args:
        print("serving user")
        username = request.args.get('username')
        password = request.args.get('password')
        school = request.args.get('school')
        return jsonify(main.accesstoken(username, password, school))
    else:
        return "missing arguments"


# Creating first api route to fetch rooster:
@app.route('/api/rooster', methods=['GET'])
def rooster():
    if 'apitoken' in request.args and 'dateFrom' in request.args and 'dateTill' in request.args and 'school' in request.args:
        print("serving user")
        apitoken = request.args.get('apitoken')
        dateFrom = request.args.get('dateFrom')
        dateTill = request.args.get('dateTill')
        school = request.args.get('school')
        return jsonify(main.rooster(school, dateFrom, dateTill, apitoken))
    elif not('apitoken' in request.args):
        return "Missing api token"
    else:
        return "missing arguments"

@app.route('/api/grades', methods=['GET'])
def grades():
    if 'apitoken' in request.args and 'school' in request.args:
        print("serving user")
        apitoken = request.args.get('apitoken')
        school = request.args.get('school')
        dateFrom = request.args.get('dateFrom')
        dateTill = request.args.get('dateTill')
        return jsonify(main.grades(school, apitoken, dateFrom, dateTill))
    elif not('apitoken' in request.args):
        return "Missing api token"
    else:
        return "missing arguments"

app.run(host="0.0.0.0", port=5000)
