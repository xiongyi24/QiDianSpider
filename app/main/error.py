from . import main
from flask import jsonify, make_response
from .authentication import auth_token, auth_basic

@main.app_errorhandler(404)
def _404NoFound(e):
    return make_response(jsonify({'error':'资源未找到'}), 404)

@main.app_errorhandler(400)
def _400BadRequest(e):
    return make_response(jsonify({'error':'错误的请求，请检查请求格式'}), 400)

@main.app_errorhandler(500)
def _500ServerError(e):
    return make_response(jsonify({'error':'服务器错误'}), 500)

@auth_token.error_handler
def unauthorized(e):
    return make_response(jsonify({'error': '未认证用户'}), 401)

@auth_basic.error_handler
def unauthorized(e):
    return make_response(jsonify({'error': '未认证用户'}), 401)