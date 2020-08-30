from . import db
from flask import current_app, abort
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))

    def get_auth_token(self):
        serializer = Serializer(current_app.config['SECRET_KEY'], expires_in=1800)
        return serializer.dumps({'username': self.username}).decode('ascii')  # JSON序列化 -> json
        # decode 解决编码问题

    @staticmethod
    def verify_auth_token(token):
        serializer = Serializer(current_app.config['SECRET_KEY'])
        try:
            username = serializer.loads(token)  # JSON反序列化 -> dict
            username = username['username']
        except BadSignature:
            abort(403)
        return User.query.filter_by(username=username).first().username
