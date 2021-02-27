import flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import database
import models

app = flask.Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/',methods=['GET','POST'])
def index():
	if flask.request.method == 'GET':
		result = [obj.toDict() for obj in models.User.query.all() ]
		return flask.jsonify(result)
	else:
		return flask.jsonify({"message" : "これはpostです"})



if __name__ == '__main__':
	app.run(debug=True)

