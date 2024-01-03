from sqlalchemy import  Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text, BOOLEAN, Unicode, UUID, LargeBinary, CHAR)
import uuid
from datetime import datetime

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

class Users(Base):
    __tablename__ = "users"

    UUID = Column(CHAR(36), primary_key=True, default=generate_uuid)
    username = Column('username', String(50))
    email = Column('email', String(250))
    userhash = Column('userhash', Unicode(64))
    key = Column('key', Unicode(128))
    publicKey = Column('publicKey', String(4000)) # not null
    privateKey = Column('privateKey', String(4000)) # not null
    created_at = Column('created_at', DateTime, default=datetime.utcnow)
    salt = Column('salt', LargeBinary(32))
    verified =Column('verified', Boolean, default= False)
    

# class Link(Base):
#     __tablename__ = "link"

#     id = Column(Integer, primary_key=True)
#     url = Column('url', Text())
#     project_id = Column(Integer, ForeignKey('project.id')) 

# class Repo(Base):
#     __tablename__ = "repo"

#     id = Column(Integer, primary_key=True)
#     domain = Column('domain', String(200), unique=True)
#     description = Column('description', String(200))
#     lastupdate = Column('lastupdate', DateTime)
#     librarysoft = Column('librarysoft', String(100))

# class Availability(Base):
#     __tablename__ = "availability"

#     project_id = Column(Integer, ForeignKey('project.id'), primary_key=True) 
#     downloaded = Column('downloaded', BOOLEAN)
#     availability_status = Column('availability_status', BOOLEAN)
#     description = Column('description', String(200))
#     last_check = Column('last_check', DateTime)
#     embeddings_generated = Column('embeddings_generated', BOOLEAN)
#     embedded = Column('embedded', BOOLEAN)

def get_Base():
  return Base