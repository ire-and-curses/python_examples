#!/usr/bin/env python
'''
sqlalchemy_example.py - A short example of using sqlalchemy.

This script create an sqlite database, stores data and then retrieves 
the data.

Author:
    Martin Norbury (martin.norbury@gmail.com)

September 14th 2012
'''

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()
class Contact(Base):
    __tablename__ = 'contact'

    id      = Column(Integer, primary_key=True)
    name    = Column(String)
    age     = Column(Integer)
    address = Column(String)

    def __init__(self, name, age, address):
        self.name    = name
        self.age     = age
        self.address = address

    def __repr__(self):
        return "<Contact('%s','%s','%s')>" % (self.name, self.age, self.address)

# Create database engine
engine = create_engine('sqlite:///test.db', echo=True)

# Create the table
if os.path.exists('test.db'): os.remove('test.db')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create some fake data
data=[
        ( 'Trevor'      , 42 , "1234 Let's Be Avenue" ),
        ( 'Arthur'      , 412, "Camelot" ),
        ( 'Winston'     , 52 , "10 Downing Street"),
        ( 'Queenie'     , 90 , "Buckingham Palace"),
        ( 'POTUS'       , 45 , "Whitehouse"),
        ( 'Harry Potter', 10 , "Hogwarts"),
        ( 'Dracula'     , 666, "Creepy Tower"),
     ]

# Submit the data
for name, age, address in data:
    contact = Contact(name, age, address)
    session.add(contact)

# Commit all changes and close
session.commit()
session.close()

# Query database
session = Session()
old_people = session.query(Contact).filter("age>50").all()
print old_people
session.close()
