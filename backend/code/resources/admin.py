from flask_restful import Resource, reqparse
# from flask_jwt import jwt_required
from models.admin import AdminModel
from models.user import UserModel
import re 

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def checkErrorEmail(email):
    if(re.fullmatch(regex, email)):
        return False
    else:
        return True

class Admin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('fullname',
        type=str,
        required=False,
        help="This field cannot be left blank!"
    )
    parser.add_argument('username',
        type=str,
        required=False,
        help="This field cannot be left blank!"
    )
    parser.add_argument('password',
        type=str,
        required=False,
        help="This field cannot be left blank!"
    )
    parser.add_argument('email',
        type=str,
        required=False,
        help="This field cannot be left blank!"
    )
    parser.add_argument('phonenumber',
        type=str,
        required=False,
        help="This field cannot be left blank!"
    )
    parser.add_argument('position',
        type=str,
        required=False,
        help="This field cannot be left blank!"
    )


    # @jwt_required()
    def get(self, username):
        admin = AdminModel.find_by_username(username)
        if admin:
            return admin.json()
        return {'message': 'admin not found'},404

    def post(self, username):
        if AdminModel.find_by_username(username):
            return {'message': "An admin with username '{}' already exists.".format(username)},400

        data = Admin.parser.parse_args()
        admin = AdminModel()
        admin.fullname = data['fullname']
        admin.username = data['username']
        admin.password = data['password']
        admin.email = data['email']
        admin.phonenumber = data['phonenumber']
        admin.position = data['position']

        if AdminModel.find_by_email(admin.email):
            return {'message': "An admin with email '{}' already exists.".format(admin.email)},400

        if UserModel.find_by_email(admin.email):
            return {'message': "An admin with email '{}' already exists.".format(admin.email)},400

        try:
            admin.save_to_db()
        except:
            return {'message': "An error occurred inserting the admin."},500

        return admin.json(),201

    def put(self, username):
        data = Admin.parser.parse_args()
        admin = AdminModel.find_by_username(username)
    

        if admin is None: #nếu không có thì thêm vào
            admin = AdminModel()
            admin.fullname = data['fullname']
            admin.username = username
            admin.password = data['password']
            admin.email = data['email']
            admin.phonenumber = data['phonenumber']
            admin.position = data['position']
        else: # Ngược lại sẽ update
            userCheckIn_Users = UserModel.find_by_email(data['email'])
            userCheckIn_Admins = AdminModel.find_by_email(data['email'])
            if ((userCheckIn_Users is None ) or (userCheckIn_Users.email == admin.email)) and ((userCheckIn_Admins is None ) or (userCheckIn_Admins.email == admin.email)):
                admin.fullname = data['fullname']
                admin.password = data['password']
                admin.email = data['email']
                admin.phonenumber = data['phonenumber']
                admin.position = data['position']
                admin.save_to_db()
                return admin.json()       
            else:
                return {'message': "An user with email '{}' already exists.".format(data['email'])},400

 

    def delete(self, username):
        admin = AdminModel.find_by_username(username)
        if admin:
            admin.delete_from_db()
            return {'message': 'admin deleted'}
        return {'message': 'admin not found'}
        
class AdminList(Resource):
    def get(self):
        return {'admin': [admin.json() for admin in AdminModel.query.all()]}