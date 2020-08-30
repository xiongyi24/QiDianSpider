from . import main  # main : 蓝本
from app.Spider.models import Book, Page
from ..models import User
from flask import make_response, jsonify, request, abort, render_template  # 响应处理函数在路由定义处导入
from .authentication import auth_basic, auth_token


@main.route('/book')
def index():
    return render_template('QidianSpider.html')


@main.route('/book/ranking/<int:ranking>')
@auth_basic.login_required
def findByRanking_GET(ranking):
    book = Book.query.filter(Book.ranking == ranking).first()
    if book:
        response = make_response(jsonify(book.to_json()), 200)  # 调用类方法注意打括号！
        return response
    else:
        abort(404)


@main.route('/book/ranking', methods=['POST'])
@auth_token.login_required
def findByRanking_POST():
    ranking = request.form.get('ranking')
    if ranking:
        book = Book.query.filter(Book.ranking == ranking).first()
        if book:
            response = make_response(jsonify(book.to_json()), 200)  # 调用类方法注意打括号！
            return response
        else:
            abort(404)
    else:
        abort(400)


@main.route('/book/page/<int:page>')
@auth_basic.login_required
def findByPage_GET(page):
    pages = Page.query.filter_by(pages=page).first()
    if pages:
        books = pages.books
        books_list = []
        for book in books:
            books_list.append(book.to_json())
        response = make_response(jsonify(books_list), 200)
        return response
    else:
        abort(404)


@main.route('/book/page', methods=['POST'])
@auth_token.login_required
def findByPage_POST():
    page = request.form.get('page')
    if page:
        pages = Page.query.filter_by(pages=page).first()
        if pages:
            books = pages.books
            books_list = []
            for book in books:
                books_list.append(book.to_json())
            response = make_response(jsonify(books_list), 200)
            return response
        else:
            abort(404)
    else:
        abort(400)


# 获取令牌
@main.route('/book/token', methods=['POST'])
def get_token_POST():
    username = request.form.get('username')
    password = request.form.get('password')
    if username and password:
        user = User.query.filter_by(username=username).first()
        if user:
            password_know = user.password
            if password == password_know:
                token = user.get_auth_token()
                title = str(username) + ' - token'
                return make_response(jsonify({title: token}))
            else:
                return make_response(jsonify({'error': '用户密码错误'}), 200)
        else:
            return make_response(jsonify({'error': '当前请求的用户不存在'}), 200)
    else:
        abort(400)

