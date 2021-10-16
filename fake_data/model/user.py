from database.database import Base, DbEngine
from sqlalchemy import Column, String, Integer


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构-列名:
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    phone = Column(String(50))

    # def __init__(self, id, name, phone):
    #     self.id = id
    #     self.name = name
    #     self.phone = phone


# 用主键id查询一条记录
def get_by_id(user_id: int) -> User:
    return DbEngine().get_session().query(User).filter_by(id=user_id).first()
    # 创建Query查询，filter是where条件


# 用name查询所有匹配的记录
def get_by_name(user_name: str) -> list:
    return DbEngine().get_session().query(User).filter_by(name=user_name).all()


# 批量创建记录，records为表中的一行数据-列表格式。
def batch_create(records: list):
    session = DbEngine().get_session()
    try:
        session.add_all(records)
        return session.commit()
    except Exception as e:
        print(e)
        return session.rollback()


# 更新
def update_by_id(user_id: int, name=None, phone=None):
    update_fields = {}  # update对象为字典
    if name is not None:  # 若name没有更新，则把原来的name值传给name
        update_fields["name"] = name
    if phone is not None:
        update_fields["phone"] = phone

    if len(update_fields) > 0:
        session = DbEngine().get_session()
        try:
            effect_num = session.query(User).filter_by(id=user_id).update(update_fields)
            return effect_num, session.commit()
        except Exception as e:
            print(e)
            return 0, session.rollback()

    return 0, None
