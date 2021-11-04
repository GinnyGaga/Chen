# FROM:https://www.liaoxuefeng.com/wiki/1016959663602400/1017803857459008
# 导入:
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
# DATABASE_URL = 'mysql+pymysql://root:123456@localhost:3306/test02'
DATABASE_URL = 'mysql+pymysql://root:123456@localhost:3306/test03-if'

# 创建表模型对象的基类，SQLORM基类:
Base = declarative_base()


class DbEngine:
    __engine = None
    __session = None

    def __init__(self):
        # 初始化数据库连接:
        self.__engine = create_engine(DATABASE_URL)
        # 初始化会话,且创建_session对象:
        self.__session = sessionmaker(bind=self.__engine)()

    def get_session(self):
        return self.__session
