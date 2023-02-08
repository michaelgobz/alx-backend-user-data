#!/usr/bin/env python3
"""
    session auth class definition
    """
import typing
from api.v1.auth.basic_auth import BaseAuth
import uuid
from models.user import User


class SessionAuth(BaseAuth):
    """implemetation of the session auth

        Args:
            BasicAuth (Auth): Auth base class for the Authentican and Authoriation Objects
        """
    _user_id_by_session_id = {}
    
    
    def create_session(self, user_id: str = None) -> str:
        """_summary_
        Args:
        user_id (str, optional): _description_. Defaults to None.
        Returns:
        str: UDID strinf for session ID
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        else:
            session_id = uuid.uuid4(user_id)
            self._user_id_by_session_id['user_id'] = session_id
        
        
    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        retrive the user id for a given session id 
        Args:
            session_id (str, optional): session id 

        Returns:
            str: user id 
        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        else:
            return self._user_id_by_session_id.get('user_id')
        
    
    def current_user(self, request=None) -> typing.TypeVar(User):
          
