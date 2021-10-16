from database.database import Base, DbEngine
from sqlalchemy import Column, String, Integer


class UserAddress(Base):

    __tablename__ = "user_address"

    id = Column(Integer,primary_key=True)
    name = Column(String(255))
    address = Column(String(255))


# 用主键id查询一条记录
def get_by_id(user_id: int) -> UserAddress:
    return DbEngine().get_session().query(UserAddress).filter_by(id=user_id).first()



