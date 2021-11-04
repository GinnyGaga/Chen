from database.database import DbEngine, Base
from sqlalchemy import Column, String, Integer


class Ginny(Base):
    __tablename__ = 'ginny'

    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    data = Column(String(255))

    def get_list(self) -> list:
        return DbEngine().get_session().query(Ginny).all()
