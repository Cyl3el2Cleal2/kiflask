from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

from controllers.index import initial_routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{username}:{password}@{host}/{db}'.format(
    username='root', password='example', host='localhost', db='kiflask')

db = SQLAlchemy(app)

api = Api(app)

initial_routes(api)

@app.teardown_request
def teardown_request(exception):
    if exception:
        db.session.rollback()
    db.session.remove()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
