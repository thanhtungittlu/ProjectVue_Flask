from sqlalchemy.dialects.postgresql import UUID
from db import db
import uuid

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    # id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    fullname = db.Column(db.String(40))
    username = db.Column(db.String(40))
    password = db.Column(db.String(20))
    email = db.Column(db.String(40))
    phonenumber = db.Column(db.String(40))
    position = db.Column(db.String(40))
    verify = db.Column(db.Boolean,default=False)
    uuid = db.Column(db.Text(length=36), default=lambda: str(uuid.uuid4()))

    def json(self):
        return {
            'fullname': self.fullname,
            'username': self.username, 
            'password': self.password, 
            'email': self.email, 
            'phonenumber': self.phonenumber, 
            'position': self.position,
            'verify' : self.verify,  
            'uuid' : self.uuid,  
        }

    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_fullname(cls,fullname):
        return cls.query.filter_by(fullname=fullname).first()

    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_uuid(cls,uuid):
        return cls.query.filter_by(uuid=uuid).first()