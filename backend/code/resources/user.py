from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.user import UserModel



class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('fullname',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('email',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('phonenumber',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('position',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    # @jwt_required()
    def get(self, username):
        user = UserModel.find_by_username(username)
        if user:
            return user.json()
        return {'message': 'User not found'},404

    # @jwt_required()
    def post(self, username):
        if UserModel.find_by_username(username):
            return {'message': "An user with username '{}' already exists.".format(username)},400

        data = User.parser.parse_args()
        user = UserModel()
        user.fullname = data['fullname']
        user.username = data['username']
        user.password = data['password']
        user.email = data['email']
        user.phonenumber = data['phonenumber']
        user.position = data['position']        
        
        if UserModel.find_by_email(user.email):
            return {'message': "An user with email '{}' already exists.".format(user.email)},400

        try:
            user.save_to_db()
        except:
            return {'message': "An error occurred inserting the user."},500

        return user.json(),201

    # @jwt_required()
    def put(self, username):
        data = User.parser.parse_args()
        user = UserModel.find_by_username(username)
        
        if user is None: #nếu không có thì thêm vào
            user = UserModel()
            user.fullname = data['fullname']
            user.username = data['username']
            user.password = data['password']
            user.email = data['email']
            user.phonenumber = data['phonenumber']
            user.position = data['position']
        else: # Ngược lại sẽ update
            user.fullname = data['fullname']
            user.username = data['username']
            user.password = data['password']
            user.email = data['email']
            user.phonenumber = data['phonenumber']
            user.position = data['position']
        user.save_to_db()
        return user.json()

    # @jwt_required()
    def delete(self, username):
        user = UserModel.find_by_username(username)
        if user:
            user.delete_from_db()
            return {'message': 'User deleted'}
        return {'message': 'User not found'}
        
class UserList(Resource):
    # @jwt_required()
    def get(self):
        return {'users': [user.json() for user in UserModel.query.all()]}

