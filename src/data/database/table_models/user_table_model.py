from src.data.database.main_db import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship


class UserTableModel(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    is_superuser = Column(Boolean)
    tasks = relationship("TaskTableModel", cascade="delete")

    async def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
