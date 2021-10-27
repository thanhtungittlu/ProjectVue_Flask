from flask_restful import Resource, reqparse
from models.user import UserModel
import smtplib, ssl


port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "05.luutru.hinhanh@gmail.com"  # Enter your address
password = "tung99teobeng"


class UserMail(Resource):  
    def get(self,uuid):
        user = UserModel.find_by_uuid(uuid)
        receiver_email = user.email
        message = """\
        Subject: Verify!!!



        This is your account confirmation mail.
        Click to link: """ + "http://127.0.0.1:5000/verify/" + user.uuid
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

        return {"message" : "Done sending Email"}
