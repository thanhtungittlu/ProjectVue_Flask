from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.user import UserModel

class UserVerify(Resource):  
    def get(self, uuid):
        user = UserModel.find_by_uuid(uuid)
        user.verify = True
        user.save_to_db()
        return user.json()
