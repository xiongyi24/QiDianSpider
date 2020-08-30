from app import create_app, db
from app.models import User
from app.Spider.models import Book, Page, makeSQL
from flask_script import Manager, Shell

app = create_app()
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, User=User, Book=Book, Page=Page, makeSQL=makeSQL)  # 上下文关联函数时注意不要打括号


manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
