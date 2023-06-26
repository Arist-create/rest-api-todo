from src.data.database.main_db import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class TaskTableModel(Base):
    __tablename__ = "task"

    task_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    title = Column(String)
    description = Column(String)

    async def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
