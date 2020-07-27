from app import db   # 实例化的数据库拓展
from app.Spider import spider

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    ranking = db.Column(db.Integer, unique=True)
    bookName = db.Column(db.String(64), unique=True)
    author = db.Column(db.String(64))
    Type = db.Column(db.String(64))
    introduction = db.Column(db.String(512), unique=True)
    url = db.Column(db.String(64), unique=True)
    page_id = db.Column(db.Integer, db.ForeignKey('pages.id'))

    def to_json(self):
        bookInfor = {
            'ranking': self.ranking,
            'bookname': self.bookName,
            'author': self.author,
            'type': self.Type,
            'introduction': self.introduction,
            'url': self.url
        }
        return bookInfor

class Page(db.Model):
    __tablename__ = 'pages'
    id = db.Column(db.Integer, primary_key=True)
    pages = db.Column(db.Integer, unique=True)
    books = db.relationship('Book',backref='page')

def makeSQL(num=3):
    db.drop_all()
    db.create_all()
    # 爬取相关信息
    print("正在爬取书籍信息")
    DataBase = spider.spider(num)
    print("成功")
    print("正在写入数据库")
    for i in range(num):
        # 创建Pages表实例
        pages = Page(pages=i+1)
        # 创建DataBase表实例
        for j in range(len(DataBase[i])):
            dataBase = Book(ranking=DataBase[i][j][0], bookName=DataBase[i][j][1],
                        author=DataBase[i][j][2], Type=DataBase[i][j][3],
                        introduction=DataBase[i][j][4], url=DataBase[i][j][5], page=pages)  # 注意外键的设置给的参数是表实例，而不是数字
            db.session.add(pages)
            db.session.add(dataBase)
            db.session.commit()
    print("成功")