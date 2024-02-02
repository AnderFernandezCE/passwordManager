from sqlalchemy import  Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text, BOOLEAN, Unicode, UUID, LargeBinary, CHAR)
import uuid
import datetime

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

def get_verification_token_expiration_time():
    return datetime.datetime.now() + datetime.timedelta(hours=1)


class Users(Base):
    __tablename__ = "users"

    UUID = Column(CHAR(36), primary_key=True, default=generate_uuid)
    username = Column('username', String(50))
    email = Column('email', String(250))
    userhash = Column('userhash', Unicode(64))
    key = Column('key', Unicode(128))
    # publicKey = Column('publicKey', String(4000)) # not null
    # privateKey = Column('privateKey', String(4000)) # not null
    created_at = Column('created_at', DateTime, default=datetime.datetime.utcnow)
    salt = Column('salt', LargeBinary(32))
    verified =Column('verified', Boolean, default= False)
    verification_token = Column('verification_token', CHAR(36), default=generate_uuid)
    expires_at = Column('expires_at', DateTime, default=get_verification_token_expiration_time)

class AuthRequests(Base):
    __tablename__ = "auth_requests"

    id = Column(CHAR(36), primary_key=True, default=generate_uuid)
    jwt = Column(String(4096), nullable=False)
    userID = Column('userID', String(50), ForeignKey('users.UUID'), nullable=False)
    creation_date= Column('creation_date', DateTime, default=datetime.datetime.now)
    expires_at = Column('expires_at', DateTime)
    valid = Column('valid', Boolean)

class Vault(Base):
    __tablename__ = "vault"

    id = Column(CHAR(36), primary_key=True, default=generate_uuid)
    user_id = Column(String(50),ForeignKey('users.UUID'), nullable=False)
    created_at= Column('created_at', DateTime, default=datetime.datetime.now, nullable=False)
    updated_at= Column('updated_at', DateTime, default=datetime.datetime.now, nullable=False)
    name = Column('name', String(4096), nullable=False)
    data = Column('data', String(4096), nullable=False)

def get_Base():
  return Base