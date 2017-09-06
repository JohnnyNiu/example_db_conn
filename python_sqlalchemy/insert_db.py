#!virtualEnv/bin/python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from create_db import  Base, Person

engine = create_engine('sqlite:///sqlalchemy_example.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

new_person = Person(name='new person')
session.add(new_person)
session.commit()
