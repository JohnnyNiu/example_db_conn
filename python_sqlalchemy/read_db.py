#!virtualEnv/bin/python
from create_db import Person, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.bind=engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

all = session.query(Person).all()
for p in all:
    print(p.name)
