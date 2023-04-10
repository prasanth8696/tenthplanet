from sqlalchemy import create_engine,Column,String,Boolean,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


sql_alchemy_database_url = 'sqlite:///.app.db'


engine = create_engine(sql_alchemy_database_url)


sessionlocal = sessionmaker(autocommit = False,autoflush=False,bind=engine)

session = sessionlocal()

Base = declarative_base()


class SessionData(Base) :
  __tablename__ = "sessions"

  id = Column(String,primary_key=True)
  user_id = Column(String,nullable=False)
  is_loggedIn = Column(Boolean,nullable=False,default=False)
  expire_time = Column(DateTime,nullable=False)


