from flask_httpauth import HTTPTokenAuth, HTTPBasicAuth, MultiAuth
from ..models import User

auth_token = HTTPTokenAuth(scheme='Bearer')
auth_basic = HTTPBasicAuth()
auth_multi = MultiAuth(auth_token, auth_basic)

@auth_token.verify_token
def verify_token(token):
    try:
        username = User.verify_auth_token(token)
    except:
        return False
    user = User.query.filter_by(username=username).first()
    if user == None:
        return False
    else:
        return True

@auth_basic.verify_password
def verify_password(username,password):
    user = User.query.filter_by(username=username).first()
    if user == None:
        return None
    else:
        password = user.password
        return password