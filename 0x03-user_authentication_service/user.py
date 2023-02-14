#!usr/bin/env python3
"""
User Module using SQLAlchemy
"""
from typing import TypeVar

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column

Base = declarative_base()


class User(Base):
    """
    SQLAlchemy Supported user class
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)

    def __repr__(self) -> str:
        return "<User(id='%s', email='%s'," \
               " hashed_password='%s', " \
               "session_id='%s', reset_token='%s' )>" \
            % (self.id, self.email, self.hashed_password,
               self.session_id, self.reset_token)
