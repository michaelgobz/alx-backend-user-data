#!usr/bin/env python3
"""DB module
"""
import typing

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from typing import TypeVar
from sqlalchemy.exc import NoResultFound, InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> TypeVar(User):
        """
        add user to the db based on the db session
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> TypeVar(User):
        """
        find user by the email arguments
        """
        db_session = self.__session()
        try:
            return db_session.query(User).filter(**kwargs).first()
        except(NoResultFound, InvalidRequestError) as e:
            if isinstance(e, NoResultFound):
                print("NoResultFound")
            elif isinstance(e, InvalidRequestError):
                print("invalidRequestError")

    def update_user(self, user_id: int, **kwargs):
        """
        update a known user
        """
        user = self.find_user_by(id=user_id)
        try:
            for key, value in kwargs:
                if hasattr(user, key):
                    setattr(user, key, value)
                else:
                    raise InvalidRequestError()
            self.__session().commit()
        except (NoResultFound, InvalidRequestError, ValueError):
            raise ValueError
