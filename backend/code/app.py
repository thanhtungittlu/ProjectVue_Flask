from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT
from flask_cors import CORS

from security import authenticate, identity
from resources.admin import Admin,AdminList
from resources.user import User, UserList
from resources.verify import UserVerify
from resources.mail import UserMail



app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

@app.before_first_request
def create_table():
    db.create_all()


app.config['JWT_AUTH_URL_RULE'] = '/login' #Thay /auth = /login
jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(User, '/user/<string:fullname>')
api.add_resource(UserList, '/users')
api.add_resource(Admin, '/admin/<string:username>')
api.add_resource(AdminList, '/admins')
api.add_resource(UserVerify, '/verify/<string:uuid>')
api.add_resource(UserMail, '/email/<string:uuid>')





if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)  # important to mention debug=True