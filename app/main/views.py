from . import main  # main : 蓝本
from app.Spider.models import Book, Page
from ..models import User
from flask import make_response, jsonify, request   # 响应处理函数在路由定义处导入
from .authentication import auth_basic, auth_token

@main.route('/book/ranking/<int:ranking>')
@auth_basic.login_required
def findByRanking_GET(ranking):
    book = Book.query.filter(Book.ranking == ranking).first()
    if book != None:
        response = make_response(jsonify(book.to_json()))   # 调用类方法注意打括号！
        response.status = '200'
    else:
        response = make_response(jsonify({'error':'资源未找到'}))
        response.status = '404'
    return response

@main.route('/book/ranking', methods=['POST'])
@auth_token.login_required
def findByRanking_POST():
    ranking = request.form.get('ranking')
    book = Book.query.filter(Book.ranking == ranking).first()
    if book != None:
        response = make_response(jsonify(book.to_json()))  # 调用类方法注意打括号！
        response.status = '200'
    else:
        response = make_response(jsonify({'error': '资源未找到'}))
        response.status = '404'
    return response

@main.route('/book/page/<int:page>')
@auth_basic.login_required
def findByPage_GET(page):
    pages = Page.query.filter_by(pages=page).first()
    if pages != None:
        books = pages.books
        books_list = []
        for book in books:
            books_list.append(book.to_json())
        response = make_response(jsonify(books_list))
        response.status = '200'
    else:
        response = make_response(jsonify({'error': '资源未找到'}))
        response.status = '404'
    return response

@main.route('/book/page', methods=['POST'])
@auth_token.login_required
def findByPage_POST():
    page = request.form.get('page')
    pages = Page.query.filter_by(pages=page).first()
    if pages != None:
        books = pages.books
        books_list = []
        for book in books:
            books_list.append(book.to_json())
        response = make_response(jsonify(books_list))
        response.status = '200'
    else:
        response = make_response(jsonify({'error': '资源未找到'}))
        response.status = '404'
    return response

# 获取令牌
@main.route('/token/<username>')
def get_token(username):
    user = User.query.filter_by(username=username).first()
    if user != None:
        token = user.get_auth_token()
        title = str(username) + ' - token'
        return make_response(jsonify({title:token}))
    else:
        return make_response(jsonify({'error':'当前请求的用户不存在'}), 404)