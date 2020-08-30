from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config

db = SQLAlchemy()
bootstrap = Bootstrap()


# 工厂函数
def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])  # 导入配置信息
    config[config_name].init_app(app)

    # 初始化拓展
    db.init_app(app)
    bootstrap.init_app(app)

    # 注册蓝本
    from .main import main as main_blueprint  # .main/__init__/main
    app.register_blueprint(main_blueprint)

    return app
