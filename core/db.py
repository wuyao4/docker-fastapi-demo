import databases
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import DATABASE_URL

# print(DATABASE_URL)
engine = create_engine(str(DATABASE_URL))  # 将DATABASE_URL转换为字符串类型
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base: DeclarativeMeta = declarative_base()

# 异步查询db链接池
database = databases.Database(str(DATABASE_URL))
