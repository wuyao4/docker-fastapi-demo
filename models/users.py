from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, sql
from sqlalchemy.orm import relationship, backref
from core.db import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    username = Column(String(30), comment="邮箱/用户名")
    password = Column(String(20), comment="密码")
    name = Column(String(20), comment="姓名")
    sex = Column(Integer, comment="性别 1:男 2:女")
    create_at = Column(DateTime(timezone=True), server_default=sql.func.now())


posts = User.__table__
