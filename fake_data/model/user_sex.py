from database.database import Base, DbEngine
from sqlalchemy import Column,Integer,String


class UserSex(Base):

    __tablename__ = "user_sex"

    id = Column(Integer,primary_key=True)
    sex = Column(String(255))
    address = Column(String(255))


