from db import db

class AdminModel(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(40))
    username = db.Column(db.String(40))
    password = db.Column(db.String(20))
    email = db.Column(db.String(40))
    phonenumber = db.Column(db.String(40))
    position = db.Column(db.String(40))


    
    def json(self):
        return {
            'fullname': self.fullname,
            'username': self.username, 
            'password': self.password, 
            'email': self.email, 
            'phonenumber': self.phonenumber, 
            'position': self.position
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
    def find_by_email(cls,email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls,_id):
        return cls.query.filter_by(id = _id).first()