from sqlalchemy import create_engine
from sqlalchemy.ext import declarative_base
from sqlalchemy.orm import sessionmaker



sql_alchemy_database_url = 'postgres://dev044:123456@localhost:5432/o-16'


engine = create_engine(sql_alchemy_database_url)


sessionlocal = sessionmaker(autocommit = False,autoflush=False,bin=engine)

session = sessionlocal()



session.
